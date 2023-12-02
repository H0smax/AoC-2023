numbers_as_written = [["one", "1"], ["two", "2"], ["three", "3"], ["four", "4"], ["five", "5"], ["six", "6"], ["seven", "7"], ["eight", "8"], ["nine", "9"]]

numbers = []

filename = "./day_1/input.txt"
with open(filename) as file:
  lines = file.read().splitlines()
  for line in lines:
    first_digit = None
    last_digit = None
    first_digit_index = 99999
    last_digit_index = 0
    current_index = 0
    line_numbers_data = []
    line_numbers_index = []
    for letter in line:
      if letter.isnumeric():
        if first_digit == None:
          first_digit = letter
          first_digit_index = current_index
          line_numbers_data.append(first_digit)
          line_numbers_index.append(first_digit_index)
        last_digit = letter
        last_digit_index = current_index
        line_numbers_data.append(last_digit)
        line_numbers_index.append(last_digit_index)
      current_index += 1
    for number in numbers_as_written:
      if number[0] in line:
        line_numbers_data.append(number[1])
        line_numbers_index.append(line.find(number[0]))
        line_numbers_data.append(number[1])
        line_numbers_index.append(line.rfind(number[0]))
      #print(line_numbers_data)
      #print(line_numbers_index.index(min(line_numbers_index)))
      final_first_line_number = line_numbers_data[line_numbers_index.index(min(line_numbers_index))]
      final_last_line_number = line_numbers_data[line_numbers_index.index(max(line_numbers_index))]
      #print(final_first_line_number)
    number = int(final_first_line_number + final_last_line_number)
    numbers.append(number)
  

print(sum(numbers))
  
  

  

