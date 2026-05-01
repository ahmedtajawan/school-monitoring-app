import streamlit as st
import pandas as pd

st.set_page_config(page_title="School Monitoring Dashboard", layout="wide")

st.title("📊 School Monitoring Dashboard")

st.write("Upload your monthly Excel file")

file = st.file_uploader("Upload Excel", type=["xlsx"])

if file:
    df = pd.read_excel(file)

    df.columns = df.columns.str.strip()

    st.write("Columns detected:", df.columns.tolist())

    # Sidebar
    st.sidebar.header("Filters")
    monitor = st.sidebar.selectbox("Select Monitor", df['Monitor Name'].unique())

    my_data = df[df['Monitor Name'] == monitor]

    col1, col2 = st.columns(2)
    col1.metric("Total Assignments", len(my_data))
    col2.metric("Unique Schools", my_data['EMIS Code'].nunique())

    st.subheader("Workload Comparison")
    workload = df.groupby('Monitor Name')['EMIS Code'].count()
    st.bar_chart(workload)

    st.subheader("Your Data")
    st.dataframe(my_data)
