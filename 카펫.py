def solution(brown, yellow):
    for i in range(1,int(yellow**0.5)+1):
        if yellow%i==0:
            yh=yellow//i
            
            if (brown+yellow)%(yh+2)==0:
                bh=(brown+yellow)//(yh+2)
                return [yh+2,bh]
