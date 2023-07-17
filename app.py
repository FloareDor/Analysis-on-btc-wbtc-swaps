import pandas as pd
import plotly.graph_objs as go
from flask import Flask, render_template
import re

# Read the CSV file into a DataFrame
data = pd.read_csv('data/updated_file.csv')

# Convert the 'DateTime (UTC)' column to datetime data type
data['DateTime (UTC)'] = pd.to_datetime(data['DateTime (UTC)'])

# Create Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# Define route for the interactive visualization
@app.route('/scatter')
def interactive_visualization():
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].str.replace('[$,]', '').replace('"', '').replace("'", '')
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].apply(lambda x: re.sub(r'\D', '', x)).astype(float) / 100

    # Group the data by date and calculate the sum of the volume per day
    volume_per_day = data.groupby(data['DateTime (UTC)'].dt.date)['USDValueDayOfTx'].sum()

    # Convert the relevant columns to string type for string manipulation operations
    data['TokenValue'] = data['TokenValue'].astype(str)
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].astype(str)

    # Preprocess the token value column to remove non-numeric characters and convert to numeric type
    data['TokenValue'] = data['TokenValue'].str.replace('[$,]', '').replace(",", "").replace("$", "").replace('"', "").replace('"', "").replace("1,003.30798155", "1003").astype(float)

    # Group the data by date and calculate the average token value per day
    average_token_value = data.groupby(data['DateTime (UTC)'].dt.date)['TokenValue'].mean()
    

    # Create the Plotly figures
    fig_volume = go.Figure()
    fig_volume.add_trace(go.Scatter(x=volume_per_day.index, y=volume_per_day.values, name='Volume'))
    fig_volume.update_layout(
        title='Volume per Day',
        xaxis_title='Date',
        yaxis_title='Volume (Millions)'
    )

    fig_avg_token_value = go.Figure()
    fig_avg_token_value.add_trace(go.Scatter(x=average_token_value.index, y=average_token_value.values, mode='lines', name='Average Token Value'))
    fig_avg_token_value.update_layout(
        title='Average Token Value per Day',
        xaxis_title='Date',
        yaxis_title='Average Token Value (wbtc)'
    )

    # Convert the Plotly figures to JSON for rendering
    plot_volume_json = fig_volume.to_json()
    plot_avg_token_value_json = fig_avg_token_value.to_json()

	    # Group the data by date and calculate the sum of the volume per day in BTC
    volume_btc_per_day = data.groupby(data['DateTime (UTC)'].dt.date)['TokenValue'].sum()

    # Create the Plotly figure for BTC volume
    fig_volume_btc = go.Figure()
    fig_volume_btc.add_trace(go.Scatter(x=volume_btc_per_day.index, y=volume_btc_per_day.values, name='Volume (BTC)'))
    fig_volume_btc.update_layout(
        title='Volume per Day (BTC)',
        xaxis_title='Date',
        yaxis_title='Volume (BTC)'
    )

    # Convert the Plotly figure to JSON for rendering
    plot_volume_btc_json = fig_volume_btc.to_json()
    
    # Render the HTML template with the Plotly figure JSON data
    return render_template('visualization.html', plot_volume_json=plot_volume_json, plot_avg_token_value_json=plot_avg_token_value_json, plot_volume_btc_json = plot_volume_btc_json)


