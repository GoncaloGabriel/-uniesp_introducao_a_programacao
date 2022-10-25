mtz = [
    [78,90,100],
    [56,77,93],
    [10,4,73],
]

# l = linha / c = coluna
for l in range(len(mtz)):
    for c in range(len(mtz[1])):
        if l == c:  
            print(mtz[l][c])
