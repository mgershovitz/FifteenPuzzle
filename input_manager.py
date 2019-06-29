import consts

class InputManager(object):
    def __init__(self):
        self.movement_keys = {
            consts.UP_KEY: consts.UP,
            consts.DOWN_KEY: consts.DOWN,
            consts.LEFT_KEY: consts.LEFT,
            consts.RIGHT_KEY: consts.RIGHT
        }
        self.action_key = {
        }

    def get_movement_keys_edit_func(self, get_user_input_func):
        def edit_movement_keys_func():
            print(consts.RIGHT_KEY_MESSAGE)
            self.movement_keys[get_user_input_func()] = consts.RIGHT
            print(consts.LEFT_KEY_MESSAGE)
            self.movement_keys[get_user_input_func()] = consts.LEFT
            print(consts.UP_KEY_MESSAGE)
            self.movement_keys[get_user_input_func()] = consts.UP
            print(consts.DOWN_KEY_MESSAGE)
            self.movement_keys[get_user_input_func()] = consts.DOWN
        return edit_movement_keys_func

    def get_user_move(self, char):
        if char in self.movement_keys:
            return self.movement_keys[char]

    @classmethod
    def user_input_loop(cls, message, valid_inputs, input_to_action):
        user_input = None
        while user_input not in valid_inputs:
            print(message)
            user_input = input()

        if user_input in input_to_action:
            input_to_action[user_input]()

        return user_input