import asyncio
import aiohttp
import time

URL = "http://13.233.129.130:5000/play/1"
TOTAL_REQUESTS = 10000
CONCURRENT_REQUESTS = 500


async def fetch(session):
    try:
        async with session.get(URL) as response:
            await response.read()
            return response.status
    except Exception as e:
        return str(e)


async def run_test():
    connector = aiohttp.TCPConnector(limit=CONCURRENT_REQUESTS)
    async with aiohttp.ClientSession(connector=connector) as session:

        tasks = [fetch(session) for _ in range(TOTAL_REQUESTS)]

        start = time.time()

        results = await asyncio.gather(*tasks)

        end = time.time()

        success = results.count(200)
        failed = TOTAL_REQUESTS - success

        print(f"\nTotal Requests: {TOTAL_REQUESTS}")
        print(f"Successful: {success}")
        print(f"Failed: {failed}")
        print(f"Time Taken: {end-start:.2f} seconds")


asyncio.run(run_test())