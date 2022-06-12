"""Define All Versions Available."""
from src.config import main as config
from src.helper import filesystem


def execute():
    versions = [
        {
            "slug": "catholic",
            "name": "Catholic",
            "url": config.base_url + "/en/catholic/categories.json",
        },
        {
            "slug": "protestant",
            "name": "Protestant",
            "url": config.base_url + "/en/protestant/categories.json",
        },
    ]

    filesystem.create_json_file("/en/versions.json", versions)

    for version in versions:
        slug = version["slug"]
        filesystem.directory("/en/" + slug)

    return versions
