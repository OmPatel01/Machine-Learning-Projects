# Hourly CO₂ Emission Prediction for Steel Production

## Project Overview
This project focuses on predicting **hourly CO₂ emissions** generated in the steel industry, helping stakeholders understand and reduce their environmental impact. By accurately forecasting emissions, businesses can make data-driven decisions to improve sustainability in their production processes.

## Business Problem
Steel production is a significant source of CO₂ emissions, impacting climate change and sustainability goals. To mitigate this, companies need a clear, accurate measure of their emissions on an hourly basis. This project solves the problem by providing hourly predictions of CO₂ emissions based on various operational factors, supporting efforts to:

- Monitor emissions and identify areas for improvement.
- Meet regulatory standards by maintaining emission records.
- Enhance decision-making for production schedules to reduce emissions.

## Objectives
- **Build an accurate model to predict hourly CO₂ emissions** in steel production.
- **Enable visualization and analysis** of CO₂ emission trends over time.
- **Provide insights** for operational decisions to reduce the CO₂ footprint.

## Dataset
The dataset contains the following key features:
- **Usage_kWh**: Energy consumption in kilowatt-hours.
- **Reactive Power (Lagging/Leading)**: Indicators of power quality and efficiency.
- **NSM**: Seconds elapsed in the day (useful for time tracking).
- **Power Factor**: A measure of energy efficiency.

## Methodology
1. **Data Preprocessing**:
   - Aggregated data to hourly values to align with the business use case.
   - Applied **Principal Component Analysis (PCA)** to reduce feature dimensions and visualize patterns.

2. **Initial Modeling**:
   - Started with **PCA and Linear Regression** to understand relationships in the data.
   - Visualized data in lower dimensions and observed non-linear patterns in the emission data.

3. **Advanced Modeling**:
   - Implemented **Polynomial Regression (degree 2)** to capture non-linear patterns, significantly improving prediction accuracy.

4. **Pipeline Creation**:
   - Developed a pipeline with PCA and polynomial regression to streamline preprocessing and prediction.

## Results
- The model trained with **Polynomial Regression (degree 2)** provided **more accurate predictions** than linear regression.
- Dimensionality reduction with PCA allowed us to visualize CO₂ emissions across different production settings, showing non-linear patterns in emissions over time.

## Conclusion
This project demonstrates that **Polynomial Regression** with a **degree of 2** effectively captures non-linear patterns in CO₂ emissions, enabling more accurate predictions. The solution supports operational decision-making, helps meet environmental standards, and promotes a proactive approach to managing CO₂ emissions in steel production.

## Future Directions
- Implement real-time data ingestion for dynamic CO₂ tracking.
- Expand the model to include additional factors affecting emissions, such as environmental conditions.
- Integrate a recommendation system to suggest operational changes for emission reduction.
