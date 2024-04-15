def hex_to_rgb(hex_input):

  hex = str(hex_input)

  red_hex = hex[0] + hex[1]
  green_hex = hex[2] + hex[3]
  blue_hex = hex[4] + hex[5]

  red = int(red_hex, 16)
  green = int(green_hex, 16)
  blue = int(blue_hex, 16)

  return (red, green, blue)