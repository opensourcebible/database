import typer
from src.command import bible, comment

app = typer.Typer(add_completion=True, add_help_option=False)

"""Carrega os comandos."""
app.add_typer(bible.app, name="bible")
app.add_typer(comment.app, name="comment")