# Define route for the interactive visualization
@app.route('/bar')
def interactive_visualization_bar():
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].str.replace('[$,]', '').replace('"', '').replace("'", '')
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].apply(lambda x: re.sub(r'\D', '', x)).astype(float) / 100

    # Group the data by date and calculate the sum of the volume per day
    volume_per_day = data.groupby(data['DateTime (UTC)'].dt.date)['USDValueDayOfTx'].sum()

    # Convert the relevant columns to string type for string manipulation operations
    data['TokenValue'] = data['TokenValue'].astype(str)
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].astype(str)

    # Preprocess the token value column to remove non-numeric characters and convert to numeric type
    data['TokenValue'] = data['TokenValue'].str.replace('[$,]', '').replace(",", "").replace("$", "").replace('"', "").replace('"', "").replace("1,003.30798155", "1003").astype(float)

    # Group the data by date and calculate the average token value per day
    average_token_value = data.groupby(data['DateTime (UTC)'].dt.date)['TokenValue'].mean()
    

    # Create the Plotly figures
    fig_volume = go.Figure()
    fig_volume.add_trace(go.Bar(x=volume_per_day.index, y=volume_per_day.values, name='Volume'))
    fig_volume.update_layout(
        title='Volume per Day ($)',
        xaxis_title='Date',
        yaxis_title='Volume (Millions)'
    )

    fig_avg_token_value = go.Figure()
    fig_avg_token_value.add_trace(go.Bar(x=average_token_value.index, y=average_token_value.values,  name='Average Token Value'))
    fig_avg_token_value.update_layout(
        title='Average Token Value per Day',
        xaxis_title='Date',
        yaxis_title='Average Token Value (wbtc)'
    )

    # Convert the Plotly figures to JSON for rendering
    plot_volume_json = fig_volume.to_json()
    plot_avg_token_value_json = fig_avg_token_value.to_json()

	    # Group the data by date and calculate the sum of the volume per day in BTC
    volume_btc_per_day = data.groupby(data['DateTime (UTC)'].dt.date)['TokenValue'].sum()

    # Create the Plotly figure for BTC volume
    fig_volume_btc = go.Figure()
    fig_volume_btc.add_trace(go.Bar(x=volume_btc_per_day.index, y=volume_btc_per_day.values, name='Volume (BTC)'))
    fig_volume_btc.update_layout(
        title='Volume per Day (BTC)',
        xaxis_title='Date',
        yaxis_title='Volume (BTC)'
    )

    # Convert the Plotly figure to JSON for rendering
    plot_volume_btc_json = fig_volume_btc.to_json()
    
    # Render the HTML template with the Plotly figure JSON data
    return render_template('visualization.html', plot_volume_json=plot_volume_json, plot_avg_token_value_json=plot_avg_token_value_json, plot_volume_btc_json = plot_volume_btc_json)

@app.route('/7DA')
def interactive_visualization_7DA():
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].str.replace('[$,]', '').replace('"', '').replace("'", '')
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].apply(lambda x: re.sub(r'\D', '', x)).astype(float) / 100

    # Group the data by date and calculate the sum of the volume per day
    volume_per_week = data.resample('W', on='DateTime (UTC)')['USDValueDayOfTx'].sum()

    # Convert the relevant columns to string type for string manipulation operations
    data['TokenValue'] = data['TokenValue'].astype(str)
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].astype(str)

    # Preprocess the token value column to remove non-numeric characters and convert to numeric type
    data['TokenValue'] = data['TokenValue'].str.replace('[$,]', '').replace(",", "").replace("$", "").replace('"', "").replace('"', "").replace("1,003.30798155", "1003").astype(float)

    # Group the data by date and calculate the average token value per day
    average_token_value = data.resample('W', on='DateTime (UTC)')['TokenValue'].mean()
    

    # Create the Plotly figures
    fig_volume = go.Figure()
    fig_volume.add_trace(go.Scatter(x=volume_per_week.index, y=volume_per_week.values, name='Volume'))
    fig_volume.update_layout(
        title='Volume per Week ($)',
        xaxis_title='Date',
        yaxis_title='Volume (Millions)'
    )

    fig_avg_token_value = go.Figure()
    fig_avg_token_value.add_trace(go.Scatter(x=average_token_value.index, y=average_token_value.values, mode='lines', name='Average Token Value'))
    fig_avg_token_value.update_layout(
        title='Average Token Value per Week',
        xaxis_title='Date',
        yaxis_title='Average Token Value (wbtc)'
    )

    # Convert the Plotly figures to JSON for rendering
    plot_volume_json = fig_volume.to_json()
    plot_avg_token_value_json = fig_avg_token_value.to_json()

	    # Group the data by date and calculate the sum of the volume per day in BTC
    volume_btc_per_day = data.resample('W', on='DateTime (UTC)')['TokenValue'].sum()

    # Create the Plotly figure for BTC volume
    fig_volume_btc = go.Figure()
    fig_volume_btc.add_trace(go.Scatter(x=volume_btc_per_day.index, y=volume_btc_per_day.values, name='Volume (BTC)'))
    fig_volume_btc.update_layout(
        title='Volume per Week (BTC)',
        xaxis_title='Date',
        yaxis_title='Volume (BTC)'
    )

    # Convert the Plotly figure to JSON for rendering
    plot_volume_btc_json = fig_volume_btc.to_json()
    
    # Render the HTML template with the Plotly figure JSON data
    return render_template('visualization.html', plot_volume_json=plot_volume_json, plot_avg_token_value_json=plot_avg_token_value_json, plot_volume_btc_json = plot_volume_btc_json)


