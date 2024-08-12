import plotly.graph_objects as go
from fetch_data import data_fetcher
from analyze_data import required_averages

reqs = {}
data = data_fetcher()

reqs = {
    'SMA': [50],
    'EMA': [25,50]
}

final_data = required_averages(data, reqs)

#print(final_data.head())
fig = go.Figure()

fig.add_trace(go.Scatter(x=final_data.index, y=final_data['Close'], mode='lines', name='Close Price'))

for key in final_data.columns:
    if 'SMA' in key or 'EMA' in key:
        fig.add_trace(go.Scatter(x=final_data.index, y=final_data[key], mode='markers', name=key))

fig.show()