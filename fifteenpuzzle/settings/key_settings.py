from common import consts
from settings.settings import Settings


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