import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
x = np.array([0,1,2,3,4,5,6,7,8,9,10])
y = np.array([0,1,2,3,4,5,6,7,8,9,10])
fig,ax = plt.subplots()
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.plot(x, y, label = 'NVLINK Bandwidth')
fig.set_figheight(10)
fig.set_figwidth(15)
ax.legend(loc = 'lower right',fontsize = 'xx-large')
ax.grid()
ax.set_xlabel('Vector Size (divided by 2^12 Bytes)',fontsize  = 'xx-large')
ax.set_ylabel('MB/s',fontsize  = 'xx-large')
plt.show()
