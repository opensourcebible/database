"""Define All Languages Available."""
from src.config import main as config


def execute():

    langs = [
        {
            "code": "en",
            "name": "English",
            "url": config.build_path + "/en/",
        },
        {
            "code": "es",
            "name": "Español",
            "url": config.build_path + "/es/",
        },
        {
            "code": "pt-br",
            "name": "Português",
            "url": config.build_path + "/pt-br/",
        },
    ]
    return langs
