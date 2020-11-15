def solution(n, costs):
    ans = 0
    costs.sort(key=lambda x:x[2])
    routes = set([costs[0][0]])
    
    while len(routes) != n:
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0],cost[1]])
                ans += cost[2]
                #cost[i] = [-1,-1,-1]
                break
                #without break, errors occur for the case below.
                #n=5
                #costs = [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]]
    return ans
