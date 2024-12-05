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

The study utilises several datasets. Below are the key data sources:

| Data Source      | Description                                                  |
|------------------|--------------------------------------------------------------|
| [UK Building Archetypes](https://www.gov.uk/government/statistical-data-sets/energy-performance) | Data on UK building stock, focusing on the three most common archetypes (terraced, semi-detached, and detached houses) that make up 70% of occupied residential buildings. |
| [PVWatts](https://pvwatts.nrel.gov) | NREL tool used to estimate solar energy production, specifically modelling best-case (Weymouth) and worst-case (Lerwick) UK solar profiles. Hourly solar generation data for a 4kW system can be downloaded directly from the website. The downloaded files can be preprocessed and visualised by running `data/solar/prepare_inputs.py`. |
| [SPAGHETTI](https://github.com/amcberkes/SPAGHETTI) | Synthetic data generator for post-Covid EV usage patterns, including commuting types and bidirectional charging capabilities. |
| [Residential Load Data](https://www.centrefornetzero.org) | Residential electricity load profiles modelled using the Faraday tool. Access must be requested from Centre for Net Zero Limited. A modified sample load file is provided in `data/load/` to run the code. |
| [Grid Emissions](https://www.carbonbrief.org/analysis-uk-electricity-from-fossil-fuels-drops-to-lowest-level-since-1957/) | UK grid carbon intensity data from 2023 (162 gCO₂/kWh). |
| [Grid Cost](https://assets.publishing.service.gov.uk/media/6582b65223b70a000d234c97/quarterly-energy-prices-december-2023.pdf) | UK grid electricity cost data from 2023 (0.35 £/kWh). |
| [Vehicle Emissions](https://www.some_url.com) | Carbon footprint data for fossil fuel powered cars in the UK in 2023, by market segment and fuel type (average 406 kg CO₂ per year based on average yearly distance). |
| [EV Tariff](https://www.some_url.com) | Octopus Go EV tariff data, featuring lower night-time rates (7p/kWh between 11:30pm-5:30am). |

All data sources - except for the load data - are publicly available. The residential electricity load profiles were modelled using the Faraday tool, developed by Centre for Net Zero Limited. While access to the complete Faraday dataset requires permission from Centre for Net Zero Limited, we have provided a modified sample load file in the `data/load/` directory that allows users to run and test the code.

## System Requirements

### Software Dependencies
- Python 3.8 or higher
- pip package manager
- Required Python packages (specified in requirements.txt):
  - pandas
  - matplotlib
  - seaborn

### Tested Operating Systems
- macOS Monterey (12.0) or higher

### Hardware Requirements
- Minimum 8GB RAM
- 10GB available disk space
- Any modern CPU (Intel i5/AMD Ryzen 5 or better recommended)
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
- Typical installation time should be less than 6 minutes on a normal desktop computer
- Most of this time is spent downloading and installing the Python packages

### Running the Code
- Detailed step-by-step instructions for each experiment are provided in the "Running Experiments" section above
- For quick testing, refer to the demo files in the `demos/` directory, which provide simplified examples of each analysis
- Each demo includes clear instructions and should run in less than a minute

Note: Make sure to follow the exact steps described in the "Running Experiments" section when conducting full analyses, as the demos are simplified versions meant for testing purposes.

## Methodology

The methodology implemented in this study is divided into several critical components:

- **EV Charging Patterns**: Studies the impact of different EV charging methods (unidirectional vs bidirectional) and the percentage of time an EV remains at home (CAH).
- **Solar PV Utilisation**: Models the integration and effectiveness of solar PV systems in meeting household energy demands.
- **Grid Independence Analysis**: Evaluates how bidirectional charging can enhance self-consumption and reduce grid reliance.
- **Emissions Impact**: Analyses the reduction in operational carbon emissions through combined solar PV and EV strategies.
- **Economic Evaluation**: Calculates operational expenditure savings and payback time for investment in these technologies.

[Continue with the rest of the sections, maintaining British English spelling throughout]

## License

This project is licensed under the [Creative Commons BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) Licence. You are free to share and adapt the material for non-commercial purposes, providing appropriate credit is given.

## Running Experiments

### 1. Single House Analysis
This experiment analyses the impact of different charging strategies on individual households.

1. Navigate to the `experiments` directory:
   ```bash
   cd experiments/single_house
   ```

2. Run the analysis script:
   ```bash
   python run_single_house.py
   ```

3. Results will be saved in `results/single_house/` and include:
   - Grid import/export visualisations
   - Cost comparisons
   - Emissions analyses

### 2. Archetype Analysis
This experiment examines patterns across different housing archetypes.

1. Ensure single house analysis has been completed
2. Navigate to the archetype analysis directory:
   ```bash
   cd experiments/archetype
   ```

3. Run the analysis:
   ```bash
   python run_archetype_analysis.py
   ```

### 3. National Scenario Analysis
This experiment scales the results to national level projections.

1. Complete archetype analysis first
2. Navigate to the scenarios directory:
   ```bash
   cd experiments/national
   ```

3. Run the scenario analysis:
   ```bash
   python run_national_scenarios.py
   ```

## Demo Files

The `demos/` directory contains simplified versions of each analysis for quick testing and familiarisation.

### Available Demos
1. **Grid Independence Demo**
   - Visualises how different charging strategies affect grid independence
   - Runtime: Less than 1 minute
   ```bash
   python demos/demo_independence.py
   ```

2. **Cost Analysis Demo**
   - Compares operational costs across different scenarios
   - Runtime: Less than 1 minute
   ```bash
   python demos/demo_cost.py
   ```

3. **Emissions Analysis Demo**
   - Shows CO₂ emissions reductions for different strategies
   - Runtime: Less than 1 minute
   ```bash
   python demos/demo_emissions.py
   ```

4. **National Projections Demo**
   - Demonstrates scaling of results to national level
   - Runtime: Less than 1 minute
   ```bash
   python demos/demo_national.py
   ```

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
