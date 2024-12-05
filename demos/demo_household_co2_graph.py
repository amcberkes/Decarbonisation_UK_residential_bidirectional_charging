import subprocess

# Run the single house simulation
subprocess.run(["python", "../utils/single_house_simulation.py"])

# Run the script to average results
subprocess.run(["python", "../utils/average_archetype_simulation.py"])

# Generate the household CO2 emissions graph
subprocess.run(["python", "../graphs/household_emissions_graph.py"])

print("Household CO₂ emissions analysis and graph generation complete.")
