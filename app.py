import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("⚡ Industrial Outbound Lead OS")

companies = pd.read_csv("data/companies.csv")
opps = pd.read_csv("data/opportunities.csv")
queue = pd.read_csv("data/research_queue.csv")

tab1, tab2, tab3 = st.tabs(
    ["🧭 Research Queue", "⚡ Opportunities", "🏢 All Companies"]
)

with tab1:
    st.header("Today's Research Queue")

    for _, row in queue.iterrows():
        with st.expander(row["name"]):
            st.write("Industry:", row["industry"])
            st.write("Score:", row["lead_score"])
            st.write("Growth Signal:", row["growth_signal"])

            st.write("Suggested Roles:")
            st.write(row["suggested_roles"])

with tab2:
    st.header("Opportunity Radar")

    for _, e in opps.iterrows():
        with st.expander(e["company"]):
            st.write("Industry:", e["industry"])
            st.write("Signals:", e["reasons"])
            st.write("Opportunity:", e["opportunity"])

with tab3:
    st.dataframe(companies, use_container_width=True)

    csv = companies.to_csv(index=False).encode()

    st.download_button(
        "Export CSV",
        csv,
        "companies.csv"
    )
