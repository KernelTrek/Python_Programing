count = 0

while count < 5:
    print(count)
    count += 1

count = 0

while True:
    if count >= 5:
        break
    print(count)
    count += 1

count = 0

while True:
    if count == 2:
        count += 1
        continue
    elif count >= 5:
        break
    print(count)
    count += 1

