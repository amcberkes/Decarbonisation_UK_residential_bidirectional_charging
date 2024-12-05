# Deep Decarbonisation of the UK Residential Sector Requires Bidirectional EV Charging

## Overview

This code repository provides the implementation and analysis for the study on the deep decarbonisation of the UK residential sector through bidirectional EV (Electric Vehicle) charging. 

The synergy between residential solar photovoltaic systems and electric vehicles parked at home can substantially reduce a household’s operational expenditure, capital expenditure, and payback time, as well as its CO2 emissions. These benefits are dramatically improved when an electric vehicle is allowed to discharge energy into the home (i.e., with bidirectional charging). We find that while individually each element contributes to significant cost savings and decarbonisation, their simultaneous adoption has significant additional benefits. For example, the system payback-time decreases from 14 to 2 years and household carbon emissions are reduced by up to 66%. Additional co-benefits include improved grid resilience and increased energy independence. Furthermore, at the national level, 90% adoption of bidirectional charging could reduce the UK’s CO2 emissions by 13 million tonnes annually, corresponding to a 55% decrease in current electricity and vehicle use emissions. We therefore urge policy makers and regulators to encourage its rapid adoption.

## Package Requirements

To run the code successfully, ensure you have the necessary Python packages installed. These can be found in the `requirements.txt` file, which can be used with pip:

```bash
pip install -r requirements.txt
```

## Datasets Requirements

The study uses several datasets. Below are the key data sources:

