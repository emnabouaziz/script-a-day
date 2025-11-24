#!/bin/bash

# Paths
LOG_DIR="/var/log/myapp"
TODAY_LOG="$LOG_DIR/myapp.log"
SUMMARY_FILE="$LOG_DIR/daily_summary.txt"

# Clear previous summary
> "$SUMMARY_FILE"

# Count log levels
ERROR_COUNT=$(grep -c "ERROR" "$TODAY_LOG")
WARNING_COUNT=$(grep -c "WARNING" "$TODAY_LOG")
INFO_COUNT=$(grep -c "INFO" "$TODAY_LOG")

# Write summary
{
  echo "Log Summary for $(date +%F)"
  echo "---------------------------"
  echo "INFO entries: $INFO_COUNT"
  echo "WARNING entries: $WARNING_COUNT"
  echo "ERROR entries: $ERROR_COUNT"
  echo ""
  echo "Top 3 IP addresses:"
  grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' "$TODAY_LOG" | sort | uniq -c | sort -nr | head -3
} >> "$SUMMARY_FILE"

# Compress logs older than 7 days
find "$LOG_DIR" -type f -name "*.log" -mtime +7 -exec gzip {} \;

echo "Daily summary created at $SUMMARY_FILE"
