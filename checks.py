def max_index(list1, list2):
    m = 0
    for i in list1:
        if list2.index(i)>m: m = list2.index(i)
    
    return m

def stability(assignment, uP, aP):
    for uni, u_pref in enumerate(assignment):
        for a in u_pref:
            for a_index, pref in enumerate(aP[a]):
               if a_index < aP[a].index(uni) and uP[pref].index(a)<max_index(assignment[pref], uP[pref]):
                return False
    return True



#print(max_index([0,1,2], [2,1,0]))
#print(stability([[0], [1]], [[0, 1], [1, 0]], [[0, 1], [1, 0]]))
#print(stability([[0], [1], [2]], [[1, 2, 0], [2, 0, 1], [0, 1, 2]], [[0, 1, 2], [1, 2, 0], [2, 0, 1]]))
#print(stability([[1], [2], [0]], [[1, 2, 0], [2, 0, 1], [0, 1, 2]], [[0, 1, 2], [1, 2, 0], [2, 0, 1]]))
#print(stability([[2], [3], [0], [1]], [[3, 2, 0, 1], [1, 3, 0, 2], [3, 0, 1, 2], [2, 1, 0, 3]], [[0, 1, 2, 3], [0, 3, 2, 1], [1, 0, 2, 3], [3, 1, 2, 0]]))