@app.route('/14DA')
def interactive_visualization_14DA():
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].str.replace('[$,]', '').replace('"', '').replace("'", '')
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].apply(lambda x: re.sub(r'\D', '', x)).astype(float) / 100

    # Group the data by date and calculate the sum of the volume per day
    volume_per_14_days = data.resample('2W', on='DateTime (UTC)')['USDValueDayOfTx'].sum()

    # Convert the relevant columns to string type for string manipulation operations
    data['TokenValue'] = data['TokenValue'].astype(str)
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].astype(str)

    # Preprocess the token value column to remove non-numeric characters and convert to numeric type
    data['TokenValue'] = data['TokenValue'].str.replace('[$,]', '').replace(",", "").replace("$", "").replace('"', "").replace('"', "").replace("1,003.30798155", "1003").astype(float)

    # Group the data by date and calculate the average token value per day
    average_token_value = data.resample('2W', on='DateTime (UTC)')['TokenValue'].mean()

    # Create the Plotly figures
    fig_volume = go.Figure()
    fig_volume.add_trace(go.Scatter(x=volume_per_14_days.index, y=volume_per_14_days.values, name='Volume'))
    fig_volume.update_layout(
        title='Volume per 14 days ($)',
        xaxis_title='Date',
        yaxis_title='Volume (Millions)'
    )

    fig_avg_token_value = go.Figure()
    fig_avg_token_value.add_trace(go.Scatter(x=average_token_value.index, y=average_token_value.values, mode='lines', name='Average Token Value'))
    fig_avg_token_value.update_layout(
        title='Average Token Value per 14 days',
        xaxis_title='Date',
        yaxis_title='Average Token Value (wbtc)'
    )

    # Convert the Plotly figures to JSON for rendering
    plot_volume_json = fig_volume.to_json()
    plot_avg_token_value_json = fig_avg_token_value.to_json()

	    # Group the data by date and calculate the sum of the volume per day in BTC
    volume_btc_per_14_days = data.resample('2W', on='DateTime (UTC)')['TokenValue'].sum()

    # Create the Plotly figure for BTC volume
    fig_volume_btc = go.Figure()
    fig_volume_btc.add_trace(go.Scatter(x=volume_btc_per_14_days.index, y=volume_btc_per_14_days.values, name='Volume (BTC)'))
    fig_volume_btc.update_layout(
        title='Volume per 14 days (BTC)',
        xaxis_title='Date',
        yaxis_title='Volume (BTC)'
    )

    # Convert the Plotly figure to JSON for rendering
    plot_volume_btc_json = fig_volume_btc.to_json()
    
    # Render the HTML template with the Plotly figure JSON data
    return render_template('visualization.html', plot_volume_json=plot_volume_json, plot_avg_token_value_json=plot_avg_token_value_json, plot_volume_btc_json = plot_volume_btc_json)

@app.route('/30DA')
def interactive_visualization_30DA():
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].str.replace('[$,]', '').replace('"', '').replace("'", '')
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].apply(lambda x: re.sub(r'\D', '', x)).astype(float) / 100

    # Group the data by date and calculate the sum of the volume per day
    volume_per_14_days = data.resample('30D', on='DateTime (UTC)')['USDValueDayOfTx'].sum()

    # Convert the relevant columns to string type for string manipulation operations
    data['TokenValue'] = data['TokenValue'].astype(str)
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].astype(str)

    # Preprocess the token value column to remove non-numeric characters and convert to numeric type
    data['TokenValue'] = data['TokenValue'].str.replace('[$,]', '').replace(",", "").replace("$", "").replace('"', "").replace('"', "").replace("1,003.30798155", "1003").astype(float)

    # Group the data by date and calculate the average token value per day
    average_token_value = data.resample('30D', on='DateTime (UTC)')['TokenValue'].mean()

    # Create the Plotly figures
    fig_volume = go.Figure()
    fig_volume.add_trace(go.Scatter(x=volume_per_14_days.index, y=volume_per_14_days.values, name='Volume'))
    fig_volume.update_layout(
        title='Volume per month ($)',
        xaxis_title='Date',
        yaxis_title='Volume (Millions)'
    )

    fig_avg_token_value = go.Figure()
    fig_avg_token_value.add_trace(go.Scatter(x=average_token_value.index, y=average_token_value.values, mode='lines', name='Average Token Value'))
    fig_avg_token_value.update_layout(
        title='Average Token Value per month',
        xaxis_title='Date',
        yaxis_title='Average Token Value (wbtc)'
    )

    # Convert the Plotly figures to JSON for rendering
    plot_volume_json = fig_volume.to_json()
    plot_avg_token_value_json = fig_avg_token_value.to_json()

	    # Group the data by date and calculate the sum of the volume per day in BTC
    volume_btc_per_14_days = data.resample('30D', on='DateTime (UTC)')['TokenValue'].sum()

    # Create the Plotly figure for BTC volume
    fig_volume_btc = go.Figure()
    fig_volume_btc.add_trace(go.Scatter(x=volume_btc_per_14_days.index, y=volume_btc_per_14_days.values, name='Volume (BTC)'))
    fig_volume_btc.update_layout(
        title='Volume per month (BTC)',
        xaxis_title='Date',
        yaxis_title='Volume (BTC)'
    )

    # Convert the Plotly figure to JSON for rendering
    plot_volume_btc_json = fig_volume_btc.to_json()
    
    # Render the HTML template with the Plotly figure JSON data
    return render_template('visualization.html', plot_volume_json=plot_volume_json, plot_avg_token_value_json=plot_avg_token_value_json, plot_volume_btc_json = plot_volume_btc_json)


