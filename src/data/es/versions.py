"""Define All Versions Available."""
from src.config import main as config
from src.helper import filesystem


def execute():
    versions = [
        {
            "slug": "catholic",
            "name": "Catolico",
            "url": config.base_url + "/es/catholic/categories.json",
        },
        {
            "slug": "protestant",
            "name": "Protestante",
            "url": config.base_url + "/es/protestant/categories.json",
        },
    ]

    filesystem.create_json_file("/es/versions.json", versions)

    for version in versions:
        slug = version["slug"]
        filesystem.directory("/es/" + slug)

    return versions
