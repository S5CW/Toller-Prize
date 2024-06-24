def match(uP, aP, q):
    #print("1b")

    '''
    Matching algorithm, where uP is a 2-D list containing the preferences (of applicants) of each university, 
    where each applicant is labelled as their index in the "applicants" list (data.py).

    Similarly, aP is a 2-D list containing the preferences (of univeristies) of each applicant,
    where each university is labelled as their index in the  "unis" list (data.py).

    q is a 1-D list of the quotas (number of available places) for each univeristy
    , with each data point corresponding to the univeristy with the same index in "unis".
    
    '''
    locked, waitlist, aInd = [], [[] for i in uP], [0 for i in aP]

    while len(locked) != len(uP):
        
        applied = [[] for i in uP]
        

        for index, i in enumerate(aP):

            if index not in locked: 
                applied[i[aInd[index]]].append(index)
                aInd[index] += 1

        print(f"\033[1;37;40m{applied}")
        
        for index, i in enumerate(uP):
            for a in applied[index]:
                if len(waitlist[index]) < q[index]: 
                    waitlist[index].append(a)
                    locked.append(a)

                else:
                    lowest = a
                    for w in waitlist[index]:
                        if i.index(lowest) < i.index(w): lowest = w
                    if lowest != a: 
                        waitlist[index].remove(lowest)
                        locked.remove(lowest)
                        waitlist[index].append(a)
                        locked.append(a)
        
        print(f"\033[1;32;402m{waitlist}")

       
    #print(2)
    return waitlist

#print(match([[1, 2, 0], [2, 0, 1], [0, 1, 2]], [[0, 1, 2], [1, 2, 0], [2, 0, 1]], [1, 1, 1]))
print(match([[3, 2, 0, 1], [1, 3, 0, 2], [3, 0, 1, 2], [2, 1, 0, 3]], [[0, 1, 2, 3], [0, 3, 2, 1], [1, 0, 2, 3], [3, 1, 2, 0]], [1, 1, 1, 1]))
#print(match([[0,1], [1, 0]], [[0, 1], [1, 0]], [1, 1]))
