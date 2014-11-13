#!/usr/bin/python
import os
import random


def main():
	dictionary = [i.strip() for i in open('/usr/share/dict/american-english').readlines()]
	wordone = dictionary[ random.randrange(0,len(dictionary)-1,1)]
	wordtwo = dictionary[ random.randrange(0,len(dictionary)-1,1)]
	wordthree = dictionary[ random.randrange(0,len(dictionary)-1,1)]
	wordfour = dictionary[ random.randrange(0,len(dictionary)-1,1)]


	stringofnames = os.environ['QUERY_STRING']
	namepairs = stringofnames.split('=')

	astring'''
	<!DOCTYPE html>
	<html>

		<body>
			<p> {0}</p>
		</body>
	</html>

	'''.format(namepairs[0])
	print(astring)



if __name__ == (__main__):
	main()
