import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
proba = [0.1, 0.2, 0.3, 0.4]
etats = np.array(['A', 'B', 'C', 'D'])
Simulation = np.random.choice(etats, size=1000, replace=True, p=proba)
print(Simulation[0:6])

bars = np.array(['A', 'B', 'C', 'D'])
y_pos = np.arange(len(bars))

a = len([lettre for lettre in Simulation if lettre == 'A']) / 1000.
b = len([lettre for lettre in Simulation if lettre == 'B']) / 1000.
c = len([lettre for lettre in Simulation if lettre == 'C']) / 1000.
d = len([lettre for lettre in Simulation if lettre == 'D']) / 1000.
height = np.array([a, b, c, d])

barlist = plt.bar(y_pos, height, edgecolor='blue', alpha=0.7, color=['blue', 'blue', 'blue'])  #
plt.xticks(y_pos, bars, color='black', fontweight='bold')
plt.box(False)
plt.yticks([])
for i in range(0, len(height)):
    plt.text(y_pos[i], height[i] + 0.5, str(height[i]), color='black', fontweight='bold')
plt.show()