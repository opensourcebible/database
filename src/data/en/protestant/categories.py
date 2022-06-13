"""Define All Categories Available."""
from src.config import main as config
from src.helper import filesystem


def execute():
    categories = [
        {
            "slug": "bible",
            "name": "Bible",
            "url": config.base_url + "/en/protestant/bible/bibles.json",
        },
        {
            "slug": "commentary",
            "name": "Commentary",
            "url": config.base_url + "/en/protestant/commentary/commentaries.json",
        },
    ]

    filesystem.create_json_file("/en/protestant/categories.json", categories)

    for category in categories:
        slug = category["slug"]
        filesystem.directory("/en/protestant/" + slug)

    return categories
