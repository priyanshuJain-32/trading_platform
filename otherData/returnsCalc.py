import pandas as pd
import datetime as dt

def returns_calc(tickers_list: list) -> pd.DataFrame:
    ohlc_mon = {} # database of each stocks monthly prices
    start = dt.datetime.today() - dt.timedelta(3650)
    end = dt.datetime.today()

    for ticker in tickers_list:
        
        ohlc_mon[ticker] = yf.download(ticker, start, end, interval = '1mo')
        
        ohlc_mon[ticker].dropna(inplace = True)
        
    tickers_list = ohlc_mon.keys() # keeping only those tickers for which there was no error

    # Calculate returns for each stock and save in seperate dataFrame

    return_df = pd.DataFrame()

    for ticker in tickers_list:
        ohlc_mon[ticker]["monthly_return"] = ohlc_mon[ticker]["Adj Close"].pct_change()
        return_df[ticker] = ohlc_mon[ticker]["monthly_return"]
        
    return_df.dropna(inplace = True, how="all")

    return return_df