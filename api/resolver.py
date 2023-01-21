from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

from api.schema import QUERY_USERS

transport = AIOHTTPTransport(url="http://localhost:8000/graphql")


async def execute_query(query: gql):
    async with Client(
            transport=transport,
            fetch_schema_from_transport=True,
    ) as session:
        return await session.execute(query)


async def get_users():
    print(f"{await execute_query(QUERY_USERS)}")
