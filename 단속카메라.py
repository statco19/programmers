def solution(routes):
    answer = 0
    #camera point vs. ramp-in point
    camera = -30001
    # since the lowest point of ramp-out can be -30000.
    
    routes.sort(key=lambda x:x[1])
    # sorting by ramp-out point in an ascending order
    for route in routes:
        if camera < route[0]:
            camera = route[1]
            answer += 1
    return answer
