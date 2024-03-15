def hsl_to_rgb(inputs):

  hue_input = inputs[0]
  saturation_input = inputs[1]
  lightness_input = inputs[2]
  
  hue = int(hue_input) / 60
  saturation = int(saturation_input) / 100
  lightness = int(lightness_input) / 100

  delta = saturation * (1 - abs(2 * lightness - 1))

  max_min_sum = 2 * lightness

  min = (max_min_sum - delta) / 2
  max = (max_min_sum + delta) / 2

  def get_max_channel():
    if (hue < 1) or (hue >= 5):
      return 'red'
    if (hue >= 1 and hue < 3):
      return 'green'
    if (hue >= 3 and hue < 5):
      return 'blue'
    
  def get_min_channel():
    if (hue >= 2 and hue < 4):
      return 'red'
    if (hue >= 4):
      return 'green'
    if (hue < 2):
      return 'blue'
    
  def get_mid_channel():
    if (get_max_channel() == 'red' or get_min_channel() == 'red') and (get_max_channel() == 'green' or get_min_channel() == 'green'):
      return 'blue'
    if (get_max_channel() == 'blue' or get_min_channel() == 'blue') and (get_max_channel() == 'green' or get_min_channel() == 'green'):
      return 'red'
    if (get_max_channel() == 'red' or get_min_channel() == 'red') and (get_max_channel() == 'blue' or get_min_channel() == 'blue'):
      return 'green'
    
  def get_mid_value():
    phase = hue % 2
    return (max - delta * abs(phase - 1))
    
  def get_value(channel):
    if channel == get_min_channel():
      return min * 255
    if channel == get_mid_channel():
      return get_mid_value() * 255
    if channel == get_max_channel():
      return max * 255

  red, green, blue = get_value('red'), get_value('green'), get_value('blue')

  return red, green, blue