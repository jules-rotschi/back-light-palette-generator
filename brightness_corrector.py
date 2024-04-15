from modules import set_brightness

set_brightness = set_brightness.set_brightness

base_color_hex = input('Base color (hex): ')
target_brightness = input('Target perceptual brightness: ')

new_color = set_brightness(base_color_hex, target_brightness)

print('Corrected color: ' + '#' + new_color)