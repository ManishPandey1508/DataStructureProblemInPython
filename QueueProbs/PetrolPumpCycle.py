# not Done yet

from Qimpl import Queue


class PetrolPump:

    def __init__(self, petrol, distance):
        self.petrol = petrol
        self.distance = distance

    def getPetrol(self):
        return self.petrol

    def getDistance(self):
        return self.distance


def calculateStartingPoint(ls):
    q = Queue(len(ls))
    tempq = Queue(len(ls))
    # putting all petrol pumps object in Queue
    for i in range(len(ls)):
        q.enqueueFromEnd(ls[i])
    count = 0
    while(not q.isEmpty() and count < 3):
        temp = q.dequeueFromFront()
        petrol = temp.petrol
        distance = temp.distance
        temp2 = q.rear()
        petrol += temp2.petrol
        distance += temp2.distance
        tempq.enqueueFromEnd(temp)
        if(distance > petrol):
            while(not tempq.isEmpty()):
                temp3 = tempq.dequeueFromFront()
                q.enqueueFromEnd(temp3)
            distance = 0
            petrol = 0
        else:
            x = tempq.dequeueFromFront()
            q.enqueueFromEnd(x)

        count += 1
    print q.front().getPetrol()
    print q.front().getDistance()
ls = [PetrolPump(6, 4), PetrolPump(3, 6), PetrolPump(7, 3)]
calculateStartingPoint(ls)
