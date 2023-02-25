import asyncio
import logging
import uuid
from pathlib import Path

from gql import Client, gql

from api.field import UserSchema
from api.queries import (
    QUERY_USERS, QUERY_USER,
    MUTATION_USER, MUTATION_FILE_UPLOAD, SUBSCRIPTION_ADD_USER
)
from api.utils import transport, ws_transport

logger_format = '%(asctime)s:%(threadName)s:%(message)s'
logging.basicConfig(format=logger_format, level=logging.INFO, datefmt="%H:%M:%S")

monitoring = True
last_user = {
    "username": None,
    "email": None,
    "password": None
}
current_user = {
    "username": None,
    "email": None,
    "password": None
}


async def execute_subscribe(query: gql):
    logging.info("subscription start ... ")
    async with Client(transport=ws_transport, fetch_schema_from_transport=False) as session:
        try:
            async for result in session.subscribe(query):
                logging.info(f"added: {result}")
                current_user.update(result['user'])
        except Exception as e:
            print(f"Websocket terminated: {e}")


async def monitor_added_user():
    logging.info("monitoring start ... ")
    while monitoring:
        await asyncio.sleep(1)
        if last_user["username"] != current_user["username"]:
            logging.info(f"new user: {current_user}")
            last_user.update(current_user)


async def execute_query(query: gql, variables=None, kwargs=None):
    if variables is None:
        variables = dict()
    if kwargs is None:
        kwargs = dict()
    async with Client(
            transport=transport,
            fetch_schema_from_transport=True,
    ) as session:
        return await session.execute(query, variable_values=variables, **kwargs)


async def get_users():
    logging.info(f"{await execute_query(QUERY_USERS)}")


async def get_user(user_id: int):
    logging.info(f'{await execute_query(QUERY_USER, variables={"user_id": user_id})}')


async def add_user(user: UserSchema):
    logging.info(f"{await execute_query(MUTATION_USER, variables={'input': user.dict()})}")


async def file_up_load(file: Path):
    with open(file, "rb") as f:
        params = {"filename": file.name, "file": f}
        res = await execute_query(
            MUTATION_FILE_UPLOAD,
            variables=params,
            kwargs={'upload_files': True})
    logging.info(res)


async def update_user():
    background_tasks = set()
    logging.info("Update user start...")
    task = asyncio.create_task(execute_subscribe(SUBSCRIPTION_ADD_USER))
    background_tasks.add(task)
    task.add_done_callback(background_tasks.discard)
    task = asyncio.create_task(monitor_added_user())
    background_tasks.add(task)
    task.add_done_callback(background_tasks.discard)
    await asyncio.sleep(1)
    logging.info("Add user")
    for i in range(10):
        username = uuid.uuid4()
        await add_user(UserSchema(**{
            "username": f"{username}",
            "email": f"{username}@email.com",
            "password": f"${username}^"
        }))
        await asyncio.sleep(1)

    await asyncio.sleep(1)
