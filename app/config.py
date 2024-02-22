import pathlib
import yaml

base_directory = pathlib.Path(__file__).parent.parent
path_config = base_directory / "config" / "conf.yaml"


def load_config(path):
    with open(path) as stream:
        conf = yaml.safe_load(stream)
    return conf


config = load_config(path_config)