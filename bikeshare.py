import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv', 'Chicago': 'chicago.csv', 'CHICAGO': 'chicago.csv',
              'new york city': 'new_york_city.csv', 'New York City': 'new_york_city.csv', 'NEW YORK CITY': 'new_york_city.csv',
              'washington': 'washington.csv', 'Washington': 'washington.csv', 'WASHINGTON': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        
    """
    
    #Empty name variable to store name of user to be used throughout the program
    name = ''
    print("\nHello! My name is PyEx, an exploration job that is going to guide you through the program")
    name = input("\nWhat\'s your name?\n")
    print(f"\nWell it\'s an absolute pleasure " + str(name) + "! Let\'s get in and explore some US bikeshare data!")
    
    #Another instanstiation of an empty string variable, city, to be used throughout the program
    city = ''
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print (f"\nOkay " + str(name)+ ", we will start off by selecting a location to investigate")
    print ("\nThe available locations include:\nChicago \nNew York City \nWashington:")
    
    while city not in CITY_DATA.keys():
        
        try:
            city = input("\nPlease select one of the locations above\n").lower()
        except ValueError:
            print(f"Sorry please try that input again")
            continue
        
    
        if city not in CITY_DATA.keys():
            print(f"\nSorry " + str(name)+ ", it seems that I cannot retrieve data for that location as it may not be available.")
            continue
        else:
            print(f"\nAwesome " +str(name)+"!, you chose " + str(city) + " as your location of choice, let\'s proceed to the next seletion criteria.")
            break
    
    
#For the month slecection criteria, I will utilize a dictionary to store all my available month options then reference to the functions containing the list

    month_list = ['january','february','march','april','may','june','all months']
    month = ''
    
    print(f"\nUp next , we\'ll move to selecting a month from " + str(city) + " to investigate.")
    print("\nYou can decide to select any month from the first six months of the calendar year or select them all if you wish.")

    while month not in month_list:
        try:
            month=input("\nPlease select a month:\n").lower()
        except ValueError:
            print(f"Sorry please try that input again")
            continue
        
    
        if month not in month_list:
            print(f"\nSorry " + str(name) + ", it seems that I cannot retrieve data for that month in the city of " + str(city) +" as it may not be available.")
            continue
            
        else:
            print(f"\nAlright " + str(name) + ", you chose to view the month of " + str(month) + " for the city of " + str(city) + ", let\'s proceed to the next seletion criteria.")
            break
    
    
#For the day slecection criteria, I will again utilize a list to store all my available day options then reference to the functions containing the list

    day_list = ['sunday','monday','tuesday','wednesday','thursday','friday','all days']
    day = ''
    print(f"\nOkay, we\'ll move to selecting a day from " + str(month) + " in " + str(city) + " to investigate.")
    print("\nYou can decide to select any day of the week or select them all if you wish")

    while day not in day_list:
        try:
            day=input("\nPlease select a day:\n").lower()
        except ValueError:
            print(f"Sorry please try that input again")
            continue
    
        if day not in day_list:
            print(f"\nSorry " + str(name) + ", it seems that I cannot retrieve data for that day in the month of " + str(month) + " for the city of " + str(city) + " as it is unavailable.")
            continue
            
        else:
            print(f"\nAwesome stuff " + str(name) + ", you chose to view " + str(day) + " in " + str(month) + " for the city of " + str(city) +".")
            break

    
    print('-'*40)
    return city, month, day



    


def load_data(city, month, day):
    
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
  #loading data into data frame
    df = pd.read_csv(CITY_DATA[city])

#Start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

#extracting month and day of week from Start Time to come up with new columns for fetching
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

#statement to filter data by month and get new dataframe
    if month != 'all months':
        mons = ['january','february','march','april','may','june']
        month = mons.index(month) + 1


        df = df[df['month'] == month]
    
    if day!= 'all days':
    
        df = df[df['day_of_week'] == day.title()]
 
    

    return df


def time_stats(df, city):
    """Displays statistics on the most frequent times of travel."""

    print(f"\nCalculating The Most Frequent Times of Travel in " + str(city) + " ...\n")
    start_time = time.time()

    # TO DO: display the most common month
    print(f"{df['month'].mode()[0]} is the modal(most common) month identified in " + str(city) + ".")


    # TO DO: display the most common day of week
    print(f"{df['day_of_week'].mode()[0]} is the modal(most common) day of the week identified in " + str(city) + ".")

    # TO DO: display the most common start hour
    print(f"{df['hour'].mode()[0]} is the modal(most common) hour in the day identified in " + str(city) + ".\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df, city):
    """Displays statistics on the most popular stations and trip."""

    print(f"\nCalculating The Most Popular Stations and Trip in " + str(city) + "...\n")
    start_time = time.time()
    

    # TO DO: display most commonly used start station
    print(f"{df['Start Station'].mode()[0]} is the most commonly used start station in " + str(city) + ".")

    # TO DO: display most commonly used end station
    print(f"{df['End Station'].mode()[0]} is the most commonly used end station in " + str(city) + ".")


    # TO DO: display most frequent combination of start station and end station trip
    df['startend'] = df['Start Station'] + " and " + df['End Station']
    print(f"{df['startend'].mode()[0]} are the most common combination of start and end stations respectively in " + str(city) + ".")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df, city):
    """Displays statistics on the total and average trip duration."""

    print(f"\nCalculating Trip Duration in " + str(city) + "...\n")
    start_time = time.time()

    # TO DO: display total travel time
    tot_trip = df['Trip Duration'].sum()
    
    #using divmod method to determine the duration in minutes and seconds       format
    mins, sec = divmod(tot_trip, 60)
    #duration in hours and minute
    hour, minute = divmod(mins, 60)
          
    print(f"The total trip duration is " + str(hour) + " hours, " + str(mins) + " minutes and " + str(sec) + " seconds.")
   


    # TO DO: display mean travel time
    mean_travel_time = round(df['Trip Duration'].mean())
    
    #mean travel time in min and sec format
    minute, second = divmod(mean_travel_time, 60)
          
    #if-else filter to print the travel time in hrs, min and sec format if minutes are more than 60
    if minute > 60:
        hours, minute = divmod(minute, 60)
        print(f"The mean travel time is " + str(hours) + " hours , " + str(minute) + " minutes and " + str(second) + " seconds.\n")
         
    else:
        print(f"The mean travel time is " + str(minute) + " minutes and " + str(second) + " seconds.\n")
          
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats in ' + str(city) + '...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())
   
    # TO DO: Display counts of gender
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
      print(df['Gender'].value_counts())
      print(f"{df['Birth Year'].min()} is the earliest year of birth recorded in the dataset.")
      print(f"{df['Birth Year'].max()} is the most recent year of birth recorded in the dataset.")
      print(f"{df['Birth Year'].mode()[0]} is the most common year of birth recorded in the dataset.")
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df, city):
    """Asking user if they want raw data displayed"""
    x = 0
    while True:
        inp = input(f"Do you wish to view raw data from " + str(city) + "?\n").lower()
        if inp == 'yes':
            print(df[x:x+5])
            x += 5 #similar to previous x = x + 5
        else:
            break
        
        
           
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.head())

        time_stats(df, city)
        station_stats(df, city)
        trip_duration_stats(df, city)
        user_stats(df, city)
        raw_data(df, city)

        restart = input('\nWould you like to restart?\n').lower()
        if restart.lower() != 'yes':
            print(f"Thank you for using this program for your data exploration. Hope you had as much fun on this as I did.\n")
            print(f"PyEx signing out...")
            break


if __name__ == "__main__":
	main()
