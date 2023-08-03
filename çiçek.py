import matplotlib.pyplot as plt
import numpy as np

# Dairelerin merkez koordinatlarını hesaplayın
t = np.linspace(0, 2 * np.pi, 100)
x = 0.5 * np.sin(6 * t) * np.cos(t)
y = 0.5 * np.sin(6 * t) * np.sin(t)

# Daireleri çizin
fig, ax = plt.subplots()
ax.plot(x, y, color='purple', linewidth=3)

# Çiçeğin yapraklarını çizin
ax.fill_between(x, y, where=(x > 0), interpolate=True, color='green', alpha=0.4)
ax.fill_between(x, y, where=(x < 0), interpolate=True, color='green', alpha=0.4)

# Çiçeğin merkezini çizin
ax.scatter(0, 0, s=200, color='yellow')

# Eksenleri kapatın ve grafiği gösterin
ax.axis('off')

plt.show()

