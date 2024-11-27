# domain-ch

**domain-ch** is a tool for checking the availability and status of subdomains and domains. Designed for hackers, developers, and cybersecurity enthusiasts, it provides both **real-time table output** and detailed logs for further analysis.

## Features

- **Ping Check**: Verifies if the domain/subdomain is reachable via ICMP (ping).
- **HTTP Status Check**: Fetches the HTTP response status code for the domain.
- **Real-time Table Output**: Displays results in a neat table format for easy readability.
- **Log File Output**: Saves detailed logs for deeper analysis.

## Requirements

- Python 3.6+
- `requests` library
- `tabulate` library

Install the dependencies:
```bash
pip install requests tabulate
```

## Usage

### Basic Usage
To check a list of domains from a file and display results in the console & To save detailed logs :
```bash
./main.py -file <filename>
```

## Options

| Flag      | Description                                    |
|-----------|------------------------------------------------|
| `-file`   | Specifies the file containing the domains to check. |
| `-o`      | (Optional) Specifies the log file for detailed output. |

## How It Works

1. Reads domains from the specified file.
2. For each domain:
   - Pings the domain to check network reachability.
   - Sends an HTTP GET request to fetch the status code.
3. Displays results in a table format and logs them to a file if `-o` is specified.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy hacking! 🚀
