from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Literal

EvidenceLevel = Literal["background", "supports", "mixed", "against", "needs_check"]

@dataclass
class EvidenceEdge:
    claim_id: str
    paper_id: str
    relation: EvidenceLevel
    note: str = ""

def toy_map() -> dict:
    return {
        "claims": [{"id":"C1", "text":"Public metadata can support transparent first-pass triage."}],
        "papers": [{"id":"P1", "title":"Toy public metadata record", "source":"toy"}],
        "edges": [asdict(EvidenceEdge("C1", "P1", "supports", "toy example only"))],
    }
