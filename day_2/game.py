import re

class Game:
  def __init__(self, line) -> None:
    _max_red = 12
    _max_green = 13
    _max_blue = 14
    self.possible = True
    
    # Search for ID:
    id_match = re.search("Game ([0-9]+): ", line)
    self.id = int(id_match.group(1))
    self.max_red = 0
    self.max_green = 0
    self.max_blue = 0

    # Separate by set
    sets = re.split(";", line)
    for set in sets:
      # Search all red matches
      red_matches = re.findall("([0-9]+) red", set)
      red_acc = 0
      for match in red_matches:
        red_acc += int(match)
        if red_acc > _max_red:
          self.possible = False
        if red_acc > self.max_red:
          self.max_red = red_acc

      # Search all green matches
      green_matches = re.findall("([0-9]+) green", set)
      green_acc = 0
      for match in green_matches:
        green_acc += int(match)
        if green_acc > _max_green:
          self.possible = False
        if green_acc > self.max_green:
          self.max_green = green_acc

      # Search all blue matches
      blue_matches = re.findall("([0-9]+) blue", set)
      blue_acc = 0
      for match in blue_matches:
        blue_acc += int(match)
        if blue_acc > _max_blue:
          self.possible = False
        if blue_acc > self.max_blue:
          self.max_blue = blue_acc

        


