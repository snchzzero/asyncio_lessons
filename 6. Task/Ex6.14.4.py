import asyncio


async def publish_post(text):
    await asyncio.sleep(1)
    text_p = f"Пост опубликован: {text}"
    print(text_p)
    return text_p


async def notify_subscribers(subscriber):
    await asyncio.sleep(1)
    print(f"Уведомление отправлено {subscriber}")


async def main():
    post_text = "Hello world!"
    subscribers = ["Alice", "Bob", "Charlie", "Dave", "Emma", "Frank", "Grace", "Henry", "Isabella", "Jack"]
    task_1 = asyncio.create_task(publish_post(post_text))
    task_2 = [asyncio.create_task(notify_subscribers(subscriber)) for subscriber in subscribers]
    await task_1
    await asyncio.gather(*task_2)


asyncio.run(main())