| Data Source      | Description                                                  |
|------------------|--------------------------------------------------------------|
| [UK Building Archetypes](https://www.gov.uk/government/statistical-data-sets/energy-performance) | Data on building stock, focusing on the three most common archetypes (terraced, semi-detached, and detached houses) that make up 70% of occupied residential buildings. |
| [PVWatts](https://pvwatts.nrel.gov) | NREL tool used to estimate solar energy production, specifically modelling best-case (Weymouth) and worst-case (Lerwick) UK solar profiles. Hourly solar generation data for a 4kW system can be downloaded directly from the website. The downloaded files can be preprocessed and visualised by running `data/solar/prepare_inputs.py`. |
| [SPAGHETTI](https://github.com/amcberkes/SPAGHETTI) | Synthetic data generator for post-Covid EV usage patterns, including commuting types and bidirectional charging capabilities. |
| [Residential Load Data](https://www.centrefornetzero.org) | Residential electricity load profiles modelled using the Faraday tool. Access must be requested from Centre for Net Zero Limited. A modified sample load file is provided in `data/load/` to run the code. |
| [Grid Emissions](https://www.carbonbrief.org/analysis-uk-electricity-from-fossil-fuels-drops-to-lowest-level-since-1957/) | UK grid carbon intensity data from 2023 (162 gCO₂/kWh). |
| [Grid Cost](https://assets.publishing.service.gov.uk/media/6582b65223b70a000d234c97/quarterly-energy-prices-december-2023.pdf) | UK grid electricity cost data from 2023 (0.35 £/kWh). |
| [Vehicle Emissions](https://www.statista.com/statistics/1233409/carbon-footprint-of-cars-by-type-uk/) | Carbon footprint data for fossil fuel powered cars in the UK in 2023, by market segment and fuel type (average 406 kg CO₂ per year based on average yearly distance). |
| [EV Tariff](https://octopus.energy/smart/intelligent-octopus-go/) | Octopus Go EV tariff data, featuring lower night-time rates (7p/kWh between 11:30pm-5:30am). |

All data sources - except for the load data - are publicly available. The residential electricity load profiles were modelled using the Faraday tool, developed by Centre for Net Zero Limited. While access to the complete Faraday dataset requires permission from Centre for Net Zero Limited, we have provided a modified sample load file in the `data/load/` directory that allows users to run and test the code.

## System Requirements

### Software Dependencies
- Python 3.8 or higher
- pip package manager
- Required Python packages (specified in requirements.txt):
  - pandas
  - matplotlib
  - seaborn

### Systems
- macOS Monterey (12.0) or higher
- No specialised hardware (GPU, etc.) required

### Installation Guide
1. Clone the repository:
   ```bash
   git clone https://github.com/amcberkes/Decarbonisation_UK_residential_bidirectional_charging.git
   cd Decarbonisation_UK_residential_bidirectional_charging
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure all data files are in their respective directories as described in the Dataset Requirements section

### Installation Time
- Typical installation time should be less than 5 minutes on a normal desktop computer
- Most of this time is spent downloading and installing the Python packages

### Running the Code
- Detailed step-by-step instructions for each experiment are provided in the "Running Experiments" section above
- For quick testing, refer to the demo files in the `demos/` directory, which provide simplified examples of each analysis
- Each demo includes clear instructions and should run in less than a minute

Note: Make sure to follow the exact steps described in the "Running Experiments" section when conducting full analyses, as the demos are simplified versions meant for testing purposes.

## Methodology

The methodology implemented in this study is divided into several critical components. The simulation code is based on [SOPEVS](https://github.com/amcberkes/SOPEVs), and a detailed description of themethodology can be found in the paper correpsonding to this repository (currently under review).

### Available Experiments

1. **Single House Analysis**
   - Evaluates individual household performance for different combinations of charging strategies, solar PV radiation intensities and EV usage patterns (CAH)
   - Compares different charging strategies
   - Analyses grid import patterns
   - Calculates costs and emissions

2. **Archetype Analysis**
   - Studies patterns across different UK housing types: terraced, semi-detached, and detached houses


3. **National Scenario Analysis**
   - Scales results to national level
   - Projects potential CO₂ emission reductions for different technology adoption scenarios and conversion levels


# License

This project is licensed under the [Creative Commons BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) Licence. You are free to share and adapt the material for non-commercial purposes, providing appropriate credit is given.

# Running Experiments

The repository supports several experiments to analyze different aspects of residential energy usage and EV charging. Below are detailed instructions for running each experiment:

## OPEX (Operational Expenditure) Analysis
This experiment analyzes operational costs across different scenarios. To run it:
1. **Simulate Energy Usage** (`single_house_simulation.py`)
   - Simulates energy use and EV charging for all studied households over a one-year period
   - Generates data for different combinations of:
     - CAH Types (Car at Home patterns)
     - Operation policies (unidirectional vs bidirectional charging)
     - Solar generation profiles (high/low UK solar potential)
   - Output: Raw simulation results for each household
2. **Average Across Archetypes** (`average_archetype_simulation.py`)
   - Processes raw simulation results
   - Computes average grid emissions and costs for combinations of:
     - Building archetypes
     - CAH patterns
     - Operation policies
     - Solar profiles
   - Output: Averaged results stored in `data/simulation_results/averaged_simulation_results_Faraday.csv`
3. **Generate OPEX Visualization** (`graphs/OPEX_graph.py`)
   - Creates visual representation of operational expenditure analysis
   - Uses averaged results from step 2
   - Output: OPEX comparison graphs
### Supplemental: Varying Grid Electricity Cost
- You can run the OPEX Analysis with different grid electricity cost values by modifying the `pounds_per_kwh` variable in `average_archetype_simulation.py`.
  ```python
  pounds_per_kwh = 0.35  # Default electricity cost in pounds
  ```
- Adjust this value to reflect different scenarios or assumptions about electricity costs.
## Grid Independence Analysis
This experiment evaluates how bidirectional charging can enhance self-consumption and reduce grid reliance. To run it:
1. **Compute Grid Independence:**
   - Use the following formula to calculate grid independence:
     \[
     \text{Grid Independence} = 100 - \left(\frac{\text{Grid Import}}{\text{Total Load}}\right) \times 100
     \]
   - Apply this formula to the results from the `average_archetype_simulation.py` to compute grid independence for different archetype, CAH, operation, and solar combinations.
2. **Use Faraday Data:**
   - The results using the Faraday data are already computed and stored in `data/simulation_results/independence.csv`.
   - This file can be used as input for generating the grid independence graph.
3. **Generate Grid Independence Visualization** (`graphs/grid_independence_graph.py`)
   - Run this script to create a visual representation of grid independence.
   - It uses the precomputed results from `independence.csv` to generate the graph.
## Payback Time Analysis
This experiment calculates how long it takes for the financial savings from a solar PV and EV system to offset the initial installation costs. To run it:
1. **Compute OPEX Savings** (`utils/compute_opex_savings.py`)
   - Calculates yearly operational expenditure savings when using PV and EV
   - Uses pre-conversion OPEX values computed from Faraday data (can be modified in the code)
   - Base values for houses without EV or PV are stored in the script:
     ```python
     pre_conversion_opex = {
         'Terraced': 2739.301,
         'Semi_Detached': 2904.193,
         'Detached': 2957.12
     }
     ```
2. **Calculate CAPEX Using SOPEVS**
   - Uses [SOPEVS (Single-Roof Optimal PV-EV Sizing)](https://github.com/amcberkes/SOPEVS_Single_Roof) framework to compute least-cost solar PV capacity
   - Based on the paper: Berkes, Anaïs, and Srinivasan Keshav. "SOPEVS: Sizing and Operation of PV-EV-Integrated Modern Homes." Proceedings of the 15th ACM International Conference on Future and Sustainable Energy Systems. 2024.
   - Parameters set to ensure each household can meet at least 50% of electrical load with 95% confidence
   - SOPEVS process:
     1. Samples input traces from PV generation, load, and EV usage
     2. Uses stochastic gradient descent to find minimum cost sizings
     3. Determines system sizings meeting predetermined quality-of-service criterion
3. **Compute Payback Time**
   - Uses the formula:
     \[
     \text{Payback Time} = \frac{\text{CAPEX}}{\text{Yearly OPEX Savings}}
     \]
   - Considers:
     - Two operation policies (unidirectional N-U vs bidirectional SG-B)
     - Three CAH types
     - Two solar profiles
   - Note: Includes car operation cost in OPEX but not in CAPEX due to high variability in car prices
4. **Generate Visualization** (`graphs/payback_time_graph.py`)
   - Creates visual representation of payback time analysis
   - Shows results for different scenarios and configurations
## Household CO₂ Emissions Analysis
This experiment analyzes the CO₂ emissions from both household electricity consumption and personal vehicle usage at the household level. To run it:
1. **Simulate Energy Usage** (`single_house_simulation.py`)
   - Same process as in OPEX analysis
   - Simulates energy use and EV charging for all studied households
   - Generates raw simulation results for different combinations of archetypes, CAH types, operation policies, and solar profiles
2. **Average Across Archetypes** (`average_archetype_simulation.py`)
   - Same process as in OPEX analysis
   - Processes raw simulation results to compute average values
   - Output stored in `data/simulation_results/averaged_simulation_results_Faraday.csv`
3. **Generate Emissions Visualization** (`graphs/household_emissions_graph.py`)
   - Creates visual representation of household-level CO₂ emissions
   - Combines both electricity and vehicle usage emissions
   - Shows results across different scenarios and configurations
### Supplemental: Varying Grid Carbon Intensity
- You can run the Household CO₂ Emissions Analysis with different grid carbon intensity values by modifying the `gCO2_per_kwh` variable in `average_archetype_simulation.py`.
  ```python
  gCO2_per_kwh = 162  # Default grid carbon intensity in gCO2/kWh
  ```
- Adjust this value to reflect different scenarios or assumptions about grid carbon intensity.
## National Decarbonization Scenarios Analysis
This experiment analyzes different technology adoption scenarios at a national scale. To run it:
1. **Run Single House Simulations** (`single_house_simulation.py`)
   - For each scenario, uncomment the corresponding compiled code command.
   - Each run will generate a `household_simulation_results.csv` file for that specific scenario.
2. **Run Average Archetype Simulations** (`average_archetype_simulation.py`)
   - This script calculates average values of grid emissions across households for each combination of archetype, CAH type, operation, and solar condition.
   - It provides the average grid emissions for each of the considered scenarios.
   - Collect all these average emissions values in a file. We have provided the emissions results from our analysis in the file `data/simulation_results/national_level/emissions_all_scenarios.csv`.
   
   > **Note**: The grid carbon intensity used in the simulations can be modified by changing the `gCO2_per_kwh = 162` variable in `average_archetype_simulation.py`. This allows for analysis under different grid decarbonization scenarios.
3. **Generate National Scenario Data** (`national_scenarios.py`)
   - This script processes the average emissions data to prepare it for graph generation.
   - It computes total emissions for different conversion rates (0% to 100% in 5% steps) for each scenario.
   - The script generates separate CSV files for each combination of operation type (unidirectional/bidirectional) and solar condition (best/worst).
   - Output files will be stored in `data/simulation_results/national/` with names following the pattern `{operation}_{solar}_all_scenarios.csv`.
   - These files contain the projected national emissions (in megatons of CO2) for different technology adoption rates and scenarios.
4. **Generate Graphs**
   - If you want CO₂ emissions in megatonnes as the y-axis, run:
     ```bash
     python graphs/national_emissions_graph_tonnes.py
     ```
   - If you want the percentage reduction in CO₂ emissions compared to the baseline as the y-axis:
     1. First, compute the percentage reduction:
        ```bash
        python graphs/national_emissions_percentage.py
        ```
     2. Then, generate the graph:
        ```bash
        python graphs/national_emissions_graph_percentage.py
        ```
These steps will produce visualizations of the national decarbonization scenarios, allowing you to analyze the impact of different technology adoption rates on CO₂ emissions.

   ```


# Demo Instructions
## 1. OPEX Graph Demo
This demo generates a graph showing the operational expenditure analysis.
### Instructions to Run
```bash
python demo_opex_graph.py
```
### Expected Output
- Generates OPEX comparison graphs in the graphs/ directory
- Shows operational costs across different scenarios and configurations
### Expected Run Time
- Less than a minute on a standard desktop computer
## 2. Grid Independence Graph Demo
This demo generates a graph showing how bidirectional charging enhances grid independence.
### Instructions to Run
```bash
python demo_independence_graph.py
```
### Expected Output
- Generates grid independence visualization in the graphs/ directory
- Shows the percentage of grid independence achieved under different scenarios
### Expected Run Time
- Less than a minute on a standard desktop computer
## 3. Payback Time Analysis Demo
This demo calculates and visualizes the payback time for solar PV and EV investments.
### Instructions to Run
```bash
python demo_payback_time.py
```
### Expected Output
- Computes OPEX savings for different scenarios
- Generates payback time visualization in the graphs/ directory
- Shows how long it takes for the financial savings to offset initial costs across different:
  - Operation policies (unidirectional vs bidirectional)
  - CAH types
  - Solar profiles
### Expected Run Time
- Less than a minute on a standard desktop computer
### Note
This demo uses pre-defined CAPEX values and the following base OPEX values for houses without EV or PV:
- Terraced: £2,739.30
- Semi-Detached: £2,904.19
- Detached: £2,957.12
## 4. Household CO₂ Emissions Analysis Demo
This demo calculates and visualizes CO₂ emissions from household electricity consumption and personal vehicle usage.
### Instructions to Run
```bash
python demo_household_co2_emissions.py
```
### Expected Output
- Generates a visualization of household-level CO₂ emissions in the graphs/ directory
- Combines emissions from both electricity and vehicle usage
- Shows results across different scenarios and configurations
### Expected Run Time
- Less than a minute on a standard desktop computer
### Note
This demo uses the default grid carbon intensity of 162 gCO₂/kWh. You can adjust this value in `average_archetype_simulation.py` to explore different scenarios.
## 5. National CO₂ Emissions Graph (Tonnes) Demo
This demo generates a graph showing national CO₂ emissions in tonnes.
### Instructions to Run
```bash
python demo_national_co2_graph_tonnes.py
```
### Expected Output
- Generates a national CO₂ emissions graph in tonnes in the graphs/ directory
- Shows emissions across different technology adoption scenarios
### Expected Run Time
- Less than a minute on a standard desktop computer
## 6. National CO₂ Emissions Graph (Percentage) Demo
This demo generates a graph showing the percentage reduction in national CO₂ emissions compared to the baseline.
### Instructions to Run
```bash
python demo_national_co2_graph_percentage.py
```
### Expected Output
- Generates a national CO₂ emissions reduction graph in the graphs/ directory
- Shows percentage reduction in emissions across different technology adoption scenarios
- Uses the baseline (no PV, no EV) scenario as reference point
### Expected Run Time
- Less than a minute on a standard desktop computer
### Note
This demo uses the default grid carbon intensity of 162 gCO₂/kWh. You can adjust this value in `average_archetype_simulation.py` to explore different scenarios.
## Note
All demos require:
- All necessary data files to be present in their respective directories
- Python packages listed in requirements.txt to be installed


## Data Processing

### Input Data Preparation
1. **Solar Data**
   - Download hourly generation data from PVWatts
   - Run the preprocessing script:
     ```bash
     python data/solar/prepare_inputs.py
     ```

2. **Load Profiles**
   - Place the load files in `data/load/`
   - Request to download complete UK archetype load data can be made to Faraday at Centre for Net Zero Limited

3. **EV Usage Patterns**
   - Generate synthetic patterns using [SPAGHETTI](https://github.com/amcberkes/SPAGHETTI)
  

### Output Processing
Results are processed and visualised in several stages:

   - Simulation outputs are processed into standardised formats
   - Graphs are generated using matplotlib and seaborn



## Contributing

We welcome contributions that improve the analysis or extend its scope. Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request


## Support

For questions or issues contact the maintainers via email: amcb6@cam.ac.uk

## Acknowledgements

This work was supported by the Gates Cambridge Trust and builds upon several open-source projects and datasets. We thank all contributors and data providers.
