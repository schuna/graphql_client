import os

from dotenv import load_dotenv
from gql.transport.aiohttp import AIOHTTPTransport


def file_read(filename: str) -> str:
    with open(filename) as f:
        return f.read()


load_dotenv()
schema_str = file_read('schema.graphql')
transport = AIOHTTPTransport(
    url="http://localhost:8000/graphql",
    headers={"Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}"}
)
