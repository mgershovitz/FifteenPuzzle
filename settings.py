import consts

DEFAULT_BOARD_SIZE = 3

class GameSettings(object):
    def __init__(self):
        self.id_to_setting = {
            '1': consts.BOARD_SIZE
        }
        self.settings = {
            consts.BOARD_SIZE: DEFAULT_BOARD_SIZE
        }

    @property
    def board_size(self):
        return self.settings[consts.BOARD_SIZE]

    def get_valid_inputs_for_editing(self):
        return self.id_to_setting.keys()

    def get_settings_number_to_edit_action(self):
        return {setting_id: self.edit_setting(setting) for setting_id, setting in self.id_to_setting.items()}

    def edit_setting(self, setting):
        def edit_func():
            print(consts.CHOOSE_NEW_SETTING_VALUE % (setting, '3/15'))
            # TODO -Handle this!
            self.settings[setting] = int(input())
            print(self)
            print("Done!")
        return edit_func

    def get_edit_message(self):
        return consts.CHOOSE_SETTING_TO_EDIT %\
               '/'.join(self.get_valid_inputs_for_editing())

    def __repr__(self):
        printable_settings = ""
        for att_id, att in self.id_to_setting.items():
            printable_settings += "%s) %s:\t%s" % (att_id, att, self.settings[att])
        return printable_settings
