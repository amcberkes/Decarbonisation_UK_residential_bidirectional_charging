import pandas as pd

# Load the data from the CSV file that gives OPEX for each archetype x WFH x operation x solar
file_path = '../data/simulation_results/averaged_simulation_results_Faraday.csv'
data = pd.read_csv(file_path)

# Average OPEX values computed from Faraday data for houses without EV or PV (baseline scenario)
pre_conversion_opex = {
    'Terraced': 2739.301,
    'Semi_Detached': 2904.193,
    'Detached': 2957.12
}


# Initialize a list to hold the results
results = []

# Iterate over each row in the dataframe to compute OPEX savings
for index, row in data.iterrows():
    archetype = row['Archetype']
    wfh_type = row['CAH Type']
    operation = row['Operation']
    solar = row['Solar']
    grid_cost = row['Grid Cost']
    
    # Calculate OPEX Savings
    opex_savings = pre_conversion_opex[archetype] - grid_cost
    
    # Append the results
    results.append({
        'Archetype': archetype,
        'CAH Type': wfh_type,
        'Operation': operation,
        'Solar': solar,
        'OPEX Savings': opex_savings
    })

# Convert the list of results into a DataFrame
results_df = pd.DataFrame(results)

# Save the results to a CSV file
results_df.to_csv('../data/simulation_results/opex_savings_results.csv', index=False)

print("CSV file with OPEX Savings has been created.")
