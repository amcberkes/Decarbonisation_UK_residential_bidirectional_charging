import subprocess

# Run the OPEX analysis script
subprocess.run(["python", "../utils/single_house_simulation.py"])

# Run the script to average results
subprocess.run(["python", "average_archetype_simulation.py"])

# Generate the OPEX graph
subprocess.run(["python", "../graphs/OPEX_graph.py"])

print("OPEX graph generation complete.")

# Note: this code should only run for a few seconds. 