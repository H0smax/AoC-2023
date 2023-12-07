from operator import attrgetter
import sys

filename = sys.argv[1]
lines = []
with open(filename) as file:
  file_lines = file.read().splitlines()
  for line in file_lines:
    lines.append(line)

class Hand:
  def __init__(self, line) -> None:
    self.hand = line[0:5]
    self.points = int(line[5:])
    self.type = self.check_type(self.hand, False)
    self.part_two = False

  def recheck_type(self, part_two = False):
    self.part_two = part_two
    self.type = self.check_type(self.hand, True)

  def check_type(self, hand, part_two):
    different_letters = list(set(hand))
    #print(different_letters)
    if len(different_letters) == 5: # No pairs
      if "J" in different_letters and part_two:
        return 1
      return 0
    if len(different_letters) == 4: # One pair
      if "J" in different_letters and part_two:
        return 3
      return 1
    if len(different_letters) == 3:
      if "J" in different_letters and part_two:
        if hand.count("J") > 1 and part_two:
          return 5
      for letter in different_letters:
        if hand.count(letter) == 2: # Two pairs
          if "J" in different_letters and part_two:
            if hand.count("J") == 1:
              return 4
          return 2
        if hand.count(letter) == 3: # One trio
          if "J" in different_letters and part_two:
            if hand.count("J") == 1: 
              return 5
          return 3
    if len(different_letters) == 2:
      if "J" in different_letters and part_two:
        return 6
      for letter in different_letters:
        if hand.count(letter) == 3: # Full house
          return 4
        if hand.count(letter) == 4: # Four of a kind
          return 5
    if len(different_letters) == 1: # Five of a kind
      return 6
        
  
  def letter_value(self, letter, part_two = False):
    if letter.isdigit():
      return int(letter)
    if letter == "T":
      return 10
    if letter == "J":
      if part_two:
        return 1
      return 11
    if letter == "Q":
      return 12
    if letter == "K":
      return 13
    if letter == "A":
      return 14

  def __lt__(self, other):
    if self.type < other.type:
      return True
    if self.type > other.type:
      return False
    for i, letter in enumerate(self.hand):
      if self.letter_value(letter, self.part_two) < self.letter_value(other.hand[i], self.part_two):
        return True
      if self.letter_value(letter, self.part_two) > self.letter_value(other.hand[i], self.part_two):
        return False
    return False
  
  def __gt__(self, other):
    if self.type < other.type:
      return False
    if self.type > other.type:
      return True
    for i, letter in enumerate(self.hand):
      if self.letter_value(letter) > self.letter_value(other.hand[i]):
        return True
      if self.letter_value(letter) < self.letter_value(other.hand[i]):
        return False
    return False


hands = []
for line in lines:
  hand = Hand(line)
  hands.append(hand)

hands.sort()

result = 0
for i in range(len(hands)):
  result += hands[i].points * (i+1)
print("Part one:", result)

for hand in hands:
  hand.recheck_type(True)

hands.sort()

result = 0
for i in range(len(hands)):
  print(hands[i].type, hands[i].hand, "con puntos", hands[i].points, "con ranking", i+1)
  result += hands[i].points * (i+1)
print("Part two:", result)