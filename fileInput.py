import json
import sys

def parse_line(line):
	for key, rx in rx_dict.items():
		match = rx.search(line)
		if match:
			return key, match
	return None, None

def parse_file(filepath):
	data = []
	with open(filepath, 'r') as file_obj:
		file_data = json.load(file_obj)
		for conc in file_data:
			row = []
			if conc["type"] == "key":
				for keys in conc["cmd"]:
					row.append([ keys["dur"], keys["key"] ])
				data.append([conc["type"], row])
			elif conc["type"] == "comment":
				data.append([conc["type"], conc["cmd"]])
			else:
				sys.exit("invalid json type")

	print(data)
	return data
