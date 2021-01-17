A = [
    [3,5,8],
    [4,9,1],
    [6,2,2]
]

print(A) # => [[3,5,8],[4,9,1],[6,2,2]]
print(A[0]) # => [3,5,8]
print(A[0][0]) # => 3

data = [[1,9],[2,8],[3,7],[4,6]]

x = []
y = []

for pair in data:
    x.append(pair[0])
    y.append(pair[1])

print(x)
print(y)