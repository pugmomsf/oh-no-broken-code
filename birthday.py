from datetime import datetime

number_endings = {
    1: 'st',
    2: 'nd',
    3: 'rd',
}

today = datetime.now()
todays_day = today.day

# get the right ending, e.g. 1 => 1st, 2 => 2nd
# but beware! 11 => 11th, 21 => 21st, 31 => 31st

# test your code by forcing todays_day to be something different

todays_day = 9

ending = 'th'
number = 0

#for date,ending in number_endings.items():
#	print "%d has ending %s" % (date, ending)

print todays_day

if todays_day < 10 or todays_day > 20:
    number = todays_day % 10

if number in number_endings:
	ending = number_endings[number]
#	print "Today is the {}".format(todays_day)+"%s" % ending
		 # % number_ending
		 
# if todays_day >= 10 or todays_day <= 20:

print "Today is the {}".format(todays_day)+"%s" % ending



birthday = int(raw_input("What day of the month is your birthday?"))

# make this print the birthday, and the right ending
ending = 'th'

				
if birthday < 10 or birthday > 20:
    number = birthday % 10

if number in number_endings:
	ending = number_endings[number]
	# print "Birthday is the {}".format(birthday)+"%s" % ending
		 # % number_ending
		 
# if todays_day >= 10 or todays_day <= 20:
	
print "Birthday is the {}".format(birthday)+"%s" % ending
