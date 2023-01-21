import asyncio
import typer

from api.resolver import get_users, get_user

app = typer.Typer()


@app.command("get_users")
def get_users_command():
    asyncio.run(get_users())


@app.command("get_user")
def get_user_command(user_id: int = typer.Argument(..., help="User Id")):
    asyncio.run(get_user(user_id))


if __name__ == '__main__':
    app()
