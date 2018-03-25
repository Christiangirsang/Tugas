def penyelesaian(jalur, posisi, N):
    # returns a list of the paths taken
    if posisi == (N - 1, N - 1):
        return [(N - 1, N - 1)]
    x, y = posisi
    if x + 1 < N and jalur[x+1][y] == 1:
        a = penyelesaian(jalur, (x + 1, y), N )
        if a != None:
            return [(x,y)] + a

    if y + 1 < N and jalur[x][y+1] == 1:
        b = penyelesaian(jalur,(x,y + 1), N)
        if b != None:
            return [(x, y)] + b

jalur =[[1,1,1,0,1,1,1,1],
       [1,1,0,0,0,1,1,0],
       [1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0],
       [0,0,0,1,1,1,0,0],
       [1,1,1,0,0,1,1,0],
       [1,1,1,1,1,1,1,1],
       [1,1,1,1,0,0,1,1]
        ]
print(penyelesaian(jalur,(0,1),8))