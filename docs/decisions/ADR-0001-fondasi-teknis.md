# ADR-0001 — Fondasi teknis pawonee-data-pipeline

Status: Diterima | Tanggal: 2026-10-14

## Konteks

Pedaree membutuhkan sinyal resep/preferensi Pawonee yang segar (≤15 menit) dan dapat diaudit. Sumber kebenaran: Pawonee-TownHall `platform/versions/v1.0.0` (https://github.com/Coding-Skuy/Pawonee-TownHall/tree/main/platform/versions/v1.0.0), beku 2026-10-07; lintas divisi: [KONTEKS-LINTAS-DIVISI.md](https://github.com/Coding-Skuy/ChefGenie-TownHall/blob/main/KONTEKS-LINTAS-DIVISI.md). Tiket fondasi: PWN-DATA-001 (issue #1).

## Keputusan

1. Python 3.12 + psycopg 3 untuk pipa; jadwal 15 menit via scheduler di `pawonee-infra-devops`.
2. Kontrak event berversi dengan amplop idempoten (`event_id`, `schema_version`, `source`, `batch_id`) dan retry 3× lalu DLQ (KONTEKS §3).
3. Topik keluaran `sinyal.pedaree.v1` dan tabel `sinyal_pedaree` di DB `pawonee`; Pedaree adalah konsumen tercatat.
4. Agregat serapan dihitung hanya dari `riwayat_masak` (takaran terskala), bukan klaim pengguna; waste dari laporan busuk Pedaree.
5. DB per service: pipa tidak menulis ke DB divisi lain; Titeny hanya read-only.

## Konsekuensi

- Perubahan jadwal mengubah kesegaran sinyal Pedaree; harus diumumkan satu siklus rilis sebelumnya.
- Event Pawonee (`rekomendasi.dihitung`, `resep.dimasak`, `serapan.dihitung`, `profil.disimpan`, `sinyal.diterbitkan`) belum terdaftar di registry Titeny (11 event); pendaftaran perlu keputusan TownHall.
- Tabel `sinyal_pedaree` menjadi kontrak data; perubahan kolom butuh migrasi dan ADR.
