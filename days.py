# days.py
#
# 04/30/2014
#
# author: Sahil Palvia <sap8231@rit.edu>
#
# This program reads the data from csv files and collects the data present in
# the DayOfWeek column and displays the days of the week, the number of crimes
# that took place on that day and the weeks rank from the highest to lowest.
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
# contains DayOfWeek column and stores the day of week and adds one against its
# value.
def mapper(record):
	if 'DayOfWeek' in record:
		mr.emit_intermediate(record['DayOfWeek'], 1)

# reducer()
#
# This function counts the total number instances of a particular crime on a day
# of week and stores the value in the AllWords dictionary against the day of
# week.
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
	for day in result:
		print (day,'\t',result.index(day)+1,'\t',AllWords[day])
	print ("done")

if __name__ == '__main__':
	main()
