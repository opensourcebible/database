"""Functions for Build Directory."""
import os
from src.config import main as config


def build_dir_exists():
    """Check if directory Build exists."""
    return os.path.exists(config.build_path)


def build_dir_create():
    """Create directory Build."""
    os.makedirs(config.build_path)


def build_dir():
    """Check and Create directory Build."""
    if not build_dir_exists():
        build_dir_create()
