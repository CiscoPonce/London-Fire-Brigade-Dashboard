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
    
    # Display the published Tableau dashboard
    st.success("London Fire Brigade Operations Dashboard")
    
    # Tableau Public URL for the dashboard
    tableau_url = "https://public.tableau.com/app/profile/cisco.ponce/viz/LondonFireBrigadeOperationsDashboard-March2025/LondonFireBrigadeOperationsDashboard-March2025"
    
    # Display the dashboard in an iframe
    st.markdown("""
    ### London Fire Brigade Operations Dashboard
    Below is the interactive dashboard published on Tableau Public showing the London Fire Brigade operations data.
    You can interact with the visualizations directly in this window.
    """)
    
    # Insert the Tableau Public dashboard using iframe
    components.iframe(
        src=tableau_url,
        height=800,
        scrolling=True,
        width=None
    )
    
    # Display download links for local files
    st.markdown("---")
    st.markdown("### Download Dashboard Files")
    st.markdown("You can download the Tableau workbook files from the repository:")
    
    # Create columns for the two workbooks
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Packaged Workbook (TWBX)")
        st.markdown("`tableau/Final.twbx`")
        st.markdown("This packaged workbook contains the dashboard visualizations and embedded data.")
        st.download_button(
            label="Download TWBX File",
            data=open("tableau/Final.twbx", "rb"),
            file_name="Final.twbx",
            mime="application/octet-stream"
        )
    
    with col2:
        st.markdown("#### Dashboard Workbook (TWB)")
        st.markdown("`tableau/London Fire Brigade Operations Dashboard - March 2025.twb`")
        st.markdown("This is the Tableau workbook file containing the dashboard design.")
        st.download_button(
            label="Download TWB File",
            data=open("tableau/London Fire Brigade Operations Dashboard - March 2025.twb", "rb"),
            file_name="LFB_Dashboard.twb",
            mime="application/octet-stream"
        )

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
