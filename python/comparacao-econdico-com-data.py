from datetime import datetime

dt_1 = datetime(2022,5,31,20,45)
dt_2 = datetime(2024,12,31,20,45)

if dt_2 > dt_1:
    print(f'A data {dt_2} é maior que a {dt_1}')

else:
    print(f'A data {dt_2} não é maior que {dt_1}')