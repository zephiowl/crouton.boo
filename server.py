#!/usr/bin/env python3
"""Simple HTTP server for crouton.boo with route handling."""

import http.server
import socketserver
import os
import webbrowser
import threading
import time

PORT = 8000
DIRECTORY = "/mnt/nas hdd/Nextcloud/github/crouton.boo"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def log_message(self, format, *args):
        # Suppress default logging for cleaner output
        pass
    
    def handle_one_request(self):
        # Convert routes to file paths
        if self.path == '/thorn':
            self.path = '/thorn.html'
        elif self.path == '/discord':
            self.path = '/discord.html'
        elif self.path == '/' or self.path == '':
            self.path = '/index.html'
        super().handle_one_request()

def run_server():
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Server running at http://localhost:{PORT}/")
        print("Access:")
        print("  http://localhost:{PORT}/ - Home page")
        print(f"  http://localhost:{PORT}/thorn - Thorn page")
        print("\nPress Ctrl+C to stop the server")
        httpd.serve_forever()

if __name__ == "__main__":
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    
    # Open browser after a short delay
    time.sleep(1)
    webbrowser.open(f"http://localhost:{PORT}/")
    
    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nServer stopped.")