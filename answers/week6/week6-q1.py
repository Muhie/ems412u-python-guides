# Muhie Al Haimus
# 25/09/2024
"""
Create a Program to:
a) First plot a bar chart of close vs open against time.
b) Then make a separate scatter (line) graph of the percentage difference between close and open (this will require extra processing as the dataset does not include this metric).
c) Plot a scatter graph of year-on-year stock growth.
"""
# NOTE YOU CAN DO THIS IN MANY WAYS - Parts A and B have many difference solutions
# I'm happy to take a look at other submissions which you can send to me via email: m.alhaimus@se23.qmul.ac.uk


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

"""
A function that opens takes in the file name as argument and 
opens the csv and returns all the data in the CSV as a pandas dataframe
 """
def get_data(file_path):
    data = pd.read_csv(file_path)
    return data

# A method that splits the data to individual lists
def split_data(data):
    dates = data["Date"]
    opens = data["Open"]
    highs = data["High"]
    lows = data["Low"]
    closes = data["Close"]
    adj_closes = data["Adj Close"]
    volumes = data["Volume"]
    return dates, opens, highs, lows, closes, adj_closes, volumes

# A method to get the percentage differences between open vs close for all the data set
def get_percentage_difference(opens, closes):
    percentage_difference = []
    number_of_data_points = len(opens)
    for i in range(0, number_of_data_points):
        open = opens[i]
        close = closes[i]
        percentage_difference[i] = ((close - open) / open) * 100 
    return percentage_difference


# A function to plot open vs close for 5 five days 
def plot_chart_open_vs_close(dates, opens, closes, x_label, y_label, title): # For part A
    barWidth = 0.25
    fig = plt.subplots() 
    plt.bar(dates, opens, color ='r', width = barWidth, 
    edgecolor ='green', label ='Open').set_label("Open") # Fancy formatting
    plt.bar(dates, closes, color ='g', width = barWidth, 
    edgecolor ='red', label ='Close').set_label("Close") # Fancy Formatting
    plt.xticks([])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.show()

# A method to get the difference between close and opening values
def get_percentage_difference(opens, closes):
    percentage_difference = []
    number_of_data_points = len(opens)
    for i in range(0, number_of_data_points):
        open = opens[i]
        close = closes[i]
        percentage_difference.append(((close - open) / open) * 100)
    return percentage_difference
# A method to plot scatter charts
def plot_scatter(dates, percentage_difference, x_label, y_label, title, x_ticks):
    fig, ax = plt.subplots()
    ax.plot(dates, percentage_difference) # this is just fancy formatting
    if x_ticks == False:
        plt.xticks([])

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

def split_years(data):
    df = data
    # Get data from all years you can do this in a more 
    # sophisticated way but I don't expect that this is fine 
    # Found this on stackoverflow (best website ever)
    df_2020 = df[pd.to_datetime(df['Date']).dt.strftime('%Y') == "2020"]
    df2021 = df[pd.to_datetime(df['Date']).dt.strftime('%Y') == "2021"]
    df2022 = df[pd.to_datetime(df['Date']).dt.strftime('%Y') == "2022"]
    df2023 = df[pd.to_datetime(df['Date']).dt.strftime('%Y') == "2023"]
    df2024 = df[pd.to_datetime(df['Date']).dt.strftime('%Y') == "2024"]
    return df_2020, df2021, df2022, df2023, df2024

def find_year_open_vs_close(data_frame):
    print(data_frame)
    return ((data_frame["Close"].iloc[-1] - data_frame["Open"].iloc[0]) 
            / data_frame["Open"].iloc[0]) * 100 # get percentage difference for that year



if __name__ == "__main__": # this is just best python practice, it just means that python knows you are running this program from the correct file see tech with tim for more details
    data = get_data("./week6/data.csv") # change the path accordingly to where the file is
    split_data = split_data(data)
    plot_chart_open_vs_close(split_data[0], split_data[1], split_data[4], "Date", "Open vs Close ($)", "Percentage Difference between open vs close ")
    percentage_difference = get_percentage_difference(split_data[1], split_data[4])
    plot_scatter(split_data[0],percentage_difference, "Date", "Percentage Difference (%)", "Percentage Difference between open vs close", False)
    years = split_years(data)
    percentage_differences = []
    for i in range(0, len(years)):
        percentage_differences.append(find_year_open_vs_close(years[i]))
    plot_scatter(["2020","2021","2022","2023","2024"], percentage_differences, "Year", "Year on Year growth (%)", "Year on Year Stock Growth from 2020-2024", True)
