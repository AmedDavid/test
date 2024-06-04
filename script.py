import gurobipy as gp
from gurobipy import GRB

# Data
control_technologies = {
    1: {"T_min": 2, "T_max": 9, "c_min": 0.4, "c_max": 0.65, "c_o": 1.05, "a": -0.0357, "b": 0.721},
    2: {"T_min": 2, "T_max": 8, "c_min": 0.3, "c_max": 0.7, "c_o": 0.9, "a": -0.0667, "b": 0.833},
    3: {"T_min": 4, "T_max": 14, "c_min": 0.2, "c_max": 0.5, "c_o": 1.1, "a": -0.03, "b": 0.62},
    4: {"T_min": 4, "T_max": 8, "c_min": 0.15, "c_max": 0.5, "c_o": 0.95, "a": -0.0875, "b": 0.85},
    5: {"T_min": 3, "T_max": 10, "c_min": 0.2, "c_max": 0.6, "c_o": 0.8, "a": -0.0571, "b": 0.771},
    6: {"T_min": 2, "T_max": 9, "c_min": 0.4, "c_max": 0.65, "c_o": 1.05, "a": -0.0357, "b": 0.721},
    7: {"T_min": 4, "T_max": 12, "c_min": 0.3, "c_max": 0.65, "c_o": 0.95, "a": -0.0438, "b": 0.825},
    8: {"T_min": 1, "T_max": 10, "c_min": 0.4, "c_max": 0.7, "c_o": 0.95, "a": -0.0333, "b": 0.733},
    9: {"T_min": 1, "T_max": 10, "c_min": 0.4, "c_max": 0.65, "c_o": 0.95, "a": -0.0278, "b": 0.678},
}

# Model
model = gp.Model("Air_Pollution_Control")

# Decision variables
x = {}
T = {}
for j in control_technologies.keys():
    x[j] = model.addVar(vtype=GRB.BINARY, name=f"x_{j}")
    T[j] = model.addVar(lb=0, name=f"T_{j}")

# New variable for total cost
total_cost = model.addVar(name="Total_Cost")

# Objective function
model.setObjective(
    total_cost,
    GRB.MINIMIZE
)

# Constraints
for j in control_technologies.keys():
    model.addConstr(T[j] >= control_technologies[j]["T_min"] * x[j], name=f"T_min_{j}")
    model.addConstr(T[j] <= control_technologies[j]["T_max"] * x[j], name=f"T_max_{j}")

# Define the total cost
model.addConstr(total_cost == gp.quicksum(control_technologies[j]["c_o"] * x[j] + control_technologies[j]["a"] * T[j] + control_technologies[j]["b"] for j in control_technologies.keys()))

# Budget constraint
B = 9.0  # Total budget
model.addConstr(total_cost <= B, name="Budget")

# Pollution reduction level constraint
model.addConstr(gp.quicksum(x[j] for j in control_technologies.keys()) >= 2, name="Reduction_Level")

# Set binary constraints for decision variables x[j]
for j in control_technologies.keys():
    model.addConstr(x[j] <= 1)
    model.addConstr(x[j] >= 0)

# Optimize
model.optimize()

# Print solution
if model.status == GRB.OPTIMAL:
    print("Optimal solution found!")
    for j in control_technologies.keys():
        print(f"Control {j}: x_{j} = {x[j].X}, T_{j} = {T[j].X}")
    print(f"Total cost: {total_cost.X}")
else:
    print("No solution found.")
