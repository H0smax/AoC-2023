import sys


filename = sys.argv[1]
lines = []
with open(filename) as file:
  file_lines = file.read().splitlines()
  for line in file_lines:
    lines.append(line)

def get_n_term(numbers):
  if sum(numbers) == 0:
    return 0
  new_diffs = [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]
  n = get_n_term(new_diffs)
  return numbers[len(numbers) - 1] + n

numbers = []
previous = []
for line in lines:
  terms = line.split()
  terms = [int(term) for term in terms]
  # Part one
  number = get_n_term(terms)
  # Part two
  reverse_number = get_n_term(terms[::-1])
  previous.append(reverse_number)
  numbers.append(number)

print("Part one", sum(numbers))
print("Part two", sum(previous))