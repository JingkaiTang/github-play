#! /usr/bin/env python
DATA_FILE = 'data.txt'


def _parse(data_file):
	raw_data = open(data_file).read().split('\n')
	items = [line.split() for line in raw_data]
	return {item[0][1:]:item[1:] for item in items}


def data_parse():
	return _parse(DATA_FILE)


if __name__ == '__main__':
	print(data_parse())