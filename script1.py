import gurobipy as gp

# Define the optimization model
model = gp.Model()

# Decision variables
n = 3  # Number of pollution sources
m = 2  # Number of control processes
x = {}  # Binary decision variables
y = {}  # Pollution reduction variables
for i in range(n):
    for j in range(m):
        x[i, j] = model.addVar(vtype=gp.GRB.BINARY, name=f"x[{i},{j}]")
        y[i, j] = model.addVar(vtype=gp.GRB.CONTINUOUS, name=f"y[{i},{j}]")

# Objective function
# Minimize total cost
cost = {(0, 0): 150, (0, 1): 200, (1, 0): 250, (1, 1): 300, (2, 0): 200, (2, 1): 250}  # Cost coefficients
total_cost = gp.quicksum(cost[i, j] * x[i, j] for i in range(n) for j in range(m))
model.setObjective(total_cost, sense=gp.GRB.MINIMIZE)

# Constraints
for i in range(n):
    # Each pollution source must be controlled
    model.addConstr(gp.quicksum(x[i, j] for j in range(m)) == 1, name=f"Control_constraint_{i}")
    
for j in range(m):
    # Pollution reduction constraint
    for i in range(n):
        model.addConstr(y[i, j] <= 100 * x[i, j], name=f"Reduction_constraint_{i}_{j}")
    model.addConstr(gp.quicksum(y[i, j] for i in range(n)) >= 80, name=f"Pollution_reduction_constraint_{j}")

# Solve the model
model.optimize()

# Check optimization status
if model.status == gp.GRB.OPTIMAL:
    print("Optimal solution found!")
    # Print optimal solution
    for i in range(n):
        for j in range(m):
            if x[i, j].x > 0.5:
                print(f"Control process {j} applied to pollution source {i}")
else:
    print("No solution found.")
