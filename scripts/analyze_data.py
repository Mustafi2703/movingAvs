from fetch_data import data_fetcher

#data = data_fetcher()

def required_averages(data, requirements):
    for avg_type, periods in requirements.items():
        for period in periods:
            if avg_type == 'SMA':
                data[f'SMA_{period}'] = data['Close'].rolling(window=period).mean()
            elif avg_type == 'EMA':
                data[f'EMA_{period}'] = data['Close'].ewm(span=period, adjust=False).mean()
    
    return data



# SMAS
#data['SMA_50'] = data['Close'].rolling(window=50).mean()
#data['SMA_25'] = data['Close'].rolling(window=100).mean()

#EMAS
#data['EMA_30'] = data['Close'].ewm(span=30, adjust=False).mean()
#data['EMA_50'] = data['Close'].ewm(span=50, adjust=False).mean()
#data['EMA_50'] = data['Close'].ewm(span=50, adjust=False).mean()

#print(data.head())