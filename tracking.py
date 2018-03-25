def penyelesaian(jalur, posisi, N):
    # jalur yang akan ditempuh untuk sampai
    if posisi == (N - 2, N - 4):
        return [(N - 2, N - 4)]
    x, y = posisi

    #proses bergeser ke kanan
    if x + 1 < N and jalur[x+1][y] == 1:
        a = penyelesaian(jalur, (x + 1, y), N )
        if a != None:
            return [(x,y)] + a

    # proses bergeser ke bawah
    if y + 1 < N and jalur[x][y+1] == 1:
        b = penyelesaian(jalur,(x,y + 1), N)
        if b != None:
            return [(x, y)] + b

    # proses bergeser ke kiri
    if y - 1 < N and jalur[x][y-1] == 1:
        c = penyelesaian(jalur,(x,y - 1), N)
        if c != None:
            return [(x, y)] + c

jalur =[[1,1,1,0,1,1,1,1],
       [1,1,0,0,0,1,1,0],
       [1,1,1,1,1,1,1,0],
       [1,1,1,1,1,1,1,0],
       [0,0,0,1,1,1,1,0],
       [1,1,1,0,0,1,1,0],
       [1,1,1,1,1,1,0,1],
       [1,1,1,1,0,0,1,1]
        ]
print(penyelesaian(jalur,(0,1),8))
