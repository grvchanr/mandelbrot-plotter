import pygame
import numpy as np

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 300
MAX_ITER = 50
ZOOM_FACTOR = 0.8

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mandelbrot Zoom Explorer")

# Initial complex plane boundaries
x_min, x_max = -2.5, 1.5
y_min, y_max = -1.5, 1.5

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def draw_set(xmin, xmax, ymin, ymax):
    step = 2   # draw every 2nd pixel
    for x in range(0, WIDTH, step):
        for y in range(0, HEIGHT, step):
            re = xmin + (x / WIDTH) * (xmax - xmin)
            im = ymin + (y / HEIGHT) * (ymax - ymin)
            c = complex(re, im)
            m = mandelbrot(c, MAX_ITER)
            color = 255 - int(m * 255 / MAX_ITER)
            # fill a little block so it looks solid
            for dx in range(step):
                for dy in range(step):
                    px = x + dx
                    py = y + dy
                    if px < WIDTH and py < HEIGHT:
                        screen.set_at((px, py), (color, color, color))
    pygame.display.flip()


# Main loop
running = True
draw_set(x_min, x_max, y_min, y_max)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Zoom in with mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            re = x_min + (mx / WIDTH) * (x_max - x_min)
            im = y_min + (my / HEIGHT) * (y_max - y_min)

            # Zoom in or out
            if event.button == 1:  # Left click = zoom in
                zoom = ZOOM_FACTOR
            elif event.button == 3:  # Right click = zoom out
                zoom = 1 / ZOOM_FACTOR
            else:
                zoom = 1

            width = (x_max - x_min) * zoom
            height = (y_max - y_min) * zoom
            x_min = re - width / 2
            x_max = re + width / 2
            y_min = im - height / 2
            y_max = im + height / 2

            draw_set(x_min, x_max, y_min, y_max)

pygame.quit()
