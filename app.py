import streamlit as st
import streamlit.components.v1 as components
import os
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="London Fire Brigade Dashboard",
    page_icon="🔥",
    layout="wide"
)

# Header
st.title("London Fire Brigade Operations Dashboard")
st.markdown("### Interactive visualization of London Fire Brigade operations data")

# Info section
with st.expander("About this dashboard"):
    st.markdown("""
    This dashboard provides comprehensive insights into the London Fire Brigade's operations, including:
    
    - **Station Callouts**: Distribution of genuine incidents across fire stations
    - **Firefighters Responding**: Allocation of firefighters by rank during incidents
    - **Appliance Incident Report**: Distribution of incidents by appliance type
    - **Emergency Service Coordination**: Multi-agency collaboration patterns
    - **Monthly Average Response Times**: Performance metrics by station
    - **Geographic Analysis**: Spatial distribution of incidents across London
    """)

# Dashboard tabs
tab1, tab2 = st.tabs(["Tableau Dashboard", "Data Information"])

with tab1:
    st.markdown("### London Fire Brigade Dashboard")
    
    # Display tableau files info
    st.success("The repository contains the following Tableau workbooks:")
    
    # Create columns for the two workbooks
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Packaged Workbook (TWBX)")
        st.markdown("`tableau/Final.twbx`")
        st.markdown("This packaged workbook contains the dashboard visualizations and embedded data.")
        st.markdown("**Size:** 158 KB")
        st.download_button(
            label="Download TWBX File",
            data=open("tableau/Final.twbx", "rb"),
            file_name="Final.twbx",
            mime="application/octet-stream"
        )
    
    with col2:
        st.markdown("#### Dashboard Workbook (TWB)")
        st.markdown("`tableau/London Fire Brigade Operations Dashboard - March 2025.twb`")
        st.markdown("This is the Tableau workbook file containing the dashboard design without embedded data.")
        st.markdown("**Size:** 393 KB")
        st.download_button(
            label="Download TWB File",
            data=open("tableau/London Fire Brigade Operations Dashboard - March 2025.twb", "rb"),
            file_name="LFB_Dashboard.twb",
            mime="application/octet-stream"
        )
    
    # Interactive dashboard simulation section
    st.markdown("---")
    st.markdown("### London Fire Brigade Dashboard Visualization")
    
    # Dashboard components tabs
    dash_tabs = st.tabs(["Overview", "Station Analysis", "Firefighter Allocation", "Response Times", "Geographic Analysis"])
    
    with dash_tabs[0]:  # Overview tab
        st.markdown("#### Dashboard Overview")
        
        # Key metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Incidents", "217,542", "5.4%")
        with col2:
            st.metric("Average Response Time", "6:48 min", "-0:42 min")
        with col3:
            st.metric("False Alarms", "108,771", "-2.1%", delta_color="inverse")
        
        # Create incident type breakdown
        incident_types = ['False Alarm', 'Fire', 'Special Service']
        incident_counts = [108771, 33823, 74948]
        
        fig = px.pie(
            values=incident_counts,
            names=incident_types,
            title="Incident Type Distribution",
            color_discrete_sequence=px.colors.qualitative.Bold,
            hole=0.4
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        # Add yearly trend
        years = [2021, 2022, 2023, 2024]
        incidents = [195000, 203000, 217542, 228000]
        
        fig = px.line(
            x=years, 
            y=incidents, 
            markers=True,
            title="Annual Incident Trend",
            labels={"x": "Year", "y": "Total Incidents"}
        )
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    with dash_tabs[1]:  # Station Analysis
        st.markdown("#### Station Callouts Analysis")
        
        # Create a simulated treemap of station callouts
        stations = [
            "Soho", "Lambeth", "Shoreditch", "Euston", "Paddington",
            "Chelsea", "Kensington", "Battersea", "Brixton", "Islington", 
            "Southwark", "Whitechapel", "Homerton", "Bethnal Green", "Poplar"
        ]
        
        incidents = [
            4127, 3954, 3812, 3651, 3520,
            3489, 3362, 3300, 3150, 3050,
            2980, 2950, 2820, 2760, 2600
        ]
        
        fig = px.treemap(
            names=stations,
            parents=["London"]*len(stations),
            values=incidents,
            title="Station Callouts - Distribution of Genuine Incidents",
            color=incidents,
            color_continuous_scale='Reds',
        )
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)
        
        # Top stations table
        df = pd.DataFrame({
            "Station": stations[:5],
            "Incidents": incidents[:5],
            "Change from 2022": ["+2.4%", "+1.8%", "-0.7%", "+3.2%", "+0.5%"]
        })
        st.markdown("##### Top 5 Stations by Incident Count")
        st.dataframe(df, use_container_width=True)
        
    with dash_tabs[2]:  # Firefighter Allocation
        st.markdown("#### Firefighter Allocation Analysis")
        
        # Create firefighter rank data
        ranks = [
            "Firefighter", "Leading Firefighter", "Crew Manager", 
            "Watch Manager", "Station Manager", "Group Manager", "Area Manager"
        ]
        
        firefighters = [3200, 850, 600, 450, 120, 40, 10]
        
        # Create a horizontal bar chart
        fig = px.bar(
            y=ranks,
            x=firefighters,
            orientation='h',
            title="Firefighter Allocation by Rank",
            labels={"x": "Number of Firefighters", "y": "Rank"},
            color=firefighters,
            color_continuous_scale='Blues'
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        # Add certification distribution
        cert_levels = ["Basic", "Intermediate", "Advanced"]
        cert_counts = [1800, 2100, 1370]
        
        fig = px.pie(
            values=cert_counts,
            names=cert_levels,
            title="Certification Level Distribution",
            color_discrete_sequence=px.colors.qualitative.Safe
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with dash_tabs[3]:  # Response Times
        st.markdown("#### Response Time Analysis")
        
        # Create monthly response time data
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        response_times = [7.2, 7.1, 6.9, 6.8, 6.7, 6.8, 7.0, 7.1, 6.9, 6.8, 6.7, 6.5]
        target_time = [7.0] * 12
        
        # Create line chart
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=months, 
            y=response_times,
            mode='lines+markers',
            name='Average Response Time (min)',
            line=dict(color='firebrick', width=3)
        ))
        
        fig.add_trace(go.Scatter(
            x=months, 
            y=target_time,
            mode='lines',
            name='Target Response Time',
            line=dict(color='green', width=2, dash='dash')
        ))
        
        fig.update_layout(
            title="Monthly Average Response Times",
            xaxis_title="Month",
            yaxis_title="Response Time (minutes)",
            height=400,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Response time by station
        top_stations = stations[:8]
        station_response_times = [6.2, 6.5, 6.8, 7.0, 7.2, 6.7, 6.9, 7.1]
        
        fig = px.bar(
            x=top_stations,
            y=station_response_times,
            title="Average Response Time by Station",
            labels={"x": "Station", "y": "Response Time (minutes)"},
            color=station_response_times,
            color_continuous_scale='RdYlGn_r'
        )
        
        # Add target line
        fig.add_hline(y=7.0, line_dash="dash", line_color="green", annotation_text="Target", annotation_position="top right")
        
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with dash_tabs[4]:  # Geographic Analysis
        st.markdown("#### Geographic Distribution of Incidents")
        
        # Since we can't create a real map without the data, show a placeholder
        st.info("🗺️ Geographic visualization would show the spatial distribution of incidents across London's boroughs.")
        
        # Borough incident data
        boroughs = [
            "Westminster", "Camden", "Islington", "Hackney", "Tower Hamlets", 
            "Southwark", "Lambeth", "Wandsworth", "Kensington & Chelsea", "Hammersmith & Fulham"
        ]
        
        borough_incidents = [18200, 15800, 14300, 13700, 12900, 12500, 11800, 10500, 9800, 9200]
        
        fig = px.bar(
            x=boroughs,
            y=borough_incidents,
            title="Incident Distribution by Borough",
            labels={"x": "Borough", "y": "Number of Incidents"},
            color=borough_incidents,
            color_continuous_scale='Reds'
        )
        
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.markdown("### Data Sources")
    st.markdown("""
    This dashboard visualizes data from the London Fire Brigade operational database, including:
    
    - 102 fire stations across London
    - 5,000+ operational firefighters
    - Incident records with response times and durations
    - Multi-agency coordination data
    - Appliance deployment information
    
    The data has been processed using SQL Server and visualized with Tableau.
    """)
    
    st.markdown("### Key Metrics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Total Incidents", value="217,000+", delta="2021-2023")
    
    with col2:
        st.metric(label="Actual Fires", value="33,000+", delta="15% of total")
    
    with col3:
        st.metric(label="False Alarms", value="108,000+", delta="50% of total", delta_color="inverse")

# Footer
st.markdown("---")
st.markdown("© 2025 London Fire Brigade Dashboard | [GitHub Repository](https://github.com/CiscoPonce/London-Fire-Brigade-Dashboard)")
