import streamlit as st
import streamlit.components.v1 as components

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
    
    # Dashboard preview section
    st.markdown("---")
    st.markdown("### Dashboard Preview")
    
    # Dashboard components tabs
    dash_tabs = st.tabs(["Overview", "Station Analysis", "Firefighter Allocation", "Response Times", "Geographic Distribution"])
    
    with dash_tabs[0]:  # Overview tab
        st.markdown("#### Dashboard Overview")
        st.info("📊 This dashboard provides a comprehensive overview of London Fire Brigade operations including station performance, firefighter allocation, and incident distribution.")
        
        # Placeholder metrics until screenshots are added
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Incidents", "217,542", "5.4%")
        with col2:
            st.metric("Response Time", "6:48 min", "-0:42 min")
        with col3:
            st.metric("False Alarms", "108,771", "-2.1%", delta_color="inverse")
        
        st.markdown("##### 📊 Add dashboard screenshots")
        st.info("To improve this preview, add dashboard screenshots to the '/images' folder and update this section.")
    
    with dash_tabs[1]:  # Station Analysis
        st.markdown("#### Station Callouts Analysis")
        st.info("📈 The Station Callouts visualization shows the distribution of genuine incidents across fire stations using a treemap.")
        
        # Sample data table
        st.markdown("##### Top 5 Stations by Incident Count")
        sample_data = {
            "Station": ["Soho", "Lambeth", "Shoreditch", "Euston", "Paddington"],
            "Incidents": [4127, 3954, 3812, 3651, 3520],
            "Change": ["+2.4%", "+1.8%", "-0.7%", "+3.2%", "+0.5%"]
        }
        st.dataframe(sample_data)

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
