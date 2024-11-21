
# Deep Decarbonisation of the UK Residential Sector Requires Bidirectional EV Charging

## Overview

This code repository provides the implementation and analysis for the study on the deep decarbonization of the UK residential sector through bidirectional EV (Electric Vehicle) charging. As climate-induced changes increasingly impact energy consumption patterns, understanding the integration and benefits of sustainable technologies is essential for achieving carbon neutrality and enhancing energy resilience.

## Package Requirements

To run the code successfully, ensure you have the necessary Python packages installed. These can be found in the `requirements.txt` file, which can be used with pip:

```bash
pip install -r requirements.txt
```

## Datasets Requirements

The study leverages several datasets. Below are the key data sources:

| Data Source      | Description                                                  |
|------------------|--------------------------------------------------------------|
| [UK Solar PV](https://www.some_url.com) | Data on rooftop solar photovoltaic installations in the UK.  |
| [EV Adoption Trends](https://www.some_url.com) | Datasets detailing electric vehicle adoption and usage patterns.          |
| [Tariff Information](https://www.some_url.com) | Data on electricity tariffs, including Lower By Night (LBN) tariffs.   |
| [Residential Energy Use](https://www.some_url.com) | Historical and predicted energy consumption for UK households. |

## Methodology

The methodology implemented in this study is divided into several critical components:

- **EV Charging Patterns**: Studies the impact of different EV charging methods (unidirectional vs bidirectional) and the percentage of time an EV remains at home (CAH).
- **Solar PV Utilization**: Models the integration and effectiveness of solar PV systems in meeting household energy demands.
- **Grid Independence Analysis**: Evaluates how bidirectional charging can enhance self-consumption and reduce grid reliance.
- **Emissions Impact**: Analyzes the reduction in operational carbon emissions through combined solar PV and EV strategies.
- **Economic Evaluation**: Calculates operational expenditure savings and payback time for investment in these technologies.

## Demos

This repository provides several demonstrations that showcase the application of our methodology:

1. **Simulation of Grid Independence Increase Through Bidirectional Charging**
2. **Operational Expenditure Analysis With and Without Bidirectional Charging**
3. **Emissions Reduction Comparison for Different Charging Scenarios**
4. **Economic Impact Assessment of Solar PV Installation in UK Households**

## License

This project is licensed under the [Creative Commons BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) License. You are free to share and adapt the material for non-commercial purposes, providing appropriate credit is given.

```