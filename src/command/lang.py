"""Load All Languages Available."""

import typer
import os
import tomli

from src.config import main as config
from src.helper import filesystem

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main():
    lang_dir = config.data_path + "/langs"
    langs = []

    try:
        for lang_filename in os.listdir(lang_dir):
            with open(os.path.join(lang_dir, lang_filename), "r") as lang_file:
                lang = tomli.loads(lang_file.read()).get("lang")
                langs.append(
                    {
                        "code": lang["code"],
                        "name": lang["name"],
                        "religions": {
                            "url": config.base_url + "/" + lang["code"] + "/religions.json",
                        },
                    }
                )

                filesystem.directory(lang["code"])

        # Sort
        langs.sort(key=lambda obj: obj["code"])

    except Exception as ex:
        print(str(ex))

    filesystem.create_json_file("/langs.json", langs)

    print("Load All Languages Available [OK]")
