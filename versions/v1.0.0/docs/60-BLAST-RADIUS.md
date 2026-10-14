> Versi: v1.0.0 | Status: disetujui | Menggantikan: -

# 60-BLAST-RADIUS — Batas Context (pawonee-data-pipeline)

Mengacu: Pawonee-TownHall `platform/versions/v1.0.0` (https://github.com/Coding-Skuy/Pawonee-TownHall/tree/main/platform/versions/v1.0.0), beku 2026-10-07. Baris Pawonee townhall-roadmap §2: point of concern "12 resep inti; serapan ≥1.500 g"; batas context "G2-V/U/S; porsi 1–8 jiwa; DB `pawonee`; JWT audiens `pawonee`". Rujukan lintas divisi: KONTEKS §8/§9.

## 1. Boleh disentuh repo ini

- `src/` (pipeline, sinyal_pedaree, skema), `config/pipeline.yaml`.
- Tabel `sinyal_pedaree` di DB `pawonee`; membaca `resep`, `profil_keluarga`, `riwayat_masak`.

## 2. Dilarang

- Menulis ke tabel milik Pedaree atau divisi lain.
- Mengubah payload `sinyal.pedaree.v1` tanpa bump versi + beri tahu Pedaree satu siklus rilis.
- Memakai klaim pengguna sebagai serapan.
- Menyentuh DB divisi lain (DB per service; Titeny hanya read-only ke DB sumber).
- Memakai komoditas non-pilot (kentang/wortel/tomat/kol) untuk klaim pasokan agregasi Lumbung; hanya cabai, bawang, kangkung (KONTEKS §4).
- Menambah resep ke-13, mengubah definisi G2, atau mengubah audiens JWT tanpa PR TownHall + ADR.

## 3. Kontrak yang diproduksi

- Topik `sinyal.pedaree.v1` + tabel `sinyal_pedaree` tiap 15 menit.
- Agregat mingguan serapan, rasio, waste, nilai hemat (BRD 30).

## 4. Kontrak yang dikonsumsi

- Tabel `resep`, `profil_keluarga`, `riwayat_masak` dari backend/DB `pawonee`.
- Laporan busuk dari Pedaree (lewat API/event Pedaree).
- Skema bank dari `pawonee-ai-models`.

## 5. Dampak bila berubah

- Perubahan jadwal 15 menit memengaruhi kesegaran sinyal Pedaree.
- Perubahan skema `sinyal_pedaree` memecahkan konsumen Pedaree.

## Batasan

- Dokumen ini hanya memetakan batas dan risiko; tidak mengubah kode atau konfigurasi.
- Keputusan lintas divisi dirujuk ke `KONTEKS-LINTAS-DIVISI.md` dan TownHall Pawonee v1.0.0.
