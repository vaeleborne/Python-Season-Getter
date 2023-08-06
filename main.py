"""
Purpose: Get a month and day from the user then display what season
Ensure month and day is valid

Method to achieve purpose:
    Get inputs from the user
    Define valid months

    In order to see if the date is valid define months that have 31 days
    Define months with 30 days
    Assume February date is valid if 29 or less (29 for leap year), not relevant yet

    Now we need to define which months are in which season. We could for example say
    Mar, Apr, May, Jun for Spring
    Jun, Jul, Aug, September for Summer...
    HOWEVER this will create a redundant situation and use unneeded memory. Solution below:

        This will happen as we may first see if the month is in our defined spring months
        If it is we then need to make sure it isn't March 19th or earlier(as this is Winter),
        or June 21 or later (as this is summer)

        But wait, we have now checked June for BOTH Spring and Summer values, we no longer need to check
        June when we check the summer months, similarly we have also checked March for both Spring AND winter

        Thus, we could next check the only season we haven't checked ANY values for yet being Autumn
        When we do this we are checking September for Autumn AND Summer as well as Decemember for
        Autumn AND Winter

        This means when we check for Summer and Winter months as long as it is in them it is valid
        This would cause redundancy to check either for the months mentioned before so we can also save
        A tiny bit of memory by not defining those months in our definition of Summer and Winter months

        SO, We should have something like this(using abbreviations):
            Spring Months = Mar, Apr, May, Jun
            Autumn Months = Sep, Oct, Nov, Dec
            Summer Months = Jul, Aug
            Winter Months = Jan, Feb

            IF month is a Spring month
                check if the date makes it Winter or Summer
                if not the season is spring
            Else If month is an Autumn month
                check if the date makes it a Summer or Winter month
                if not the season is Autumn
            Else If month is a Summer month
                the season must be summer
            Else If the month is a Winter month
                the season must be winter

    We now know the seasons, if one wasn't found the input must be invalid
"""

# Get the input from the user, make the month be lowercase for easy testing
input_month = input("Type the month: ").lower()
input_day = int(input("Enter the day: "))

# Define a tuple to hold the valid months
valid_months = ('january', 'february', 'march', 'april',
                'may', 'june', 'july', 'august', 'september',
                'october', 'november', 'december')

# Define a tuple with the months that have 31 days
long_months = ('january', 'march', 'may', 'july', 'august', 'october', 'december')

# Define a tuple with the months that have 30 days
short_months = ('april', 'june', 'september', 'november')

# Create a tuple for the spring months that holds the months (March-June)
spring_months = (valid_months[2:6])

# Create a tuple for the autumn months that holds the months (September-December)
autumn_months = (valid_months[8:12])

# Per our pseudo code reasoning create tuple for summer months with only July and August
summer_months = (valid_months[6:8])

# Per our pseudo code reasoning create tuple for winter months with only January and February
winter_months = (valid_months[0:1])

# Create a variable to determine if the month entered is valid
is_valid_month = input_month in valid_months

# Create a variable to use to see if the day is valid, set to False by default
is_valid_day = False

"""Figuring out validity of entered data
If the day input is not negative and month is valid we will continue to check if 
The day is valid for that month, otherwise print invalid. Check this case first as
I will assume it is the more common case to happen thus more efficient to check first"""
if input_day > 0 and is_valid_month == True:
    # If the month entered matches a month defined to have 31 days and days is 31 or less set valid
    if input_month in long_months:
        if input_day <= 31:
            is_valid_day = True
    # Else if the month entered matches a month defined to have 30 days and days is 30 or less set valid
    elif input_month in short_months:
        if input_day <= 30:
            is_valid_day = True
    # Otherwise month must be February so if days is 29 or less set valid
    else:
        if input_day <= 29:
            is_valid_day = True

    # We now know if there is a valid day(based on individual months) or not and still have a valid month
    if is_valid_day:
        # Check for season then store to print at the end

        """Here is where we implement the logic laid out in the pseudo:
        First we check if the month is a spring month, if so we check if it is March
        if it is March and the day is less than 20 then the season is Winter, else if the
        month entered is june and the date is greater than 20 the season is Summer, otherwise the
        season must be Spring."""
        if input_month in spring_months:
            if (input_month == 'march') and (input_day < 20):
                season = 'Winter'
            elif (input_month == 'june') and (input_day > 20):
                season = 'Summer'
            else:
                season = 'Spring'
        # Now we do the logic for autumn checking Sep for Summer dates and Dec for Winter dates
        elif input_month in autumn_months:
            if (input_month == 'september') and (input_day < 22):
                season = 'Summer'
            elif (input_month == 'december') and (input_day > 20):
                season = 'Winter'
            else:
                season = 'Autumn'
        # Now if the month is a summer month the season MUST be summer
        elif input_month in summer_months:
            season = 'Summer'
        # Similarly if the month is a winter month the season MUST be winter
        else:
            season = 'Winter'

        # Outside the logic for determining season, so we display the resulting season for the month and day
        print(season)
    #If the date entered is not a valid day for the given month, display invalid
    else:
        print('Invalid')

# If either the date entered was negative or the month was not valid print invalid
else:
    print('Invalid')
