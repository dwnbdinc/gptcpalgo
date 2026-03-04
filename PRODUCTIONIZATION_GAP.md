# Productionization Gap Assessment

This repository is a strong prototype, but several areas should be addressed before production use.

## 1) Data acquisition and reliability
**Current state:** Scraper modules return static, hard-coded sample rows.

**Gaps:**
- No live connectors, pagination handling, retries, or incremental fetch.
- No schema versioning or source freshness metadata.

**Recommended next steps:**
- Integrate real feed collectors (API, RSS, and HTML adapters).
- Add ingestion timestamps, source IDs, and run IDs.
- Persist raw snapshots and normalized bronze/silver datasets.

## 2) Data quality and governance
**Current state:** Minimal cleaning and no explicit validation.

**Gaps:**
- No validation checks (nulls, duplicate entities, malformed geographies).
- No deduplication across fuzzy company names.

**Recommended next steps:**
- Add quality rules with Great Expectations or Pandera.
- Add deterministic entity resolution and duplicate suppression.
- Track quality KPIs (completeness, uniqueness, validity).

## 3) Scoring and opportunity detection
**Current state:** Rule-based heuristics with fixed thresholds.

**Gaps:**
- Static weights and no calibration against outcomes.
- No confidence intervals or model explainability artifacts.

**Recommended next steps:**
- Externalize weights/thresholds to config.
- Backtest scoring using historical conversion outcomes.
- Introduce model registry if moving to ML-based ranking.

## 4) Platform architecture
**Current state:** Local script and CSV storage.

**Gaps:**
- No job scheduler, orchestration, or persistent database.
- No environment-aware configuration management.

**Recommended next steps:**
- Use orchestration (Airflow/Prefect) with daily jobs.
- Store data in Postgres/BigQuery/Snowflake instead of CSV.
- Use `.env` + secret management (Vault/SM/SSM).

## 5) Observability and operations
**Current state:** No structured logging, metrics, or alerting.

**Gaps:**
- Failures are silent unless manually checked.
- No latency/error SLIs or uptime targets.

**Recommended next steps:**
- Add structured JSON logging.
- Export metrics (ingestion count, error rate, freshness lag).
- Add alerting for pipeline failures and stale data.

## 6) Testing and CI/CD
**Current state:** No automated tests or deployment workflow.

**Gaps:**
- Heuristic logic can regress without detection.
- No quality gate before release.

**Recommended next steps:**
- Add unit tests for scoring and opportunity rules.
- Add smoke tests for `pipeline.py` + Streamlit startup.
- Set up GitHub Actions for lint, test, build, and release.

## 7) Security and compliance
**Current state:** No explicit security posture.

**Gaps:**
- No dependency scanning or secrets hygiene enforcement.
- No audit logs for data access.

**Recommended next steps:**
- Add dependency scanning (e.g., pip-audit, Dependabot).
- Add secret scanning and pre-commit checks.
- Define data retention and compliance policies.

## 8) Global expansion readiness
**Current state:** Prototype now includes multi-country sample rows.

**Gaps:**
- No true localization, FX normalization, or timezone alignment.
- Limited taxonomy mapping across regions.

**Recommended next steps:**
- Add standardized country/region codes (ISO 3166).
- Normalize currencies, units, and dates.
- Expand industry taxonomy mapping and translation support.

## Suggested phased roadmap
1. **Foundation (2–4 weeks):** real ingestion, schema validation, persistent storage.
2. **Reliability (2–4 weeks):** orchestration, metrics, alerting, CI/CD tests.
3. **Scale (4–8 weeks):** backtested ranking, localization, market-specific adapters.
