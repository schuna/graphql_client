import logging
import os

from dotenv import load_dotenv
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.websockets import WebsocketsTransport
from gql.transport.aiohttp import log as aiohttp_log
from gql.transport.websockets import log as websockets_log

aiohttp_log.setLevel(logging.WARNING)
websockets_log.setLevel(logging.WARNING)

load_dotenv()

transport = AIOHTTPTransport(
    url="http://localhost:8000/graphql",
    headers={"Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}"}
)

ws_transport = WebsocketsTransport(
    url="ws://localhost:8000/graphql"
)
