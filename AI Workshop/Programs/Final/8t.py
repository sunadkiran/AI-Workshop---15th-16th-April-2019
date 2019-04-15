tiles = [[7,4,1],[8,5,2],["_",6,3]]#goal state
given = [[7,4,1],[5,6,"_"],[8,3,2]]#given/initial state
tblr=[9,9,9,9]#contains top,bottom,left,right tiles
maxx=-2#to select tile that reduces manhatten dis by max
xx="x"#to check swaps after each while loop execution/debugging
p_tile="_"#the prev tile shouldnt be swapped again
while given!=tiles and xx=="x":
    for i in range(2,-1,-1):
        for j in range(3):
            print(given[j][i],end=" ")#printing the current state
        print()
    for i in range(3):
        for j in range(3):
            if given[i][j]=="_": #finding empty spot
                ex=i
                ey=j
                tblr=[9,9,9,9]
                if ey+1<3: #finding top,bottom,left and right tiles
                    tblr[0]=given[ex][ey+1]
                if ey-1>-1:
                    tblr[1]=given[ex][ey-1]
                if ex-1>-1:
                    tblr[2]=given[ex-1][ey]
                if ex+1<3:
                    tblr[3]=given[ex+1][ey]
                ex=i+1
                ey=j+1
                #####print(ex,ey)
    #####print(tblr)
    maxx=-2
    count=0#counts possible tile swaps(mid=4,corner=2,rest=3)
    flag=0
    for aa in tblr:
        if aa!=9:#9 is for out of boundary coordinates
            count+=1
    for a in tblr:
        if a!=9:
            print()
            print("neighbouring tile: " + str(a))
            for b in range(3):
                for c in range(3):
                    #finding coordinates,calculating manhatten dis before and after swap
                    if a == given[b][c]:
                        x1=b+1
                        y1=c+1
                    if a ==tiles[b][c]:
                        x2=b+1
                        y2=c+1
            #####print(x1,y1,x2,y2)
            b_swap=abs(x1-x2)+abs(y1-y2)
            print("Manhatten Distance of "+str(a)+" before swap is "+str(abs(x1-x2)+abs(y1-y2)))
            a_swap=abs(ex-x2)+abs(ey-y2)
            print("Manhatten Distance of "+str(a)+" after swap is "+str(abs(ex-x2)+abs(ey-y2)))
            diff=b_swap-a_swap
            print("Difference: "+str(diff))
            #####print("Maxx: "+str(maxx))
            if diff>=maxx and a!=p_tile:#prev_tile should not be moved again
                if count!=2 and b_swap!=0 and a_swap==0:#higher priority is given to that tile that would go to correct pos
                    maxx=diff
                    tile=a
                    tx=x1
                    ty=y1
                    flag=1
                    #print(maxx,tile,tx,ty)
                if count!=2 and b_swap!=0 and flag!=1:#prev_tile, correct_pos tile not moved
                    maxx=diff
                    tile=a
                    tx=x1
                    ty=y1
                    #print(maxx,tile,tx,ty)
                if count==2:#only two possible ways, choosing the one that wasnt moved in the previous step even if it might be in the correct position
                    maxx=diff
                    tile=a
                    tx=x1
                    ty=y1
                    #print(maxx,tile,tx,ty)
                
    #swapping 
    given[ex-1][ey-1]=tile
    given[tx-1][ty-1]="_"
    p_tile=tile
    print()
    print("After swapping:")
    for i in range(2,-1,-1):#printing the puzzle
        for j in range(3):
            print(given[j][i],end=" ")
        print()
    xx=input("Enter x")#stops(for debugging)
    print()
