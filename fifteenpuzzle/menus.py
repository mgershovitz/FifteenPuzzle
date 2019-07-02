from common import consts
from settings.settings import SettingsType


class MenuOption(object):
    def __init__(self, option_name, action):
        self.option_name = option_name
        self.action = action

    def choose(self):
        self.action()


class Menus(object):
    def __init__(self, input_manager, display, game_settings, key_settings, start_func, quit_func):
        self.input_manager = input_manager
        self.display = display
        self.game_settings = game_settings
        self.keys_settings = key_settings
        self.start_game_func = start_func
        self.quit_func = quit_func

        self.main_menu = {
            '1': MenuOption(consts.OPTION_EDIT_GAME_SETTINGS,
                            self.open_game_settings_menu),
            '2': MenuOption(consts.OPTION_EDIT_CONTROL_KEYS,
                            self.open_keys_settings_menu),
            '3': MenuOption(consts.OPTION_START_NEW_GAME,
                            self.start_game_func),
            '4': MenuOption(consts.OPTION_QUIT,
                            self.quit_func)
        }

    def open_main_menu(self):
        menu_for_display = [consts.CHOOSE_OPTION]
        for option_id, option in self.main_menu.items():
            menu_for_display.append("%s) %s" % (option_id, option.option_name))
        menu_for_display = '\n'.join(menu_for_display)
        user_input = self.input_manager.basic_user_input_loop(menu_for_display,
                                                              ['1', '2', '3', '4'])
        self.main_menu[user_input].choose()
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

        if self.input_manager.basic_user_input_loop(
                message=consts.EDIT_GAME_SETTINGS_AGAIN, valid_inputs=[consts.YES, consts.NO]) == consts.YES:
            self.open_game_settings_menu()

        self.game_settings.save_settings()