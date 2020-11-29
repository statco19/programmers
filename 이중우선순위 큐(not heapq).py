def solution(operations):
    answer=[]
    for op in operations:
        if "I" in op:
            tmplst=op.split(" ")
            tmp=int(tmplst[1])
            answer.append(tmp)
        elif answer and op=="D -1":
            MIN=min(answer)
            answer.remove(MIN)
        elif answer and op=="D 1":
            MAX=max(answer)
            answer.remove(MAX)
    if answer:
        mn=min(answer)
        mx=max(answer)
        return [mx,mn]
    else:
        return [0,0]
