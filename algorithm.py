from ortools.linear_solver import pywraplp

def solver(table, maximize, name):
    solver = pywraplp.Solver(
        "problema de asignacion",
        pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    
    #define parameters
    print(table)
    n = len(table)
    m = len(table[0])
    print(n)
    print(m)

    vars = []

    for i in range(n):
        tmp = []
        for j in range(m):
            tmp.append(solver.BoolVar(f'x{i}{j}'))
        vars.append(tmp)
    
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
            sum += vars[i][j]*table[i][j]

    if maximize:
        solver.Minimize(sum)
    else:
        solver.Maximize(sum)


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
                    print(f' x{i+1}{j+1} = {vars[i][j].solution_value()}  => {table[i][j]}')
        
        arrsol = []

        for i in range(n):
            tmp = []
            for j in range(m):
                if (vars[i][j].solution_value() == 1):
                    tmp.append(1)
                else:
                    tmp.append(0) 
                # tmp.append(vars[i][j].solution_value())
            arrsol.append(tmp)
        return arrsol, int(solver.Objective().Value())
    else:
        print('The solver could not find an optimal solution.')
    




