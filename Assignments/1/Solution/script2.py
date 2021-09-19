# Enter the value in seconds and display it in hours, minutes and seconds.

s = int(input("Enter the value in seconds: "))

hours = s // 3600
minutes = (s % 3600) // 60
seconds = s % 60

print()
print(s, 'seconds is segregated as', hours, 'hours,', minutes, 'minutes and', seconds, 'seconds.')
