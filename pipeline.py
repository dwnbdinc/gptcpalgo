from collector import collect_companies

from enrichment import enrich
from growth_signals import detect_growth
from scoring import score
from intelligence import build_context
from opportunity_engine import opportunity_angle
from summaries import generate_summary

from radar_engine import detect_opportunities
from events import build_event_table

from research_queue import build_research_queue
from account_mapper import suggest_contacts

from history import append_signals_log


FOCUSED_INDUSTRIES = {
    "Energy",
    "Mining",
    "Engineering",
    "Infrastructure",
}


def run():
    df = collect_companies()

    # Keep only industrially relevant accounts.
    df = df[df["industry"].isin(FOCUSED_INDUSTRIES)].copy()

    # Keep one canonical row per company-country pair.
    df.drop_duplicates(subset=["name", "country"], inplace=True)

    df = enrich(df)
    df = detect_growth(df)
    df = score(df)

    df["context"] = df.apply(build_context, axis=1)
    df["opportunity"] = df.apply(opportunity_angle, axis=1)
    df["summary"] = df.apply(generate_summary, axis=1)

    # Phase-6 account mapping
    df["suggested_roles"] = df["industry"].apply(suggest_contacts)

    # Save companies snapshot
    df.to_csv("data/companies.csv", index=False)

    # Phase-5 radar
    events = detect_opportunities(df)
    build_event_table(events).to_csv("data/opportunities.csv", index=False)

    # Phase-6 queue
    queue = build_research_queue(df)
    queue.to_csv("data/research_queue.csv", index=False)

    # Phase-7 history log
    append_signals_log(df)


if __name__ == "__main__":
    run()
