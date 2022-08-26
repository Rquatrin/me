from datetime import date,timedelta

dt_1 = date(2022, 5, 31)
dt_2 = date(2022, 12,31)

data_180 = dt_1 + timedelta(days=180)
print(data_180)