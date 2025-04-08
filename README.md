# London Fire Brigade Operations Dashboard

## Overview
This repository contains an interactive Tableau dashboard that visualizes operations data for the London Fire Brigade (LFB). The dashboard provides stakeholders with comprehensive insights into emergency response activities, resource allocation, and performance metrics across London's fire stations.

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

## Screenshots
![Dashboard Overview](/images/dashboard_overview.png)
(Additional screenshots in the /images folder)

## Data Source
This dashboard uses simulated data based on the London Fire Brigade operational model. The data structure includes:
- Fire station information
- Staff and firefighter details
- Incident records
- Appliance deployment
- Multi-agency coordination

## Contact
For more information or to request access to the full Tableau workbook, please contact [Your Contact Information].
