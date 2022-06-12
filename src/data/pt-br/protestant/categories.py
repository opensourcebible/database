"""Define All Categories Available."""
from src.config import main as config
from src.helper import filesystem


def execute():
    categories = [
        {
            "slug": "bible",
            "name": "Bíblia",
            "url": config.base_url + "/pt-br/protestant/bible/bibles.json",
        },
        {
            "slug": "commentary",
            "name": "Comentário",
            "url": config.base_url + "/pt-br/protestant/commentary/commentaries.json",
        },
    ]

    filesystem.create_json_file("/pt-br/protestant/categories.json", categories)

    for category in categories:
        slug = category["slug"]
        filesystem.directory("/pt-br/protestant/" + slug)

    return category
