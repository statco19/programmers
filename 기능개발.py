def solution(progresses, speeds):
    answer = []
    days = [0 for _ in range(len(progresses))]
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i] == 0:
            days[i] = (100-progresses[i])//speeds[i]
        else:
            days[i] = (100-progresses[i])//speeds[i] + 1
            
    st=[]
    for j in range(len(days)):
        if st and st[0] < days[j]:
            answer.append(len(st))
            st = []
        st.append(days[j])
        
    if st:
        answer.append(len(st))
        
    return answer
