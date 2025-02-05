def countServers(grid):
    row = len(grid)
    col = len(grid[0])
    count = 0
    
    for i in range(row):
        
        for j in range(col):
            print("i" , i , "j " ,j)
            if (grid[i][j] == 1):
                res = False
                if grid[i].count(1) > 1:
                    count += 1                
                elif not res :
                    for k in range(0,i):
                        print("K:" ,k)
                        if grid[k][j] == 1 :
                            res = True
                            break
                    if not res:
                        for k in range(i,row):
                            print("K:" ,k)
                            if grid[k][j] == 1 :
                                res = True
                                break
                    if res :
                        count += 1
    return count
grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
print(countServers(grid))


                

               

