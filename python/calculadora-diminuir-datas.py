from datetime import date

dt_1 = date(2022, 5, 31)
dt_2 = date(2022, 12, 31)

dt_3 = dt_2 -dt_1
dt_4 = (dt_3/30).days
print(f'Faltam {dt_3.days} dias ou {dt_4} meses para a data: {dt_2}')