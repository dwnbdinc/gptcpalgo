from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, List

import pandas as pd


@dataclass(frozen=True)
class SourceSpec:
    key: str
    label: str
    kind: str  # "seed" | "registry" | "procurement" | "directory"
    rank: int  # lower = better quality (overrides higher rank)
    enabled: bool
    scraper: Callable[[], pd.DataFrame]


def get_sources() -> List[SourceSpec]:
    """
    Add new sources here.
    rank rules (suggested):
      0-19: authoritative registries (gov/associations)
      20-49: reputable industry directories
      50-79: broad business directories
      80-99: seed/synthetic/bootstrap lists
    """
    # Local imports so sources can be optional without breaking import time
    from sources_seed import scrape_seed_global_1000
    from sources_amq import scrape_amq_source
    from sources_seao import scrape_seao_source

    return [
        SourceSpec(
            key="amq",
            label="Quebec Mining Association",
            kind="registry",
            rank=10,
            enabled=True,
            scraper=scrape_amq_source,
        ),
        SourceSpec(
            key="seao",
            label="SEAO Procurement",
            kind="procurement",
            rank=15,
            enabled=True,
            scraper=scrape_seao_source,
        ),
        SourceSpec(
            key="seed_global_1000",
            label="Global Seed 1000",
            kind="seed",
            rank=90,
            enabled=True,
            scraper=scrape_seed_global_1000,
        ),
    ]
