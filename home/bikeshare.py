import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
   Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("please enter required city name: chicago, new York City or washington!").lower()
        if city not in CITY_DATA:
            print('you entered invalid city name')
            continue   
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input('Please Enter Required Month From January Until June ,Or Write"All"To Display Data For All Months').title()
        months =['January' , 'Feburary' ,'March' ,'April' ,'May' ,'June' ]
        if month not in months and month!='all':
            print ('please enter correct month')
        else:
            break
     # TO DO: get user input for weekdays              
    while True:
        day=input('please enter required day of week or write"all"to display data for all weekdays').lower()
        days=['sunday','monday','tuesday','wedensday','thursday','friday']
        if day not in days and day!='all':
            print('you have entered wrong input , please enter correct day')
        else:
            break
    return(city , month , day)
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month)+ 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df
def time_stats(df):
        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()
          # TO DO: display the most requested month
        months =['january','february','march','april','may','june',]
        month =df['month'].mode()[0]
        print(f' the most popular month is: {months[month-1]}')
            # TO DO: display the most required day of week
        day=df['day_of_week'].mode()[0]
        print(f'the most common day of week is : {day}')
            # TO DO: display the most required start hour
        df['hour']=df['Start Time'].dt.hour
        popular_hour=df['hour'].mode()[0]
        print(f'the most popular start hour is : {popular_hour}')

        print('\nThis took %s seconds'%(time.time()-start_time))

        print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start=df['Start Station'].mode()[0]
    print(common_start)

    # TO DO: display most commonly used end station
    common_end=df['End Station'].mode()[0]
    print(common_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination']=df['Start Station'] + ' to ' + df['End Station']
    common_combination=df['combination'].mode()[0]
    print(common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel=df['Trip Duration'].sum()
    print(total_travel)


    # TO DO: display mean travel time
    mean_travel=df['Trip Duration'].mean()
    print(mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print(user_types)


    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender=df['Gender'].value_counts()
        print(gender)
    else:
        print("This city does not have any gender information.")


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest=df['Birth_Year'].min()
        print(earliest)
        recent=df['Birth_Year'].max()
        print(recent)
        common_birth=df['Birth Year'].mode()[0]
        print(common_birth)
    else:
        print("this city does not have any birth year information.")

        print("\nThis took %s seconds." %(time.time()-start_time))
        print('-'*40)
def main():
    while True:
        city,month,day = get_filters()
        df=load_data(city, month, day)

        time_stats(df)
       
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        counter=0
        while True:
            entry=input("Do you wish to print more raw data?").lower()
            if entry == "yes":
                print(df.iloc[counter:counter+5])
                counter += 5
            elif entry=="no":
                break
                
                
        restart=input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
if __name__== "__main__":
     main()

