def total_euro(work_hours, pay_per_hour):
    return work_hours*pay_per_hour

work_hours = float(input('Input work hours: '))
pay_per_hour = float(input('Input pay per hour: '))
print(f'Total: {total_euro(work_hours, pay_per_hour)} €')