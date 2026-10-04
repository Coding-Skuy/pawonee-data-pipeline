-- Tabel keluaran pipa Pawonee untuk konsumen Pedaree.

CREATE TABLE IF NOT EXISTS sinyal_pedaree (
    id BIGSERIAL PRIMARY KEY,
    topik TEXT NOT NULL DEFAULT 'sinyal.pedaree.v1',
    muatan JSONB NOT NULL,
    dibuat_pada TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_sinyal_pedaree_waktu ON sinyal_pedaree (dibuat_pada DESC);
