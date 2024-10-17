import os
from typing import Annotated

import httpx
import typer
from rich import print

from url2markdown_cli import __version__

URL2MARKDOWN_URL = os.environ.get(
    "URL2MARKDOWN_URL", "https://urltomarkdown.herokuapp.com/?url={url}"
)


cli = typer.Typer()


def url2markdown(*, url: str) -> str:
    response = httpx.get(URL2MARKDOWN_URL.format(url=url))
    response.raise_for_status()
    return response.text


def version_callback(value: bool):
    if value:
        print(f"url2markdown-cli version: {__version__}")
        raise typer.Exit()


@cli.command()
def main(
    url: str,
    version: Annotated[
        bool | None, typer.Option("--version", callback=version_callback)
    ] = None,
):
    print(url2markdown(url=url))


if __name__ == "__main__":
    cli()
