# London Fire Brigade Operations Dashboard

## Overview
This repository contains an interactive Tableau dashboard that visualizes operations data for the London Fire Brigade (LFB). The dashboard provides stakeholders with comprehensive insights into emergency response activities, resource allocation, and performance metrics across London's fire stations.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://london-fire-brigade-dashboard-nvt8pz5kpbqcx2cqddxdez.streamlit.app/)

> **Note:** The Streamlit app allows you to view the dashboard directly in your browser without Tableau Desktop. See the [Streamlit Deployment Guide](STREAMLIT_DEPLOYMENT.md) for details.

## Dashboard Components

### 1. Station Callouts (Treemap)
Visualizes the distribution of genuine incidents across fire stations, with rectangle size representing call volume. Helps identify the busiest stations for resource allocation planning.

### 2. Firefighters Responding (Bar Chart)
Displays the allocation of firefighters by rank during incident responses, showing staffing distribution and availability patterns.

### 3. Appliance Incident Report (Pie Chart)
Illustrates the distribution of incidents by appliance type, providing insights into fleet utilization and specialization needs.

### 4. Emergency Service Coordination (Network Visualization)
Shows the relationships between LFB and other emergency services during joint operations, highlighting multi-agency collaboration patterns.

### 5. Monthly Average Response Times (Bar Chart)
Compares station performance using color-coded response metrics, identifying high and low-performing stations.

### 6. London Incidents Geographic Analysis (Interactive Map)
Plots incidents across London with detailed tooltips providing incident context, allowing for geographic pattern analysis.

## Interactive Features
- Borough filtering
- Incident type selection
- Date range filtering
- Cross-visualization filtering for detailed analysis

## Technical Implementation
The dashboard connects to a SQL Server database containing the LFB operational data structured according to the entity-relationship model in the /documentation folder. Queries used to extract the data can be found in the /sql folder.

### Repository Structure
- `/tableau`: Contains the Tableau workbook files
- `/sql`: SQL queries used to extract data
- `/images`: Dashboard screenshots
- `app.py`: Streamlit application for web-based dashboard viewing
- `requirements.txt`: Dependencies for the Streamlit app

## Screenshots

View the live dashboard on Tableau Public:

[![Tableau Dashboard](https://public.tableau.com/static/images/Lo/LondonFireBrigadeOperationsDashboard-March2025/LondonFireBrigadeOperationsDashboard-March2025/1_rss.png)](https://public.tableau.com/views/LondonFireBrigadeOperationsDashboard-March2025/LondonFireBrigadeOperationsDashboard-March2025)

### Dashboard Components:

1. **Station Callouts** - Treemap visualization of incident distribution across fire stations
2. **Firefighter Response Analysis** - Deployment patterns by rank and role
3. **Appliance Utilization** - Distribution of incidents by vehicle type
4. **Multi-Agency Coordination** - Network visualization of emergency service collaboration
5. **Response Time Analysis** - Performance metrics by station
6. **Geographic Incident Distribution** - Spatial analysis of incidents across London

The dashboard demonstrates the integration of multiple data sources to provide actionable intelligence for emergency service management.

## Data Source
This dashboard uses simulated data based on the London Fire Brigade operational model. The data structure includes:
- Fire station information
- Staff and firefighter details
- Incident records
- Appliance deployment
- Multi-agency coordination

## Contact
For more information or to request access to the full Tableau workbook, please contact [Your Contact Information].
