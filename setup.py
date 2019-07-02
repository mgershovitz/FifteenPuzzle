from distutils.core import setup
import setuptools

setup(
    name='FifteenPuzzle',
    version='2.1',
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={'console_scripts': [
        'fifteenpuzzle = fifteenpuzzle.game_ui:play_in_cli',
    ]},
)