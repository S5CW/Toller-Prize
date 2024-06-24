from numpy import random
import math

def generate(n):

    '''
    A function to generate a list of n applicants' strict preference lists of 20 selected universities (See "unis", below).

    Also generates a 2-D list containing the 20 universities' strict preference lists of all applicants.

    Applicant preferences are based on real-life rankings of the universities, with a certain random shifting factor.
    Shifting factor is normally distributed with mean = 0, sd = 2 and allows varied preference lists to be generated for applicants.

    '''

    unis  = ["Oxford", "Cambridge", "Imperial", "UCL", "Edinburgh", "King's", "LSE", "Manchester", "Bristol", "St Andrews", "Loughborough", "Durham", "Bath", "Warwick", "Glasgow", "Southampton", "Sheffield", "Leeds", "Nottingham", "Birmingham"]
    times = ["Oxford", "Cambridge", "Imperial", "UCL", "Edinburgh", "King's", "LSE", "Manchester", "Bristol", "Glasgow", "Southampton", "Birmingham", "Sheffield", "Warwick", "Leeds", "Nottingham", "Durham", "St Andrews", "Bath", "Loughborough"]
    qs = ["Imperial", "Oxford", "Cambridge", "UCL", "Edinburgh", "Manchester", "King's", "LSE", "Bristol", "Warwick", "Glasgow", "Birmingham", "Southampton", "Leeds", "Durham", "St Andrews", "Sheffield", "Nottingham", "Bath", "Loughborough"]
    profs = ["Oxford", "Cambridge", "Imperial", "UCL", "St Andrews", "Bath", "King's", "LSE", "Loughborough", "Manchester", "Durham", "Bristol", "Glasgow", "Warwick", "Birmingham", "Southampton", "Edinburgh", "Leeds", "Nottingham", "Sheffield"]

    meanrank = []
    for i in unis:
        meanrank.append((times.index(i)+qs.index(i)+profs.index(i))/3)

    # print(unisind)
    # print(len(unisind), len(unis))



    applicants, universities = [], []

    for _ in range(n):

        a_numPref = []
        # print(len(unis))
        for i in range(len(meanrank)):
            a_numPref.append(meanrank[i]+random.normal(loc = 0, scale = 2))


        a_preferences, copy = [], a_numPref.copy()
        for i in range(len(unis)):
            # print(min(unisind2), unisind2)
            a_preferences.append(a_numPref.index(min(copy)))
            copy.remove(min(copy))
        applicants.append(a_preferences)

    # print(applicants)

    u_numPref = [[0 for i in applicants] for uni in unis]
    for u_index, uni in enumerate(unis):
        for index, i in enumerate(applicants):
            u_numPref[u_index][index] = index+random.normal(loc = 0, scale = n/10)

    #print(u_numPref)


    for u_index, uni in enumerate(u_numPref):

        u_preferences = []
        copy = uni.copy()

        for i in range(len(uni)):
            #if u_index == 0: print(min(copy))
            u_preferences.append(uni.index(min(copy)))
            copy.remove(min(copy))
        universities.append(u_preferences)

    print(1)
    return universities, applicants

    # print(universities)
    #print(applicants)

#print(generate(5)[1])
