from random import sample

head = int(input("\nWhat sector will the head start at?\n> "))
print("Head starting at Sector " + str(head))

orders = sample(range(1, 11), 10)
originalOrders = list(orders)
print("\nOriginal Orders:\n" + str(originalOrders))

buffer = orders[:3]
del orders[:3]
print("\nPost-Buffer Orders:\n" + str(orders))
print("\nBuffer Sectors:\n" + str(buffer))

totalMoved = 0
headMovement = 0
wentAround = False

def headMovement():
    global totalMoved, buffer, orders, head, wentAround, originalOrders
    print("\nCurrent Buffer Sectors: " + str(buffer))

    def findNewHead(currentBuffer, currentHead):
        global wentAround

        upBuffer = []
        for sector in currentBuffer:
            if sector >= currentHead:
                upBuffer.append(sector)
        if not upBuffer:
            print("\nNothing found...\n")
            print("Going around...\n")
            wentAround = True
            currentHead = min(currentBuffer)
            return findNewHead(currentBuffer, currentHead)
        else:
            return min(upBuffer)

    newHead = findNewHead(buffer, head)
    print("Current Head: " + str(head))
    print("Closest Sector: " + str(newHead))
    if wentAround == True:
        headMovement = (abs((newHead + len(originalOrders)) - head))
        totalMoved += headMovement
    else:
        headMovement = (abs(newHead - head))
        totalMoved += headMovement
    
    wentAround = False
    print("+" + str(headMovement) + " Head Movement")
    head = newHead
    del buffer[buffer.index(newHead)]
    if orders:
        buffer.append(orders[0])
        del orders[0]

for sector in range(len(orders)):
    headMovement()

if not orders:
    for sector in range(len(buffer)):
        headMovement()

print("\nTotal Head Movement: " + str(totalMoved))
