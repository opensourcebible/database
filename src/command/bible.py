"""Build Bible."""

import typer
from src.helper import build, filesystem
from src.data import langs

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main():
    build.build_dir()

    langs_available = langs.execute()
    filesystem.create_json_file("/langs.json", langs_available)
    for lang in langs_available:
        code = lang["code"]
        filesystem.directory(code)
