import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file into a pandas DataFrame
file_name = r"C:\Users\Owner\Downloads\Microbitsound.csv"
data = pd.read_csv(file_name)

# Display the first few rows to ensure the data is loaded correctly
print("Data Loaded:")
print(data.head())

# Basic statistics
mean_sound = round(data["Sound"].mean(), 2) #specifying column name 
min_sound = data["Sound"].min()
max_sound = data["Sound"].max()
median_sound = data["Sound"].median()

print(f"\nStatistics:")
print(f"Mean: {mean_sound}")
print(f"Min: {min_sound}")
print(f"Max: {max_sound}")
print(f"Median: {median_sound}")

# Plotting the data
plt.plot(data["Sound"])
plt.axhline(mean_sound, color="red", linestyle="--", label=f"Mean: {mean_sound}") #adds mean line
plt.title("Microbit Sound Data")
plt.xlabel("Sample Number")
plt.ylabel("Sound Level")
plt.legend()
plt.grid(True)
plt.show()


