import matplotlib.pyplot as plt
import numpy as np
for procs in [1,2,4,8]:
    with plt.xkcd():
        fig, ax = plt.subplots()
        labels = ["Collecting\nresults", "Preprocessing", "Parallel work"]
        sizes = [0.05, 0.1, 0.85/procs]

        ax.pie(sizes, labels=labels, normalize=False)
        ax.set_title(f"Proportion of runtime ({procs} processors)")
        fig.savefig(f"workload_example_{procs}.svg")
