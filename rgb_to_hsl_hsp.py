def rgb_to_hslp(inputs):

  red_input = inputs[0]
  green_input = inputs[1]
  blue_input = inputs[2]

  red = int(red_input) / 255
  green = int(green_input) / 255
  blue = int(blue_input) / 255

  max_value = max(red, green, blue)
  min_value = min(red, green, blue)
  delta = max_value - min_value

  def get_hue() :
    if delta == 0:
      return 0
    elif red == max_value:
      return (green - blue) / (delta)
    elif green == max_value:
      return 2 + (blue - red) / (delta)
    elif blue == max_value:
      return 4 + (red - green) / (delta)
    
  def get_hue_in_degrees(hue):
    hue_in_degrees = hue * 60
    while hue_in_degrees < 0:
      hue_in_degrees = hue_in_degrees + 360
    return hue_in_degrees

  def get_lightness():
    return (max_value + min_value) / 2

  def get_saturation():
    if get_lightness() == 1:
      return 0
    else:
      return (delta / (1 - abs(2 * get_lightness() - 1))) * 100
    
  hue = get_hue_in_degrees(get_hue())

  saturation = get_saturation()

  lightness = get_lightness() * 100

  perceptual_brightness = (0.299 * red + 0.587 * green + 0.114 * blue) * 100

  return (hue, saturation, lightness, perceptual_brightness)