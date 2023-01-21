import os

from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

from api.schema import QUERY_USERS, QUERY_USER
from dotenv import load_dotenv

load_dotenv()

transport = AIOHTTPTransport(
    url="http://localhost:8000/graphql",
    headers={"Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}"}
)


async def execute_query(query: gql, variables=None):
    if variables is None:
        variables = dict()
    async with Client(
            transport=transport,
            fetch_schema_from_transport=True,
    ) as session:
        return await session.execute(query, variable_values=variables)


async def get_users():
    print(f"{await execute_query(QUERY_USERS)}")


async def get_user(user_id: int):
    print(f'{await execute_query(QUERY_USER, variables={"user_id": user_id})}')
