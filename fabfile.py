import os
from fabric.api import local, lcd

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))


def serve():
    "Serve local website for preview purposes"
    with lcd(os.path.join(ROOT_DIR, '_build', 'html')):
        local('python -m SimpleHTTPServer')
