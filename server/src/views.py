from flask import Blueprint, request, jsonify
import time

# Create a Blueprint for main routes
views = Blueprint('views', __name__)

# Initialize server state variables
start_time = time.time()
success_count = 0
fail_count = 0
api_version = 1

# Returns server status including uptime, success/fail counters, and API version
@views.route('/status', methods=['GET'])
def status():
    uptime = round(time.time() - start_time, 3)
    return jsonify({
        "status": {
            "uptime": uptime,
            "processed": {
                "success": success_count,
                "fail": fail_count
            },
            "health": "ok",
            "api_version": api_version
        }
    }), 200

# Handles image upload; returns classification result or error codes
@views.route('/upload_image', methods=['POST'])
def upload_image():
    global success_count, fail_count

    # Check if the 'image' file is missing → 400
    if 'image' not in request.files:
        fail_count += 1
        return jsonify(error={"http_status": 400, "message": "No image provided"}), 400

    image = request.files['image']
    # Check if the filename is empty → 400
    if image.filename == '':
        fail_count += 1
        return jsonify(error={"http_status": 400, "message": "No image provided"}), 400

    # Check for unsupported file extensions → 400
    if not image.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        fail_count += 1
        return jsonify(error={"http_status": 400, "message": "Unsupported image format"}), 400

    try:
        # Dummy classification result (to be replaced with real logic)
        matches = [
            {"name": "tomato", "score": 0.9},
            {"name": "carrot", "score": 0.1}
        ]
        success_count += 1
        return jsonify(matches=matches), 200

    except Exception as e:
        # Catch any internal error → 500
        fail_count += 1
        return jsonify(error={"http_status": 500, "message": str(e)}), 500
