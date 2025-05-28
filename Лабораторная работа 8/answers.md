# Ответы на контрольные вопросы

### 1. Определение времени с заданного момента
```python
from datetime import datetime

start = datetime(2025, 5, 1, 12, 0)  # Фиксированная дата
now = datetime.now()                  # Текущий момент
delta = now - start                   # Разница

print(f"Прошло: {delta.days} дней и {delta.seconds//3600} часов")
# Пример вывода: "Прошло: 3 дня и 5 часов"
```

### 2. Копирование файлов и директорий
```python
import shutil, os

# Копирование файла
shutil.copy("data.txt", "backup/data.txt")

# Копирование папки
if not os.path.exists("backup"):
    shutil.copytree("my_folder", "backup/my_folder")
```

### 3. Формат даты в JSON
```json
{
    "last_backup": "2025-05-20T14:30:00",
    "paths": ["C:/data", "D:/docs"]
}
```
Для работы в Python:
```python
from datetime import datetime
date = datetime.strptime("2025-05-20T14:30:00", "%Y-%m-%dT%H:%M:%S")
```

### 4. Создание лог-файла
```python
import logging

logging.basicConfig(
    filename='backup.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.info("Старт копирования")
logging.error("Ошибка доступа к файлу")
```

### 5. Возможности argparse
```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--source", help="Папка-источник")
parser.add_argument("--force", action="store_true", help="Принудительный запуск")
args = parser.parse_args()

if args.source:
    print(f"Копируем из {args.source}")
```

### 6. Сохранение списка путей в JSON
```python
import json

data = {
    "backup_paths": [
        "C:/Users/Документы",
        "D:/Фото"
    ],
    "settings": {"compression": True}
}

with open('config.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
```