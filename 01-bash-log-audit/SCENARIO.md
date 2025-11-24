# Day 01 – Bash Challenge: Daily Log Audit

## Scenario

You are a DevOps engineer responsible for monitoring a Linux server that generates application logs at: /var/log/myapp/myapp.log

The logs contain entries of various severity levels and IP addresses accessing the system.

Your task is to automate a **daily log audit** that provides key metrics to your team.

---

## Requirements

Write a Bash script that:

1. **Counts log levels**  
   - Count how many lines contain `INFO`, `WARNING`, and `ERROR`.

2. **Top IPs**  
   - Extract all IPv4 addresses from the log and list the **top 3 most frequent IPs**.

3. **Generate a summary**  
   - Create a file called `daily_summary.txt` containing:
     - Today's date  
     - Count of INFO, WARNING, ERROR  
     - Top 3 IP addresses  

4. **Optional: archive old logs**  
   - Compress `.log` files older than 7 days with `gzip`.

---

## Constraints

- Use only **standard Bash/Linux tools** (`grep`, `awk`, `sort`, `uniq`, `find`).  
- The script must run **without user interaction**.  
- Logs can be large (thousands of lines).  
- Summary file must be human-readable.

---

## Estimated time: ~30 minutes
