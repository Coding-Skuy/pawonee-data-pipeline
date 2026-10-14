> Versi: v1.0.0 | Status: disetujui | Menggantikan: -

# 40-TECHSTACK — Tumpukan Teknologi (pawonee-data-pipeline)

Mengacu: Pawonee-TownHall `platform/versions/v1.0.0` (https://github.com/Coding-Skuy/Pawonee-TownHall/tree/main/platform/versions/v1.0.0), beku 2026-10-07. Tidak menduplikasi BRD/PRD/FRD/FSD/SRS; hanya mengunci stack repo ini.

## 1. Matriks stack

| Komponen | Kondisi saat ini (tercatat) | Target terkunci v1.0.0 |
|---|---|---|
| Python | 3.12.7 | 3.12.x (pin eksak saat kickoff) |
| Driver DB | psycopg[binary] 3.2.1 | psycopg 3.x |
| Postgres | 16.4 | 16.x, DB logis `pawonee` |
| Jadwal | `config/pipeline.yaml` (15 menit) | 15 menit via scheduler infra |
| Kontrak | skema SQL `src/skema.sql` | Event berversi + amplop idempoten (KONTEKS §3) |



## Batasan

- Dokumen ini tidak mengubah manifes atau kode; kondisi saat ini dicatat apa adanya dari manifes/README repo.
- Versi dikunci eksak di manifes saat kickoff coding; perubahan versi dicatat di dokumen ini lewat versi dokumen berikutnya dan ADR baru.
- JWT audiens `pawonee`, DB logis `pawonee`, dan `:shared:pantry-resep` milik Pawonee tidak berubah oleh dokumen ini.
