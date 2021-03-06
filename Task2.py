"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
numbers = dict()

for i in range(len(calls)):
	numbers[calls[i][0]] = numbers.get(calls[i][0] , 0) + int(calls[i][3])
	numbers[calls[i][1]] = numbers.get(calls[i][1] , 0) + int(calls[i][3])
	
max_time = max(numbers.values())
time = 0

for num , time in numbers.items():
	if time == max_time:
		print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(num , max_time))
