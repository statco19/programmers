def solution(number, k):
    collected=[]

    for i,num in enumerate(number):
        while collected and collected[-1]<number[i] and k>0:
            collected.pop()
            k-=1
        collected.append(number[i])
    if k>0:
        collected=collected[:-k]
    return ''.join(collected)
    
if __name__ == "__main__":
    number="999"
    k=2
    print(solution(number,k))
