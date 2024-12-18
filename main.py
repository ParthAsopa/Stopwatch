import time

print("Type Start to start and stop to stop.")

while True:
    cmd = input(">")
    if cmd.lower() == "start":
        ti = time.time()
    elif cmd.lower() == "stop":
        tf = time.time()
        break

time_sec = round((tf - ti), 3)
milsec = int((time_sec * 1000) % 1000)
sec = int((time_sec * 1000) // 1000)
minutes = int((time_sec // 60) % 60)
hours = int(time_sec // 3600)

print(f"{hours}:{minutes}:{sec}:{milsec}")
