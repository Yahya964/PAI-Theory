import numpy as np

print("Yahya Shamim")
print("24k-0020")

data = []
with open("sensor_data.csv", "r") as file:
    #spilliting commas
    for datalines in file:
        row = datalines.strip().split(",")
        data.append(row)
#making 2d array
arr = np.array(data, dtype=float)
#data cleaning
arr[arr == -999] = np.nan
arr[(arr < 0) | (arr > 100)] = np.nan
#data analysis
sensor_mean = np.nanmean(arr, axis=0)
moisture_median = np.nanmedian(arr, axis=1)
count = np.isnan(arr).sum(axis=0)
worst_sensor = np.argmax(count)
#normalization
min_reading = np.nanmin(arr)
max_reading = np.nanmax(arr)
min_max_norm = (arr - min_reading) / (max_reading - min_reading)
#save output
np.savetxt("sensor_data_normalized.csv", min_max_norm, delimiter=",")
print("worst sensor index:", worst_sensor)