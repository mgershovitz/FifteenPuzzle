import json
import os


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


