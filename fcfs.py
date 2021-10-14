from random import sample

head = int(input("\nWhat sector will the head start at?\n> "))
print("Head starting at Sector " + str(head))

orders = sample(range(1, 11), 10)
print("\nOriginal Orders:\n" + str(orders))

buffer = orders[:3]
del orders[:3]
print("\nPost-Buffer Orders:\n" + str(orders))
print("\nBuffer:\n" + str(buffer))

totalMoved = 0

def headMovement():
    global totalMoved, buffer, orders, head
    newHead = buffer[0]
    totalMoved += (abs(buffer[0] - head))
    head = newHead
    if orders:
        buffer.append(orders[0])
        del orders[0]
    del buffer[0]

for sector in range(len(orders)):
    headMovement()

if not orders:
    for sector in range(len(buffer)):
        headMovement()

print("\nTotal Head Movement: " + str(totalMoved))
