# Enter the value in seconds and display it 
# in hours, minutes and seconds.

s = int(input('Enter the number of seconds: ')) 

hour = s // 3600
# seconds_life_after_removing_hour is also
# the minutes left after removing hour, but 
# the value is in seconds
seconds_left_after_removing_hour = s % 3600
minute = seconds_left_after_removing_hour // 60
seconds_left_after_removing_minute = seconds_left_after_removing_hour % 60
second = seconds_left_after_removing_minute

print(s, 'seconds is', hour, "hours", minute, "minutes", second, "seconds")