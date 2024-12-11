import asyncio


# An asynchronous function allows pausing its execution and resuming later.
async def main():  # defines an asynchronous function
    print("Hello ...")
    """
    - This function `asyncio.sleep(1)` suspends the execution of the current coroutine (which is main in this case) for one second.
    - Unlike the regular `time.sleep` function, `asyncio.sleep` is non-blocking. This means that while main is suspended, other tasks or coroutines can continue execution.
    """
    await asyncio.sleep(1)
    print("... World!")


"""
The asyncio.run function takes an asynchronous function (like main here) and executes it within an event loop.
"""
asyncio.run(main())
