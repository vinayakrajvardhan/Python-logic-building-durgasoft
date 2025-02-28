video_time = input("Enter the time")
print(video_time.split(":"))

value_time = video_time.split(":")
print(float(value_time[0])* 60 + float(value_time[1]))

