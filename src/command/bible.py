"""Build Bible."""

import importlib
import os
import shutil
import typer

from src.config import main as config
from src.data import langs
from src.helper import build

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main():

    # Remove Build Directory
    shutil.rmtree(config.build_path, ignore_errors=True)

    # Create Build Directory
    build.build_dir()

    # Copy Public Files to Build Directory
    shutil.copytree(config.public_path, config.build_path, dirs_exist_ok=True)

    # Execute Lang Commands
    langs_available = langs.execute()

    for lang in langs_available:
        code = lang["code"]

        # Execute Version Commands for Each Language
        version_module = importlib.import_module("src.data.%s.versions" % code)
        versions = version_module.execute()

        for version in versions:
            slug_version = version["slug"]

            # Execute Category Commands for Each Version
            category_module = importlib.import_module("src.data.%s.%s.categories" % (code, slug_version))
            categories = category_module.execute()

            for category in categories:
                slug_category = category["slug"]

                bible_module = importlib.import_module("src.data.%s.%s.%s.bibles" % (code, slug_version, slug_category))
