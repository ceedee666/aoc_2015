def parse_input_file(input_file):
  with open(input_file) as f:
    lines = f.readlines()

  boxes =[line.split("x") for line in lines]
  boxes = [[int(x) for x in box] for box in boxes]
  return boxes

def solve_part_1(input_file):
  boxes = parse_input_file(input_file)
  sides = [(a*b,b*c,a*c) for a,b,c in boxes]
  paper = [2*a + 2*b +2*c + min(a,b,c) for a,b,c in sides]
  return sum(paper)

def solve_part_2(input_file):
  boxes = parse_input_file(input_file)
  perimeter = [min(2*a+2*b, 2*a+2*c, 2*b+2*c)for a,b,c in boxes]
  volumes = [a*b*c for a,b,c in boxes]
  ribbon = [p+v for p,v in zip(perimeter, volumes)]
  return sum(ribbon)

if __name__ == "__main__":
  print("The elves should order", solve_part_1("input.txt"), "square feet of wrapping paper.")
  print("The elves should order", solve_part_2("input.txt"), "feet of ribbon.")
