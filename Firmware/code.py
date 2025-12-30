import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.extensions.RGB import RGB

keyboard = KMKKeyboard()

# Definice pinů pro 9 tlačítek (podle tvého schématu)
# Pořadí v seznamu určuje pořadí v keymapě níže
PINS = [
    board.D26, # SW1 (A0)
    board.D27, # SW2 (A1)
    board.D28, # SW3 (A2)
    board.D29, # SW4 (A3)
    board.D6,  # SW5
    board.D7,  # SW6
    board.D0,  # SW7
    board.D3,  # SW8
    board.D2,  # SW9
]

# Nastavení scanneru pro přímé zapojení tlačítek ke GND
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False, # Tlačítko sepne pin k zemi (GND)
)

# Nastavení RGB (podle schématu Pin 10 = GPIO4)
rgb = RGB(
    pixel_pin=board.D4,  # GPIO4 na XIAO RP2040
    num_pixels=4,        # Máš 4 LED diody
    val_default=100,     # Jas (0-255)
)
keyboard.extensions.append(rgb)

# Definice funkcí pro jednotlivá tlačítka
keyboard.keymap = [
    [
        KC.LCTL(KC.C),      # SW1: Copy
        KC.LCTL(KC.V),      # SW2: Paste
        KC.LCTL(KC.Z),      # SW3: Undo
        KC.LCTL(KC.Y),      # SW4: Redo
        KC.MUTE,            # SW5: Ztlumit zvuk
        KC.VOLU,            # SW6: Hlasitost nahoru
        KC.VOLD,            # SW7: Hlasitost dolů
        KC.MPLY,            # SW8: Play/Pause
        KC.LWIN(KC.D),      # SW9: Zobrazit plochu (Win+D)
    ]
]

if __name__ == '__main__':
    keyboard.go()