@app.route('/7DA/bar')
def interactive_visualization_7DA_bar():
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].str.replace('[$,]', '').replace('"', '').replace("'", '')
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].apply(lambda x: re.sub(r'\D', '', x)).astype(float) / 100

    # Group the data by date and calculate the sum of the volume per day
    volume_per_week = data.resample('W', on='DateTime (UTC)')['USDValueDayOfTx'].sum()

    # Convert the relevant columns to string type for string manipulation operations
    data['TokenValue'] = data['TokenValue'].astype(str)
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].astype(str)

    # Preprocess the token value column to remove non-numeric characters and convert to numeric type
    data['TokenValue'] = data['TokenValue'].str.replace('[$,]', '').replace(",", "").replace("$", "").replace('"', "").replace('"', "").replace("1,003.30798155", "1003").astype(float)

    # Group the data by date and calculate the average token value per day
    average_token_value = data.resample('W', on='DateTime (UTC)')['TokenValue'].mean()
    

    # Create the Plotly figures
    fig_volume = go.Figure()
    fig_volume.add_trace(go.Bar(x=volume_per_week.index, y=volume_per_week.values, name='Volume'))
    fig_volume.update_layout(
        title='Volume per Week ($)',
        xaxis_title='Date',
        yaxis_title='Volume (Millions)'
    )

    fig_avg_token_value = go.Figure()
    fig_avg_token_value.add_trace(go.Bar(x=average_token_value.index, y=average_token_value.values, name='Average Token Value'))
    fig_avg_token_value.update_layout(
        title='Average Token Value per Week',
        xaxis_title='Date',
        yaxis_title='Average Token Value (wbtc)'
    )

    # Convert the Plotly figures to JSON for rendering
    plot_volume_json = fig_volume.to_json()
    plot_avg_token_value_json = fig_avg_token_value.to_json()

	    # Group the data by date and calculate the sum of the volume per day in BTC
    volume_btc_per_day = data.resample('W', on='DateTime (UTC)')['TokenValue'].sum()

    # Create the Plotly figure for BTC volume
    fig_volume_btc = go.Figure()
    fig_volume_btc.add_trace(go.Bar(x=volume_btc_per_day.index, y=volume_btc_per_day.values, name='Volume (BTC)'))
    fig_volume_btc.update_layout(
        title='Volume per Week (BTC)',
        xaxis_title='Date',
        yaxis_title='Volume (BTC)'
    )

    # Convert the Plotly figure to JSON for rendering
    plot_volume_btc_json = fig_volume_btc.to_json()
    
    # Render the HTML template with the Plotly figure JSON data
    return render_template('visualization.html', plot_volume_json=plot_volume_json, plot_avg_token_value_json=plot_avg_token_value_json, plot_volume_btc_json = plot_volume_btc_json)


