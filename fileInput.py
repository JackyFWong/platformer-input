import re
import sys

# set up regular expressions
rx_dict = {
	'frame_in': re.compile(r'(\d+ .)\n')
}

def parse_line(line):
	for key, rx in rx_dict.items():
		match = rx.search(line)
		if match:
			return key, match
	return None, None

def parse_file(filepath):
	data = []
	with open(filepath, 'r') as file_obj:
		line = file_obj.readline()
		while line:
			key, match = parse_line(line)
			if key == 'frame_in':
				frame_in = match.group(1)
			else:
				sys.exit('invalid input')

			line = file_obj.readline()
			row = frame_in.split()
			row = [ int(row[0]), row[1] ]
			data.append(row)

	print(data)
	return data
