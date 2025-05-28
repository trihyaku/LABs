import asyncio
import random

async def mock_request(request_id: int, delay: float):
    try:
        print(f"Запрос {request_id} начал выполнение (задержка: {delay} сек)")
        await asyncio.sleep(delay)
        print(f"Запрос {request_id} завершён")
        return f"Результат запроса {request_id}"
    except asyncio.CancelledError:
        print(f"Запрос {request_id} был отменён")
        raise

async def main():
    tasks = [
        asyncio.create_task(mock_request(i, random.uniform(1, 5)))
        for i in range(1, 6)
    ]
    
    try:
        results = await asyncio.wait_for(asyncio.gather(*tasks), timeout=3.0)
        print("\nВсе запросы выполнены успешно!")
        print("Результаты:", results)
    except asyncio.TimeoutError:
        print("\nПревышено время ожидания (3 сек)!")
        for task in tasks:
            if not task.done():
                task.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    asyncio.run(main())