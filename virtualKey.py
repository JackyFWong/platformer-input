import sys
import time
import keyboard as kb
import fileInput as fin

# define variables
keys = [ 'w', 'a', 'd', 'j', 'k' ]
wait = 'f'

def to_frames(int):
	return int/60

def sortFirst(val):
	return val[0]

def typekey(conc_keys):
	if conc_keys[0][1] == 'f':
			waitframes(conc_keys[0][0])
	else:
		conc_keys.sort(key = sortFirst)
		# might be too slow
		inputstr = ''
		for fcmd in conc_keys:
			inputstr = inputstr + fcmd[1] + ', '
		inputstr = inputstr[:(len(inputstr)-2)]
		kb.press(inputstr)
		for fcmd in conc_keys:
			waittime = fcmd[0]
			waitframes(waittime)
			kb.release(fcmd[1])
			del conc_keys[0]
			for others in conc_keys:
				others[0] -= waittime

def waitframes(frames):
	time.sleep(to_frames(frames))

if __name__ == '__main__':
	filepath = 'tasjson.json'
	data = fin.parse_file(filepath)
	for elem in data:
		# comment
		if elem[0] == "key":
			typekey(elem[1])
		elif elem[0] == "comment":
			print(elem[1])
		else:
			sys.exit('invalid input')
