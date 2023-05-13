def numbers(*n, situation=False):
    """
    => Function to analyze grades and situation of several students.
    n: one or more student grades (more than 1 accepted).
    situation: optional value, indicating whether or not to add a situation.
    return: dictionary with various information about the situation of the class.
    """
    listtemp = []
    for n in n:
        listtemp.append(n)

    maindict = {
        'total' : len(listtemp),
        'bigger' : max(listtemp),
        'lesser' : min(listtemp),
        'grade' : sum(listtemp)/len(listtemp)
        }
    
    if situation == True and maindict['grade'] < 6:
        maindict['situation'] = 'SO BAD :('
    elif situation == True and maindict['grade'] >= 6 and maindict['grade'] <= 8:
        maindict['situation'] = 'REASONABLE ;)'
    else:
        maindict['situation'] = 'GREAT!'
    if situation == False:
        del maindict['situation']

    return maindict


print(numbers(0,5.9,6.5,0, situation=True))
