"""
A helper module that initializes the display and buttons for the PicoSystem
game console. See https://shop.pimoroni.com/products/picosystem
"""

import board
import analogio
import stage
import keypad


K_X = 0x01  # A
K_O = 0x02  # B
K_SELECT = 0x04  # X
K_START = 0x08   # Y
K_DOWN = 0x10
K_LEFT = 0x20
K_RIGHT = 0x40
K_UP = 0x80


class _Buttons:
    def __init__(self):
        self.keys = keypad.Keys((
            board.SW_A,
            board.SW_B,
            board.SW_X,
            board.SW_Y,
            board.SW_DOWN,
            board.SW_LEFT,
            board.SW_RIGHT,
            board.SW_UP
        ), value_when_pressed=False, pull=True, interval=0.05)
        self.last_state = 0
        self.event = keypad.Event(0, False)

    def get_pressed(self):
        buttons = self.last_state
        events = self.keys.events
        while events:
            if events.get_into(self.event):
                bit = 1 << self.event.key_number
                if self.event.pressed:
                    buttons |= bit
                    self.last_state |= bit
                else:
                    self.last_state &= ~bit

        return buttons


display = board.DISPLAY
buttons = _Buttons()
audio = stage.Audio(board.AUDIO, None)
battery = analogio.AnalogIn(board.BAT_SENSE)
