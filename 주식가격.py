def solution(prices):
    answer = [0 for _ in range(len(prices))]
    st = [0]
    for i in range(1,len(prices)): # 스택에 쌓은 건 아직 언제 떨어질지 모르는 시간들
        while st and prices[st[-1]] > prices[i]:
            prev = st[-1]
            answer[prev] = i-prev
            st.pop()
        st.append(i)
    
    for sec in st:
        answer[sec] = i - sec
    return answer
