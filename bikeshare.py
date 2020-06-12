import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

class bcolors:
    BLUE = '\u001b[34;1m'
    MAGENTA = '\u001b[35;1m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33;1m'
    CYAN = '\u001b[36;1m'
    ENDC = '\033[0m'

def print_pause(message_to_print):
    """Pause on printing delay to calibrate speed of delivery of information to user"""
    time.sleep(1)
    print(message_to_print)    
    
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
        choose_city = input("Please enter the number corresponding to the city you\'d like to see bikeshare data for:\n"
                     "1 Chicago\n"
                     "2 New York City\n"
                     "3 Washington\n").lower()
        if choose_city == '1':
            city = 'chicago'
            print_pause(bcolors.GREEN + "You selected Chicago" + bcolors.ENDC)
            break
        elif choose_city == '2':
            city = 'new york city'
            print_pause(bcolors.GREEN + "You selected New York City" + bcolors.ENDC)
            break
        elif choose_city == '3':
            city = 'washington'
            print_pause(bcolors.GREEN + "You selected Washington" + bcolors.ENDC)
            break
        
    # TO DO: get user input for month (all, january, february, ... , june)
    print_pause("")
    while True:
        choose_month = input("Please enter the number corresponding to the month(s) you\'d like to see bikeshare data for:\n"
                      "1 January\n"
                      "2 February\n"
                      "3 March\n"
                      "4 April\n"
                      "5 May\n"
                      "6 June\n"
                      "7 All\n").lower()
        if choose_month == '1':
            month = 1
            print_pause(bcolors.GREEN + "You selected January" + bcolors.ENDC)
            break
        elif choose_month == '2':
            month = 2
            print_pause(bcolors.GREEN + "You selected February" + bcolors.ENDC)
            break
        elif choose_month == '3':
            month = 3
            print_pause(bcolors.GREEN + "You selected March" + bcolors.ENDC)
            break
        elif choose_month == '4':
            month = 4
            print_pause(bcolors.GREEN + "You selected April" + bcolors.ENDC)
            break
        elif choose_month == '5':
            month = 5
            print_pause(bcolors.GREEN + "You selected May" + bcolors.ENDC)
            break
        elif choose_month =='6':
            month = 6
            print_pause(bcolors.GREEN + "You selected June" + bcolors.ENDC)
            break
        elif choose_month =='7':
            month = 7
            print_pause(bcolors.GREEN + "You selected all months" + bcolors.ENDC)
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print_pause("")
    while True:
        choose_day = input("Please enter the number corresponding to the day(s) you\'d like to see bikeshare data for:\n"
                      "1 Monday\n"
                      "2 Tuesday\n"
                      "3 Wednesday\n"
                      "4 Thursday\n"
                      "5 Friday\n"
                      "6 Saturday\n"
                      "7 Sunday\n"
                      "8 All\n").lower()
        if choose_day == '1':
            day = 'Monday'
            print_pause(bcolors.GREEN + "You selected Monday" + bcolors.ENDC)
            break
        elif choose_day == '2':
            day = 'Tuesday'
            print_pause(bcolors.GREEN + "You selected Tuesday" + bcolors.ENDC)
            break
        elif choose_day == '3':
            day = 'Wednesday'
            print_pause(bcolors.GREEN + "You selected Wednesday" + bcolors.ENDC)
            break
        elif choose_day == '4':
            day = 'Thursday'
            print_pause(bcolors.GREEN + "You selected Thursday" + bcolors.ENDC)
            break
        elif choose_day == '5':
            day = 'Friday'
            print_pause(bcolors.GREEN + "You selected Friday" + bcolors.ENDC)
            break
        elif choose_day =='6':
            day = 'Saturday'
            print_pause(bcolors.GREEN + "You selected Saturday" + bcolors.ENDC)
            break
        elif choose_day =='7':
            day = 'Sunday'
            print_pause(bcolors.GREEN + "You selected Sunday" + bcolors.ENDC)
            break
        elif choose_day =='8':
            day = 'all'
            print_pause(bcolors.GREEN + "You selected to see the whole week" + bcolors.ENDC)
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
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # create two columns for month and day of the week
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # create a column to hold the count of trips per line, equal to 1 per line (for pivot_birth_year())
    df['no._of_trips'] = 1
    
    # filter results for selected month 
    if month != 7:
        df = df[df['month'] == month]
    
    # filter results for selected day
    if day != 'all':
        df = df[df['day_of_week'] == day]
   
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print_pause('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month 
    # Display most common month if 'all' months have been selected in get_filters()
    if month == 7:
        common_month = df['month'].mode()[0]
        print_pause(bcolors.MAGENTA + "The most common month to use bikeshare is: {}".format(month_names[common_month - 1]) + bcolors.ENDC)

    # TO DO: display the most common day of week
    # Display most commo day if 'all' days of week have been selected in get_filters()
    if day == 'all':
        common_day_week = df['day_of_week'].mode()[0]
        print_pause(bcolors.MAGENTA +"The most common day of the week to use bikeshare is: {}".format(common_day_week) + bcolors.ENDC)

    # TO DO: display the most common start hour
    # extract hour from Timestamp to find most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print_pause(bcolors.MAGENTA + "The most common hour to rent a bikeshare is: {} ".format(common_start_hour) + bcolors.ENDC)

    print_pause("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print_pause('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_stn = df['Start Station'].mode()[0]
    count_start_stn = df['Start Station'].value_counts()[start_stn]
    print_pause(bcolors.BLUE + "The most commonly used start station was {}, used a total of {} times.".format(start_stn, count_start_stn) + bcolors.ENDC)
    
    # TO DO: display most commonly used end station
    end_stn = df['End Station'].mode()[0]
    count_end_stn = df['End Station'].value_counts()[end_stn]
    print_pause(bcolors.BLUE + "The most commonly used end station was {}, used a total of {} times.".format(end_stn, count_end_stn) + bcolors.ENDC)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End Station Combo'] = df['Start Station'] + " " + "and ended at" + " "  + df['End Station']
    start_end_stns = df['Start End Station Combo'].mode()[0]
    count_start_end_stns = df['Start End Station Combo'].value_counts()[start_end_stns]
    print_pause(bcolors.BLUE + "For the most common combination of start and end stations, journeys began at {}.".format(start_end_stns) +        bcolors.ENDC)
    print(bcolors.BLUE + "{} journeys began and ended from these stations.".format(count_start_end_stns) + bcolors.ENDC)

    print_pause("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # travel time calculated in seconds and broken down to days, hours, minutes and seconds
    travel_secs = df['Trip Duration'].sum()
    m, s = divmod(travel_secs, 60)
    h, m  = divmod(m, 60)
    d, h  = divmod(h, 24)
    print_pause(bcolors.YELLOW + 'The total duration for these trips undertaken via bikeshare is the equivalent of {} days, {} hours, {} minutes and {} seconds.'.format(d, h, m, s) + bcolors.ENDC)
   
    # TO DO: display mean travel time
    # calculate the mean Trip Duration and split into minutes and hours
    mean_duration = int(df['Trip Duration'].mean())
    m, s = divmod(mean_duration, 60)
    print_pause(bcolors.YELLOW + "The mean trip duration was {} minutes and {} seconds.".format(m,s) + bcolors.ENDC)

    # Display the longest journey time and the start and end station of that journey
    longest_journey = df['Trip Duration'].max()
    hr = longest_journey // 3600
    row = df[df['Trip Duration'] == longest_journey]
    start_long_journey = row['Start Station'].to_string(index=False)
    end_long_journey = row['End Station'].to_string(index=False)
    print_pause(bcolors.YELLOW + "The longest journey took approx {} hours, it started at {} and ended at {}.".format(hr, start_long_journey, end_long_journey) + bcolors.ENDC)
   
    
    print_pause("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    s, c = (df['User Type'].value_counts()['Subscriber'], df['User Type'].value_counts()['Customer'])
    print_pause(bcolors.CYAN + "Of the user types, there are a total number of {} Subscribers and {} Customers.".format(s,c) + bcolors.ENDC)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        m, f = (df['Gender'].value_counts()['Male'], df['Gender'].value_counts()['Female'])
        print_pause(bcolors.CYAN + "There were {} transactions made by males and {} made by females.".format(m,f) + bcolors.ENDC)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        early_birth = int(df['Birth Year'].min())
        recent_birth = int(df['Birth Year'].max())
        common_birth_year = int(df['Birth Year'].mode()[0])
        print_pause(bcolors.CYAN + "The earliest birth year of a user was {}, the most recent {}. The most common birth year for users was {}.".            format(early_birth, recent_birth, common_birth_year) + bcolors.ENDC)
   
    
    print_pause("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def display_data(df):
    """Displays the underlying line by line data"""
    
    # Get user input to establish if user wants to see raw data
    view = input("Would you like to see some of the underlying line by line data? Enter y or n.\n").lower()
    if view == 'y':
        s = 0
        f = s + 5
        while view.lower() == 'y':
            print(df.iloc[s : f, :])
            s += 5
            f += 5
            view = input("Would you like to see more of the underlying line by line data? Press 'y' to see the next 5 lines or another key to progress.\n")
    elif view == 'n':
        restart_programme()
    else:
        display_data(df)

def restart_programme():
    """Ask user if they want to exit the programme or start again"""
    
    restart = input('\nWould you like to restart? Enter y or n.\n')
    if restart.lower() == 'y':
        main()
    elif restart.lower() == 'n':
        exit()
    else:
        restart_programme()
        
def pivot_birth_year(df):
    """Displays a pivot table of the no.of journeys and trip duration by Birth Year"""
    
    if 'Birth Year' in df:
        start_time = time.time()
        print_pause('\nCalculating number of journeys by Birth Year...\n')
        print_pause("")
        pivot = df.pivot_table(index = df["Birth Year"], values = ['no._of_trips','Trip Duration'], aggfunc = sum)
        pivot_sorted = pivot.reindex(pivot['no._of_trips'].sort_values(ascending = False).index)
        print_pause(pivot_sorted)
        print_pause("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        pivot_birth_year(df)
        display_data(df)
        restart_programme()


if __name__ == "__main__":
	main()
