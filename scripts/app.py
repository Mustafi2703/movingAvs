import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import yfinance as yf
import plotly.graph_objects as go
from fetch_data import data_fetcher
from analyze_data import required_averages

app = dash.Dash(__name__)

# Assuming you already have a list of tickers
tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'NFLX', 'NVDA', 'JPM']

app.layout = html.Div([
    dcc.Dropdown(
        id='stock-dropdown',
        options=[{'label': ticker, 'value': ticker} for ticker in tickers],
        value='AAPL'  # Default value
    ),
    dcc.Graph(id='price-chart')
])

@app.callback(
    Output('price-chart', 'figure'),
    [Input('stock-dropdown', 'value')]
)
def update_chart(selected_ticker):
    data = data_fetcher(selected_ticker)  # Modify this to fetch data for the selected ticker
    reqs = {
        'SMA': [50],
        'EMA': [25, 50]
    }
    final_data = required_averages(data, reqs)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=final_data.index, y=final_data['Close'], mode='lines', name='Close Price'))

    for key in final_data.columns:
        if 'SMA' in key or 'EMA' in key:
            fig.add_trace(go.Scatter(x=final_data.index, y=final_data[key], mode='markers', name=key))

    fig.update_layout(
        width=1400,  # Adjust width as needed
        height=750,  # Adjust height as needed
        plot_bgcolor='black',   # Sets the plot area background color
        paper_bgcolor='black',  # Sets the outer 'paper' background color
        font=dict(color='white')
    )
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)