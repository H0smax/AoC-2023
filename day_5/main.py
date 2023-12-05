filename = "./day_5/input.txt"

lines = []
with open(filename) as file:
  file_lines = file.read().splitlines()
  for line in file_lines:
    lines.append(line)

seeds = lines[0][6:].split()
seeds = [int(i) for i in seeds]

print("seeds generated")

differences = []
current_diff = []
ranges = []
current_range = []
for i in range(3, len(lines)):
  line = lines[i]
  if line == "":
    differences.append(current_diff)
    ranges.append(current_range)
    current_diff = []
    current_range = []
    continue
  elif "map:" in line:
    continue
  line = line.split()
  source = int(line[1])
  destiny = int(line[0])
  leng = int(line[2])
  difference = destiny - source
  current_range.append([source, source + leng])
  current_diff.append(difference)

differences.append(current_diff)
ranges.append(current_range)
#print(differences)

# Part one:
def part_one(seeds):
  global ranges
  global differences
  for e, seed in enumerate(seeds):
    for i, event in enumerate(ranges):
      already_match = False
      for j, limit in enumerate(ranges[i]):
        if seed >= limit[0] and seed <= limit[1] and not already_match: 
          seed += differences[i][j]
          already_match = True
    locations.append(seed)
  return locations
locations = []
locations = part_one(seeds)
print("Part one:", min(locations))


