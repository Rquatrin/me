from datetime import datetime,date

dt_assinatura = date(2022,5,31)

dt_renovacao = dt_assinatura + timedelta(days=30)

print(f'Data de assinatura: {dt_assinatura}')

print(f'Data de renovação: {dt_renovacao}')

