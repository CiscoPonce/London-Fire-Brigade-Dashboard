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
    st.markdown("### Full Interactive Dashboard")
    st.warning("To display the actual dashboard, publish your Tableau workbook to Tableau Public and replace the URL below.")
    
    # Your Tableau Public profile
    profile_url = "https://public.tableau.com/app/profile/cisco.ponce/vizzes"
    
    # When you publish your London Fire Brigade dashboard, replace this URL with the specific dashboard URL
    # For example: "https://public.tableau.com/views/LondonFireBrigade/Dashboard"
    dashboard_url = ""
    
    if dashboard_url:
        # Display the specific dashboard if URL is provided
        st.success("Showing your London Fire Brigade Dashboard")
        components.iframe(
            src=dashboard_url,
            height=800,
            scrolling=True
        )
    else:
        # Display the profile page if no specific dashboard URL is provided yet
        st.info("Please publish your London Fire Brigade dashboard to Tableau Public and update the URL in app.py")
        st.markdown(f"[View your Tableau Public Profile]({profile_url})")
        components.iframe(
            src=profile_url,
            height=800,
            scrolling=True
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
