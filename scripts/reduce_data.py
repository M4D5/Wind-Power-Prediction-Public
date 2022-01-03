import pandas as pd

day_interval_size = 96
days_to_skip = 10

df = pd.read_csv("../Cleaned_data_v1_case3.lfs.csv")

result = pd.DataFrame()

current_day = 0

while current_day * day_interval_size < len(df):
	start_index = current_day * day_interval_size
	result = result.append(df[start_index:start_index + day_interval_size])
	current_day += days_to_skip

result.to_csv('../Cleaned_data_v1_case3.reduced.lfs.csv')
