import json
import os

from common import consts

class SettingsType(object):
    TYPE_NUMERIC = 'numeric'
    TYPE_STR = 'str'
    TYPE_RAW = 'raw'
    TYPE_TUPLE = 'tuple'


class Settings(object):
    def __init__(self):
        self.settings_file_path = os.path.dirname(os.path.abspath(__file__)) + self.get_settings_file_name()
        self.settings_names = []
        self.settings = {}

    def get_settings_file_name(self):
        raise NotImplementedError

    def get(self, setting_name):
        if setting_name in self.settings:
            return self.settings[setting_name]
        else:
            # TODO - handle
            raise Exception()

    def set(self, setting_name, setting_type, val, valid_values=None):
        if setting_type == SettingsType.TYPE_NUMERIC:
            val = int(val)

        if valid_values is not None and val not in valid_values:
            raise Exception
        self.settings[setting_name] = val

    def load_settings(self):
        with open(self.settings_file_path) as fp:
            settings_from_file = json.load(fp)
            for setting_name in self.settings_names:
                self.set(setting_name, SettingsType.TYPE_RAW, settings_from_file[setting_name])

    def save_settings(self):
        with open(self.settings_file_path, 'w') as fp:
            json.dump(self.settings, fp)

    def settings_to_display(self):
        raise NotImplementedError


class KeySettingsManager(Settings):
    def __init__(self):
        super(KeySettingsManager, self).__init__()
        self.settings_names = [consts.RIGHT, consts.LEFT, consts.UP, consts.DOWN]
        self.keys_names_to_edit_message = {
            consts.RIGHT: consts.RIGHT_KEY_MESSAGE,
            consts.LEFT: consts.LEFT_KEY_MESSAGE,
            consts.UP: consts.UP_KEY_MESSAGE,
            consts.DOWN: consts.DOWN_KEY_MESSAGE
        }
        self.keys_to_keys_names = {}

    def get_settings_file_name(self):
        return consts.KEYS_SETTINGS_FILE

    def set(self, setting_name, setting_type, val, valid_values=None):
        super(KeySettingsManager, self).set(setting_name, setting_type, val, valid_values)
        self.keys_to_keys_names[val] = setting_name

    def settings_to_display(self):
        settings_table = []
        for setting_name, setting_val in self.settings.items():
            settings_table.append([setting_name, setting_val])
        return settings_table

class GameSettingsManager(Settings):
    def __init__(self):
        super(GameSettingsManager, self).__init__()
        self.settings_names = [
            consts.BOARD_SIZE_STR,
            consts.EMPTY_SPOT_STR,
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

    def get_setting_name_to_edit_params(self):
        return {
            consts.BOARD_SIZE_STR: {
                'msg': consts.CHOOSE_NEW_SETTING_VALUE_NUMERIC % (consts.BOARD_SIZE_STR, '3/15'),
                'valid_inputs': range(3,15),
                'type': SettingsType.TYPE_NUMERIC
            },
            consts.EMPTY_SPOT_STR: {
                'msg': consts.CHOOSE_NEW_SETTING_VALUE_STR % (consts.EMPTY_SPOT_STR, 'x y'),
                'valid_inputs': [[i,j]
                                 for i in range(0, self.get(consts.BOARD_SIZE_STR))
                                 for j in range(0, self.get(consts.BOARD_SIZE_STR))],
                'type': SettingsType.TYPE_TUPLE
            },
            consts.DIFFICULTY_LEVEL_STR: {
                'msg': consts.CHOOSE_NEW_SETTING_VALUE_NUMERIC % (consts.DIFFICULTY_LEVEL_STR, '1-20'),
                'valid_inputs': range(1, 20),
                'type': SettingsType.TYPE_NUMERIC

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
