import argparse
import json
import os
import shutil
import logging
from datetime import datetime, timedelta
from pathlib import Path

os.chdir(Path(__file__).parent)

logging.basicConfig(
    filename='backup.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def load_config():
    """Загружает конфигурацию из файла config.json."""
    try:
        print("Пытаюсь загрузить config.json...")
        print("Текущая директория:", os.getcwd())
        print("Содержимое папки:", os.listdir())
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error("Файл конфигурации config.json не найден.")
        return None
    except json.JSONDecodeError:
        logging.error("Ошибка чтения config.json: неверный формат.")
        return None

def save_config(config):
    """Сохраняет конфигурацию в файл."""
    try:
        with open('config.json', 'w') as f:
            json.dump(config, f, indent=4)
        logging.info("Конфигурация сохранена.")
    except Exception as e:
        logging.error(f"Ошибка сохранения config.json: {e}")

def interactive_config():
    """Интерактивное меню для настройки конфигурации."""
    config = {
        "backup_paths": [],
        "backup_dir": "",
        "period_days": 1,
        "last_backup": ""
    }
    print("\n=== Настройка резервного копирования ===")
    config["backup_dir"] = input("Папка для резервных копий: ").strip()
    config["period_days"] = int(input("Периодичность (в днях): "))
    
    while True:
        path = input("Добавьте путь для копирования (или Enter для завершения): ").strip()
        if not path:
            break
        if os.path.exists(path):
            config["backup_paths"].append(path)
        else:
            print(f"Ошибка: путь '{path}' не существует.")
    
    config["last_backup"] = datetime.now().strftime('%Y-%m-%d %H:%M')
    save_config(config)
    print("Конфигурация сохранена в config.json.")

def perform_backup():
    """Выполняет резервное копирование на основе конфигурации."""
    config = load_config()
    if not config:
        print("Ошибка: не удалось загрузить конфигурацию. Сначала настройте её через --config.")
        return

    last_backup = datetime.strptime(config["last_backup"], '%Y-%m-%d %H:%M')
    now = datetime.now()
    
    if now - last_backup < timedelta(days=config["period_days"]):
        logging.info("Резервное копирование пропущено: период не истёк.")
        print("Пока рано для следующего копирования.")
        return

    backup_name = f"backup_{now.strftime('%Y%m%d_%H%M')}"
    backup_path = os.path.join(config["backup_dir"], backup_name)
    
    try:
        os.makedirs(backup_path, exist_ok=True)
        for src in config["backup_paths"]:
            if os.path.isfile(src):
                shutil.copy(src, backup_path)
            elif os.path.isdir(src):
                shutil.copytree(src, os.path.join(backup_path, os.path.basename(src)))
        config["last_backup"] = now.strftime('%Y-%m-%d %H:%M')
        save_config(config)
        logging.info(f"Резервное копирование завершено: {backup_path}")
        print(f"Копирование успешно создано: {backup_path}")
    except Exception as e:
        logging.error(f"Ошибка при копировании: {e}")
        print(f"Ошибка: {e}")

def main():
    parser = argparse.ArgumentParser(description="Утилита резервного копирования")
    parser.add_argument('--config', action='store_true', help="Настроить параметры копирования")
    args = parser.parse_args()

    if args.config:
        interactive_config()
    else:
        perform_backup()

if __name__ == "__main__":
    main()