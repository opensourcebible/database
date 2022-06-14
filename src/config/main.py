"""Configuration file for application."""
import os

base_url = os.environ["BASE_URL"]

config_path = os.path.abspath(os.path.dirname(__file__))

base_path = config_path + "/.."

build_path = base_path + "/../build"

data_path = base_path + "/data"

public_path = base_path + "/../public"

command_path = base_path + "/command"
