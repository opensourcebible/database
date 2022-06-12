"""Define All Categories Available."""
from src.config import main as config
from src.helper import filesystem


def execute():
    categories = [
        {
            "slug": "bible",
            "name": "Bible",
            "url": config.base_url + "/en/catholic/bible/bibles.json",
        },
        {
            "slug": "commentary",
            "name": "Commentary",
            "url": config.base_url + "/en/catholic/commentary/commentaries.json",
        },
    ]

    filesystem.create_json_file("/en/catholic/categories.json", categories)

    for category in categories:
        slug = category["slug"]
        filesystem.directory("/en/catholic/" + slug)

    return category
