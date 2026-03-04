import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

st.title("🌍 Industrial Opportunity Radar")

companies = pd.read_csv("data/companies.csv")
opps = pd.read_csv("data/opportunities.csv")

tab1, tab2 = st.tabs(["Companies", "🚨 Opportunity Radar"])

with tab1:
    st.metric("Companies", len(companies))
    st.metric("Countries", companies["country"].nunique())
    st.dataframe(companies, width="stretch")

    csv = companies.to_csv(index=False).encode()
    st.download_button("Export CSV", csv, "companies.csv")

with tab2:
    st.header("Detected Opportunities")

    for _, event in opps.iterrows():
        with st.expander(f"🚨 {event['company']} ({event['country']})"):
            st.write("Industry:", event["industry"])
            st.write("Region:", event["region"])
            st.write("Confidence:", event["confidence"])
            st.write("Signals:", event["reasons"])
            st.write("Opportunity:", event["opportunity"])
