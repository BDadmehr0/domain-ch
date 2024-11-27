#!/usr/bin/env python3

import sys
import subprocess
import requests
import logging
from tabulate import tabulate

def check_ping(domain):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", domain],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            return "Success"
        else:
            return "Failed"
    except Exception as e:
        return f"Error ({str(e)})"

def check_http(domain):
    try:
        response = requests.get(f"http://{domain}", timeout=5)
        return f"{response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error ({str(e)})"

def setup_logging(output_file):
    logging.basicConfig(
        filename=output_file,
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

if len(sys.argv) < 3 or sys.argv[1] != "-file":
    print("Usage: ./main.py -file <filename> [-o <output_log_file>]")
    sys.exit(1)

filename = sys.argv[2]
output_file = None

if len(sys.argv) == 5 and sys.argv[3] == "-o":
    output_file = sys.argv[4]
    setup_logging(output_file)

try:
    with open(filename, "r") as file:
        results = []
        for line in file:
            domain = line.strip()
            if not domain:
                continue
            print(f"Checking {domain}...")
            
            ping_status = check_ping(domain)
            http_status = check_http(domain)

            # Add to results for table display
            results.append([domain, ping_status, http_status])

            # Log details to file if logging is enabled
            if output_file:
                logging.info(f"{domain} - Ping: {ping_status}, HTTP: {http_status}")

        # Display results as a table
        print("\nResults:")
        print(tabulate(results, headers=["Domain", "Ping Status", "HTTP Status"], tablefmt="pretty"))

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    sys.exit(1)

