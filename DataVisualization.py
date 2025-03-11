import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create the Dow Jones dataset
data = {
    "Date": ["1914-12-01", "1915-01-01", "1915-02-01", "1915-03-01", "1915-04-01"],
    "Price": [55.00, 56.55, 56.00, 58.30, 66.45]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Display the first few rows
print(df.head())

# Plot Dow Jones price over time
plt.figure(figsize=(8, 4))
plt.plot(df["Date"], df["Price"], marker="o", linestyle="-", color="blue")
plt.xlabel("Date")
plt.ylabel("Dow Jones Price")
plt.title("Dow Jones Industrial Average Over Time")
plt.xticks(rotation=45)
plt.show()

# Bar chart: Dow Jones prices
plt.figure(figsize=(8, 4))
plt.bar(df["Date"], df["Price"], color="green")
plt.xlabel("Date")
plt.ylabel("Dow Jones Price")
plt.title("Dow Jones Price by Month")
plt.xticks(rotation=45)
plt.show()
