#!/bin/bash
while true; do
  python /efsweb/web.py &
  sleep 60
  kill -9 $! 
done
