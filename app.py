import time

i = 0

while True:
    with open('asd', 'w+') as f:
        f.write(i)
    time.sleep(120)
