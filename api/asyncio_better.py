import asyncio
import logging
import time

logger_format = '%(asctime)s:%(threadName)s:%(message)s'
logging.basicConfig(format=logger_format, level=logging.INFO, datefmt="%H:%M:%S")

num_word_mapping = {1: 'ONE', 2: 'TWO', 3: "THREE", 4: "FOUR", 5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT",
                    9: "NINE", 10: "TEN"}


async def delay_message(delay, message):
    logging.info(f"{message} received")
    await asyncio.sleep(
        delay)  # time.sleep is blocking call. Hence, it cannot be awaited and we have to use asyncio.sleep
    logging.info(f"Printing {message}")


async def main():
    background_tasks = set()
    logging.info("Main started")
    logging.info("Creating multiple tasks with asyncio.gather")
    for i in range(5):
        task = asyncio.create_task(delay_message(i + 1, num_word_mapping[i + 1]))
        background_tasks.add(task)
        task.add_done_callback(background_tasks.discard)
    await asyncio.sleep(0)
    logging.info("Main Ended")
    await asyncio.sleep(5)


if __name__ == '__main__':
    asyncio.run(main())
