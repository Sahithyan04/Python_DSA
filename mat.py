
import copy
def gameOfLife(board):
   """
   Do not return anything, modify board in-place instead.
   """

   nboard = copy.deepcopy(board)
   print(nboard[0][1])
   n = len(board)
   m = len(board[0])
   for i in range(0,n):
       for j in range(m):
           n_count = 0
           if i == 0 :
               if j == 0:
                   n_count = (nboard[i+1][j+1]) + (nboard[i][j+1]) + nboard[i+1][j]
                   
               elif j ==  m -1:
                   print(i,j,"--------------------------------",n_count)
                   print("-----------------> " ,i+1 , j ," " , i ,j-1 , " " , i+1 , j-1)
                   print("------>" ,nboard[i+1][j]  , nboard[i][j-1] , nboard[i+1][j-1])
                   n_count =  nboard[i+1][j]   + nboard[i][j-1] + nboard[i+1][j-1]
                   print(i,j,"--------------------------------",n_count)

               else:
                   n_count = (nboard[i+1][j+1]) + (nboard[i][j+1]) + nboard[i+1][j]   + nboard[i][j-1] + nboard[i+1][j-1]      
           elif i == n -1:
               if j == 0:
                    n_count =  (nboard[i][j+1])  + nboard[i-1][j]  + nboard[i-1][j+1]                    
               elif j == m-1:
                    n_count =   nboard[i-1][j-1] + nboard[i-1][j] + nboard[i][j-1]
               
               else:
                   n_count =  (nboard[i][j+1])  + nboard[i-1][j-1] + nboard[i-1][j] + nboard[i][j-1]  + nboard[i-1][j+1]
           elif 0 < i < n and (j == 0 or j == m-1):
               
               if j == 0 :
                   print('++++++')
                   n_count = (nboard[i+1][j+1]) + (nboard[i][j+1]) + nboard[i+1][j] +  nboard[i-1][j] +  nboard[i-1][j+1]      
               elif j == m-1:
                   print('++++++')
                   n_count =  nboard[i+1][j] + nboard[i-1][j-1] + nboard[i-1][j] + nboard[i][j-1] + nboard[i+1][j-1]



           elif 0 < i  and 0 < j :
              
              n_count = (nboard[i+1][j+1]) + (nboard[i][j+1]) + nboard[i+1][j] + nboard[i-1][j-1] + nboard[i-1][j] + nboard[i][j-1] + nboard[i+1][j-1] + nboard[i-1][j+1]
           print("i" , i , 'j' , j)
           print("NC ==> " , n_count)
           if nboard[i][j] == 0 : 
               if n_count == 3:
                   board[i][j] = 1
               
           if nboard[i][j] == 1:
               if n_count > 3:
                   board[i][j] = 0
               elif n_count <2:
                   board[i][j] = 0
               elif n_count <= 3:
                   board[i][j] = 1

   return board

board =[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

print(gameOfLife(board))