import numpy as np
import matplotlib.pyplot as plt


width, height = 800, 800
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5
max_iter = 100


image = np.zeros((height, width))


for x in range(width):
    for y in range(height):
        real = x_min + (x / width) * (x_max - x_min)
        imag = y_min + (y / height) * (y_max - y_min)
        c = complex(real, imag)
        z = 0
        count = 0
        while abs(z) <= 2 and count < max_iter:
            z = z**2 + c
            count += 1
        image[y, x] = count


plt.imshow(image, cmap='hot', extent=[x_min, x_max, y_min, y_max])
plt.title("Mandelbrot Set")
plt.xlabel("Re")
plt.ylabel("Im")
plt.colorbar(label="Iterations")
plt.savefig("mandelbrot.png", dpi=300)
plt.show()

