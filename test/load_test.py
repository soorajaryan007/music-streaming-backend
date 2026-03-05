import asyncio
import aiohttp
import time

URL = "http://13.233.129.130:5000/play/1"

TOTAL_REQUESTS = 100
CONCURRENT_REQUESTS = 5


async def fetch(session):
    start = time.time()

    try:
        async with session.get(URL) as response:
            await response.read()

            latency = time.time() - start
            return response.status, latency

    except Exception as e:
        return str(e), 0


async def run_test():

    connector = aiohttp.TCPConnector(limit=CONCURRENT_REQUESTS)

    async with aiohttp.ClientSession(connector=connector) as session:

        tasks = [fetch(session) for _ in range(TOTAL_REQUESTS)]

        start_time = time.time()

        results = await asyncio.gather(*tasks)

        end_time = time.time()

        success = sum(1 for r in results if r[0] == 200)
        failed = TOTAL_REQUESTS - success

        latencies = [r[1] for r in results if isinstance(r[1], float)]

        avg_latency = sum(latencies) / len(latencies)

        print("\nLoad Test Result")
        print("-------------------")
        print("Total Requests:", TOTAL_REQUESTS)
        print("Successful:", success)
        print("Failed:", failed)
        print("Total Time:", round(end_time - start_time, 2), "seconds")
        print("Average Latency:", round(avg_latency, 3), "seconds")


asyncio.run(run_test())