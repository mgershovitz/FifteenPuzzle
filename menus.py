from common import consts
from settings.settings import SettingsType


class Menus(object):
    def __init__(self, input_manager, display, game_settings, key_settings, start_func, quit_func):
        self.input_manager = input_manager
        self.display = display
        self.game_settings = game_settings
        self.keys_settings = key_settings
        self.start_game_func = start_func
        self.quit_func = quit_func

    def open_main_menu(self):
        self.input_manager.basic_user_input_loop(consts.MENU_OPTIONS,
                                                 ['1', '2', '3', '4'],
                                                 {'1': self.open_game_settings_menu,
                                                  '2': self.open_keys_settings_menu,
                                                  '3': self.start_game_func,
                                                  '4': self.quit_func})
        self.open_main_menu()

    def open_keys_settings_menu(self):
        self.display.display_table(self.keys_settings.settings_to_display())
        for key_name, key_message in self.keys_settings.keys_names_to_edit_message.items():
            self.display.display_message(key_message)
            user_input = self.input_manager.get_user_input()
            self.keys_settings.set(
                key_name,
                SettingsType.TYPE_STR,
                user_input
            )
        self.keys_settings.save_settings()

    def open_game_settings_menu(self):
        self.display.display_table(self.game_settings.settings_to_display())
        user_input = None

        while user_input not in self.game_settings.settings_ids:
            self.display.display_message(consts.CHOOSE_SETTING_TO_EDIT
                                         % '/'.join(self.game_settings.settings_ids))
            user_input = self.input_manager.get_user_input()

        setting_id = user_input
        setting_name = self.game_settings.id_to_setting_name[setting_id]
        edit_params = self.game_settings.setting_name_to_edit_params[setting_name]

        user_edit_value = None
        while user_edit_value not in edit_params['valid_inputs']:
            self.display.display_message(edit_params['msg'])
            user_edit_value = self.input_manager.get_user_input()
            if edit_params['type'] == SettingsType.TYPE_NUMERIC:
                user_edit_value = int(user_edit_value)
            elif edit_params['type'] == SettingsType.TYPE_TUPLE:
                user_edit_value = [int(item) for item in user_edit_value.split(' ')]

        self.game_settings.set(setting_name, edit_params['type'], user_edit_value, edit_params['valid_inputs'])
        self.display.display_table(self.game_settings.settings_to_display())
        self.input_manager.basic_user_input_loop(message=consts.EDIT_GAME_SETTINGS_AGAIN,
                                                 valid_inputs=[consts.YES, consts.NO],
                                                 input_to_action={'y': self.open_game_settings_menu})
