from common import consts
from settings.settings import SettingsType


class InputManager(object):
    def __init__(self, game_settings, keys_settings, display):
        self.game_settings = game_settings
        self.keys_settings = keys_settings

        self.display = display

    def edit_game_settings(self):
        self.edit_settings_prompt(consts.EDIT_GAME_SETTINGS_PROMPT, self.handle_game_settings_edit)

    def edit_keys_settings(self):
        self.edit_settings_prompt(consts.EDIT_KEYS_SETTINGS_PROMPT, self.handle_keys_settings_edit)

    def edit_settings_prompt(self, message, edit_func):
        self.basic_user_input_loop(message=message, valid_inputs=[consts.YES, consts.NO],
                                   input_to_action={'y': edit_func})

    def handle_game_settings_edit(self):
        self.display.display_table(self.game_settings.settings_to_display())
        user_input = None

        while user_input not in self.game_settings.settings_ids:
            self.display.display_message(consts.CHOOSE_SETTING_TO_EDIT
                                         % '/'.join(self.game_settings.settings_ids))
            user_input = self.display.get_user_input()

        setting_id = user_input
        setting_name = self.game_settings.id_to_setting_name[setting_id]
        edit_params = self.game_settings.setting_name_to_edit_params[setting_name]

        user_edit_value = None
        while user_edit_value not in edit_params['valid_inputs']:
            self.display.display_message(edit_params['msg'])
            user_edit_value = self.display.get_user_input()
            if edit_params['type'] == SettingsType.TYPE_NUMERIC:
                user_edit_value = int(user_edit_value)
            elif edit_params['type'] == SettingsType.TYPE_TUPLE:
                user_edit_value = [int(item) for item in user_edit_value.split(' ')]

        self.game_settings.set(setting_name, edit_params['type'], user_edit_value, edit_params['valid_inputs'])
        self.game_settings.save_settings()
        self.edit_settings_prompt(consts.EDIT_GAME_SETTINGS_PROMPT, self.handle_game_settings_edit)

    def handle_keys_settings_edit(self):
        self.display.display_table(self.keys_settings.settings_to_display())
        for key_name, key_message in self.keys_settings.keys_names_to_edit_message.items():
            self.display.display_message(key_message)
            user_input = self.display.get_user_input()
            self.keys_settings.set(
                key_name,
                SettingsType.TYPE_STR,
                user_input
            )
        self.keys_settings.save_settings()

    def get_user_move(self, char):
        move = self.keys_settings.keys_to_keys_names.get(char)
        return move

    def basic_user_input_loop(self, message, valid_inputs, input_to_action):
        user_input = None
        while user_input not in valid_inputs:
            self.display.display_message(message)
            user_input = self.display.get_user_input()

        if user_input in input_to_action:
            input_to_action[user_input]()

        return user_input
