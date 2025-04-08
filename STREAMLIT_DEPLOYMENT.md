# Streamlit Deployment Guide

This guide explains how to deploy your London Fire Brigade Dashboard using Streamlit.

## Local Testing

1. **Install Requirements**
   ```
   pip install -r requirements.txt
   ```

2. **Run the App Locally**
   ```
   streamlit run app.py
   ```

3. **View in Browser**
   The app will automatically open in your default browser, typically at http://localhost:8501

## Deployment to Streamlit Cloud

1. **Publish your Tableau Dashboard to Tableau Public**
   - Open your Tableau workbook in Tableau Desktop
   - Go to Server → Tableau Public → Save to Tableau Public
   - Follow the prompts to create/sign into your Tableau Public account
   - Make note of the public URL for your dashboard

2. **Update the app.py file**
   - Replace the placeholder Tableau URL with your actual Tableau Public URL:
   ```python
   tableau_url = "https://public.tableau.com/views/YourActualDashboardURL/Dashboard"
   ```

3. **Deploy to Streamlit Cloud**
   - Go to [Streamlit Cloud](https://streamlit.io/cloud)
   - Sign in with your GitHub account
   - Select your repository and branch
   - Specify the entry point: `app.py`
   - Deploy!

4. **Update Your GitHub README**
   - Add the Streamlit Cloud URL to your README.md for easy access

## Customization Options

- **Appearance**: Customize the app's appearance in the `st.set_page_config()` function
- **Content**: Add more tabs, text, or interactive elements as needed
- **Layout**: Adjust the layout using Streamlit's column and container functions

## Troubleshooting

- If your Tableau embed doesn't display, check that the URL is correct and the dashboard is set to public
- For local testing issues, ensure all dependencies are installed
- For deployment issues, check the Streamlit Cloud logs
