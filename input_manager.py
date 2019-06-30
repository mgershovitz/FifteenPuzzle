import consts

class InputManager(object):
    def __init__(self, settings, display):
        self.settings = settings
        self.display = display
        self.movement_keys = {
            consts.UP_KEY: consts.UP,
            consts.DOWN_KEY: consts.DOWN,
            consts.LEFT_KEY: consts.LEFT,
            consts.RIGHT_KEY: consts.RIGHT
        }
        self.action_key = {
        }

    def edit_settings(self):
        user_input = None
        while user_input != 'n':
            user_input = self.user_input_loop(
                message=consts.EDIT_SETTINGS_PROMPT,
                valid_inputs=[consts.YES, consts.NO],
                input_to_action={'y': self.handle_settings_edit}
            )

    def handle_settings_edit(self):
        print(self.settings)
        self.user_input_loop(
            consts.CHOOSE_SETTING_TO_EDIT % \
            '/'.join(self.settings.get_valid_inputs_for_editing()),
            self.settings.id_to_setting.keys(),
            self.settings.get_settings_number_to_edit_action()
        )

    def get_movement_keys_edit_func(self):
        def edit_movement_keys_func():
            print(consts.RIGHT_KEY_MESSAGE)
            self.movement_keys[self.display.get_user_input()] = consts.RIGHT
            print(consts.LEFT_KEY_MESSAGE)
            self.movement_keys[self.display.get_user_input()] = consts.LEFT
            print(consts.UP_KEY_MESSAGE)
            self.movement_keys[self.display.get_user_input()] = consts.UP
            print(consts.DOWN_KEY_MESSAGE)
            self.movement_keys[self.display.get_user_input()] = consts.DOWN
        return edit_movement_keys_func

    def get_user_move(self, char):
        if char in self.movement_keys:
            return self.movement_keys[char]

    def user_input_loop(self, message, valid_inputs, input_to_action):
        user_input = None
        while user_input not in valid_inputs:
            print(message)
            user_input = self.display.get_user_input()

        if user_input in input_to_action:
            input_to_action[user_input]()

        return user_input