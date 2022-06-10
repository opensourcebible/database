"""OS Functions."""
import os
import json
from src.config import main as config


def create_json_file(relative_path, json_object):
    """Create JSON file in Build directory."""
    with open(config.build_path + relative_path, "w") as json_file:
        json_data = json.dumps(json_object)
        json_file.write(json_data)


def directory(relative_path):
    """Check and Create directory in Build directory."""
    dir = config.build_path + "/" + relative_path
    if not os.path.exists(dir):
        os.makedirs(dir)
