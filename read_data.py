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
    plt.close() 
    
    print(df.head())
 # You'll use pandas to read the CSV data from the URL.
 # The read_csv function from pandas can accept a URL directly.
 # Print the total number of rows and columns in the dataset.
 # Plot the results and save the plot as 'apple_stock.png'.
    return df # or whatever variable you use to store the dataframe

df = read_and_visualize()

def calculate_moving_average(df, window_size=30):
    df['Simple Moving_Average'] = df['AAPL_y'].rolling(window=window_size).mean()

    plt.figure(figsize=(8, 5))
    plt.plot(pd.to_datetime(df['AAPL_x']), df['AAPL_y'])
    plt.plot(pd.to_datetime(df['AAPL_x']), df['Simple Moving_Average'], label='30-Day SMA', color='orange')
    plt.xlabel('Date')
    plt.ylabel('Close')
    plt.title('Apple Close Pricing with 30-Day Simple Moving Average')
    plt.savefig('apple_stock_Simple_Moving_Average.png')
    plt.close() 

    return df

calculate_moving_average(df, window_size=30)

def calculate_bollinger_bands(df, window_size=7):
    df['Middle Band'] = df['AAPL_y'].rolling(window=window_size).mean()
    df['Standard Deviation'] = df['AAPL_y'].rolling(window=window_size).std()
    df['Upper Band'] = df['Middle Band'] + (df['Standard Deviation'] * 2)
    df['Lower Band'] = df['Middle Band'] - (df['Standard Deviation'] * 2)

    plt.figure(figsize=(8, 5))
    plt.plot(pd.to_datetime(df['AAPL_x']), df['AAPL_y'])
    plt.plot(pd.to_datetime(df['AAPL_x']), df['Middle Band'], label='Middle Band', color='orange')
    plt.plot(pd.to_datetime(df['AAPL_x']), df['Upper Band'], label='Upper Band', color='green')
    plt.plot(pd.to_datetime(df['AAPL_x']), df['Lower Band'], label='Lower Band', color='red')
    plt.xlabel('Date')
    plt.ylabel('Close')
    plt.title('Apple Close Pricing with Implementing Bollinger Bands')
    plt.legend()
    plt.savefig('apple_stock_Bollinger_Bands.png')
    plt.close() 

    return df

calculate_bollinger_bands(df, window_size=7)

def calculate_Drawdown(df):

    AAPL_Prices = df['AAPL_y'].tolist()
    Max_Price = max(AAPL_Prices)
    Min_Price = min(AAPL_Prices)
    MDD = (Max_Price - Min_Price) / Max_Price
    print(f"Maximum Drawdown is: {MDD:.2%}")

    peak = AAPL_Prices[0]
    DDD = []

    for price in AAPL_Prices:
        if price > peak:
            peak = price
        drawdown = (peak - price) / peak
        DDD.append(drawdown)

    plt.figure(figsize=(8, 5))
    plt.plot(pd.to_datetime(df['AAPL_x']), DDD, label='Drawdown', color='orange')
    plt.xlabel('Date')
    plt.ylabel('Drawdown')
    plt.title('Apple Close Pricing with Drawdown')
    plt.savefig('apple_stock_Daily_Drawdown.png')
    plt.close()

    return df,DDD

calculate_Drawdown(df)

def Calculate_RSI(df, window_size=3):
    
    diff = df['AAPL_y'].diff().tolist()

    Gains = []
    Losses = []
    
    for difference in diff:
        if difference == 0:
            Gains.append(0)
            Losses.append(0)
        elif difference > 0:
            Gains.append(difference)
            Losses.append(0)        
        else:
            Gains.append(0)
            Losses.append(-difference)
    
    df['Gain'] = Gains
    df['Loss'] = Losses

    df['Average Gain'] = df['Gain'].rolling(window=window_size).mean()
    df['Average Loss'] = df['Loss'].rolling(window=window_size).mean()
    

    Relative_Strength_RS = df['Average Gain'] / df['Average Loss']

    df['RSI'] = 100 - (100 / (1 + Relative_Strength_RS))

    plt.figure(figsize=(8, 5))
    plt.plot(pd.to_datetime(df['AAPL_x']), df['RSI'], label='RSI', color='orange')
    plt.axhline(70, color='red', linestyle='--')
    plt.axhline(30, color='green', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.title('Apple Close Pricing with RSI')
    plt.savefig('apple_stock_RSI.png')
    plt.close() 

    return df['RSI']

Calculate_RSI(df, window_size=3)