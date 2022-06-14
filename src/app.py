import typer
import importlib
import os

from src.config import main as config

app = typer.Typer(add_completion=True, add_help_option=False)

"""Load All Commands Available."""
for command_file in os.listdir(config.command_path):
    if command_file.endswith(".py"):
        command_name = command_file.replace(".py", "")
        command_module = importlib.import_module("src.command.%s" % command_name)
        app.add_typer(command_module.app, name=command_name)
