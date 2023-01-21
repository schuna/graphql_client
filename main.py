import asyncio
import typer

from api.resolver import get_users

app = typer.Typer()


@app.command("get_users")
def get_users_command():
    asyncio.run(get_users())


@app.callback()
def callback():
    pass


if __name__ == '__main__':
    app()
