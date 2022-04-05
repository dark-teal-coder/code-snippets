# 2.6.1.11 LAB: Operators and expressions

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
dur_hr_min = divmod(dura, 60)
total_min = mins + dur_hr_min[1]
total_hr = (hour + dur_hr_min[0] + (total_min // 60))
end_hr = total_hr % 24
end_min = (total_min % 60)

print(f"{end_hr}:{end_min}")
