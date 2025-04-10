employees = {
  'Alice': 2200.0,
  'Bob': 1950.0,
  'Charlie': 2500.0,
  'Dave': 1850.0,
  'Eve': 2050.0
}

for employee, salary in employees.items():
    if salary > 2000:
        print(employee)
