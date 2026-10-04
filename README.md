# pawonee-data-pipeline

Pipa data Pawonee — **Divisi Pawonee (AI Cooking Assistant)**, org `Coding-Skuy`. Mengumpulkan peristiwa resep/preferensi dan menerbitkan **sinyal untuk Pedaree**. Bagian dari arsitektur **Opsi A ChefGenie**.

- TownHall: [Coding-Skuy/Pawonee-TownHall](https://github.com/Coding-Skuy/Pawonee-TownHall).
- Model peristiwa selaras dengan modul `:shared:pantry-resep` **milik Pawonee** (sumber: `pawonee-app-kmp/shared/pantry-resep`); pipa ini tidak mengubah kontrak modul tersebut.
- Konsumen: **Pedaree** membaca topik keluaran `sinyal.pedaree.v1` sebagai masukan rekomendasi pendampingnya.

## Teknologi (versi dipin)

| Komponen | Versi |
|---|---|
| Python | 3.12.7 |
| Postgres | 16.4 |

## Aliran

```
pawonee-backend-service (tabel resep, preferensi)
  -> src/pipeline.py (ekstrak + validasi skema ai-models)
  -> src/sinyal_pedaree.py (agregat sinyal: resep populer, preferensi umum)
  -> topik `sinyal.pedaree.v1` + tabel `sinyal_pedaree` (src/skema.sql)
```

Jadwal bawaan: tiap 15 menit via `config/pipeline.yaml` (dijalankan scheduler di `pawonee-infra-devops`).

## Cara jalan

```bash
pip install -r requirements.txt
python src/pipeline.py --sekali
```

## Repo terkait

- [pawonee-backend-service](https://github.com/Coding-Skuy/pawonee-backend-service)
- [pawonee-ai-models](https://github.com/Coding-Skuy/pawonee-ai-models)
- [pawonee-infra-devops](https://github.com/Coding-Skuy/pawonee-infra-devops)
