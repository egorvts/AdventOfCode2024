from sys import stdin

left, right = [], []

for line in stdin:
  splitLine = line.split()
  left.append(int(splitLine[0]))
  right.append(int(splitLine[1]))

left.sort()
right.sort()

distance = 0
for i in range(len(left)):
  distance += abs(left[i] - right[i])

print(distance)