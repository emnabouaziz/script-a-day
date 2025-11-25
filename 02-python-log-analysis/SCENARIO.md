# Day 02 – Python Challenge: Log Analysis & Alerting

## Scenario

As a DevOps engineer, you want to improve monitoring by **analyzing server logs** programmatically.  
The logs are stored in:

/var/log/myapp/myapp.log

sql
Copier le code

Each log line contains a timestamp, log level, message, and IP address:

2025-11-24 12:30:45 INFO User 192.168.1.10 accessed /home
2025-11-24 12:31:12 ERROR Failed transaction for user 192.168.1.12
2025-11-24 12:32:00 WARNING Slow response on /checkout

markdown
Copier le code

---

## Requirements

Write a Python script that:

1. **Counts log levels**  
   - Number of `INFO`, `WARNING`, and `ERROR` entries.

2. **Tracks requests per endpoint**  
   - For example, `/home`, `/checkout`, `/profile`  
   - Generate a **summary table** with endpoint and request count.

3. **Detects slow requests**  
   - Any log line containing `Slow response` should be flagged.

4. **Generates a report file**  
   - Output results into `log_report.json` containing:
     - Counts of INFO, WARNING, ERROR  
     - Endpoint request counts  
     - List of slow requests (with timestamp and endpoint)

---

## Constraints

- Use **Python 3** standard libraries only (`re`, `json`, `collections`)  
- Script must be **idempotent** and handle large log files efficiently  
- Report file must be **JSON formatted** and human-readable

---

## Estimated time

**~30 minutes**
