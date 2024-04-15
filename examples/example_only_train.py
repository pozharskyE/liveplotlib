from liveplotlib import LivePlotOnlyTrain

J_train_history = []


live_plot = LivePlotOnlyTrain(slice_fraction=0.1, slice_bias=10)


# XXXXXXXX Don't worry about this code XXXXXXXXXXX
# (it is just simulation for demonstration)
import random
import time
import numpy as np

SIMULATION_SPEED = 1
NUM_ITERATIONS = 100

old_J_train = None
for i, num in enumerate(np.linspace(0.7, 0.1, NUM_ITERATIONS)):
    print(f"[Iteration {i} started]")
    time.sleep(1 / (SIMULATION_SPEED))

    new_J_train = (num  + (random.random() - 0.5) * 0.1)

    print(f"J_train: {old_J_train} => {new_J_train}")
    old_J_train = new_J_train
    print('----------------------------------------')
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    J_train_history.append(new_J_train)
    live_plot.update(J_train_history)




# Making the plot stay after everything is done
import matplotlib.pyplot as plt
plt.show()

# live_plot.close()


# plt.plot(J_history)
# plt.title('J_history')
# plt.show()
