import json
import os

from common import consts
from common.consts import SETTINGS_FILE


class SettingsManager(object):
    def __init__(self):
        self.settings_file_path = os.path.dirname(os.path.abspath(__file__)) + SETTINGS_FILE
        self.id_to_setting = {
            '1': consts.BOARD_SIZE_STR,
            '2': consts.EMPTY_SPOT_STR,
            '3': consts.DISPLAY_TYPE_STR,
            '4': consts.DIFFICULTY_LEVEL_STR
        }
        self.settings = {}

    def load_settings(self):
        with open(self.settings_file_path) as fp:
            settings_from_file = json.load(fp)
            for setting in self.id_to_setting.values():
                self.settings[setting] = settings_from_file[setting]

    def save_settings(self):
        with open(self.settings_file_path, 'w') as fp:
            json.dump(self.settings, fp)

    def get(self, setting):
        if setting in self.settings:
            return self.settings[setting]
        else:
            # TODO - handle
            raise Exception()

    def get_valid_inputs_for_editing(self):
        return self.id_to_setting.keys()

    def get_settings_number_to_edit_action(self):
        return {setting_id: self.edit_setting(setting) for setting_id, setting in self.id_to_setting.items()}

    def edit_setting(self, setting):
        def edit_func():
            if setting in [consts.BOARD_SIZE_STR]:
                print(consts.CHOOSE_NEW_SETTING_VALUE_NUMERIC % (setting, '3/15'))
                # TODO -Handle this!
                self.settings[setting] = int(input())
            elif setting in [consts.EMPTY_SPOT_STR]:
                print(consts.CHOOSE_NEW_SETTING_VALUE_STR % (setting, 'x y'))
                new_empty_spot_tuple = [int(i) for i in input().split(' ')]
                self.settings[setting] = new_empty_spot_tuple
            else:
                print(consts.CHOOSE_NEW_SETTING_VALUE % setting)

            print(self)
            print("Done!")
        return edit_func

    def get_edit_message(self):
        return consts.CHOOSE_SETTING_TO_EDIT %\
               '/'.join(self.get_valid_inputs_for_editing())

    def __repr__(self):
        printable_settings = ""
        for att_id, att in self.id_to_setting.items():
            printable_settings += "%s) %s:\t%s\n" % (att_id, att, self.settings[att])
        return printable_settings
