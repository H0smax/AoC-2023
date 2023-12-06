import sys, re

class Race:
  def __init__(self, time, distance) -> None:
    self.time = time
    self.distance = distance
  
  def ways_to_win(self):
    self.ways = 0
    left_time = self.time
    charged_time = 0
    while left_time > charged_time:
      left_time = self.time - charged_time
      #print("#####################")
      #print("Total time:", self.time)
      #print("Charged time: ", charged_time)
      #print("Movement time: ", left_time)
      #print("New distance", left_time * charged_time)
      if charged_time * left_time > self.distance:
        self.ways += 1
        if charged_time != left_time:
          self.ways += 1
      #print("Counts", self.ways)
      charged_time += 1
    return self.ways
  

filename = sys.argv[1]
lines = []
with open(filename) as file:
  file_lines = file.read().splitlines()
  for line in file_lines:
    lines.append(line)


times = []
distances = []
for line in lines:
  line = line.split()
  if line[0] == "Time:":
    line = line[1:]
    times += line
  if line[0] == "Distance:":
    line = line[1:]
    distances += line

ways_to_win = []
result = 1
for i in range(len(times)):
  race = Race(int(times[i]), int(distances[i]))
  ways_to_win.append(race.ways_to_win())
  result *= race.ways_to_win()
print(ways_to_win)
print("Part one:", result)

# Part two:
single_distance = ""
for distance in distances:
  single_distance += distance

single_time = ""
for time in times:
  single_time += time

single_race = Race(int(single_time), int(single_distance))
print("Part two:", single_race.ways_to_win())