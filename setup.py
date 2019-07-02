from distutils.core import setup

setup(
    name='FifteenPuzzle',
    version='0.7',
    packages=['fifteenpuzzle',],
    entry_points={'console_scripts': [
        'fifteenpuzzle = fifteenpuzzle.game_ui:play_in_cli',
    ]},
)