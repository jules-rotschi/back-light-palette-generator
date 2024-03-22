def rgb_to_hex(inputs):

  red_input = inputs[0]
  green_input = inputs[1]
  blue_input = inputs[2]

  red = int(red_input)
  green = int(green_input)
  blue = int(blue_input)
  
  red_hex = (hex(red))[2::]
  green_hex = (hex(green))[2::]
  blue_hex = (hex(blue))[2::]

  def secure(hexa_comp):
    if len(hexa_comp) == 0:
      return '00'
    if len(hexa_comp) == 1:
      return '0' + hexa_comp
    else: return hexa_comp

  hexa = secure(red_hex) + secure(green_hex) + secure(blue_hex)

  return hexa