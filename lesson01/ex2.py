import time

timeSec = int(input("Введите время в секундах: "))

# (tm_year,tm_mon,tm_mday,tm_hour,tm_min, tm_sec,tm_wday,tm_yday,tm_isdst)
t = time.localtime(timeSec)

print(f"{t.tm_hour:02d}:{t.tm_min:02d}:{t.tm_sec:02d}")
