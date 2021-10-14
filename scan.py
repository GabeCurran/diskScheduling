from random import sample

head = int(input("\nWhat sector will the head start at?\n> "))
print("Head starting at Sector " + str(head))

orders = sample(range(1, 11), 10)
print("\nOriginal Orders:\n" + str(orders))

buffer = orders[:3]
del orders[:3]
print("\nPost-Buffer Orders:\n" + str(orders))
print("\nBuffer Sectors:\n" + str(buffer))

totalMoved = 0
scanningUp = True

def headMovement():
    global totalMoved, buffer, orders, head
    print("\nCurrent Buffer Sectors: " + str(buffer))

    def findNewHead(currentBuffer, currentHead):
        global scanningUp

        if scanningUp == True:
            print("Going Up!")
            upBuffer = []
            for sector in currentBuffer:
                if sector >= currentHead:
                    upBuffer.append(sector)
            if not upBuffer:
                print("\nNothing found...\n")
                scanningUp = False
                return findNewHead(currentBuffer, currentHead)
            else:
                return min(upBuffer)

        elif scanningUp == False:
            print("Going Down!")
            downBuffer = []
            for sector in currentBuffer:
                if sector <= currentHead:
                    downBuffer.append(sector)
            if not downBuffer:
                print("\nNothing found...\n")
                scanningUp = True
                return findNewHead(currentBuffer, currentHead)
            else:
                return max(downBuffer)

    newHead = findNewHead(buffer, head)
    print("Current Head: " + str(head))
    print("Closest Sector: " + str(newHead))
    print("+" + str(abs(newHead - head)) + " Head Movement")
    totalMoved += (abs(newHead - head))
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
