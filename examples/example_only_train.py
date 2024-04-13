from liveplotlib import LivePlotOnlyTrain


J_history = []


live_plot = LivePlotOnlyTrain(slice_fraction=0.1, slice_bias=10)


# XXXXXXXX Don't worry about this code XXXXXXXXXXX
# (it is just simulation for demonstration)
import random
import time
import numpy as np

SIMULATION_SPEED = 1.5
ITERS = 100

for i in np.linspace(0.7, 0.1, ITERS):
    time.sleep(1 / (SIMULATION_SPEED * 10))

    new_J = (i  + (random.random() - 0.5) * 0.1)
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    J_history.append(new_J)
    live_plot.update(J_history)


live_plot.close()


# import matplotlib.pyplot as plt
# plt.plot(J_history)
# plt.title('J_history')
# plt.show()
