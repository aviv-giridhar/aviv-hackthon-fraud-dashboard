import streamlit as st
#import requests
import pandas as pd
import altair as alt

# URL of your Flask app's API endpoint
#api_url = 'http://localhost:5000/api/messages'


def get_message_counts():
    # Replace this with your own code to retrieve the message counts
    # For demonstration purposes, we'll return some sample data
    message_counts = {
        'Fraud': 10,
        'False Positive': 5,
        'Total Messages': 12
    }
    return message_counts

# Get the message counts
message_counts = get_message_counts()

# Convert the dictionary to a DataFrame
df = pd.DataFrame.from_dict(message_counts, orient='index', columns=['Classified Message Count'])
df = df.reset_index().rename(columns={'index': 'SeekerGPT Analysis'})

# Create the Streamlit app
st.title('Fraudbuster ChatGPT Dashboard')

# Set font style
st.markdown('<style>body{font-family: Arial, sans-serif;}</style>', unsafe_allow_html=True)

# Display the message counts in a table
#st.header('Message Counts')
st.dataframe(df.style.set_properties(**{'font-size': '16px'}))

# Create a bar chart to visualize the message counts
st.header('Message Count Bar Chart')

# Add a bar chart to visualize the message counts
#st.bar_chart(df)

# Highlight fraud in red color
fraud_color = alt.condition(alt.datum.User == 'Fraud', alt.value('red'), alt.value('steelblue'))

# Create the bar chart using Altair
chart = alt.Chart(df).mark_bar().encode(
    x='SeekerGPT Analysis',
    y='Classified Message Count',
    color=fraud_color
).properties(
    width=400,
    height=300
)

st.altair_chart(chart)
