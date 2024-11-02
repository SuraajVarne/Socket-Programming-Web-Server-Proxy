# Socket Programming: Web Server & Proxy

## Description

This project implements a web server and a web proxy server using Python, as part of the CSCE 3530 course requirements. The web server handles HTTP GET requests and serves files from its local directory, while the web proxy acts as an intermediary between a client and a web server, caching web pages for improved efficiency.

### Project Components

1. **Web Server**: 
   - Accepts connections from clients and listens for HTTP GET requests.
   - Parses the request to identify the requested file.
   - Serves the file if available; otherwise, it returns a "404 Not Found" response.
   - Demonstrates the basics of socket programming and HTTP protocol handling.

2. **Web Proxy**: 
   - Sits between a client and the web server to handle HTTP GET requests.
   - Caches responses from the web server to serve future requests more quickly.
   - Forwards requests for resources not present in its cache to the web server, and subsequently caches the responses.
   - Allows users to experience faster page loads after the initial request.


## Instructions to Run the Web Server

1. Ensure Python is installed on your system.
2. Place a simple HTML file in the same directory as `web_server.py`.
3. Run the server using the command:
   ```bash
   python3 web_server.py





