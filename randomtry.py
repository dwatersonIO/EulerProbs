chessboard = {}
for row in range(8):
    for col in range(8):
        chessboard[(row,col)] = 0

chessboard[(2, 2)]="D"
print (chessboard)

counter=0
for key in sorted(chessboard):
    print(chessboard[key], end=" ")
    counter = counter +1
    if counter % 8 == 0:
        print()    
