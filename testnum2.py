from collections import defaultdict
import datetime


start_date = datetime.datetime.now()
total_line = 0
total_ms = 0
filename = 'test.log'
statuses = defaultdict(int)
with open(filename, 'r') as myfile:
    for line in myfile:
        date, time, method, path, status, ms = line.split(" ")
        total_ms += float(ms)

        statuses[str(status)] += 1
        total_line += 1

distribution = dict()
for item in statuses.items():
    code, count = item
    distribution[code] = str((count / total_line) * 100) + "%"

print(f"success_count : {statuses['200']}")
print(f"time_avg : {(total_ms / total_line)}")
for key, val in distribution.items():
    print(f"{key} : {val}")




end_date = datetime.datetime.now()
delta = end_date - start_date

print(f"count generated in {delta.total_seconds()} seconds")