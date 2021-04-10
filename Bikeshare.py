import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months=['january', 'february', 'march', 'april', 'may', 'june']
days = ['sunday', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday' ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('please enter name of the city to analyze : chicago, new york city, washington : ')
        city=city.lower()
        if city in CITY_DATA.keys():
            print("ok")
            break
        print('plese enter correct input')

    # get user input for month (all, january, february, ... , june)
    while True:
        month=input('please enter name of month to fillter (january, february, ... , june) or( all ) to no month filltering :')
        month=month.lower()
        if month in months or month== 'all':
            print("ok")
            break
        print('plese enter correct input')

            

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('please enter  day of week ( monday, tuesday, ... sunday) or (all) to no day filtering :')
        day=day.lower()
        if day in days or day=='all':
            print("ok")
            break
        print('plese enter correct input')
        
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

#     # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hours']= df['Start Time'].dt.hour

#     # filter by month if applicable
    if month != 'all':
        month = months.index(month)+1
        df = df[ df['month'] == month ]

#     # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    print(' the most common start month : {}\n with count = {}'.format(df['month'].value_counts().idxmax(),df['month'].value_counts().max()))

    # TO DO: display the most common day of week
    print(' the most common start day : {}\n with count = {}'.format(df['day_of_week'].value_counts().idxmax(),df['day_of_week'].value_counts().max()))


    # TO DO: display the most common start hour
    print(' the most common start hour : {}\n with count = {}'.format(df['hours'].value_counts().idxmax(),df['hours'].value_counts().max()))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(' the most common start station is : {}\n with count = {}'.format(df['Start Station'].value_counts().idxmax(),df['Start Station'].value_counts().max()))


    # TO DO: display most commonly used end station
    print(' the most common end station : {}\n with count = {}'.format(df['End Station'].value_counts().idxmax(),df['End Station'].value_counts().max()))


    # TO DO: display most frequent combination of start station and end station trip
    arr=df[['Start Station','End Station']].mode().loc[0]
    print(' the most common start_to_end station :{} to {} '.format(arr[0],arr[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time:{} sec'.format(df['Trip Duration'].sum()))



    # TO DO: display mean travel time
    print('avg travel time :{} sec'.format(df['Trip Duration'].mean()))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users=df.groupby(['User Type'])['User Type'].count()
    print('counts of user types are ')
    for i in users.keys():
        print (i,':',users[i]) 

    if 'Gender' in df.columns:
        # TO DO: Display counts of gender
        gender=df.groupby(['Gender'])['Gender'].count()
        print('counts of gender is ..')
        for i in gender.keys():
            print (i,':',gender[i]) 


    if 'Birth Year' in df.columns:
        # TO DO: Display earliest, most recent, and most common year of birth year
        print('most common birth year:{}'.format(df['Birth Year'].mode().loc[0]))
        print('earliest birth year:{}'.format(df['Birth Year'].min()))
        print('most recent birth year:{}'.format(df['Birth Year'].max()))


    
    




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_row(df,ans):
    """
    view 5 rows of individual trip data.
    Args:
        (dataframe) df - data of the city
        (str) ans - answer of the qwestion yes/no
    print:
        5 rows by evry 
    """

    start_loc = 0
    while ans=='yes':
        print(df[start_loc:start_loc+5])
        start_loc += 5
        #To Get answer if user want see next 5 rows or not 
        view_display = input("Do you want see next 5 rows ? (yes/no): ").lower()
        ans='no'
        while view_display=='yes':
            print(df[start_loc:start_loc+5])
            start_loc += 5
            view_display = input("Do you want see next 5 rows ? (yes/no): ").lower()
            if view_display=='no':
                break


            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter  (yes/no) \n').lower()
        display_row(df,view_data)
        restart = input('\nWould you like to restart? Enter (yes/no) .\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
