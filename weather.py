import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    # this one is already done
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):

    date = datetime.fromisoformat(iso_string)
    return date.strftime('%A %d %B %Y')


    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """


def convert_f_to_c(temp_in_farenheit):
    temp_in_farenheit_float = float(temp_in_farenheit)
    temp_in_celsius = float((temp_in_farenheit_float - 32) * 5/9)
    result = round(temp_in_celsius,1)
    return result


def calculate_mean(weather_data):
    # print(weather_data)
    # print(type(weather_data))
    len_weather = int(len(weather_data))
    # print(len_weather)
    sum_weather = (sum(float(x) for x in weather_data))
    mean_weather = (sum_weather / len_weather)
    # print(sum_weather)
    # print(mean_weather)
    # print(type(mean_weather))
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers. 
        # (I heard that weather data is a list of lists)
    Returns:
        A float representing the mean value.
    """
    return mean_weather
# calculate_mean([49, 57, 56, 55, 53])
# calculate_mean([51.0, 58.2, 59.9, 52.4, 52.1, 48.4, 47.8, 53.43])
# calculate_mean(["51", "58", "59", "52", "52", "48", "47", "53"])
# calculate_mean([-51, -58, -59, -52, -52, -48, -47, -53])

def load_data_from_csv(csv_file):
    with open (csv_file, encoding="utf-8") as current_file:
        reader = csv.reader(current_file)
        next(reader)

        weather_data = []
#   turn the temp values into integers
        for row in reader:
            if row:
                row[1] = int(row[1])
                row[2] = int(row[2])
                weather_data.append(row[:])


    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    return list(weather_data)

def find_min(weather_data):

    if weather_data:
        min_value = float(min(weather_data))
        min_positions = [i for i in range(len(weather_data)) if float((weather_data)[i]) == min_value]
        if min_positions:
            last_min_position = max(min_positions)
        else:
            return ()
    else:
        return ()
        """Calculates the minimum value in a list of numbers.
        Args:
            weather_data: A list of numbers.
        Returns:
            The minium value and of there is moe than one min value, the last min value's position in the list.
        """

    return (min_value, last_min_position)

def find_max(weather_data):
    if weather_data:
        max_value = float(max(weather_data))
        max_positions = [i for i in range(len(weather_data)) if float((weather_data)[i]) == max_value]
        if max_positions:
            last_max_position = max(max_positions)
        else:
            return ()
    else:
        return ()
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    return (max_value, last_max_position)

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
