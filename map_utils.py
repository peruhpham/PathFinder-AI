import numpy as np
from PIL import Image
import cv2
from constants import MAP, M, N, W, mau_den, mau_trang

def generate_maze_image():
    image = np.ones((M * W, N * W, 3), np.uint8) * 255

    for x in range(0, M):
        for y in range(0, N):
            if MAP[x][y] == '#':
                image[x * W:(x + 1) * W, y * W:(y + 1) * W] = mau_den
            elif MAP[x][y] == ' ':
                image[x * W:(x + 1) * W, y * W:(y + 1) * W] = mau_trang

    color_converted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return Image.fromarray(color_converted)
