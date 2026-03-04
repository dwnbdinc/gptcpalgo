import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("🇨🇦 Industrial Opportunity Radar")

companies=pd.read_csv("data/companies.csv")
opps=pd.read_csv("data/opportunities.csv")

tab1,tab2=st.tabs(["Companies","🚨 Opportunity Radar"])

with tab1:

    st.metric("Companies",len(companies))
    st.dataframe(companies,use_container_width=True)

    csv=companies.to_csv(index=False).encode()
    st.download_button("Export CSV",csv,"companies.csv")

with tab2:

    st.header("Detected Opportunities")

    for _,e in opps.iterrows():
        with st.expander(f"🚨 {e['company']}"):
            st.write("Industry:",e["industry"])
            st.write("Confidence:",e["confidence"])
            st.write("Signals:",e["reasons"])
            st.write("Opportunity:",e["opportunity"])
