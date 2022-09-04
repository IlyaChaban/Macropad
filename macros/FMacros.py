# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Mouse control

# The syntax for Mouse macros is highly peculiar, in order to maintain
# backward compatibility with the original keycode-only macro files.
# The third item for each macro is a list in brackets, and each value within
# is normally an integer (Keycode), float (delay) or string (typed literally).
# Consumer Control codes were added as list-within-list, and then mouse
# further complicates this by adding dicts-within-list. Each mouse-related
# dict can have any mix of keys 'buttons' w/integer mask of button values
# (positive to press, negative to release), 'x' w/horizontal motion,
# 'y' w/vertical and 'wheel' with scrollwheel motion.

# To reference Mouse constants, import Mouse like so...
from adafruit_hid.keycode import Keycode
# You can still import Keycode and/or ConsumerControl as well if a macro file
# mixes types! See other macro files for typical Keycode examples.

app = {               # REQUIRED dict, must be named 'app'
    'name' : 'F macros', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000500, 'F13', [Keycode.F13]),
        (0x000500, 'F14', [Keycode.F14]),
        (0x000500, 'F15', [Keycode.F15]),
        # 2nd row ----------
        (0x000500, 'F16', [Keycode.F16]),
        (0x000500, 'F17', [Keycode.F17]),
        (0x000500, 'F18', [Keycode.F18]),
        # 3rd row ----------
        (0x000500, 'F19', [Keycode.F19]),
        (0x000500, 'F20', [Keycode.F20]),
        (0x000500, 'F21', [Keycode.F21]),
        # 4th row ----------
        (0x000500, 'F22', [Keycode.F22]),
        (0x000500, 'F23', [Keycode.F23]),
        (0x000500, 'F24', [Keycode.F24]),
        # Encoder button ---
        (0x000000, '', [])
        ],
    
    'icons' : 'F_macros.bmp'
}
