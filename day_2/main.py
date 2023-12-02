from game import Game

filename = "./day_2/input.txt"
with open(filename) as file:
  lines = file.read().splitlines()
  sum_of_possible_id = 0
  sum_of_power = 0
  for line in lines:
    game = Game(line)

    # Part one
    if game.possible:
      sum_of_possible_id += game.id

    # Part two
    sum_of_power += game.max_red * game.max_green * game.max_blue

  print("Part one:", sum_of_possible_id)
  print("Part two:", sum_of_power)