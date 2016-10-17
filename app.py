import time

i = 0

while True:
    with open('asd', 'wb') as f:
        f.write(i)
    time.sleep(120)
