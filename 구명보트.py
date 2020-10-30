def solution(people, limit):
    cnt = 0
    people.sort()
    light,heavy=0,len(people)-1
    
    while light<heavy:
        if people[light]+people[heavy] <= limit:
            cnt += 1
            light+=1
            heavy-=1
        else:
            heavy-=1
    return len(people)-cnt
