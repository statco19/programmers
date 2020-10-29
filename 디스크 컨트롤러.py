def solution(jobs):
    answer = 0
    time = 0 # 현재 작업이 끝나는 시간
    jobs.sort(key = lambda x : x[1]) # 작업 소요시간 기준으로 배열
    length = len(jobs) # jobs의 길이 바뀔 예정이므로 초기 jobs의 길이를 length에 저장
    
    while jobs: # 모든 작업이 완료되어 없어질 때까지 while 문 실행
        for i in range(len(jobs)):
            if time >= jobs[i][0]:
                time += jobs[i][1] # 현재 time + (작업이 완료되어 끝나는 시간)
                answer += time - jobs[i][0] # (현재 작업이 끝나는 시간) - (작업을 요청하기까지 걸린 시간)
                
                jobs.pop(i) # 완료된 작업 jobs에서 제외
                break # IndexError를 방지
            
            if i == len(jobs) - 1:
                # 작업 소요시간 기준으로 jobs를 배열했기 때문에 소요시간이 길어도 먼저 요청된 작업은 처리해야함.
                # 그렇기 때문에 끝까지 for 문을 돌리고, 끝까지 갔을 때도 time보다 시간 상 앞서는 작업이 없다면 time++
                time += 1
    return answer // length
