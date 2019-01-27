import sys
import time
import copy
import keyboard as kb
import fileInput as fin

# define variables
infile = 'tas_tut_total.json'
keys = [ 'w', 'a', 'd', 'j', 'k', 's' ]
wait = 'f'

# game runs at 60 fps
def to_frames(int):
	return int/60

# function for sorting unordered simulaneous inputs
def sortFirst(val):
	return val[0]

# press keys
# conc_keys = list of concurrent keys
# do not have both an f key and something else
def typekey(conc_keys):
	# f key is for pausing all actions
	if conc_keys[0][1] == 'f':
			waitframes(conc_keys[0][0])
	else:
		conc_keys.sort(key = sortFirst)

		# gather all simul inputs
		inputstr = ''
		for fcmd in conc_keys:
			inputstr = inputstr + fcmd[1] + ', '
		# remove last comma and space
		inputstr = inputstr[:(len(inputstr)-2)]
		kb.press(inputstr)

		# release buttons, shortest duration first
		# fcmd = frame, command
		for fcmd in conc_keys:
			waittime = fcmd[0]
			waitframes(waittime)
			kb.release(fcmd[1])
			del fcmd
			# update other wait times according to current
			for others in conc_keys:
				others[0] -= waittime

# sleep for a given num of frames
def waitframes(frames):
	time.sleep(to_frames(frames))

if __name__ == '__main__':
	filepath = infile
	data = fin.parse_file(filepath)
	for elem in data:
		# action
		if elem[0] == "key":
			i = elem[2]
			while i > 0:
				typekey(copy.deepcopy(elem[1]))
				i -= 1
		# comment printed on console
		elif elem[0] == "comment":
			print(elem[1])
		else:
			sys.exit('invalid input: element type error')
