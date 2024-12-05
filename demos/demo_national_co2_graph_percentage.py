import subprocess

# Run single house simulations
subprocess.run(["python", "../utils/single_house_simulation.py"])

# Run average archetype simulations
subprocess.run(["python", "../utils/average_archetype_simulation.py"])

# Prepare national scenario data
subprocess.run(["python", "../utils/national_scenarios.py"])

# First compute the percentage reduction
subprocess.run(["python", "../graphs/national_emissions_percentage.py"])

# Then generate the percentage reduction graph
subprocess.run(["python", "../graphs/national_emissions_graph_percentage.py"])

print("National CO₂ emissions percentage reduction graph generation complete.")
