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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
no_call_senders = set()
call_senders = set()

for i in texts:
	no_call_senders.add(i[0])
	no_call_senders.add(i[1])
	
for i in calls:
	no_call_senders.add(i[1])
	call_senders.add(i[0])

telemarketers = list(call_senders - no_call_senders)
telemarketers.sort()

print("These numbers could be telemarketers: ")
#print(len(telemarketers))
for number in telemarketers:
	print(number)
	

	

	
	
	
	
	
	
	
	
	
	
	
	

