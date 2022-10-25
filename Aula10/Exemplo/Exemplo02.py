mtz = [
    [78,90,100],
    [56,77,93],
    [10,4,73]
]
# l - linha / c = coluna
for l in range(len(mtz)):
    
    for c in range(len(mtz[l])):

        if l == c:
            print(mtz[l][c])

        if (mtz [l][c] % 2) == 0:
            print(f"{mtz[l][c]}-> É par!")
        else:
            print(f"{mtz[l][c]}-> É ímpar!!")
