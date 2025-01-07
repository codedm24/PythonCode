#Analyze dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns', None)

#change current directory 
print(f"Current Directory: {os.getcwd()}")
os.chdir('Exercises') 
print(f"Current Directory: {os.getcwd()}")
#sys.exit()

#Read csv file into a datset
#df = pd.read_csv('F:\\Projects\\Python\\PythonCode\\Exercises\\Divvy_Trips_2019_Q1.csv')
df = pd.read_csv('Divvy_Trips_2019_Q1.csv')

#Display the first five rows
print(df.head().to_markdown(index=False,numalign="left",stralign="left"))

#Print the column names and their data types
print(df.info())

#Print the dataset description
print(df.describe)

#convert 'start_time' and 'end_time' columns to datetime
df['start_time'] = pd.to_datetime(df['start_time'])
df['end_time'] = pd.to_datetime(df['end_time'])

print(df.info())

#Remove ',' from tripduration column and convert it to numeric
df['tripduration'] = df['tripduration'].astype(str).str.replace(',','',regex=False)
df['tripduration'] = pd.to_numeric(df['tripduration'])

print(df.info())

#Print descriptive statistics of 'tripduration'
print(df['tripduration'].describe().to_markdown(numalign='left',stralign='left'))

#Extract hour from 'start_time' and store it in a new column 'start_hour'
df['start_hour'] = df['start_time'].dt.hour

#Calculate count of trips for each 'start_hour' and print top 10 hoours
print('\nTop 10 start hours:\n')
print(df['start_hour'].value_counts().head(10).to_markdown(numalign='left', stralign='left'))

#Calculate count of trips for each 'from_station_name' and print top 10 stations
print('\nTop 10 from station name')
print(df['from_station_name'].value_counts().head(10).to_markdown(numalign='left', stralign='left'))

#Calculate count of trips for each combination of 'usertype' and 'gender' and print the results
print('\nTrips by usertype and gender')
print(df.groupby(['usertype','gender']).size().to_markdown(numalign='left', stralign='left'))

#Extract day of week and month from 'start_time' and store in new columns
df['day_of_week'] = df['start_time'].dt.day_name()
df['month'] = df['start_time'].dt.month_name().str.slice(0,3)

#Calculate count of trips for each 'day_of_week' and print the results
print('\nTrips by day of week:\n')
print(df['day_of_week'].value_counts().to_markdown(numalign='left', stralign='left'))

#Calculate count of trips for each 'month' and print the results
print('\nTrips by month:')
print(df['month'].value_counts().to_markdown(numalign='left',stralign='left'))

#Visualize months wise rides count using Matplotlib
# month_counts = df['month'].value_counts().sort_index()
# plt.figure(figsize=(10,6))
# month_counts.plot(kind='bar')
# plt.title('Count of rides by month')
# plt.xlabel('Month')
# plt.ylabel('Count of rides')
# plt.xticks(rotation=45)
# plt.show()

#Visualize month wise rides using Seaborn
# month_counts = df['month'].value_counts().reset_index()
# month_counts.columns = ['Month', 'Count']
# plt.figure(figsize=(10,6))
# sns.barplot(x='Month', y='Count', data=month_counts, order = month_counts['Month'])
# plt.title('Count of Rides by month')
# plt.xlabel('Month')
# plt.ylabel('Count of Rides')
# plt.xticks(rotation=45)
# plt.show()

#Visualize day of week wise rides count using Matplotlib
# categories = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
# df['day_of_week'] = pd.Categorical(df['day_of_week'], categories = categories, ordered = True)
# dayofweek_counts = df['day_of_week'].value_counts().sort_index() 
# plt.figure(figsize=(10,6))
# dayofweek_counts.plot(kind='bar')
# plt.title('Count of rides by day')
# plt.xlabel('Day of Week')
# plt.ylabel('Count of rides')
# plt.xticks(rotation=45)
# plt.show()

#Visualize 'start station' wise rides count using Matplotlib for top 5 stations
startstation_count = df['from_station_name'].value_counts().head(5)
plt.figure(figsize=(10,6))
startstation_count.plot(kind='bar')
plt.title('Count of rides by Start station')
plt.xlabel('Start Station')
plt.ylabel('Count of rides')
plt.xticks(rotation=25, ha='right')
plt.tight_layout()
plt.show()

