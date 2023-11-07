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
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """    
    if weather_data:
        max_value = float(max(weather_data))
        max_positions = [i for i in range(len(weather_data)) if float((weather_data)[i]) == max_value]
        if max_positions:
            last_max_position = max(max_positions)
        else:
            return ()
    else:
        return ()
    return (max_value, last_max_position)

def generate_summary(weather_data):

    count_rows = len(weather_data) # counting the rows of data - a row for each day

    # convert the array into lists
    date_list = [row[0] for row in weather_data]
    mins_list = [row[1] for row in weather_data]
    maxs_list = [row[2] for row in weather_data]

    # min_tuple = find_min(mins_list)
    # min_value = min_tuple[0]
    # min_position = min_tuple[1]
    # min_date = convert_date(date_list[min_position])
    # min_temp = format_temperature(convert_f_to_c(min_value))

    min_temp = format_temperature(convert_f_to_c(find_min(mins_list)[0]))
    min_date = convert_date(date_list[find_min(mins_list)[1]])

    # max_tuple = find_max(maxs_list)
    # max_value = find_max(maxs_list)[0]
    # max_position = find_max(maxs_list)[1]

    max_temp = format_temperature(convert_f_to_c(find_max(maxs_list)[0]))
    max_date = convert_date(date_list[find_max(maxs_list)[1]])

    avg_min = format_temperature(convert_f_to_c(calculate_mean(mins_list)))
    avg_max = format_temperature(convert_f_to_c(calculate_mean(maxs_list)))
        
    summary = (f"{count_rows} Day Overview\n  The lowest temperature will be {min_temp}, and will occur on {min_date}.\n  The highest temperature will be {max_temp}, and will occur on {max_date}.\n  The average low this week is {avg_min}.\n  The average high this week is {avg_max}.\n")
    """    
   Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """ 
    return (summary)

def generate_daily_summary(weather_data):
    daily_summary =""
    for row in weather_data:

        date = convert_date(row[0])
        min_temp = format_temperature(convert_f_to_c(row[1])) 
        max_temp = format_temperature(convert_f_to_c(row[2]))
        daily_summary += (f"---- {date} ----\n  Minimum Temperature: {min_temp}\n  Maximum Temperature: {max_temp}\n\n")

    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    return((daily_summary))

