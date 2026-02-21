CREATE TABLE "vessels" (
  "vessel_id" INTEGER PRIMARY KEY,
  "imo" TEXT,
  "name" TEXT,
  "type" TEXT
);

CREATE TABLE "ports" (
  "port_id" INTEGER PRIMARY KEY,
  "name" TEXT,
  "lat" REAL,
  "lon" REAL
);

CREATE TABLE "ais_data" (
  "ais_id" INTEGER PRIMARY KEY,
  "vessel_id" INTEGER,
  "port_id" INTEGER,
  "timestamp" TIMESTAMP,
  "lat" REAL,
  "lon" REAL,
  "speed" REAL,
  "heading" REAL
);

CREATE TABLE "weather_data" (
  "weather_id" INTEGER PRIMARY KEY,
  "port_id" INTEGER,
  "timestamp" TIMESTAMP,
  "temp" REAL,
  "wind_speed" REAL,
  "wave_height" REAL,
  "visibility" REAL
);

CREATE TABLE "maintenance_events" (
  "maintenance_id" INTEGER PRIMARY KEY,
  "vessel_id" INTEGER,
  "port_id" INTEGER,
  "event_type" TEXT,
  "start_date" TIMESTAMP,
  "end_date" TIMESTAMP,
  "status" TEXT
);

ALTER TABLE "ais_data" ADD FOREIGN KEY ("vessel_id") REFERENCES "vessels" ("vessel_id");

ALTER TABLE "ais_data" ADD FOREIGN KEY ("port_id") REFERENCES "ports" ("port_id");

ALTER TABLE "weather_data" ADD FOREIGN KEY ("port_id") REFERENCES "ports" ("port_id");

ALTER TABLE "maintenance_events" ADD FOREIGN KEY ("vessel_id") REFERENCES "vessels" ("vessel_id");

ALTER TABLE "maintenance_events" ADD FOREIGN KEY ("port_id") REFERENCES "ports" ("port_id");
