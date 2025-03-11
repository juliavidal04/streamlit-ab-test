import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Function to fetch data from Google Sheets
def fetch_google_sheets_data():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("hola").sheet1 
    data = sheet.get_all_records()
    return pd.DataFrame(data)

# Load data from Google Sheets
df = fetch_google_sheets_data()

# Convert 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

st.title("Dow Jones Data Visualization")

# Show the question
st.write("Which trend do you observe in the Dow Jones Industrial Average?")

# Session state for tracking clicks
if "start_time" not in st.session_state:
    st.session_state.start_time = None
    st.session_state.chart_selected = None
    st.session_state.show_second_button = False
    st.session_state.time_taken = None

# Function to plot line chart
def plot_line_chart():
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(df["Date"], df["Price"], marker="o", linestyle="-", color="blue")
    ax.set_xlabel("Date")
    ax.set_ylabel("Dow Jones Price")
    ax.set_title("Dow Jones Industrial Average Over Time")
    plt.xticks(rotation=45)
    return fig

# Function to plot bar chart
def plot_bar_chart():
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(df["Date"], df["Price"], color="green")
    ax.set_xlabel("Date")
    ax.set_ylabel("Dow Jones Price")
    ax.set_title("Dow Jones Price by Month")
    plt.xticks(rotation=45)
    return fig

# Button to show one of the charts at random
if st.button("Show a chart"):  
    st.session_state.chart_selected = random.choice(["line", "bar"])
    st.session_state.start_time = time.time()  # Start timing
    st.session_state.show_second_button = True

# Display the selected chart
if st.session_state.chart_selected:
    if st.session_state.chart_selected == "line":
        st.pyplot(plot_line_chart())
    else:
        st.pyplot(plot_bar_chart())

# Show the second button after clicking the first
if st.session_state.show_second_button:
    if st.button("I answered your question"):
        st.session_state.time_taken = round(time.time() - st.session_state.start_time, 2)
        st.write(f"You took {st.session_state.time_taken} seconds to answer!")