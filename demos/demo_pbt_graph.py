import subprocess

# Run the single house simulation
subprocess.run(["python", "../utils/single_house_simulation.py"])

# Run the script to average results
subprocess.run(["python", "../utils/average_archetype_simulation.py"])

# Compute OPEX savings
subprocess.run(["python", "../utils/compute_opex_savings.py"])

# Generate the payback time graph
subprocess.run(["python", "../graphs/payback_time_graph.py"])

print("Payback time analysis and graph generation complete.")

# Note: this code should only run for a few seconds. 