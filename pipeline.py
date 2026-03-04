import pandas as pd

from amq_scraper import scrape_amq
from seao_scraper import scrape_seao
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


def run():
    df = pd.concat([scrape_amq(), scrape_seao()], ignore_index=True)
    df = df.drop_duplicates(subset=["name", "country", "source"])

    df = enrich(df)
    df = detect_growth(df)
    df = score(df)

    df["context"] = df.apply(build_context, axis=1)
    df["opportunity"] = df.apply(opportunity_angle, axis=1)
    df["summary"] = df.apply(generate_summary, axis=1)
    df["suggested_roles"] = df["industry"].apply(suggest_contacts)

    df = df.sort_values(by="lead_score", ascending=False).reset_index(drop=True)
    df.to_csv("data/companies.csv", index=False)

    events = detect_opportunities(df)
    build_event_table(events).to_csv("data/opportunities.csv", index=False)

    queue = build_research_queue(df)
    queue.to_csv("data/research_queue.csv", index=False)


if __name__ == "__main__":
    run()
