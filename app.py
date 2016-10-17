import time

i = 0

while True:
    with open('asd', 'w+') as f:
        f.write(str(i))
    i += 1
    time.sleep(60)    
