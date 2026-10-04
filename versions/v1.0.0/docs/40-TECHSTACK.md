> Versi: v1.0.0 | Status: disetujui | Menggantikan: -

# 40-TECHSTACK — Tumpukan Teknologi (pawonee-data-pipeline)

Mengacu: Pawonee-TownHall v1.0.0 (https://github.com/Coding-Skuy/Pawonee-TownHall).

## 1. Kondisi saat ini (tercatat)

- Python 3.12.7, psycopg 3.2.1, Postgres 16.4 (sumber: `requirements.txt`, `README.md`).

## 2. Target standar emas (rencana)

- Python 3.12 (patch terbaru), psycopg 3.x terbaru, Postgres 16.x terbaru.
- Selaras divisi: KMP Kotlin 2.2.20 dan Compose 1.8.2 dan nav3 1.0.0; Rust axum 0.8.4; Python 3.12; web SvelteKit dan Bun terbaru; Postgres 16.x; database `pawonee`; JWT audiens `pawonee`.

## 3. Langkah penyesuaian (rencana — bukan eksekusi sekarang)

1. Kunci versi eksak pada `requirements.txt` saat fase coding dimulai.
2. Selaraskan matriks `VERSIONS.md` di `pawonee-infra-devops` setelah fase coding dimulai.
3. Jalankan pemeriksaan bangun sinyal sebelum menaikkan versi.
4. Catat perubahan versi pada dokumen ini dan TownHall Pawonee-TownHall v1.0.0.

## Batasan

- Dokumen versi ini tidak mengubah manifes, kode, atau versi terpasang; semua target adalah rencana.
- Tidak ada migrasi framework atau kenaikan versi dalam dokumen ini.
- Model tetap mengikuti `:shared:pantry-resep` milik Pawonee; tidak ada duplikasi model baru.
- Perencanaan BRD, PRD, FSD, dan roadmap repo ini mengacu Pawonee-TownHall v1.0.0 dan tidak diduplikasi di sini.
