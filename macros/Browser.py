# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Browser', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000500, '< Back', [Keycode.ALT, Keycode.LEFT_ARROW]),
        (0x000500, 'Fwd >', [Keycode.ALT, Keycode.RIGHT_ARROW]),
        (0x050000, 'Up', [Keycode.UP_ARROW]),      # Scroll up
        # 2nd row ----------
        (0x050500, '- Size', [Keycode.CONTROL, Keycode.KEYPAD_MINUS]),
        (0x050500, 'Size +', [Keycode.CONTROL, Keycode.KEYPAD_PLUS]),
        (0x050000, 'Down', [Keycode.DOWN_ARROW]),                     # Scroll down
        # 3rd row ----------
        (0x000005, 'Reload', [Keycode.CONTROL, 'r']),
        (0x000005, 'Home', [Keycode.ALT, Keycode.HOME]),
        (0x000005, 'Clsd Tab', [Keycode.CONTROL, Keycode.SHIFT, 't']),
        # 4th row ----------
        (0x000000, 'Ada', [Keycode.CONTROL, 't', -Keycode.COMMAND,
                           'www.adafruit.com\n']),   # Adafruit in new window
        (0x050000, 'Digi', [Keycode.CONTROL, 't', -Keycode.COMMAND,
                            'www.digikey.com\n']),   # Digi-Key in new window
        (0x050505, 'Hacks', [Keycode.CONTROL, 't', -Keycode.COMMAND,
                             'www.hackaday.com\n']), # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close tab
    ],
    'icons' : 'Browser.bmp'
}
