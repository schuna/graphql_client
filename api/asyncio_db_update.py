import asyncio
import logging

logger_format = '%(asctime)s:%(threadName)s:%(message)s'
logging.basicConfig(format=logger_format, level=logging.INFO, datefmt="%H:%M:%S")


class DbUpdate:
    def __init__(self):
        self.value = 0

    async def update(self):
        logging.info("Update Started")
        logging.info("Sleeping")
        await asyncio.sleep(1)
        logging.info("Reading Value From Db")
        tmp = self.value ** 2 + 1
        logging.info("Updating Value")
        self.value = tmp
        logging.info("Update Finished")


async def main():
    db = DbUpdate()
    await asyncio.gather(*[db.update() for _ in range(2)])
    logging.info(f"Final value is {db.value}")


if __name__ == '__main__':
    asyncio.run(main())
