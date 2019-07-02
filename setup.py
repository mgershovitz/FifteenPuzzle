from distutils.core import setup
import setuptools

setup(
    name='FifteenPuzzle',
    version='0.9',
    packages=setuptools.find_packages(),
    entry_points={'console_scripts': [
        'fifteenpuzzle = fifteenpuzzle.game_ui:play_in_cli',
    ]},
)