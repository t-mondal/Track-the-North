# import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from time import sleep
import pandas as pd

# initiate running variable which is True until end of input (i.e. end of video)
running = True

# initiate latest frame variable to hold id of latest time frame
latest_frame = -1

#initiate list to hold data
data = pd.DataFrame(columns=['frame', 'time', 'object_type', 'object_id', 'x', 'y'])
new_data = data

# while loop keeps running until end of input
while running == True:
	try:
		# get data from input text file
		with open('new_data.txt', 'r') as f:
			new_data = pd.read_csv(f, sep = " ")
			# latest frame id
			frame_id = new_data.iloc[0,0]
			# if input has not been updated, then nothing needs to be added for this iteration
			if frame_id == latest_frame:
				#sleep(10)
				continue
			else:
				# update to newest frame
				latest_frame = frame_id
				data = data.append(new_data, ignore_index = True)
	# Use ^C to exit when enough data is collected, or when necessary (emergency, etc.)
	except KeyboardInterrupt:
		break

# spacing out output
print '\n'

# Colour dictionary
colour_dict = {0:'b', 1:'g', 2:'r', 3:'c', 4:'m', 5:'y'}
letter_dict = {0:'blue', 1:'green', 2:'red', 3:'cyan', 4:'magenta', 5:'yellow'}

# list of unique objects and making corresponding legend
objects = data['object_id'].unique()
legend_dict = {}

for num in range(len(objects)):
	legend_dict[letter_dict[num]] = objects[num]

# display legend
print 'Legend: '
for each in legend_dict:
	print each + ': ' + str(legend_dict[each])

# for each object
for o in range(len(objects)):
	# set a colour
	colour = colour_dict[o]
	# find the unique frames of this object
	frames = data[data['object_id']==objects[o]]['frame'].unique()
	#number of unique frames
	num_frames = len(frames)

	# for each frame for each object
	for f in range(num_frames):
		# set a transparency based on where in object's path
		transparency = float(f)/num_frames

		# all points in object's path at a specific frame
		point = data[(data['object_id']==objects[o]) & (data['frame']==frames[f])]
		# plot point with corresponding colour and transparency
		plt.plot(point['x'], point['y'], colour + 'o', alpha=transparency)
# display graph
plt.show()

#write values to files
with open('dataframe.txt', 'w') as f:
 	f.write(str(data))

# with open('y.txt', 'w') as f:
# 	for row in range(len(data)):
# 		f.write(str(data.iloc[row]['time']) + ',' + str(data.iloc[row]['y']) + '\n')

# # load back data
# t1, x = np.loadtxt('x.txt',delimiter=',', unpack = False)#,) unpack=True)
# t2, y = np.loadtxt('y.txt',delimiter=',', unpack = False)#,) unpack=True)

