def fetch_asset_data():
    import pandas as pd
    import requests

    symbols = {
        'BTC/EUR': 'BTC/EUR',
        'USD/EUR': 'USD/EUR'
    }

    API_KEY = "Enter your API key here"
    
    dfs = []

    for label, symbol in symbols.items():
        url = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval=1day&apikey={API_KEY}&outputsize=895'
        response = requests.get(url)
        data = response.json()

        if 'values' not in data:
            raise ValueError(f"API error for {symbol}: {data.get('message', 'Unknown error')}")

        df = pd.DataFrame(data['values'])
        df['datetime'] = pd.to_datetime(df['datetime'])
        df.set_index('datetime', inplace=True)
        df = df.sort_index()
        df = df.rename(columns={'close': label})
        df = df[[label]].astype(float)
        dfs.append(df)

    merged = pd.concat(dfs, axis=1)
    return merged.dropna()
