import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def remove_quotes_and_process(input_file, output_file):
    # Read and remove quotes from the CSV file
    with open(input_file, 'r') as file:
        content = file.read()
    modified_content = content.replace('"', '')
    
    with open(input_file, 'w') as file:
        file.write(modified_content)

    # Load and process the CSV data
    data = pd.read_csv(input_file)
    print(f"Processing {input_file} to {output_file}")
    print(data)

    # Extract the 'AC System Output (W)' column and convert values from watts to kilowatts
    ac_output_kw = data['AC System Output (W)'] / 1000

    # Write to output text file with each value on a new line
    with open(output_file, 'w') as file:
        for value in ac_output_kw:
            file.write(f"{value}\n")

    # Print confirmation of lines written
    print(f"Total lines written: {len(ac_output_kw)}")

def read_and_process(file_path):
    with open(file_path, 'r') as file:
        # Read all lines and convert them to floats
        data = np.array([float(line.strip()) for line in file.readlines()])
        
    # Calculate total PV generation
    total_pv_generation = np.sum(data)
    
    # Calculate average hourly production
    hourly_averages = [np.mean(data[hour::24]) for hour in range(24)]
    
    return total_pv_generation, hourly_averages

def analyze_and_plot():
    lerwick_data, lerwick_hourly = read_and_process('../data/simulation_results/national/Lerwick_pv_4kw.txt')
    weymouth_data, weymouth_hourly = read_and_process('../data/simulation_results/national/Weymouth_pv_4kw.txt')
    
    print(f"Total PV generation for Lerwick: {lerwick_data} kWh")
    print(f"Total PV generation for Weymouth: {weymouth_data} kWh")
    
    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(range(24), lerwick_hourly, label='Lerwick', marker='o')
    plt.plot(range(24), weymouth_hourly, label='Weymouth', marker='o')
    plt.title('Average Hourly PV Production')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Average Production (kWh)')
    plt.xticks(range(24), labels=[f'{hour}:00' for hour in range(24)], rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('../data/simulation_results/national/average_daily_pv_production.png')
    plt.show()

if __name__ == "__main__":
    # Ensure the output directory exists
    os.makedirs('../data/simulation_results/national/', exist_ok=True)

    # First process the raw data
    remove_quotes_and_process('pvwatts_hourly.csv', '../data/simulation_results/national/Weymouth_pv_4kw.txt')
    remove_quotes_and_process('pvwatts_hourly_lerwick.csv', '../data/simulation_results/national/Lerwick_pv_4kw.txt')
    
    # Then analyze and plot the processed data
    analyze_and_plot()
