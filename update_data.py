import csv 
import random
import time

x_value = 0
total_one = 1000
total_two = 1000

fieldnames = ['x_value','total_one','total_two']

with open('data.csv','w') as csv_file:
	csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	csv_writer.writeheader()

while True:
	with open('data.csv','a') as csv_file:
		csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

		info = {
			'x_value': x_value,
			'total_one': total_one,
			'total_two': total_two,
		}

		csv_writer.writerow(info)
		print(x_value, total_one, total_two)

		x_value += 1
		total_one = total_one + random.randint(-5, 7)
		total_two = total_two + random.randint(-6, 8)

	time.sleep(1)

