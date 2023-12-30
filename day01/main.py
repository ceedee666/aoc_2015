def solve_part_1(input_file):
  with open(input_file) as f:
    lines = f.readlines()

  values = [1 if ch == "(" else -1 for ch in lines[0]]
  return sum(values)

def solve_part_2(input_file):
  with open(input_file) as f:
    lines = f.readlines()

  values = [1 if ch == "(" else -1 for ch in lines[0]]
  sum =0
  for i, val in enumerate(values):
    sum += val
    if sum == -1:
      return i+1

if __name__ == "__main__":
  print("The instructions take Santa to floor", solve_part_1("input.txt"))
  print("The character at position", solve_part_2("input.txt"), "causes Santa to first enter floor -1")