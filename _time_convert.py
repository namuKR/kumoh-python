time = int(input("Input seconds? "))

hour = time // 3600
minute = (time-hour*3600) // 60
seconds = (time-hour*3600-minute*60)

print("%d sec = %d hour %d minute %d second" % (time, hour, minute, seconds))