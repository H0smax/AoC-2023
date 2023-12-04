import re
filename = "./day_4/sample.txt"

lines = []
points = []
with open(filename) as file:
  file_lines = file.read().splitlines()
  for line in file_lines:
    lines.append(line)

for line in lines:
  match = re.search("Card\s+([0-9]+):", line)
  card_id = match.group(1)
  card_content = line.split(":")[1]
  winning_string = card_content.split("|")[0]
  winning_list = winning_string.split(" ")
  winning_list = list(filter(None, winning_list))
  actual_string = card_content.split("|")[1]
  actual_list = actual_string.split(" ")
  actual_list= list(filter(None, actual_list))

  matching_numbers = [int(number) for number in actual_list if number in winning_list]
  points.append(round(pow(2, (len(matching_numbers) - 1))))

print(sum(points))

# Part two

count = 0
while len(lines) > 0:
  line = lines[count]
  match = re.search("Card\s+([0-9]+):", line)
  card_id = match.group(1)
  card_content = line.split(":")[1]
  winning_string = card_content.split("|")[0]
  winning_list = winning_string.split(" ")
  winning_list = list(filter(None, winning_list))
  actual_string = card_content.split("|")[1]
  actual_list = actual_string.split(" ")
  actual_list= list(filter(None, actual_list))

  matching_numbers = [number for number in actual_list if number in winning_list]
  acc_numbers = range(int(card_id) + 1, len(matching_numbers) + int(card_id) + 1)
  acc_quantities = []
  print(acc_numbers)
  if len(matching_numbers) > 0:
    for line in lines:
      match2 = re.search("Card\s+([0-9]+):", line)
  count += 1

print("Part two:", count)