from sys import stdin

left, right = [], []

for line in stdin:
  splitLine = line.split()
  left.append(int(splitLine[0]))
  right.append(int(splitLine[1]))

left.sort()
right.sort()

similarity = 0
for i in range(len(left)):
  similarity += left[i] * right.count(left[i])

print(similarity)