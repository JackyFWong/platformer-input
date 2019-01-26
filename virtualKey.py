import keyboard as kb
import fileInput as fin

if __name__ == '__main__':
	filepath = 'tas.txt'
	data = fin.parse_file(filepath)
	print(data)
	
