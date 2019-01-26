import sys
import time
import keyboard as kb
import fileInput as fin

# define variables
keys = [ 'w', 'a', 'd', 'j', 'k' ]
wait = 'f'

def to_frames(int):
	return int/60

def typekey(frames, cmd):
	kb.press(cmd)
	time.sleep(to_frames(frames))
	kb.release(cmd)

def waitframes(frames):
	time.sleep(to_frames(frames))

if __name__ == '__main__':
	filepath = 'tas.txt'
	data = fin.parse_file(filepath)
	for elem in data:
		# comment
		if len(elem) == 1:
			print(elem[0])
		elif len(elem) == 2:
			if elem[1] in keys:
				typekey(elem[0], elem[1])
			elif elem[1] == wait:
				waitframes(elem[0])
			else:
				sys.exit('invalid command')
		else:
			sys.exit('invalid input')
