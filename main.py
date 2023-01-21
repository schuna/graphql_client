import asyncio
from pathlib import Path

import typer

from api.field import UserSchema
from api.resolvers import get_users, get_user, add_user, file_up_load

app = typer.Typer()


@app.command("get_users")
def get_users_command():
    asyncio.run(get_users())


@app.command("get_user")
def get_user_command(user_id: int = typer.Argument(..., help="User Id")):
    asyncio.run(get_user(user_id))


@app.command("add_user")
def add_user_command(
        username: str = typer.Argument(..., help="username"),
        email: str = typer.Argument(..., help="email"),
        password: str = typer.Argument(..., help="password")):
    asyncio.run(add_user(
        UserSchema(**{"username": username, "email": email, "password": password})))


@app.command("upload_file")
def upload_file_command(file: Path = typer.Argument(..., help="file to upload")):
    asyncio.run(file_up_load(file))


if __name__ == '__main__':
    app()
