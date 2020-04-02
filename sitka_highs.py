import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = "data/sitka_weather_2018_full.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        print(index,column_header)

    #Get high temps for the day and record dates
    highs, dates = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        highs.append(high)
        dates.append(current_date)

#Plot the high temperatures
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

#Format the plot
plt.title("Daily High Temperatures in Sitka, AL. 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()