import os
from fabric.api import local, lcd

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
BUILD_PATH = os.path.join(ROOT_DIR, '_build', 'html')


def serve():
    "Serve local website for preview purposes"
    with lcd(BUILD_PATH):
        local('python -m SimpleHTTPServer')


def clean():
    "Clean build dir without breaking everything"
    with lcd(BUILD_PATH):
        local('rm -Rf _images _sources aventure _static jeu')
        local('rm -f *')
        local('rm -f .buildinfo')
