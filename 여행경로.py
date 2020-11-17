def solution(tickets):
    t=dict()
    for ticket in tickets:
        if ticket[0] not in t:
            t[ticket[0]]=[ticket[1]]
        else:
            t[ticket[0]].append(ticket[1])
    
    for departure in t.keys():
        t[departure].sort(reverse=True)
    
    stack=["ICN"]
    answer=[]
    while stack:
        top = stack[-1]
        
        if top not in t or len(t[top])==0:
            tmp=stack.pop()
            answer.append(tmp)
        else:
            temp=t[top].pop()
            stack.append(temp)
            
    answer.reverse()
    return answer
