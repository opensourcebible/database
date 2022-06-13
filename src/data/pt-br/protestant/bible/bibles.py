"""Define All Bibles Available."""
import os
import tomli

from src.config import main as config
from src.helper import filesystem


def execute():
    bibles = []

    # Get all bible infos from the toml file.
    current_dir = os.path.abspath(os.path.dirname(__file__))
    for dir_name in os.listdir(current_dir):
        info_path = os.path.join(current_dir, dir_name, "info.toml")
        if os.path.exists(info_path):
            with open(info_path, "r") as info_file:
                info = tomli.loads(info_file.read())
                bible = {
                    "code": info["bible"]["code"],
                    "name": info["bible"]["name"],
                    "url": config.base_url + "/pt-br/protestant/bible/" + info["bible"]["code"] + "/all.json",
                }
                bibles.append(bible)

    print(bibles)

    # filesystem.create_json_file("/pt-br/protestant/bible/bibles.json", bibles)

    # for bible in bibles:
    #     slug = bible["code"]
    #     filesystem.directory("/pt-br/protestant/bible/" + slug)

    return bibles
