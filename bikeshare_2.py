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
    while True:
        city = input("Would you like to analyze Chicago, New York City, or Washington?\n").lower()
        if city == 'chicago' or city == 'new york city' or city == 'washington':
            break
        else:
            print("That\'s not a valid input")

    while True:
        filter = input("Would you like to filter by month, day, or not at all? Type \"none\" for no time filter\n").lower()
        if filter == 'month' or filter == 'day' or filter == 'none':
            break
        else:
            print("That\'s not a valid input")


    if filter == "month":
        while True:
            month = input("Which month? January, February, March, April, May, or June? Please type full month name\n").lower()
            if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june':
                break
            else:
                print("That\'s not a valid input")
        day = "all"

    elif filter == "day":
        while True:
            day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? Please type full day name\n").lower()
            if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday':
                break
            else:
                print("That\'s not a valid input")
        month = "all"

    elif filter == "none":
        month = "all"
        day = "all"


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != "all":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != "all":
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    popular_month = df['month'].mode()[0]
    print("The most common month is: {}".format(popular_month)) # display the most common month


    popular_day = df['day_of_week'].mode()[0]
    print("The most common day of week is: {}".format(popular_day)) # display the most common day of week


    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most common start hour is: {}".format(popular_hour)) # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    popular_start_station = df['Start Station'].mode()[0]
    print("The most commonly used Start Station is: {}".format(popular_start_station)) # display most commonly used start station


    popular_end_station = df['End Station'].mode()[0]
    print("The most commonly used End Station is: {}".format(popular_end_station)) # display most commonly used end station


    popular_combination = df.groupby(['Start Station', 'End Station']).size()
    print("The most frequent combination is: {}".format(popular_combination.index[0])) # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is {} seconds".format(total_travel_time)) # display total travel time


    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time is {} seconds".format(mean_travel_time)) # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print("User Type Count:")
    print(user_types) # Display counts of user types

    if 'Gender' and 'Birth Year' in df.columns:
        user_gender = df['Gender'].value_counts()
        print("Gender Count:")
        print(user_gender) # Display counts of gender

        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print("Earliest Birth Year: {} \nMost Recent Birth Year: {} \nMost Common Birth Year: {}".format(earliest_birth_year, recent_birth_year, common_birth_year)) # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """Displays 5 rows of raw data."""
    i = 0
    raw_data = input("\nWould you like to view 5 rows of raw data? Enter yes or no.\n")
    while raw_data.lower() == 'yes' and i+5 < df.shape[0]:
        print(df.iloc[i:i+5])
        i += 5
        raw_data = input("Would you like to view 5 more rows of raw data? Enter yes or no.\n")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
