from modules import get_brightness

get_brightness = get_brightness.get_brightness

base_color_hex = input('Color (hex): ')

brightness = get_brightness(base_color_hex)

print('Perceptual brightness: ' + str(round(brightness, 0)))