hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

ends_min = (hour*60 + mins + dura)%60
ends_hours = (((hour*60 + mins + dura) - ends_min)/60)%24
print(ends_hours,":",ends_min)