# Global Industrial Opportunity Radar

## Run locally
pip install -r requirements.txt
python pipeline.py
streamlit run app.py

## What this prototype does
- Aggregates sample opportunity signals from AMQ and SEAO feeds.
- Enriches company/tender records with geography, domain guesses, and language hints.
- Scores opportunities with transparent industry + geography + growth heuristics.
- Detects high-confidence opportunities and serves a Streamlit radar view.

## Scope
The sample dataset now includes opportunities across Canada, Australia, Brazil, Germany, and Indonesia.

## Productionization notes
See `PRODUCTIONIZATION_GAP.md` for a detailed gap assessment and roadmap.
