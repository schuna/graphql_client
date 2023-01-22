import os

from dotenv import load_dotenv
from gql.transport.aiohttp import AIOHTTPTransport

load_dotenv()

transport = AIOHTTPTransport(
    url="http://localhost:8000/graphql",
    headers={"Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}"}
)
