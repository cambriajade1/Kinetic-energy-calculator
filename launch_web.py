#!/usr/bin/env python3
"""
Web Interface Launcher
Opens the Energy Calculator web interface in your default browser
"""

import webbrowser
import http.server
import socketserver
import threading
import time
import os
import sys

PORT = 8000
HANDLER = http.server.SimpleHTTPRequestHandler


def start_server():
    """Start the HTTP server."""
    with socketserver.TCPServer(("", PORT), HANDLER) as httpd:
        print(f"\n✅ Server running at: http://localhost:{PORT}")
        print(f"📂 Serving from: {os.getcwd()}\n")
        print("Press Ctrl+C to stop the server")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n✓ Server stopped successfully")
            sys.exit(0)


def main():
    """Main entry point."""
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Check if index.html exists
    if not os.path.exists("index.html"):
        print("❌ Error: index.html not found in the current directory")
        print(f"📂 Current directory: {os.getcwd()}")
        sys.exit(1)
    
    print("=" * 50)
    print("Energy Calculator - Web Interface")
    print("=" * 50)
    
    # Start server in a background thread
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    # Give server a moment to start
    time.sleep(1)
    
    # Open in default browser
    url = f"http://localhost:{PORT}/index.html"
    print(f"\n🌐 Opening web interface in your browser...")
    print(f"🔗 Opening: {url}\n")
    
    webbrowser.open(url)
    
    # Keep the server running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
