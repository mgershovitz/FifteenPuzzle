class InputManager(object):
    def __init__(self, game_settings, keys_settings, display):
        self.game_settings = game_settings
        self.keys_settings = keys_settings
        self.display = display

    @staticmethod
    def get_user_input():
        return input()

    def get_user_move(self, char):
        move = self.keys_settings.keys_to_keys_names.get(char)
        return move

    def basic_user_input_loop(self, message, valid_inputs, input_to_action=None):
        user_input = None
        while user_input not in valid_inputs:
            self.display.display_message(message)
            user_input = self.get_user_input()

        if input_to_action and user_input in input_to_action:
            input_to_action[user_input]()

        return user_input
