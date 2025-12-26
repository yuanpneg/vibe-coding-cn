---
name: timescaledb
description: Manage time-series data in PostgreSQL with TimescaleDB. Use this skill to install, configure, optimize, and interact with TimescaleDB for high-performance time-series data storage and analysis. This includes creating hypertables, continuous aggregates, handling data retention, and querying time-series data efficiently.
---

# TimescaleDB Skill

Manage time-series data in PostgreSQL using TimescaleDB, extending PostgreSQL for high-performance time-series workloads.

## When to Use This Skill

Use this skill when you need to:
- Work with time-series data in PostgreSQL
- Install and configure TimescaleDB
- Create and manage hypertables
- Optimize performance for time-series data
- Implement continuous aggregates for rollup data
- Manage data retention and compression
- Query and analyze time-series data
- Migrate existing PostgreSQL tables to hypertables
- Integrate with other PostgreSQL tools and extensions

## Not For / Boundaries

This skill is NOT for:
- General PostgreSQL administration (use a specific PostgreSQL skill for that)
- Deep database tuning unrelated to time-series performance
- Replacing dedicated time-series databases if TimescaleDB's PostgreSQL foundation is not a requirement
- Providing data visualization beyond basic SQL queries (use a BI tool or separate visualization library)

## Quick Reference

### Installation & Configuration

**Install TimescaleDB Extension (Debian/Ubuntu):**
```bash
sudo apt install -y postgresql-{{pg_version}}-timescaledb
sudo pg_createcluster {{pg_version}} main --start
sudo pg_ctlcluster {{pg_version}} main start
sudo -u postgres psql -c "CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;"
```
*(Replace `{{pg_version}}` with your PostgreSQL version, e.g., 16)*

**Configuration (postgresql.conf):**
```ini
# Add to postgresql.conf
shared_preload_libraries = 'timescaledb'
timescaledb.max_background_workers = 8 # Adjust based on CPU cores
max_connections = 100 # Adjust based on workload
```
*(After changes, restart PostgreSQL: `sudo systemctl restart postgresql`)*

### Hypertables

**Create Hypertables:**
```sql
CREATE TABLE sensor_data (
  time TIMESTAMPTZ NOT NULL,
  device_id INT,
  temperature DOUBLE PRECISION,
  humidity DOUBLE PRECISION
);

SELECT create_hypertable('sensor_data', 'time');
```

**Convert Existing Table to Hypertable:**
```sql
SELECT create_hypertable('your_existing_table', 'time_column', migrate_data => true);
```

**Show Hypertables:**
```sql
\d+
SELECT * FROM timescaledb_information.hypertables;
```

### Continuous Aggregates

**Create Continuous Aggregate:**
```sql
CREATE MATERIALIZED VIEW device_hourly_summary
WITH (timescaledb.continuous) AS
SELECT
  time_bucket('1 hour', time) AS bucket,
  device_id,
  AVG(temperature) AS avg_temp,
  MAX(temperature) AS max_temp
FROM sensor_data
GROUP BY time_bucket('1 hour', time), device_id
WITH NO DATA; -- Initially create without data

-- Refresh the continuous aggregate
CALL refresh_continuous_aggregate('device_hourly_summary', NULL, NULL);
```

**Get Continuous Aggregates Info:**
```sql
SELECT * FROM timescaledb_information.continuous_aggregates;
```

### Data Retention & Compression

**Set Data Retention Policy (Drop data older than 3 months):**
```sql
SELECT add_retention_policy('sensor_data', INTERVAL '3 months');
```

**Enable Compression (Compress data older than 7 days):**
```sql
ALTER TABLE sensor_data SET (timescaledb.compress = TRUE);
SELECT add_compression_policy('sensor_data', INTERVAL '7 days');
```

**Show Compression Status:**
```sql
SELECT * FROM timescaledb_information.compression_settings;
```

### Querying Time-Series Data

**Basic Time-Range Query:**
```sql
SELECT * FROM sensor_data
WHERE time >= NOW() - INTERVAL '1 day'
  AND time < NOW()
ORDER BY time DESC;
```

