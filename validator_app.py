import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import io

# 1. Page Configuration
st.set_page_config(page_title="Professional Data Quality Validator", layout="wide")

st.title(" Data Quality Validator")
st.markdown("---")

# 2. Sidebar - File Upload
st.sidebar.header("1. Upload Data")
uploaded_file = st.sidebar.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])

if uploaded_file:
    # Load Data
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # --- MAIN DASHBOARD METRICS ---
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Rows", df.shape[0])
    with col2:
        st.metric("Total Columns", df.shape[1])
    with col3:
        total_nulls = df.isnull().sum().sum()
        st.metric("Missing Values", total_nulls, delta="- Issues" if total_nulls > 0 else "Clean", delta_color="inverse")
    with col4:
        total_dupes = df.duplicated().sum()
        st.metric("Duplicate Rows", total_dupes, delta="- Issues" if total_dupes > 0 else "Clean", delta_color="inverse")

    # --- TABS SYSTEM ---
    tab_table, tab_quality, tab_viz, tab_map, tab_clean = st.tabs([
        " Interactive Table", " Quality Analysis", " Visual Charts", " Geospatial Map", " Data Cleaning"
    ])

    # TAB 1: INTERACTIVE TABLE
    with tab_table:
        st.subheader("Explore Your Dataset")
        st.dataframe(df, use_container_width=True)
        
    # TAB 2: QUALITY ANALYSIS
    with tab_quality:
        col_q1, col_q2 = st.columns(2)
        
        with col_q1:
            st.write("### Missing Values Per Column")
            missing_df = df.isnull().sum().reset_index()
            missing_df.columns = ['Column', 'Missing Count']
            st.bar_chart(missing_df.set_index('Column'))

        with col_q2:
            st.write("### Data Type Health")
            st.write(df.dtypes.to_frame(name='Data Type'))

        st.markdown("---")
        st.write("###  Outlier Detection (Numerical)")
        num_cols = df.select_dtypes(include=[np.number]).columns
        if len(num_cols) > 0:
            selected_col = st.selectbox("Select Column to Check Outliers", num_cols)
            # Z-Score Logic
            z_scores = (df[selected_col] - df[selected_col].mean()) / df[selected_col].std()
            outliers = df[np.abs(z_scores) > 3]
            st.write(f"Found {len(outliers)} outliers in `{selected_col}`")
            st.dataframe(outliers)
        else:
            st.info("No numerical columns found for outlier detection.")

    # TAB 3: VISUAL CHARTS (The "Heatmap" Section)
    # TAB 3: VISUAL CHARTS
    with tab_viz:
        st.subheader("Data Visualization")
        
        viz_col1, viz_col2 = st.columns(2)
        
        with viz_col1:
            st.write("### Missing Value Heatmap")
            fig, ax = plt.subplots(figsize=(10, 8)) # Increased height
            sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis', ax=ax)
            plt.xticks(rotation=45, ha='right') # Rotate column names
            st.pyplot(fig)
            st.caption("Yellow lines indicate missing data.")

        with viz_col2:
            st.write("### Feature Correlation")
            numeric_only = df.select_dtypes(include=[np.number])
            if not numeric_only.empty:
                # FIX: Increase figure size to give numbers more room
                fig_corr, ax_corr = plt.subplots(figsize=(12, 10)) 
                
                # FIX: Use fmt=".2f" for 2 decimals and smaller font size (annot_kws)
                sns.heatmap(
                    numeric_only.corr(), 
                    annot=True, 
                    fmt=".2f",           # Limit to 2 decimal places
                    annot_kws={"size": 8}, # Make the numbers smaller
                    cmap='RdBu', 
                    ax=ax_corr,
                    linewidths=0.5       # Add thin lines between boxes
                )
                
                # FIX: Rotate labels so they don't overlap
                plt.xticks(rotation=45, ha='right')
                plt.yticks(rotation=0)
                
                st.pyplot(fig_corr)
            else:
                st.warning("Not enough numeric data for correlation.")

        st.markdown("---")
        st.write("### Interactive Distribution Plot")
        if len(num_cols) > 0:
            dist_col = st.selectbox("Select column to see distribution", num_cols, key="dist")
            fig_dist = px.histogram(df, x=dist_col, marginal="box", nbins=50, title=f"Distribution of {dist_col}")
            st.plotly_chart(fig_dist, use_container_width=True)

    # TAB 4: GEOSPATIAL MAP
    with tab_map:
        st.subheader("Geospatial Visualization")
        # Logic: Look for columns that might be Lat/Lon
        lat_cols = [c for c in df.columns if c.lower() in ['lat', 'latitude', 'latit']]
        lon_cols = [c for c in df.columns if c.lower() in ['lon', 'longitude', 'long']]
        
        if lat_cols and lon_cols:
            map_df = df[[lat_cols[0], lon_cols[0]]].dropna()
            map_df.columns = ['lat', 'lon'] # Streamlit requires these exact names
            st.write(f"Found coordinates in `{lat_cols[0]}` and `{lon_cols[0]}`")
            st.map(map_df)
        else:
            st.info("No Latitude/Longitude columns found (e.g., 'lat', 'lon').")

    # TAB 5: DATA CLEANING
    with tab_clean:
        st.subheader("One-Click Fixes")
        
        c_fix1, c_fix2, c_fix3 = st.columns(3)
        
        processed_df = df.copy()

        with c_fix1:
            if st.button("Drop Duplicate Rows"):
                processed_df = processed_df.drop_duplicates()
                st.success("Duplicates Dropped!")

        with c_fix2:
            if st.button("Fill Missing with Mean"):
                for col in processed_df.select_dtypes(include=[np.number]):
                    processed_df[col] = processed_df[col].fillna(processed_df[col].mean())
                st.success("Numeric Missing Values Filled!")

        with c_fix3:
            if st.button("Drop Rows with Any Missing"):
                processed_df = processed_df.dropna()
                st.success("Rows with missing data removed!")

        st.markdown("---")
        st.subheader("Download Results")
        csv = processed_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Cleaned Dataset",
            data=csv,
            file_name="cleaned_data.csv",
            mime="text/csv"
        )

else:
    # Landing Page
   
    st.info(" Please upload a dataset in the sidebar to start the validation.")