import argparse
from website import create_app

app = create_app()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Flask HW1 Server')
    parser.add_argument('--port', type=int, default=5000, help='Port to listen on')
    args = parser.parse_args()
    app.run(debug=True, host='127.0.0.1', port=args.port)
