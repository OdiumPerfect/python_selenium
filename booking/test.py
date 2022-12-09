import datetime

print(datetime.date.today())
first_date = datetime.date.today() + datetime.timedelta(days=10)
print(first_date)
second_date = first_date + datetime.timedelta(days=15)
print(second_date)