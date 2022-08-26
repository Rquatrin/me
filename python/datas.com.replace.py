from datetime import date

data_nascimento = date(1989,6,12)
hoje = date.today()
hoje = hoje.replace(day = hoje.day-1)

print(data_nascimento)
print(hoje)