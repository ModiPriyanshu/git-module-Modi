import pandas as pd
import matplotlib.pyplot as plt
import os

DATA_URL = 'https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv'
def read_and_visualize():
    df = pd.read_csv(DATA_URL)
    print(f"Total rows: {df.shape[0]}, Total columns: {df.shape[1]}")

    plt.figure(figsize=(8, 5))
    plt.plot(pd.to_datetime(df['AAPL_x']), df['AAPL_y'])
    plt.xlabel('Date')
    plt.ylabel('Close')
    plt.title('Apple Close Pricing over the Time')
    plt.savefig('apple_stock.png')
    plt.show() 
    
    print(df.head())
 # You'll use pandas to read the CSV data from the URL.
 # The read_csv function from pandas can accept a URL directly.
 # Print the total number of rows and columns in the dataset.
 # Plot the results and save the plot as 'apple_stock.png'.
    return df # or whatever variable you use to store the dataframe

read_and_visualize()
