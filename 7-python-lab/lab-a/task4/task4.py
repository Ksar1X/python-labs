import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=0, scale=1, size=10000)
bins = 10
fig, axes = plt.subplots(1, 2, figsize=(12, 5))


axes[0].hist(data, bins=bins)
axes[0].set_title("Histogram (10 bins)")
axes[0].set_xlabel("Value")
axes[0].set_ylabel("Frequency")

counts, bin_edges = np.histogram(data, bins=bins)

bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

axes[1].bar(bin_centers, counts, width=(bin_edges[1] - bin_edges[0]))
axes[1].set_title("Bar Plot (10 bins)")
axes[1].set_xlabel("Value")
axes[1].set_ylabel("Frequency")

plt.tight_layout()

plt.show()