# This file has a few mistakes and some things I forgot to put in.
# When I run it I don't get anything... can you fix it so I
# get asked for my vacation spot, and get a recommendation?
# Hint:
# Start at the bottom and work upwards.


seasons = ['spring', 'summer', 'fall', 'winter']

weather_patterns = {
    'spring': 'rain',
    'summer': 'sun',
    'fall': 'wind',
    'winter': 'snow'
}

activities = {
    'rain': 'visiting museums',
    'wind': 'kiteboarding',
    'sun': 'sunbathing',
    'snow': 'skiing'
}

vacation_spots = {
	'snow': 'Tahoe',
	'wind': 'Hawaii',
	'rain': 'New York',
	'sun': 'Mexico'
}


def best_vacation_spot(weather_type):
    # Look at the weather type and return the vacation spot that
    # is the best for that weather.
    # You can use this mapping:
    # snow = Tahoe
    # wind = Hawaii
    # rain = New York
    # sun = Mexico
    
    vacation_spot = vacation_spots[weather_type]
    print vacation_spot
    return vacation_spot

    
    #return "Stay at home"


def vacation_activity(weather_type):
    # Look up the vacation activity from activities
    # and return just the activity itself
    vacation_activity = activities[weather_type]
    print vacation_activity
    return vacation_activity


def get_my_vacation():

    season = raw_input("What season do you want to travel? ")
	
    # check if season is in the seasons list
    if not seasons:
        print "Sorry, that isn't a season. I can't help you."

    # look up the weather type for that season
    else:
    	weather_type = weather_patterns[season]
	
	print weather_type
	
	
    # get the best vacation spot for that type
    best_vacation_spot(weather_type)
    
    # get the best vacation activity for that type
    vacation_activity(weather_type)
    
    # print "You should travel to {}, where you can spend your time {}!".format(vacation_spot, vacation_activity)
    print vacation_spot
    print vacation_activity

def main():
    print "Welcome to the Vacation-o-Matic!"


if __name__=="__main__":
	main()
	get_my_vacation()
