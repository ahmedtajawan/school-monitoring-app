import streamlit as st
import pandas as pd

st.title("📊 Monthly School Assignment Analysis")

# ---- LOAD DATA ----
url = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/roaster_assignment.csv"

@st.cache_data
def load_data(url):
    return pd.read_csv(url)

df = load_data(url)

# Clean columns
df.columns = df.columns.str.strip()

# ---- FILTER: MALE ASSIGNMENTS ----
male_df = df[df['Gender'] == 'Boys']

# ---- PIVOT TABLE ----
st.subheader("👨 Male Monitor Assignments (Boys Schools)")

pivot = (
    male_df.groupby('Monitor Name')['EMIS Code']
    .nunique()
    .reset_index()
    .rename(columns={'EMIS Code': 'Total Schools'})
    .sort_values(by='Total Schools', ascending=False)
)

# Add ranking
pivot['Rank'] = pivot['Total Schools'].rank(ascending=False, method='dense')

st.dataframe(pivot)

# ---- BAR CHART ----
st.subheader("📊 Workload Distribution (Male Monitors)")
st.bar_chart(pivot.set_index('Monitor Name'))
