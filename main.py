weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
print(weather_c)
# new_items = {key:values * 9.5 + 32 for (key,values) in variable.items()}
#NOTE {key:values.... }  - Semicolon, (key,values) - comma (Imp) 
weather_f = {day:temp * 9.5 + 32 for (day,temp) in weather_c.items()}
print(weather_f)

