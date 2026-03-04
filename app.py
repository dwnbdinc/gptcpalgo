import streamlit as st
import pandas as pd

from history import load_signals_log, company_timeline
from heat import heating_up_accounts
from watchlist import load_watchlist_from_upload, apply_watchlist_filter, empty_watchlist

st.set_page_config(layout="wide")
st.title("⚡ Industrial Outbound Lead OS")

companies = pd.read_csv("data/companies.csv")
opps = pd.read_csv("data/opportunities.csv")
queue = pd.read_csv("data/research_queue.csv")
log_df = load_signals_log()

st.sidebar.header("Controls")

watchlist_upload = st.sidebar.file_uploader("Upload watchlist CSV", type=["csv"])
watchlist_df = load_watchlist_from_upload(watchlist_upload)

use_watchlist = st.sidebar.checkbox("Filter by watchlist", value=False)
if use_watchlist and not watchlist_df.empty:
    companies = apply_watchlist_filter(companies, watchlist_df)
    queue = apply_watchlist_filter(queue, watchlist_df)

min_score = st.sidebar.slider("Minimum lead score", 0, 100, 0)
companies = companies[companies["lead_score"] >= min_score]
queue = queue[queue["lead_score"] >= min_score]

tabs = st.tabs([
    "🧭 Research Queue",
    "🔥 Heating Up",
    "📈 Timelines",
    "⭐ Watchlist",
    "🚨 Opportunity Radar",
    "🏢 All Companies"
])

# 1) Research Queue
with tabs[0]:
    st.header("Today's Research Queue")

    st.caption("Top accounts to research today. Click to see role hypotheses and context.")
    for _, row in queue.iterrows():
        with st.expander(row["name"]):
            st.write("Industry:", row.get("industry", ""))
            st.write("Province:", row.get("province", ""))
            st.write("Lead score:", row.get("lead_score", ""))
            st.write("Growth signal:", row.get("growth_signal", ""))

            st.write("Suggested roles:")
            st.write(row.get("suggested_roles", ""))

            st.write("Context:")
            st.write(row.get("context", ""))

            st.write("Opportunity angle:")
            st.write(row.get("opportunity", ""))

# 2) Heating Up
with tabs[1]:
    st.header("Heating Up Accounts")
    st.caption("Biggest movers since the last nightly run, based on score and growth deltas.")

    heat_df = heating_up_accounts(log_df, top_n=30)
    if heat_df.empty:
        st.info("Not enough history yet. This view activates after at least 2 nightly runs.")
    else:
        st.dataframe(heat_df, use_container_width=True)
        csv = heat_df.to_csv(index=False).encode("utf-8")
        st.download_button("Export heating up CSV", csv, "heating_up.csv", "text/csv")

# 3) Timelines
with tabs[2]:
    st.header("Company Timelines")
    st.caption("Select a company to see how its signals and score change over time.")

    company_names = sorted(log_df["name"].dropna().unique().tolist()) if not log_df.empty else []
    if not company_names:
        st.info("No timeline data yet. It will appear after the first nightly run logs signals.")
    else:
        selected = st.selectbox("Company", company_names)
        tdf = company_timeline(log_df, selected)

        if tdf.empty:
            st.info("No timeline rows found for this company.")
        else:
            st.dataframe(tdf[[
                "run_date", "lead_score", "growth_signal", "industry", "source", "opportunity", "context"
            ]], use_container_width=True)

            # Simple chart using Streamlit built-in
            chart_df = tdf[["run_date", "lead_score", "growth_signal"]].copy()
            chart_df = chart_df.set_index("run_date")
            st.line_chart(chart_df)

            csv = tdf.to_csv(index=False).encode("utf-8")
            st.download_button("Export timeline CSV", csv, f"{selected}_timeline.csv", "text/csv")

# 4) Watchlist
with tabs[3]:
    st.header("Watchlist")
    st.caption("Upload a watchlist CSV to focus the tool. You can export a template, edit it locally, and re-upload.")

    template = empty_watchlist()
    tpl_csv = template.to_csv(index=False).encode("utf-8")
    st.download_button("Download watchlist template CSV", tpl_csv, "watchlist_template.csv", "text/csv")

    if watchlist_df.empty:
        st.info("No watchlist uploaded. Upload one to enable filtering.")
    else:
        st.success(f"Watchlist loaded: {len(watchlist_df)} accounts")
        st.dataframe(watchlist_df, use_container_width=True)

# 5) Opportunity Radar
with tabs[4]:
    st.header("Opportunity Radar")
    if opps.empty:
        st.info("No opportunities detected in the current dataset.")
    else:
        for _, e in opps.iterrows():
            with st.expander(f"🚨 {e['company']}"):
                st.write("Industry:", e.get("industry", ""))
                st.write("Confidence:", e.get("confidence", ""))
                st.write("Signals:", e.get("reasons", ""))
                st.write("Opportunity:", e.get("opportunity", ""))

# 6) All Companies + Export
with tabs[5]:
    st.header("All Companies")
    st.dataframe(companies, use_container_width=True)

    csv = companies.to_csv(index=False).encode("utf-8")
    st.download_button("Export companies CSV", csv, "companies.csv", "text/csv")
