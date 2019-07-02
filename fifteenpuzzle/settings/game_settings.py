from common import consts
from settings.settings import Settings, SettingsType


class GameSettingsManager(Settings):
    def __init__(self):
        super(GameSettingsManager, self).__init__()
        self.settings_names = [
            consts.BOARD_SIZE_STR,
            consts.DISPLAY_TYPE_STR,
            consts.DIFFICULTY_LEVEL_STR
        ]

        self.id_to_setting_name = None
        self.setting_name_to_edit_params = None

    def get_settings_file_name(self):
        return consts.GAME_SETTINGS_FILE

    def load_settings(self):
        super(GameSettingsManager, self).load_settings()
        self.id_to_setting_name = self.get_id_to_setting()
        self.setting_name_to_edit_params = self.get_setting_name_to_edit_params()

    def get_id_to_setting(self):
        id_to_setting_name = {}
        for i in range(1, len(self.settings_names)+1):
            id_to_setting_name[str(i)] = self.settings_names[i-1]
        return id_to_setting_name

    @staticmethod
    def get_setting_name_to_edit_params():
        return {
            consts.BOARD_SIZE_STR: {
                'msg': consts.CHOOSE_NEW_SETTING_VALUE % (consts.BOARD_SIZE_STR, '3/9'),
                'valid_inputs': range(3,10),
                'type': SettingsType.TYPE_NUMERIC
            },
            consts.DIFFICULTY_LEVEL_STR: {
                'msg': consts.CHOOSE_NEW_SETTING_VALUE % (consts.DIFFICULTY_LEVEL_STR, '1-20'),
                'valid_inputs': range(1, 20),
                'type': SettingsType.TYPE_NUMERIC
            },
            consts.DISPLAY_TYPE_STR: {
                'msg': consts.CHOOSE_NEW_SETTING_VALUE % (consts.DISPLAY_TYPE_STR, consts.BASIC_DISPLAY_TYPE),
                'valid_inputs': [consts.BASIC_DISPLAY_TYPE],
                'type': SettingsType.TYPE_STR
            }
        }

    @property
    def settings_ids(self):
        return self.id_to_setting_name.keys()

    def get_edit_message(self):
        return consts.CHOOSE_SETTING_TO_EDIT %\
               '/'.join(self.settings_ids())

    def settings_to_display(self):
        settings_table = []
        for settings_id, settings_name in self.id_to_setting_name.items():
            settings_table.append([settings_id, settings_name, self.settings[settings_name]])
        return settings_table