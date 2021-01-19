import csv
import numpy as np
import matplotlib.pyplot as plt

def graph_to_png(x,y,y_min,y_max,y_label,y_color,title,prefix):
	plt.clf()
	plt.cla()
	plt.plot(x,y,color=y_color)
	plt.axis([min(x),max(x),y_min,y_max])
	plt.xlabel('Time in Seconds')
	plt.ylabel(y_label)
	plt.title(title)
	plt.savefig('{}{}.png'.format(prefix,int(min(x))))

data = []

for i in range(0,12):
	print("Opening data_part_{}.csv".format(i))
	with open('data_part_{}.csv'.format(i), newline='\r\n') as csvfile:
		reader = csv.reader(csvfile,delimiter=',',quotechar='"')
		data.append([])
		for j,row in enumerate(reader):
			if j == 0:
				continue
			data[i].append([int(row[1]),float(row[2]),float(row[4]),float(row[5]),float(row[6])])

print("{} csv files processed".format(len(data)))

for chunk in data:
	columns = np.transpose(chunk)
	x = columns[0]
	gwr = columns[1]
	g1 = columns[2]
	g2 = columns[3]
	g3 = columns[4]
	print("Plotting data for {} to {}".format(int(min(x)),int(max(x))))
	graph_to_png(x,gwr,0,2,"GWR Level in Volts","brown","GWR Fill Draw Cycles","data_gwr_")
	graph_to_png(x,g1,0,250,"Gauge Resistance in Ohms","blue","Gauge Number 1 Fill Draw Cycles","data_g1_")
	graph_to_png(x,g2,0,250,"Gauge Resistance in Ohms","red","Gauge Number 2 Fill Draw Cycles","data_g2_")
	graph_to_png(x,g3,0,250,"Gauge Resistance in Ohms","green","Gauge Number 3 Fill Draw Cycles","data_g3_")

"""columns = np.transpose(data[0])
x_axis, y_axis = columns[0], columns[2]
plt.plot(x_axis,y_axis)
plt.grid()
plt.axis([min(x_axis),max(x_axis),min(y_axis),max(y_axis)])
plt.title('Testing')
plt.savefig('data_0_GWR.png')
print('Done!')"""
