#!/bin/bash

# DevOps Solutions with Bash
# Author: cb0n3y
# Scriptname: estimate-log-growth.sh
# Usage: Run the script to monitor /var/log/messages growth and estimate time until disk fills
# Description: Monitors the growth of /var/log/messages and estimates time remaining before /var partition fills up
# Author: cb0n3y
# Created: 2025-07-03

# Estimate log growth rate for /var/log/messages
FILE="/var/log/messages"
SAMPLE_TIME=3600  # 1 hour in seconds
MAX_ITERATIONS=5

for ((i=1; i<=MAX_ITERATIONS; i++)); do
  SIZE1=$(stat -c %s "$FILE")
  sleep $SAMPLE_TIME
  SIZE2=$(stat -c %s "$FILE")

  GROWTH=$((SIZE2 - SIZE1))  # in bytes

  if [ "$GROWTH" -le 0 ]; then
    echo "No growth detected."
    exit 0
  fi

  FREESPACE=$(df --output=avail /var | tail -n 1)  # in KB
  GROWTH_KB=$((GROWTH / 1024))  # Convert to KB
  HOURS_LEFT=$((FREESPACE / GROWTH_KB))

  echo "Growth in the last hour: $GROWTH_KB KB"
  echo "Approx. time until full: $HOURS_LEFT hours"
done
