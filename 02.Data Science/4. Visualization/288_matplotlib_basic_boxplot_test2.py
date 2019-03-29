import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

simple_data=[3,12,15,16,16,17,19,34]
box_plot_data=[simple_data]

fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

box_labels=['s1']
ax1.boxplot(box_plot_data,notch=False, sym='.',vert=True , whis=1.5 , showmeans=True, labels=box_labels)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.set_title('Box plots: Resampling of Two Distributions')
ax1.set_xlabel('Distribution')
ax1.set_ylabel('Value')

plt.show()