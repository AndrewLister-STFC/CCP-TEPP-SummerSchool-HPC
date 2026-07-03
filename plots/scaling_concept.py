import matplotlib.pyplot as plt
import numpy as np
with plt.xkcd():
    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.spines[['top', 'right']].set_visible(False)
    ax.set_xticks([1,2,3,4,5,6,7], labels=["1", "2", "4", "8", "16", "32", "..."])
    ax.set_yticks([1,2,3,4,5,6,7], labels=["1", "2", "4", "8", "16", "32", "..."])
    ax.set_ylim(1, 7)

    x = np.linspace(1, 7, num=100)
    best_case = [d*1 for d in x]
    average_case = [1/(0.1 + 0.9/d) for d in x]
    worst_case = [1/(0.5 + 0.5/d) for d in x]

    ax.annotate(
        'Perfect scaling',
        xy=(5, 5), arrowprops=dict(arrowstyle='->'), xytext=(3.5, 6))

    # ax.annotate(
    #     'P scaling',
    #     xy=(5, 5), arrowprops=dict(arrowstyle='->'), xytext=(4, 4))

    ax.plot(x, worst_case)
    ax.plot(x, average_case)
    ax.plot(x, best_case)


    ax.set_xlabel('processors')
    ax.set_ylabel('speedup')
    fig.savefig("scaling_concept.svg")
