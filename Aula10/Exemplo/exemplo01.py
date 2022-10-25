mtz =[ 
[78, 90, 100, 98, 7],
[56, 72, 93, 77, 93],
[10, 4, 73, 77, 93],
[78, 90, 17, 13, 55],
]

for l in range(len(mtz)):
    for c in range(len(mtz[1])):

        if l == c:
            print(mtz[l][c])
        
        if(mtz[l][c] %2) == 0:
            print(f"{mtz[1][c]} ->É par!")
        else:
            print(f"{mtz[1][c]} ->É ímpar!")
