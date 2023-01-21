from pathlib import Path

from gql import Client, gql

from api.field import UserSchema
from api.queries import (
    QUERY_USERS, QUERY_USER,
    MUTATION_USER, MUTATION_FILE_UPLOAD
)
from api.utils import transport, schema_str


async def execute_query(query: gql, variables=None, kwargs=None):
    if variables is None:
        variables = dict()
    if kwargs is None:
        kwargs = dict()
    async with Client(
            schema=schema_str,
            transport=transport,
            fetch_schema_from_transport=False,
    ) as session:
        return await session.execute(query, variable_values=variables, **kwargs)


async def get_users():
    print(f"{await execute_query(QUERY_USERS)}")


async def get_user(user_id: int):
    print(f'{await execute_query(QUERY_USER, variables={"user_id": user_id})}')


async def add_user(user: UserSchema):
    print(f"{await execute_query(MUTATION_USER, variables={'input': user.dict()})}")


async def file_up_load(file: Path):
    with open(file, "rb") as f:
        params = {"file": f}
        res = await execute_query(
            MUTATION_FILE_UPLOAD,
            variables=params,
            kwargs={'upload_files': True})
    print(res.get("readFile"))
