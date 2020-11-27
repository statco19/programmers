def solution(priorities, location):
    answer = 0
    st=[]
    lth = len(priorities)
    idx = list(range(lth))
    MAX = max(priorities)
    
    cnt = 0
    while priorities:
        curr = idx.pop(0)
        waiting = priorities.pop(0)
        if waiting == MAX:
            st.append(curr)
            if priorities:
                MAX = max(priorities)
        else:
            priorities.append(waiting)
            idx.append(curr)
        cnt += 1
        
    answer = st.index(location) + 1
    return answer
