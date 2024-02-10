import socket
from urllib.parse import urlparse

# Function to parse URL and determine port number
def parse_url_for_tcp(url):
    parsed_url = urlparse(url.strip())
    protocol = parsed_url.scheme
    host = parsed_url.netloc
    path = parsed_url.path
    port = 443 if protocol == 'https' else 80  # Default ports for https and http
    return host, port, path

# Function to establish TCP connection and send HTTP GET request
def fetch_url(url):
    host, port, path = parse_url_for_tcp(url)
    try:
        with socket.create_connection((host, port), timeout=5) as sock:
            # send http request
            request = f'GET {path} HTTP/1.0\\r\\nHost: {host}\\r\\n\\r\\n'
            sock.send(bytes(request, 'utf-8'))

            # receive http response (omitting response handling for simplicity)
            # ...
            return 'Success'
    except Exception as e:
        return f'Network Error: {str(e)}'

# Read URLs from file
with open('urls.txt', 'r') as file:
    urls = file.readlines()

# Process each URL
for url in urls:
    status = fetch_url(url.strip())
    print(f'URL: {url.strip()}\\nStatus: {status}\\n')

