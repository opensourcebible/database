"""Define All Versions Available."""
from src.config import main as config
from src.helper import filesystem


def execute():
    versions = [
        {
            "slug": "catholic",
            "name": "Católico",
            "url": config.base_url + "/pt-br/catholic/categories.json",
        },
        {
            "slug": "protestant",
            "name": "Protestante",
            "url": config.base_url + "/pt-br/protestant/categories.json",
        },
    ]

    filesystem.create_json_file("/pt-br/versions.json", versions)

    for version in versions:
        slug = version["slug"]
        filesystem.directory("/pt-br/" + slug)

    return versions
