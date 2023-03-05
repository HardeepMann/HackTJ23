import healthkit as phk
import pandas as pd
import matplotlib.pyplot as plt

# request authorization to access the HealthKit API
phk.get_authorization()

# create a query to retrieve heart rate data for the past 7 days
query = phk.DataQuery('heart_rate', days=7)

# retrieve the data
data = phk.get_data(query)

# convert the data to a pandas dataframe
df = pd.DataFrame(data)

# plot the data using matplotlib
plt.plot(df['start_time'], df['value'])
plt.xlabel('Date/Time')
plt.ylabel('Heart Rate')
plt.show()
