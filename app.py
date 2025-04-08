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

# Dashboard content
st.markdown("### London Fire Brigade Dashboard")

# Display the published Tableau dashboard
st.success("London Fire Brigade Operations Dashboard")

# Tableau Public URL for the dashboard
tableau_url = "https://public.tableau.com/views/LondonFireBrigadeOperationsDashboard-March2025/LondonFireBrigadeOperationsDashboard-March2025?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"

# Display the dashboard information
st.markdown("""
### London Fire Brigade Operations Dashboard
Below is the interactive dashboard published on Tableau Public showing the London Fire Brigade operations data.
You can interact with the visualizations directly in this window.
""")

# Insert the Tableau Public dashboard using the official embed code
tableau_html = '''
<div class='tableauPlaceholder' id='viz1744131858257' style='position: relative'>
    <noscript>
        <a href='#'>
            <img alt='London Fire Brigade Operations Dashboard - March 2025 ' src='https://public.tableau.com/static/images/Lo/LondonFireBrigadeOperationsDashboard-March2025/LondonFireBrigadeOperationsDashboard-March2025/1_rss.png' style='border: none' />
        </a>
    </noscript>
    <object class='tableauViz' style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
        <param name='embed_code_version' value='3' /> 
        <param name='site_root' value='' />
        <param name='name' value='LondonFireBrigadeOperationsDashboard-March2025/LondonFireBrigadeOperationsDashboard-March2025' />
        <param name='tabs' value='no' />
        <param name='toolbar' value='yes' />
        <param name='static_image' value='https://public.tableau.com/static/images/Lo/LondonFireBrigadeOperationsDashboard-March2025/LondonFireBrigadeOperationsDashboard-March2025/1.png' /> 
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='en-US' />
    </object>
</div>
<script type='text/javascript'>
    var divElement = document.getElementById('viz1744131858257');
    var vizElement = divElement.getElementsByTagName('object')[0];
    // Set fixed dimensions to ensure full dashboard visibility
    vizElement.style.width='100%';
    vizElement.style.height='1600px'; // Increased fixed height to show entire dashboard
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>
'''

# Use a larger height and set scrolling to false to see the whole dashboard
st.components.v1.html(tableau_html, height=1200, scrolling=False)

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

# Footer
st.markdown("---")
st.markdown("© 2025 London Fire Brigade Dashboard | [GitHub Repository](https://github.com/CiscoPonce/London-Fire-Brigade-Dashboard)")
