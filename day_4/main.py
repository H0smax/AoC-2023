import re
filename = "./day_4/input.txt"

lines = []
points = []
matching_amounts = []
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
  matching_amounts.append(len(matching_numbers))

print("Part one:", sum(points))

# Part two
counts = []
for line in lines:
  counts.append(1)

for i in range(len(points)):
  if points[i] > 0:
    for amount in range(matching_amounts[i]):
      next_to_add = i + amount + 1 
      if next_to_add < len(counts):  
        print(i, "Añado", counts[i], " a", next_to_add + 1)
        counts[next_to_add] += counts[i]
print(points)
print(counts)
print("Part two:", sum(counts))