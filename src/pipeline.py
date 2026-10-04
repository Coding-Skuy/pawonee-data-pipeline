"""Orkestrasi pipa Pawonee: ekstrak peristiwa resep lalu terbitkan sinyal Pedaree."""

import argparse
import json
from pathlib import Path

from sinyal_pedaree import bangun_sinyal

DASAR = Path(__file__).resolve().parent.parent


def ekstrak_contoh() -> dict:
    bank = json.loads((DASAR / ".." / "pawonee-ai-models" / "models" / "bank_resep_grade2.json").read_text()) \
        if (DASAR / ".." / "pawonee-ai-models" / "models" / "bank_resep_grade2.json").exists() \
        else {"resep": []}
    return bank


def main(sekali: bool) -> None:
    bank = ekstrak_contoh()
    sinyal = bangun_sinyal(bank.get("resep", []))
    print(json.dumps(sinyal, indent=2, ensure_ascii=False))
    if sekali:
        print(f"Selesai sekali jalan: {len(sinyal['resepPopuler'])} resep populer diterbitkan.")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--sekali", action="store_true")
    args = p.parse_args()
    main(args.sekali)
