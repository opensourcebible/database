"""Rotinas relacionadas ao uso da Bíblia."""

import typer

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main():
    print("Bibles")
