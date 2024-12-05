import subprocess

# Run single house simulations
subprocess.run(["python", "../utils/single_house_simulation.py"])

# Run average archetype simulations
subprocess.run(["python", "../utils/average_archetype_simulation.py"])

# Prepare national scenario data
subprocess.run(["python", "../utils/national_scenarios.py"])

# Generate the national CO2 emissions graph in tonnes
subprocess.run(["python", "../graphs/national_emissions_graph_tonnes.py"])

print("National CO₂ emissions graph (tonnes) generation complete.")
