import sys, re
from math import lcm
filename = sys.argv[1]
lines = []
nodes = []
lefts = []
rights = []
with open(filename) as file:
  file_lines = file.read().splitlines()
  for line in file_lines:
    lines.append(line)
    nodes.append(line[0:3])
    lefts.append(line[7:10])
    rights.append(line[12:15])

nodes = nodes[2:]
rights = rights[2:]
lefts = lefts[2:]
instructions = lines[0]

current_node = "AAA"

i = 0
steps = 0
while current_node != "ZZZ":
  steps += 1
  if i == len(instructions):
    i = 0
  current_node_index = nodes.index(current_node)
  if instructions[i] == "L":
    current_node = lefts[current_node_index]
  if instructions[i] == "R":
    current_node = rights[current_node_index]
  i += 1

print("Part one:", steps)

current_nodes = []

for node in nodes:
  if re.search("\w\wA", node):
    current_nodes.append(node)

print(current_nodes)

def check_finished_nodes(nodes):
  for node in nodes:
    if not re.search("\w\wZ", node):
      return False
  return True

i = 0
steps_to_first_match = []
z_nodes = []
for current_node in current_nodes:
  steps = 0
  while not re.search("\w\wZ", current_node):
    steps += 1
    if i == len(instructions):
      i = 0
    current_node_index = nodes.index(current_node)
    if instructions[i] == "L":
      current_node = lefts[current_node_index]
    if instructions[i] == "R":
      current_node = rights[current_node_index]
    i += 1
  z_nodes.append(current_node)
  steps_to_first_match.append(steps)

steps = lcm(*steps_to_first_match)


print(steps_to_first_match)
print("Part two:", steps)