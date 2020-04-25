import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
plt.style.use('seaborn')

x_vals = []
y_vals = []

index = count()

def animation(i):
	data = pd.read_csv('data.csv')
	x = data['x_value']
	y1 = data['total_one']
	y2 = data['total_two']

	# x_vals.append(next(index))
	# y_vals.append(random.randint(0,5))

	plt.cla()
	plt.plot(x,y1,label='Stock 1')
	plt.plot(x,y2,label='Stock 2')
	plt.legend(loc='upper left')
	plt.tight_layout()

animate = FuncAnimation(plt.gcf(), animation, interval=1000)
plt.tight_layout()
plt.show()


# Note: First Run update_data.py file then run this file 
# real time plotting live data
# If you want to Stop live data then first stop update_data file.

