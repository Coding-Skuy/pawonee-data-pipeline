"""Agregat sinyal Pawonee untuk konsumen Pedaree (topik `sinyal.pedaree.v1`)."""

from collections import Counter


def bangun_sinyal(daftar_resep: list) -> dict:
    hitung_bahan = Counter()
    for r in daftar_resep:
        for b in r.get("bahan", []):
            hitung_bahan[b["nama"]] += 1

    populer = sorted(daftar_resep, key=lambda r: r.get("menit", 999))[:5]
    return {
        "topik": "sinyal.pedaree.v1",
        "resepPopuler": [{"id": r["id"], "nama": r["nama"]} for r in populer],
        "bahanTeratas": [{"nama": n, "jumlah": j} for n, j in hitung_bahan.most_common(10)],
        "jumlahResep": len(daftar_resep),
    }
