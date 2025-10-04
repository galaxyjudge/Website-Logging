# Website-Logging
# 🌐 Website Uptime Monitor

A lightweight Python script that checks if websites are up every 5 minutes, logs results to scrpt.log, auto-clears the log every hour, and runs continuously. Built for DevOps — no frameworks, pure Python. Perfect for monitoring, learning, or building alert systems.

---

## Features

- Checks website status using HTTP requests
- Logs uptime/down events with timestamps
- Auto-clears log file every hour to avoid bloat
- Reads URLs from web_address.txt — one per line
- Runs checks every 5 minutes — fully configurable
- Terminal output + persistent logging
- Ready for email/SMS alert integration (planned)

---

## How to Run

Install required packages:
pip install requests schedule

Create web_address.txt in the same folder — example:
https://google.com
https://github.com

Run the script:
python scpt.py

Watch terminal output + check scrpt.log for history

---

## Log Format

All logs written to scrpt.log — example:
2025-09-21 21:52 - INFO - [OK] https://google.com is UP — Status: 200
2025-09-21 21:57 - WARNING - https://fakesite.com is DOWN — Error: ...

Log file is auto-cleared every 1 hour.

---

## Configuration

Check interval: 5 minutes → schedule.every(5).minutes.do(readfile)
Log clear interval: 1 hour → schedule.every(1).hours.do(auto_clear_log)
Request timeout: 7 seconds
Log file: scrpt.log (UTF-8, overwritten on each run)

---

## Requirements

Python 3.6+
Libraries: requests, schedule

Install with:
pip install requests schedule

---

## Folder Structure

project/
├── scpt.py              # Your script
├── web_address.txt      # List of URLs to monitor
└── scrpt.log            # Auto-generated log file (ignored by Git)

---

## Next Steps (Planned)

- Email alerts on downtime
- Telegram/SMS notifications
- Web dashboard (Flask)
- Export logs to CSV or database

---

## Contributing

Fork it. Tweak intervals. Add retry logic. Build email alerts. Go wild. PRs welcome.

---

## License

MIT — Do whatever you want with it.

---

Made with ❤️ for DevOps builders and learners.
