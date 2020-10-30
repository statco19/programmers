def solution(name):
    answer = 0
    move = [min(ord(c) - ord('A'), ord('Z') - ord(c) + 1) for c in name]
    where = 0
    
    while True:
        answer += move[where]
        move[where] = 0
        
        if sum(move) == 0:
            break
        
        left, right = (1,1)
        while move[where - left] == 0:
            left += 1
        while move[where + right] == 0:
            right += 1
            
        if left < right: # 왼쪽, 오른쪽 거리가 같을 때 오른쪽으로 가게 해야 풀림;;
            answer += left
            where -= left
        else:
            answer += right
            where += right
    
    return answer
