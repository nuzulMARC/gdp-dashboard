import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
annual_data = pd.read_csv('gdp_annual_real_supply_sub.csv')

# Extract year from the 'Date' column
annual_data['Year'] = pd.to_datetime(annual_data['Date']).dt.year

# Configure Streamlit layout
st.set_page_config(layout="wide")

# Auto-populate categories from the 'Sector Description' column
def extract_categories(data):
    categories = {}
    for description in data['Sector Description'].unique():
        # Use the first word or parent category logic to group sectors
        parent_category = description.split()[0]  # Simple logic to extract category
        if parent_category not in categories:
            categories[parent_category] = []
        categories[parent_category].append(description)
    return categories

categories = extract_categories(annual_data)

# Sidebar Header
st.sidebar.header("Filters")

# Dropdown for Categories (dynamically populated from the dataset)
selected_category = st.sidebar.selectbox(
    "Select Category", 
    options=["All Categories"] + list(categories.keys())
)

# Extract sectors from the selected category
if selected_category == "All Categories":
    sectors = annual_data['Sector Description'].unique()
else:
    sectors = categories[selected_category]

# Multi-select box for Sector Selection
selected_sectors = st.sidebar.multiselect(
    "Select Sectors", 
    options=sectors, 
    default=sectors
)

# Button to Unselect All
if st.sidebar.button("Unselect All"):
    selected_sectors = []  # Clear all selections

# Sidebar - Year Filter (Range Selector)
years = annual_data['Year'].unique()
start_year, end_year = st.sidebar.select_slider(
    "Select Year Range",
    options=sorted(years),
    value=(min(years), max(years))
)

# Sidebar - Value Filter (Range Slider)
value_min = float(annual_data['Value'].min())
value_max = float(annual_data['Value'].max())
value_range = st.sidebar.slider(
    "Select Value Range", 
    min_value=value_min, 
    max_value=value_max, 
    value=(value_min, value_max)
)

# Filter data based on user inputs
filtered_data = annual_data[
    (annual_data['Year'] >= start_year) &
    (annual_data['Year'] <= end_year) &
    (annual_data['Value'] >= value_range[0]) &
    (annual_data['Value'] <= value_range[1]) &
    (annual_data['Sector Description'].isin(selected_sectors))
]

# Aggregate duplicate entries by taking the mean value (or sum)
aggregated_data = filtered_data.groupby(['Sector Description', 'Year'], as_index=False)['Value'].mean()

# Display selected sectors and year range
st.subheader(f"Selected Sectors - Values ({start_year} - {end_year})")

# Line Chart of Values Over Time
fig, ax = plt.subplots(figsize=(10, 5))
for sector in aggregated_data['Sector Description'].unique():
    sector_data = aggregated_data[aggregated_data['Sector Description'] == sector]
    ax.plot(sector_data['Year'], sector_data['Value'], label=sector)
ax.set_xlabel("Year")
ax.set_ylabel("Value")
ax.legend(loc='upper right')
st.pyplot(fig)

# Heatmap of Sector-wise Values
st.subheader("Sector-wise Values Heatmap")
heatmap_data = aggregated_data.pivot(index='Sector Description', columns='Year', values='Value')
fig, ax = plt.subplots(figsize=(10, 5))
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', center=0, ax=ax)
st.pyplot(fig)

# Pie Chart of Sector Proportions
st.subheader("Sector Proportions")
sector_sum = aggregated_data.groupby('Sector Description')['Value'].sum()
fig, ax = plt.subplots()
ax.pie(sector_sum, labels=sector_sum.index, autopct='%1.2f%%', startangle=90)
st.pyplot(fig)
