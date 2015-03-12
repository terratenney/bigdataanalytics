#Aurhor: Sahil Palvia

#This program counts the number of times the word health is present in any
#tweet and displays the count.

import sys, json

#usage()
#This function prints out how the program is supposed to be called.
def usage():
	print 'Usage: python health.py <filename>'

#findCount()
#This function takes the file name as an argument and checks the number if
#tweets that have the word health present in them.
def findCount(filename):
	#Checking if the file exists.
	try:
		f = open(filename)
		lines = f.readlines()
		f.close()
	except:
		print 'Error Occured'
		sys.exit(1)
	
	count = 0

	#Counting the number of times we see health in a tweet
	for line in lines:
		try:
			tweet = json.loads(line)
			if 'text' in tweet:
				text = tweet['text']
				if 'health' in text.lower():
					count = count + 1
		except:
			print 'Error Occured'
			sys.exit(1)

	print count

#main()
#Takes in the filename and calls the findCount() function.
def main():
	if (len(sys.argv) != 2):
		usage()
	else:
		findCount(sys.argv[1])

if __name__ == '__main__':
    main()
