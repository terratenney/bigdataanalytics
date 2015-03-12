# mission.py
#
# 04/30/2014
#
# author: Sahil Palvia <sap8231@rit.edu>
#
# This program reads the data from csv files and collects the data present in
# pdistrict column and check if the district is Mission and then stores the 
# category of crime in the Mission district and displays the 3 most frequent
# categories of crimes.
import sys, json, csv, MapReduce

AllWords = {}

mr = MapReduce.MapReduce()

# usage()
#
# This function displays the usage of the program.
def usage():
	sys.exit('Usage: python category.py <filename>')

# mapper()
#
# This function takes a Json object as an argument and checks if the Json object
# contains PdDistrict and if that value is MISSION and then stores the category.
def mapper(record):
	if 'PdDistrict' in record:
		if record['PdDistrict'] == 'MISSION':
			if 'Category' in record:
				mr.emit_intermediate(record['Category'], 1)

# reducer()
#
# This function counts the total number instances of a particular value
# and stores the value in the AllWords dictionary against the crime category.
def reducer(key,list_of_values):
	total = 0
	for v in list_of_values:
		total += v
		mr.emit((key,total))
	AllWords[key] = total

# main()
#
# The main gets the csv file reads the lines from the file and converts each
# line into a json object and calls the execute of the MapRecude program.
def main():
	if len(sys.argv) > 1:
		try:
			for i in range(1, len(sys.argv)):
				f = open(sys.argv[i])
				lines = csv.reader(f)
				columns = next(lines)
				lines = csv.DictReader(f, columns)
				json_file = []
				for line in lines:
					json_file.append(json.dumps(line))
				mr.execute(json_file, mapper, reducer)
				f.close()
		except:
			sys.exit('Error Occured')
	else:
		usage()
	result = sorted(AllWords, key=AllWords.__getitem__, reverse=True)
	for i in range(0, 3):
		print (result[i],'\t',AllWords[result[i]])
	print ("done")

if __name__ == '__main__':
	main()
