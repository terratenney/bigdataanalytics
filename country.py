#Author: Sahil Palvia

#This function searches for the countries where most of the tweets were not
#retweeted.

import sys, json

#usage()
#This function prints out how the program is supposed to be called.
def usage():
	print "Usage: python country.py <Filename>"

def findCountries(filename):
	#Checking if the file exists.
	try:
		f = open(filename, 'r')
		lines = f.readlines()
		f.close()
	except ValueError, err:
		print err
		sys.exit(1)

	country = dict()

	#Searching for countries where tweets were not retweeted.
	for line in lines:
		try:
			tweet = json.loads(line)

			place = {}
			place = None

			if 'retweeted' in tweet:
				if tweet['retweeted'] == False:
					if 'place' in tweet:
						place = tweet['place']
						if place != None:
							for field in place.keys():
								if field == 'country':
									countryName = place['country']
									if countryName in country:
										country[countryName] = country[countryName] + 1
									else:
										country[countryName] = 1


		except ValueError, err:
			print 'Error'
			sys.exit(1)

	#Sorting the country in reverse order and then printing the result
	country = sorted(country, key=country.get, reverse=True)
	if len(country) != 0:
		print "Countries with most no of tweets not retweeted"
		if len(country) < 3:
			for i in range (0,len(country)):
				print country[i]
		else:
			for i in range (0,3):
				print country[i]
	else:
		print "No countries found"

#main()
#Takes in the filename and calls the findCount() function.
def main():
	if len(sys.argv)==2:
		findCountries(sys.argv[1])
	else:
		usage()

if __name__ == '__main__':
	main()
