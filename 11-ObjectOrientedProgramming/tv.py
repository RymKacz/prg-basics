class TV:
    def __init__(self):
      self.is_on = False
    def turn_off(self):
      self.is_on = False
    def turn_on(self):
      self.is_on = True
    def set_channel(self, channel):
      self.channel = channel
      self.channels = []
      self.channels.append(self.channel)
    def show_status(self):
      if self.is_on:
        return f"The TV is on, channel {self.channels[self.channel]}."
      else:
        return "The TV is off."