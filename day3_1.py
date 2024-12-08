from sys import stdin
from re import findall

def parse(input: str):
  return findall(r"mul\((\d{1,3}),\s*(\d{1,3})\)", input)

def get_sum(parsed_input: list):
  result = 0
  for pair in parsed_input:
    result += int(pair[0]) * int(pair[1])
  return result

lines = stdin.readlines()
input = ""
for line in lines:
  input += line

print(get_sum(parse(input)))