**Gapfilling and Interpolation:**
```sql
SELECT
  time_bucket('1 hour', time) AS bucket,
  AVG(temperature) AS avg_temp,
  locf(AVG(temperature)) OVER (ORDER BY time_bucket('1 hour', time)) AS avg_temp_locf
FROM sensor_data
GROUP BY bucket
ORDER BY bucket;
```

### High-Performance Queries

**Approximate Count:**
```sql
SELECT COUNT(*) FROM sensor_data TABLESAMPLE BERNOULLI (1);
```

**Top-N Queries:**
```sql
SELECT time, device_id, temperature
FROM sensor_data
WHERE time >= NOW() - INTERVAL '1 day'
ORDER BY temperature DESC
LIMIT 10;
```

## Examples

### Example 1: IoT Sensor Data Pipeline

- Input: Stream of sensor readings (time, device_id, value)
- Steps:
  1. Create a hypertable for `iot_readings`.
  2. Ingest data into the hypertable.
  3. Create a continuous aggregate to compute hourly average readings.
  4. Query the continuous aggregate for a specific device's hourly trend.
  5. Set a retention policy to keep only 1 year of raw data.
- Expected output / acceptance: Efficient storage, automatic hourly rollups, and proper data pruning.

### Example 2: Financial Tick Data Analysis

- Input: High-frequency financial tick data (timestamp, symbol, price, volume)
- Steps:
  1. Create a hypertable `tick_data` with proper chunk sizing for high ingest rate.
  2. Enable compression for older `tick_data`.
  3. Query `tick_data` to calculate 5-minute VWAP (Volume Weighted Average Price) for a specific symbol.
  4. Visualize the VWAP over the last trading day.
- Expected output / acceptance: Ability to ingest and analyze millions of rows/second, with optimized storage and fast analytical queries.

### Example 3: Monitoring System Metrics

- Input: Server metrics (timestamp, host_id, cpu_usage, memory_usage, network_io)
- Steps:
  1. Create a hypertable `system_metrics` partitioned by `time` and `host_id`.
  2. Use a `time_bucket_gapfill` query to find CPU usage for all hosts over the last 24 hours, filling in missing data points.
  3. Create an alert based on `MAX(cpu_usage)` exceeding a threshold using a continuous aggregate.
- Expected output / acceptance: Comprehensive monitoring with gap-filled data for visualization and real-time alerting.

## References

- `references/installation.md`: Detailed installation and setup
- `references/hypertables.md`: Deep dive into hypertable management
- `references/continuous_aggregates.md`: Advanced continuous aggregate techniques
- `references/compression.md`: Comprehensive guide to data compression
- `references/api.md`: TimescaleDB SQL functions and commands reference
- `references/performance.md`: Performance tuning and best practices
- `references/getting_started.md`: Official TimescaleDB Getting Started Guide
- `references/llms.md`: Using TimescaleDB with LLMs (e.g., storing embeddings, RAG)
- `references/llms-full.md`: Full LLM integration scenarios
- `references/tutorials.md`: Official TimescaleDB Tutorials and Use Cases
- `references/time_buckets.md`: Guide to `time_bucket` and gapfilling functions
- `references/hyperfunctions.md`: Advanced analytical functions for time-series

## Maintenance

- Sources: Official TimescaleDB Documentation, GitHub repository, blog posts.
- Last updated: 2025-12-17
- Known limits: This skill focuses on core TimescaleDB features. Advanced PostgreSQL features (e.g., PostGIS, JSONB) are covered by other specialized skills.

## Troubleshooting

### Slow Queries
- Ensure indexes are on `time` and other frequently queried columns.
- Verify chunk sizing is appropriate for your data ingestion rate.
- Use `EXPLAIN ANALYZE` to identify bottlenecks.
- Consider creating continuous aggregates for frequently accessed aggregated data.

### High Disk Usage
- Implement data retention policies for older, less critical data.
- Enable compression for older chunks.
- Regularly run `VACUUM ANALYZE` on your tables.

### Failed to Create Hypertable
- Ensure the `time` column is `TIMESTAMPTZ` or a supported integer type.
- The table must be empty or you must use `migrate_data => true`.
- Check for existing triggers or foreign keys that might conflict.

---

**This skill provides a robust foundation for managing time-series data with TimescaleDB!**