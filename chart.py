import csv
import numpy as np
import matplotlib.pyplot as plt

def graph_to_png(x,y,y_min,y_max,y_label,y_color,title,prefix):
	plt.clf()
	plt.cla()
	plt.figure(figsize=(15,5))
	plt.plot(x,y,color=y_color)
	plt.axis([min(x),max(x),y_min,y_max])
	plt.xlabel('Time in Seconds')
	plt.ylabel(y_label)
	plt.title(title)
	plt.savefig('{}{}.png'.format(prefix,int(min(x))),dpi=300)
	plt.close()

data = []

'''for i in range(0,12):
	print("Opening data_part_{}.csv".format(i))
	with open('data_part_{}.csv'.format(i), newline='\r\n') as csvfile:
		reader = csv.reader(csvfile,delimiter=',',quotechar='"')
		while(len(data) <= i):
			data.append([])
		for j,row in enumerate(reader):
			if j == 0:
				continue
			data[i].append([int(row[1]),float(row[2]),float(row[4]),float(row[5]),float(row[6])])'''

for i in range(0,12):
	print("Opening data_part_{}.csv".format(i))
	data = []
	with open('data_part_{}.csv'.format(i),newline='\r\n') as csvfile:
		reader = csv.reader(csvfile,delimiter=',',quotechar='"')
		for j,row in enumerate(reader):
			if j == 0:
				continue
			data.append([int(row[1]),float(row[2]),float(row[4]),float(row[5]),float(row[6])])
	if len(data) == 0:
		continue
	columns = np.transpose(data)
	x = columns[0]
	gwr = columns[1]
	g1 = columns[2]
	g2 = columns[3]
	g3 = columns[4]
	print("Plotting data for {} to {}".format(int(min(x)),int(max(x))))
	graph_to_png(x,gwr,0,2,"GWR Level in Volts","brown","GWR Fill Draw Cycles","data_gwr_")
	print("GWR done")
	graph_to_png(x,g1,0,250,"Gauge Resistance in Ohms","blue","Gauge Number 1 Fill Draw Cycles","data_g1_")
	print("G1 done")
	graph_to_png(x,g2,0,250,"Gauge Resistance in Ohms","red","Gauge Number 2 Fill Draw Cycles","data_g2_")
	print("G2 done")
	graph_to_png(x,g3,0,250,"Gauge Resistance in Ohms","green","Gauge Number 3 Fill Draw Cycles","data_g3_")
	print("G3 done")
	
'''print("{} csv files processed".format(len(data)))

for chunk in data:
	if len(chunk) == 0:
		continue
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
	graph_to_png(x,g3,0,250,"Gauge Resistance in Ohms","green","Gauge Number 3 Fill Draw Cycles","data_g3_")'''

print("Done!")