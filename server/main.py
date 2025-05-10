"""
main.py

This script runs the Flask HW1 server application.
It uses the app factory (create_app) from the 'src' package,
parses an optional --port argument, and starts the Flask server.
"""

import argparse
from src import create_app

# Create the Flask app instance using the factory function
app = create_app()

if __name__ == '__main__':
    # Parse optional command-line arguments (default port 5000)
    parser = argparse.ArgumentParser(description='Flask HW1 Server')
    parser.add_argument('--port', type=int, default=5000, help='Port to listen on')
    args = parser.parse_args()

    # Run the Flask development server
    app.run(debug=True, host='127.0.0.1', port=args.port)
