import matplotlib.pyplot as plt
import numpy as np

# Start and end points
p = np.array([2, 2])
q = np.array([8, 5])

# Euclidean distance line
euclidean_line_x = [p[0], q[0]]
euclidean_line_y = [p[1], q[1]]

# 8-neighbor approximate path
path_x = [p[0]]
path_y = [p[1]]

dx = q[0] - p[0]
dy = q[1] - p[1]

# 8-neighbor movement: diagonal first, then straight
min_d = min(abs(dx), abs(dy))
max_d = max(abs(dx), abs(dy))

# Generate 8-neighbor path points
x, y = p
for i in range(min_d):
    x += np.sign(dx)
    y += np.sign(dy)
    path_x.append(x)
    path_y.append(y)

for i in range(max_d - min_d):
    if abs(dx) > abs(dy):
        x += np.sign(dx)
    else:
        y += np.sign(dy)
    path_x.append(x)
    path_y.append(y)

# Plotting
plt.figure(figsize=(6,6))
plt.plot(euclidean_line_x, euclidean_line_y, 'b-', label='Euclidean distance')
plt.plot(path_x, path_y, 'ro-', label='8-neighbor approximate distance')

# Mark start and end points
plt.scatter(*p, c='green', s=100, label='Start p')
plt.scatter(*q, c='purple', s=100, label='End q')

plt.grid(True)
plt.xticks(range(0, 11))
plt.yticks(range(0, 11))
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title('8-Neighbor Euclidean Approximation Example')
plt.show()
