
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
