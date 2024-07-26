def pillar_check(complete, x,y):
    if y==0 or complete[(x,y-1)]==0 or complete[(x-1,y)]==1 or complete[(x+1,y)]==1:
        return True