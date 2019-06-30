YES = 'y'
NO = 'n'
MENU = 'm'
START = 's'
EMPTY_STR = " "

# User Messages

GAME_OPENING = "Hi! Welcome to 15 puzzle!"
CHOOSE_OPTION = "Choose option:"
SEE_MENU_OR_START = "Would you like to see the menu or start a new game? [%s/%s]" % (MENU, START)
GOODBYE = "Goodbye, come back again."
INIT_NEW_BOARD = "Initializing a new board for you..."
LETS_START_THE_GAME = "Lets start the game!\n" \
                      "Use your arrow keys to move any plate adjacent to an empty spot and press any other key to quit."

MENU_OPTIONS = "1) Edit game settings\n2) Edit control keys\n3) Start a new game\n4) Quit"
EDIT_GAME_SETTINGS_AGAIN = "Would you like to change another game settings? [%s/%s]" % (YES, NO)

CHOOSE_SETTING_TO_EDIT = "Choose the number of the setting you would like to edit [%s]"
CHOOSE_NEW_SETTING_VALUE_NUMERIC = "Enter new value for setting %s [%s]"
CHOOSE_NEW_SETTING_VALUE_STR = "Enter new value for setting %s in the format - %s"
CHOOSE_NEW_SETTING_VALUE = "Enter new value for setting %s"
WIN_MESSAGE = "Hooray! you've won the game! Want to play again? [%s/%s]" % (YES, NO)
SURE_YOU_WANT_TO_QUIT = "Are you sure you want to quit? [%s/%s]" % (YES, NO)
START_A_NEW_GAME = "Would you like to start a new game? [%s/%s]" % (YES, NO)

RULES = "The objective of the game is to get all the tiles on your bord in the right order.\n" \
        "To order your tiles, use your arrow keys to move tiles adjacent to the empty spot,\n" \
        "when all the tiles are in the right place the game is won.\n"

MOVEMENT_SETTINGS_MESSAGE = "Choose the keys you want to use for the game (don't worry, we'll record them for later)"
UP_KEY_MESSAGE = "Press the key you want to use for 'up' movement"
DOWN_KEY_MESSAGE = "Press the key you want to use for 'down' movement"
RIGHT_KEY_MESSAGE = "Press the key you want to use for 'right' movement"
LEFT_KEY_MESSAGE = "Press the key you want to use for 'left' movement"

# Game Settings
GAME_SETTINGS_FILE = "/game_settings.json"
KEYS_SETTINGS_FILE = "/keys_settings.json"

BOARD_SIZE_STR = "Board Size"
EMPTY_SPOT_STR = "Empty Spot"
DISPLAY_TYPE_STR = "Display Type"
DIFFICULTY_LEVEL_STR = "Difficulty"

# Display Settings
TABLE_PADDING = 3
BASIC_DISPLAY_TYPE = "basic"
CONTROLLED_DISPLAY_TYPE = "controlled"

# Directions
RIGHT = 'Right'
LEFT = 'Left'
UP = 'Up'
DOWN = 'Down'