@app.route('/14DA/bar')
def interactive_visualization_14DA_bar():
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].str.replace('[$,]', '').replace('"', '').replace("'", '')
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].apply(lambda x: re.sub(r'\D', '', x)).astype(float) / 100

    # Group the data by date and calculate the sum of the volume per day
    volume_per_14_days = data.resample('2W', on='DateTime (UTC)')['USDValueDayOfTx'].sum()

    # Convert the relevant columns to string type for string manipulation operations
    data['TokenValue'] = data['TokenValue'].astype(str)
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].astype(str)

    # Preprocess the token value column to remove non-numeric characters and convert to numeric type
    data['TokenValue'] = data['TokenValue'].str.replace('[$,]', '').replace(",", "").replace("$", "").replace('"', "").replace('"', "").replace("1,003.30798155", "1003").astype(float)

    # Group the data by date and calculate the average token value per day
    average_token_value = data.resample('2W', on='DateTime (UTC)')['TokenValue'].mean()

    # Create the Plotly figures
    fig_volume = go.Figure()
    fig_volume.add_trace(go.Bar(x=volume_per_14_days.index, y=volume_per_14_days.values, name='Volume'))
    fig_volume.update_layout(
        title='Volume per 14 days ($)',
        xaxis_title='Date',
        yaxis_title='Volume (Millions)'
    )

    fig_avg_token_value = go.Figure()
    fig_avg_token_value.add_trace(go.Bar(x=average_token_value.index, y=average_token_value.values, name='Average Token Value'))
    fig_avg_token_value.update_layout(
        title='Average Token Value per 14 days',
        xaxis_title='Date',
        yaxis_title='Average Token Value (wbtc)'
    )

    # Convert the Plotly figures to JSON for rendering
    plot_volume_json = fig_volume.to_json()
    plot_avg_token_value_json = fig_avg_token_value.to_json()

	    # Group the data by date and calculate the sum of the volume per day in BTC
    volume_btc_per_14_days = data.resample('2W', on='DateTime (UTC)')['TokenValue'].sum()

    # Create the Plotly figure for BTC volume
    fig_volume_btc = go.Figure()
    fig_volume_btc.add_trace(go.Bar(x=volume_btc_per_14_days.index, y=volume_btc_per_14_days.values, name='Volume (BTC)'))
    fig_volume_btc.update_layout(
        title='Volume per 14 days (BTC)',
        xaxis_title='Date',
        yaxis_title='Volume (BTC)'
    )

    # Convert the Plotly figure to JSON for rendering
    plot_volume_btc_json = fig_volume_btc.to_json()
    
    # Render the HTML template with the Plotly figure JSON data
    return render_template('visualization.html', plot_volume_json=plot_volume_json, plot_avg_token_value_json=plot_avg_token_value_json, plot_volume_btc_json = plot_volume_btc_json)

@app.route('/30DA/bar')
def interactive_visualization_30DA_bar():
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].str.replace('[$,]', '').replace('"', '').replace("'", '')
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].apply(lambda x: re.sub(r'\D', '', x)).astype(float) / 100

    # Group the data by date and calculate the sum of the volume per day
    volume_per_14_days = data.resample('30D', on='DateTime (UTC)')['USDValueDayOfTx'].sum()

    # Convert the relevant columns to string type for string manipulation operations
    data['TokenValue'] = data['TokenValue'].astype(str)
    data['USDValueDayOfTx'] = data['USDValueDayOfTx'].astype(str)

    # Preprocess the token value column to remove non-numeric characters and convert to numeric type
    data['TokenValue'] = data['TokenValue'].str.replace('[$,]', '').replace(",", "").replace("$", "").replace('"', "").replace('"', "").replace("1,003.30798155", "1003").astype(float)

    # Group the data by date and calculate the average token value per day
    average_token_value = data.resample('30D', on='DateTime (UTC)')['TokenValue'].mean()

    # Create the Plotly figures
    fig_volume = go.Figure()
    fig_volume.add_trace(go.Bar(x=volume_per_14_days.index, y=volume_per_14_days.values, name='Volume'))
    fig_volume.update_layout(
        title='Volume per month ($)',
        xaxis_title='Date',
        yaxis_title='Volume (Millions)'
    )

    fig_avg_token_value = go.Figure()
    fig_avg_token_value.add_trace(go.Bar(x=average_token_value.index, y=average_token_value.values, name='Average Token Value'))
    fig_avg_token_value.update_layout(
        title='Average Token Value per month',
        xaxis_title='Date',
        yaxis_title='Average Token Value (wbtc)'
    )

    # Convert the Plotly figures to JSON for rendering
    plot_volume_json = fig_volume.to_json()
    plot_avg_token_value_json = fig_avg_token_value.to_json()

	    # Group the data by date and calculate the sum of the volume per day in BTC
    volume_btc_per_14_days = data.resample('30D', on='DateTime (UTC)')['TokenValue'].sum()

    # Create the Plotly figure for BTC volume
    fig_volume_btc = go.Figure()
    fig_volume_btc.add_trace(go.Bar(x=volume_btc_per_14_days.index, y=volume_btc_per_14_days.values, name='Volume (BTC)'))
    fig_volume_btc.update_layout(
        title='Volume per month (BTC)',
        xaxis_title='Date',
        yaxis_title='Volume (BTC)'
    )

    # Convert the Plotly figure to JSON for rendering
    plot_volume_btc_json = fig_volume_btc.to_json()
    
    # Render the HTML template with the Plotly figure JSON data
    return render_template('visualization.html', plot_volume_json=plot_volume_json, plot_avg_token_value_json=plot_avg_token_value_json, plot_volume_btc_json = plot_volume_btc_json)

# Run the Flask app

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8001)