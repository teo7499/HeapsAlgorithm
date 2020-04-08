#Heap's algorithm
def start() :
    preTransform = input("Enter Variables (Comma Separated) : ")
    if(preTransform == ""):
        print ("Invalid Input")
        start()
    postTransform = preTransform.split(",")
    heapAlgo(postTransform, len(postTransform))


def heapAlgo(postTransform: list, lstLen: int):
    if lstLen == 1:
        print(postTransform)
    else:
        #heapAlgo(postTransform, lstLen - 1)
        for i in range(lstLen):
            heapAlgo(postTransform, lstLen - 1)
            if (i < lstLen - 1):
                #swap positions of elements in collections based on whether lstLen is even/odd
                if (lstLen % 2 == 0):
                    postTransform[i], postTransform[lstLen-1] = postTransform[lstLen-1], postTransform[i]
                else:
                    postTransform[0], postTransform [lstLen-1] = postTransform[lstLen-1], postTransform[0]

start()
