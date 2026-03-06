import time
def measure_latency(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Response time: {time.time() - start:.4f}s")
        return result
    return wrapper