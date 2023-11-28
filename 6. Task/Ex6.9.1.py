import asyncio
from call_company import data


async def call_company(company_info):
    if company_info['call_time'] > 5:
        await asyncio.sleep(5)
        raise asyncio.CancelledError()
    await asyncio.sleep(company_info['call_time'])
    print(f'Company {company_info["Name"]}: {company_info["Phone"]} дозвон успешен')


async def main():
    tasks = [asyncio.create_task(call_company(company_info)) for company_info in data]
    await asyncio.wait(tasks, timeout=10)
    for task in tasks:
        if not task.done():
            print(task)
            task.cancel()

asyncio.run(main())
