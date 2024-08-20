



# Contoh result (dalam file txt)

# 2024-08-18T10:21:32.123Z GET /api/user 200 120
# 2024-08-18T10:21:34.456Z POST /api/login 404 400
# 2024-08-18T10:21:35.789Z GET /api/dashboard 200 95
# 2024-08-18T10:21:37.012Z DELETE /api/product 500 700


import logging
import datetime
import random


logging.basicConfig(
    filename="test.log",
    level=logging.INFO,
    format='%(message)s'
)

start_date = datetime.datetime.now()

#proces 
# time.sleep(2)

status_codes = [200,201,204,400,401,402,403,500]
methods = ["POST", "PUT", "DELETE", "GET", "PATCH"]
paths = [
    "/api",
    "/api2",
    "/api3",
    "/api4",
    "/api5",
]

total = 30_000_000


buffer = []
buffer_size = 10000
log_info = logging.info

for i in range(total):
# 2024-08-18T10:21:37.012Z DELETE /api/product 500 700
    rand_status = random.choice(status_codes)
    rand_method = random.choice(methods)
    rand_path = random.choice(paths)

    process_date = datetime.datetime.now()
    ms = random.randrange(100, 2000)
    msg = f"{process_date} {rand_method} {rand_path} {rand_status} {ms}"
    buffer.append(msg)

    if len(buffer) >= buffer_size:
        log_info("\n".join(buffer))
        buffer.clear()

if buffer:
    log_info("\n".join(buffer))

end_date = datetime.datetime.now()
delta = end_date - start_date

print(f"log file generated in {delta.total_seconds()} seconds")

