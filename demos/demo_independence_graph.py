import subprocess

# Run the single house simulation
subprocess.run(["python", "../utils/single_house_simulation.py"])

# Run the script to average results
subprocess.run(["python", "../utils/average_archetype_simulation.py"])

# Generate the grid independence graph
subprocess.run(["python", "../graphs/grid_independence_graph.py"])

print("Grid independence graph generation complete.")

# Note: this code should only run for a few seconds. 