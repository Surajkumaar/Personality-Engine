#!/usr/bin/env python3
"""
Simple HTTP server for the frontend
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

PORT = 3002

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def serve_frontend():
    # Change to frontend directory
    frontend_dir = Path(__file__).parent
    os.chdir(frontend_dir)
    
    print(f"🌐 Starting frontend server on port {PORT}...")
    print(f"📁 Serving files from: {frontend_dir}")
    print(f"🔗 Frontend URL: http://localhost:{PORT}")
    print(f"🤖 Make sure backend is running on: http://127.0.0.1:8000")
    print("\n" + "="*50)
    print("🚀 Opening browser...")
    
    # Open browser automatically
    webbrowser.open(f'http://localhost:{PORT}')
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Frontend server stopped")

if __name__ == "__main__":
    serve_frontend()