import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

files = [
    "1. Keto.xlsx",
    "2. Carnivore.xlsx",
    "3. Lion Diet.xlsx",
    "4. Raw Lion Diet.xlsx",
    "5. Lion Diet.xlsx",
    "6. Relaxed Carnivore.xlsx",
]

weight = []
time = []

for f in files:
    a = pd.read_excel(f)

    x = list(a["Дата"].dropna())
    y = list(a["Вес"].dropna())

    ms = min(len(x), len(y))

    x = x[:ms]
    y = y[:ms]

    time += x
    weight += y

time2 = [time[i].timestamp() for i in range(len(time))]

fig, ax = plt.subplots()
fig.canvas.manager.set_window_title("exFatLoss")

model = np.poly1d(np.polyfit(time2, weight, 3))
deriv = model.deriv()

# ax.plot(time, model(time2), color="#8acfa0", alpha=0.5)
# ax.axhspan(60, 81, facecolor="#82be48", alpha=0.25)
# ax.axhspan(81, 97, facecolor="#ffc232", alpha=0.25)
ax.axhline(75, color="r", alpha=0.5)

edgecolors = ['#82BE48' if 60 < i < 81 else '#FFC232' if 81 < i < 97 else '#D5232B' for i in weight]

ax.scatter(time, weight, facecolors="none", edgecolors=edgecolors, s=10)

fig.show()
