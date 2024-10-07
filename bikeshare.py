import time
import pandas as pd
import numpy as np

# Dictionary to hold the data files for each city
CITY_DATA = {

    'chicago': 'chicago.csv',
    'new york': 'new_york_city.csv',
    'washington': 'washington.csv'
}

#---------------------------------------------------------------------------------------------

def load_data(city, month=None, day=None):
    #Loads data for the specified city and filters by month and day if applicable.
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extract month and day of week from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month if applicable
    if month:
        df = df[df['month'] == month]

    # Filter by day if applicable
    if day:
        df = df[df['day_of_week'] == day.title()]

    return df

#---------------------------------------------------------------------------------------------

def popular_times_of_travel(df):
    #Displays the most common month, day, and hour.

    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()  # Start timer

    most_common_month = df['month'].mode()[0]
    most_common_day = df['day_of_week'].mode()[0]
    most_common_hour = df['hour'].mode()[0]

    end_time = time.time()  # End timer

    print(f'Most common month: {most_common_month}')
    print(f'Most common day of week: {most_common_day}')
    print(f'Most common hour: {most_common_hour}')
    print(f"Time taken: {end_time - start_time:.4f} seconds")  # Display time taken
    print('-'*40)
#---------------------------------------------------------------------------------------------

def popular_stations_and_trip(df):
    #Displays the most common start station, end station, and trip.

    print('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = time.time()  # Start timer
    
    most_common_start_station = df['Start Station'].mode()[0]
    most_common_end_station = df['End Station'].mode()[0]
    most_common_trip = (df['Start Station'] + " to " + df['End Station']).mode()[0]
    
    end_time = time.time()  # End timer

    print(f'Most common start station: {most_common_start_station}')
    print(f'Most common end station: {most_common_end_station}')
    print(f'Most common trip: {most_common_trip}')
    print(f"Time taken: {end_time - start_time:.4f} seconds")  # Display time taken
    print('-'*40)

#---------------------------------------------------------------------------------------------

def trip_duration(df):
    #Displays total and average trip duration.

    print('\nCalculating Trip Duration...\n')

    start_time = time.time()  # Start timer
   
    total_travel_time = np.sum(df['Trip Duration'])  # Using numpy to sum
    average_travel_time = np.mean(df['Trip Duration'])  # Using numpy to calculate mean
   
    end_time = time.time()  # End timer

    print(f'Total travel time: {total_travel_time}')
    print(f'Average travel time: {average_travel_time}')
    print(f"Time taken: {end_time - start_time:.4f} seconds")  # Display time taken
    print('-'*40)

#---------------------------------------------------------------------------------------------

def user_info(df):
    #Displays counts of user types and gender, and birth year statistics.
    
    print('\nCalculating User Statistics...\n')

    start_time = time.time()  # Start timer
    
    user_types = df['User Type'].value_counts()
    print(user_types)

    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)

    if 'Birth Year' in df.columns:
        earliest_year = int(np.min(df['Birth Year']))  # Using numpy to find min
        most_recent_year = int(np.max(df['Birth Year']))  # Using numpy to find max
        most_common_year = int(df['Birth Year'].mode()[0])

        print(f'Earliest year of birth: {earliest_year}')
        print(f'Most recent year of birth: {most_recent_year}')
        print(f'Most common year of birth: {most_common_year}')
    
    end_time = time.time()  # End timer
   
    print(f"Time taken: {end_time - start_time:.4f} seconds")  # Display time taken
    print('-'*40)

#---------------------------------------------------------------------------------------------

def get_filters():
    print('^' * 40)
    print("\n******Explore US Bikeshare Data******\n")
    print('^' * 40)
    print('Hello! Let\'s explore some US bikeshare data!')
    #Gets user input for city, month, and day.

    city = input("\nWould you like to see data for Chicago, New York, or Washington? ").lower()

    while city not in CITY_DATA:
        print("")
        print('*' * 40)
        city = input("Invalid input. Please choose Chicago, New York, or Washington: ").lower()

    filter_type = input("\nWould you like to filter the data by month, day, or not at all? Type 'month', 'day', or 'none': ").lower()
    
    while filter_type not in ['month', 'day', 'none']:
        print("")
        print('*' * 40)
        filter_type = input("Invalid input. Please type 'month', 'day', or 'none' as mentioned: ").lower()
    
    month = None
    day = None


    if filter_type == 'month':
                
        month_input = input("\nWhich month - January (1), February (2), March (3), April (4), May (5), or June (6)? ").lower()
        
        # Month mapping
        month_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
        
        # Check if input is numeric
        if month_input.isdigit():
            month = int(month_input)
        else:
            month = month_dict.get(month_input, None)

        # Validate month input
        while month not in month_dict.values():
            print("")
            print('*' * 40)
            month_input = input("Invalid input. Please enter a valid month name or number (1-6): ").lower()
            
            if month_input.isdigit():
                month = int(month_input)
            else:
                month = month_dict.get(month_input, None)

    #------------------------------------------

    elif filter_type == 'day':
        day = input("\nWhich day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ").title()
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        while day not in days_of_week:
            print("")
            print('*' * 40)
            day = input("Invalid input. Please enter a valid day of the week (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday): ").title()

    
    return city, month, day

#---------------------------------------------------------------------------------------------

def show_first_five_rows(df):
    #Asks the user if they want to see the first five rows of the dataset.
    flag = True
    show_rows = input("Do you want to check the first 5 rows of the dataset related to the chosen city? (yes or no): ").lower()

    while flag is True:
        
        if show_rows == 'yes':
            print("")
            print('-' * 100)
            print(df.head(5))

            # Check for more rows
            more_rows = input("Do you want to check another 5 rows of the dataset? (yes or no): ").lower()

            flag2 = True

            while flag2 is True:

                if more_rows == 'yes':
                    print("")
                    print('-' * 100)
                    print(df.iloc[len(df.head(5)):len(df.head(5)) + 5])
                    more_rows = input("Do you want to check another 5 rows of the dataset? (yes or no): ").lower()

                elif more_rows == 'no':
                    flag2 = False
                    flag = False
                    break

                else:
                    print("")
                    print('*' * 40)
                    more_rows = input("Invalid input. Please enter 'yes' or 'no':").lower()

        elif show_rows == 'no':
            flag = False
            break

        else:
            print("")
            print('*' * 40)
            show_rows = input("Invalid input. Please enter 'yes' or 'no':").lower()

#---------------------------------------------------------------------------------------------

def run_analysis():
    """
    Handles the main loop for the bike share data analysis.
    """
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        print('-' * 80)
        print(f"\nData for {city} loaded successfully. Number of rows: {df.shape[0]}")

        # Optionally ask if the user wants to restart or exit
	restart = input("\nWould you like to restart? (yes or no): ").lower()

        while restart not in ['yes', 'no']:
            print("")
            print('*' * 40)
            restart = input("Invalid input. Please enter 'yes' or 'no': ").lower()

        if restart != 'yes':
            


#---------------------------------------------------------------------------------------------

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        print('-' * 80)
        print(f"\nAnalyzing data for {city.title()}...\n")

        popular_times_of_travel(df)
        popular_stations_and_trip(df)
        trip_duration(df)
        user_info(df)
        show_first_five_rows(df)
	run_analysis()

#---------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

