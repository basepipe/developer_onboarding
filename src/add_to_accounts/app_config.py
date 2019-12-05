import yaml
import sys
import os


def _load_yaml(path):
    with open(path, 'r') as stream:
        try:
            result = yaml.load(stream)

            if result:
                return result
            else:
                return {}
        except yaml.YAMLError as exc:
            print(exc)
            sys.exit(99)


def config():
    path_, file_ = os.path.split(__file__)
    config_ = _load_yaml(os.path.join(path_, 'config.yaml'))
    return config_
