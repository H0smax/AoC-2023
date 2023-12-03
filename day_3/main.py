import re

filename = "./day_3/input.txt"
lines = []
adjacent_numbers = []
with open(filename) as file:
  file_lines = file.read().splitlines()
  for line in file_lines:
    lines.append(line)

for line_index in range(len(lines)):
  line = lines[line_index]
  number_matches = re.finditer("([0-9]+)", line)
  #print("Line:", line)
  for match in number_matches:
    #print("Looking at number", match)
    start_index = match.start()
    end_index = match.end() - 1
    # Cover diagonals
    if start_index > 0:
      start_index -= 1
    if end_index < len(line) - 1:
      end_index += 1

    # Check laterals:
    if re.search("[^\w.]", line[start_index]):
      #print("Left symbol:", line[start_index])
      adjacent_numbers.append(int(match.group()))
      continue
    
    if re.search("[^\w.]", line[end_index]):
      #print("Right symbol:", line[end_index])
      adjacent_numbers.append(int(match.group()))
      continue

    # Check up
    if line_index != 0:
      adjacent_upper = lines[line_index - 1][start_index:end_index + 1]
      #print("Upper line adjacent:", adjacent_upper)
      if re.search("[^\w.]", adjacent_upper):
        #print("Up symbol")
        adjacent_numbers.append(int(match.group()))
        continue
      
    # Check down
    if line_index != len(lines) - 1:
      adjacent_lower = lines[line_index + 1][start_index:end_index + 1]
      #print("Lower line adjacent:", adjacent_lower)
      if re.search("[^\w.]", adjacent_lower):
        #print("Down symbol")
        adjacent_numbers.append(int(match.group()))
        continue

print("Part one:", sum(adjacent_numbers))

# Part two
gear_ratios = []
for line_index in range(len(lines)):
  line = lines[line_index]
  gear_matches = re.finditer("(\*)", line)
  for gear in gear_matches:
    connected_numbers = []
    gear_index = gear.start()
    # Upper row
    for number in re.finditer("([0-9]+)", lines[line_index - 1]):
      if gear_index - 1 in range(number.start(), number.end()):
        connected_numbers.append(number.group())
        continue
      if gear_index in range(number.start(), number.end()):
        connected_numbers.append(number.group())
        continue
      if gear_index + 1 in range(number.start(), number.end()):
        connected_numbers.append(number.group())
        continue
    # Same row
    for number in re.finditer("([0-9]+)", lines[line_index]):
      if gear_index - 1 in range(number.start(), number.end()):
        connected_numbers.append(number.group())
        continue
      if gear_index + 1 in range(number.start(), number.end()):
        connected_numbers.append(number.group())
        continue

    # Lower row
    for number in re.finditer("([0-9]+)", lines[line_index + 1]):
      if gear_index - 1 in range(number.start(), number.end()):
        connected_numbers.append(number.group())
        continue
      if gear_index in range(number.start(), number.end()):
        connected_numbers.append(number.group())
        continue
      if gear_index + 1 in range(number.start(), number.end()):
        connected_numbers.append(number.group())
        continue
    if len(connected_numbers) == 2:
      gear_ratio = int(connected_numbers[0]) * int(connected_numbers[1])
      gear_ratios.append(gear_ratio)

print("Part two:", sum(gear_ratios))
    