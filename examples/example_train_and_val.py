import matplotlib.pyplot as plt
import numpy as np
import random
import time

from liveplotlib import LivePlotTrainAndVal


J_train_history = []
J_val_history = []

live_plot = LivePlotTrainAndVal(slice_bias=10, slice_fraction=0.1)


# xxxxxxxxxx Don't worry about this code xxxxxxxxxx
# (it is just simulation for demonstration)
SIMULATION_SPEED = 1.5
NUM_ITERATIONS = 100

for i, num in enumerate(np.linspace(0, 0.8, NUM_ITERATIONS)):
    print(f"[Iteration {i}]")
    time.sleep(1 / (SIMULATION_SPEED * 10))

    new_J_train = 1 - num**(1/4) + ((random.random() - 0.5) * 0.1)

    new_J_val = (num - 0.8)**2 + 0.2 + ((random.random() - 0.5) * 0.1)
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

    J_train_history.append(new_J_train)
    J_val_history.append(new_J_val)
    live_plot.update(J_train_history, J_val_history)

plt.show()
# live_plot.close()

# plt.plot(J_train_history)
# plt.plot(J_val_history)
# plt.show()