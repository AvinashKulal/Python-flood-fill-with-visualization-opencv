import cv2
import numpy as np

# each number represents color in board
board =[
        [3, 2, 1, 3, 1, 1, 2, 1, 4, 1],
        [2, 1, 1, 4, 1, 1, 4, 1, 3, 1],
        [1, 2, 4, 2, 2, 2, 2, 4, 2, 3],
        [1, 2, 1, 2, 3, 3, 2, 1, 1, 1],
        [3, 4, 3, 2, 1, 1, 2, 1, 3, 1],
        [2, 3, 4, 2, 2, 2, 2, 3, 2, 3],
        [1, 1, 1, 2, 4, 1, 4, 1, 3, 1],
        [4, 2, 1, 2, 3, 2, 1, 3, 2, 3],
        [2, 4, 1, 4, 2, 3, 3, 1, 2, 1],
        [2, 4, 1, 2, 2, 4, 4, 1, 2, 1]
    ]

# display  board here
def flood_vizualize(board,window_name):

    img = np.zeros(( 300,300,3))
    color = [(0,0,255),(0,255,0),(255,0,0),(0,255,255),(255,0,255)]
    row = 0
    for j in range(0,300,30):
        col = 0
        for i in range(0,300,30):

            val = board[row][col]
            b,g,r = color [ val ]
            img = cv2.rectangle(img,(i,j),(i+30,j+30),(b,g,r),-1)
            col += 1
        row +=1
    cv2.imshow(window_name,img)

window_name= 'BEFORE FLOOD FILL'
flood_vizualize(board,window_name)


n = len(board)

#  determine a bounded area
def flood_fill( board,pixel,new_color,prev_color ):

    x,y = pixel
    if x<0 or y<0 or x>=n or  y>=n :
        return

    if board[x][y] != prev_color:
        return

    board[x][y] = new_color
    flood_fill(board,(x,y-1),new_color,prev_color)
    flood_fill(board,(x-1,y),new_color,prev_color)
    flood_fill(board,(x,y+1),new_color,prev_color)
    flood_fill(board,(x+1,y),new_color,prev_color)



px ,py = 2,3 # pixel point to brush
new_color = 0 # brush pixel with red color
prev_color = board[px][py]
flood_fill(board,(px,py),new_color,prev_color)


# call once again for display board for new value that are changed in fool_fill()
win_name = 'AFTER FLOOD FILL'
flood_vizualize(board,win_name)

cv2.waitKey(0)
cv2.destroyAllWindows()
