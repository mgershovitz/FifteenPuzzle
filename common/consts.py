YES = 'y'
NO = 'n'
EMPTY_STR = " "

# User Messages

GAME_OPENING = "Hi! Welcome to 15 puzzle!"
GOODBYE = "Goodbye, come back again."
INIT_NEW_BOARD = "Initializing a new board for you..."
LETS_START_THE_GAME = "Lets start the game!\n" \
                      "Use your arrow keys to move any plate adjacent to an empty spot into the empty spot\n" \
                      "and press any other key to quit"
EDIT_SETTINGS_PROMPT = "Would you like to change the game settings? [%s/%s]" % (YES, NO)
EDIT_MOVEMENT_SETTINGS_PROMPT = "Would you like to change the movement keys? [%s/%s]" % (YES, NO)
CHOOSE_SETTING_TO_EDIT = "Choose the number of the setting you would like to edit [%s]"
CHOOSE_NEW_SETTING_VALUE_NUMERIC = "Enter new value for setting %s [%s]"
CHOOSE_NEW_SETTING_VALUE_STR = "Enter new value for setting %s in the format - %s"
CHOOSE_NEW_SETTING_VALUE = "Enter new value for setting %s"
WIN_MESSAGE = "Hooray! you've won the game! Want to play again? [%s/%s]" % (YES, NO)
SURE_YOU_WANT_TO_QUIT = "Are you sure you want to quit? [%s/%s]" % (YES, NO)

MOVEMENT_SETTINGS_MESSAGE = "Choose the keys you want to use for the game (don't worry, we'll record them for later)"
UP_KEY_MESSAGE = "Press the key you want to use for 'up' movement"
DOWN_KEY_MESSAGE = "Press the key you want to use for 'down' movement"
RIGHT_KEY_MESSAGE = "Press the key you want to use for 'right' movement"
LEFT_KEY_MESSAGE = "Press the key you want to use for 'left' movement"

# Game Settings
SETTINGS_FILE = "/common/settings.json"

BOARD_SIZE_STR = "Board Size"
EMPTY_SPOT_STR = "Empty Spot"
DISPLAY_TYPE_STR = "Display Type"

UP_KEY = 'k'
DOWN_KEY = ','
LEFT_KEY = 'm'
RIGHT_KEY = '.'

# Display Settings
TABLE_PADDING = 3
BASIC_DISPLAY_TYPE = "basic"

# Directions
RIGHT = 'Right'
LEFT = 'Left'
UP = 'Up'
DOWN = 'Down'

# READ ME
README = "These are the rules of the game: You can quit at any time using 'q' or start a new game using 'r'"