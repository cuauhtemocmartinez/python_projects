import csv

f = open("report.csv")
csv_f = csv.reader(f)
for row in csv_f:
    name, age, company, amount = row
    print(f"Name: {name}, Age: {age}, Company: {company}, Amount: {amount}")
f.close