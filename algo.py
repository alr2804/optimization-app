from ortools.linear_solver import pywraplp
# Create a solver using the GLOP backend
#define the name of the problem
solver = pywraplp.Solver('Problema de asignacion', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

#read csv
import csv

arr = []

arr = [
    [2, 3, 2, 2],
    [1, 2, 1, 1],
    [2, 1, 2, 1]]

# with open("./test.csv", 'r') as file:
#   csvreader = csv.reader(file)
#   for row in csvreader:
#     tmp = []
#     for e in row:
#       # print(e)
#       tmp.append(int(e))
#     arr.append(tmp)

print(arr)
n = len(arr)
m = len(arr[0])
print(n)
print(m)

#define an arr of variables
vars = []

for i in range(n):
  tmp = []
  for j in range(m):
    tmp.append(solver.BoolVar(f'x{i}{j}'))
  vars.append(tmp)


  #define parameters

for i in range(n):
  sum  = 0
  for j in range(m):
    sum += vars[i][j]
  #it should change accord n and m values req vs res
  if n == m:
    solver.Add( sum == 1 )
  elif n > m:
    solver.Add(sum <= 1)
  else:
    solver.Add(sum == 1)


for i in range(m):
  sum = 0
  for j in range(n):
    sum += vars[j][i]
  
  if n == m:
    solver.Add( sum == 1 )
  elif n > m:
    solver.Add(sum == 1)
  else:
    solver.Add(sum <= 1)


sum = 0
for i in range(n):
  for j in range(m):
    sum += vars[i][j]*arr[i][j]

solver.Minimize(sum)


status = solver.Solve()

# If an optimal solution has been found, print results
if status == pywraplp.Solver.OPTIMAL:
  print('================= Solution =================')
  print(f'Solved in {solver.wall_time():.2f} milliseconds in {solver.iterations()} iterations')
  print()
  print(f'Optimal power = {solver.Objective().Value()} 💪power')
  print('Values:')
  for i in range(n):
    for j in range(m):
      if vars[i][j].solution_value() == 1:
        print(f' x{i+1}{j+1} = {vars[i][j].solution_value()}  => {arr[i][j]}')

else:
  print('The solver could not find an optimal solution.')