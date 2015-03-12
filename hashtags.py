#Author Sahil Palvia

#This program gets us the most frequently used tweets.

import sys, json

#usage()
#This function prints out how the program is supposed to be called.
def usage():
	print 'Usage: python hashtags.py <filename>'

#findHashTags()
#This function searches through all the tweets to get the most frequently used
#hashtags.
def findHashTags(filename):
	#Checking if the file exists.
	try:
		f = open(filename)
		lines = f.readlines()
		f.close()
	except:
		print 'Error occured'
		sys.exit(1)
	
	hashtags = dict()

	#Searching for the most frequently used tweets.
	for line in lines:
		try:
			tweet = json.loads(line)
			if 'entities' in tweet:
				entities = tweet['entities']
				if 'hashtags' in entities:
					tags = entities['hashtags']
					for tag in tags:
						if 'text' in tag:
							text = tag['text']
							text = text.encode('utf-8')
							if text in hashtags:
								hashtags[text] = hashtags[text] + 1
							else:
								hashtags[text] = 1
		except:
			print 'Error Occured'
			sys.exit(1)

	#Sorting the hash tags in reverse order and then printing the result
	hashtags = sorted(hashtags, key=hashtags.get, reverse = True)
	if len(hashtags) != 0:
		print 'Most frequently used hashtags:'
		if len(hashtags) < 10:
			for i in range (0, len(hashtags)):
				print hashtags[i]
		else:
			for i in range (0, 10):
				print hashtags[i]
	else:
		print 'No hashtags found'

#main()
#Takes in the filename and calls the findCount() function.
def main():
	if len(sys.argv) != 2:
		usage()
	else:
		findHashTags(sys.argv[1])

if __name__ == '__main__':
    main()
