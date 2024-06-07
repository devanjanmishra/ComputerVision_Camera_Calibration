import cv2
import numpy as np

# Define the dimensions of the chessboard
rows, cols = 6, 9 # of squares
square_size = 50  # size of squares in pixels

# Create a chessboard image
img = np.zeros((rows * square_size, cols * square_size, 3), dtype=np.uint8)

for i in range(rows):
    for j in range(cols):
        if (i + j) % 2 == 0:
            cv2.rectangle(img, (j * square_size, i * square_size),
                          ((j + 1) * square_size, (i + 1) * square_size),
                          (255, 255, 255), -1)

# Save the chessboard image
cv2.imwrite('chessboard.png', img)
