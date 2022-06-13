"""Define All Categories Available."""
from src.config import main as config
from src.helper import filesystem


def execute():
    categories = [
        {
            "slug": "bible",
            "name": "Biblia",
            "url": config.base_url + "/es/protestant/bible/bibles.json",
        },
        {
            "slug": "commentary",
            "name": "Comentario",
            "url": config.base_url + "/es/protestant/commentary/commentaries.json",
        },
    ]

    filesystem.create_json_file("/es/protestant/categories.json", categories)

    for category in categories:
        slug = category["slug"]
        filesystem.directory("/es/protestant/" + slug)

    return categories
