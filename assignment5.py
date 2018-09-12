def half_squared(l):
    result = []
    for element in l :
        results = element*element/2
        result.append(results)
    return result
if half_squared([3,3])==[4.5,4.5]:
    print('True')
else:
    print('false')

