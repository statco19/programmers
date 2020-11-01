def solution(m, n, puddles):
    way = [[0] * (m + 1) for _ in range(n + 1)]
    way[0][1] = 1

    for i in range(1,n+1):
        for j in range(1,m+1):
            if [j,i] in puddles: # puddles 좌표 반전되어야 함.
                way[i][j] == 0
                continue
            way[i][j] = way[i-1][j] + way[i][j-1]
    
    nominator = way[n][m]
    return nominator % 1000000007
