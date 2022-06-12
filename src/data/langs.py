"""Define All Languages Available."""
from src.config import main as config
from src.helper import filesystem


def execute():

    langs = [
        {
            "code": "en",
            "name": "English",
            "url": config.base_url + "/en/versions.json",
        },
        {
            "code": "es",
            "name": "Español",
            "url": config.base_url + "/es/versions.json",
        },
        {
            "code": "pt-br",
            "name": "Português",
            "url": config.base_url + "/pt-br/versions.json",
        },
    ]

    filesystem.create_json_file("/langs.json", langs)

    for lang in langs:
        code = lang["code"]
        filesystem.directory(code)

    return langs
