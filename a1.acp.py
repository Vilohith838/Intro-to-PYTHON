import numpy as np

np.random.seed(42)
data = np.random.normal(25, 5, (3, 12, 30))

print(f"Dataset Shape: {data.shape}")

city_means = np.mean(data, axis=(1, 2))
print(f"Average Annual Temp per City: {city_means}")

heatwaves = data[data > 35]
print(f"Number of heatwave days recorded: {heatwaves.size}")

city_zero_trend = data[0].flatten()

monthly_avg_city_1 = np.mean(data[1], axis=1)
hottest_month = np.argmax(monthly_avg_city_1)
print(f"City 1's hottest month (index): {hottest_month}")

data_fahrenheit = (data * 9/5) + 32