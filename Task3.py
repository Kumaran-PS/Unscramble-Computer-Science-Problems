"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

'''part A'''

bgr_code= set()

for x in calls:

	if x[0].startswith("(080)"):
		if x[1].startswith("7" or "8" or "9"): # mobile number starts with 7 or 8 or 9
			bgr_code.add(x[1][:4])
    	#in last submission 
    	#if " " in x[1]: # as mobile number has a space between them , checking for space
     		# bgr_code.add(x[1][:4])
		if x[1].startswith("(0"): # area telephone code starts with zero
			bgr_code.add(x[1][:x[1].find(")")+1])
		if x[1].startswith("140"): # telemarketers number starts with 140 
			bgr_code.add(140)

bgr_codelist = sorted(list(bgr_code))

print("The numbers called by people in Bangalore have codes:")
for x in bgr_codelist:
	print(x)
	
'''part B'''

no_bgr_calls = 0
bgr_calls = 0

for number in calls:
	if number[0][:5] == "(080)":
	
		if number[1][:5] == "(080)":
			bgr_calls += 1
		else:
			no_bgr_calls += 1
			
percent = (bgr_calls) / (bgr_calls + no_bgr_calls) *100
print("{:5.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percent))
		
