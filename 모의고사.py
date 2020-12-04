def solution(answers):
    answer = []
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    foo=[p1,p2,p3]
    l1,l2,l3 = list(map(len,foo))
    scores = [0,0,0]
    
    for idx,ans in enumerate(answers):
        if ans==p1[idx%l1]:
            scores[0]+=1
        if ans==p2[idx%l2]:
            scores[1]+=1
        if ans==p3[idx%l3]:
            scores[2]+=1
    
    mx=max(scores)
    for idx,score in enumerate(scores):
        if score == mx:
            answer.append(idx+1)
    return answer
