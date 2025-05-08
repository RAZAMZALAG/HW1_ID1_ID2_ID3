from flask import Blueprint, request, jsonify
import time

views = Blueprint('views', __name__)

start_time = time.time()
success_count = 0
fail_count = 0
api_version = 1

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

@views.route('/upload_image', methods=['POST'])
def upload_image():
    global success_count, fail_count

    # missing file → 400
    if 'image' not in request.files:
        fail_count += 1
        return jsonify(error={"http_status": 400, "message": "No image provided"}), 400

    image = request.files['image']
    if image.filename == '':
        fail_count += 1
        return jsonify(error={"http_status": 400, "message": "No image provided"}), 400

    # unsupported extension → 400
    if not image.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        fail_count += 1
        return jsonify(error={"http_status": 400, "message": "Unsupported image format"}), 400

    try:
        # classification stub: replace with real model or API call as desired
        matches = [
            {"name": "tomato", "score": 0.9},
            {"name": "carrot", "score": 0.1}
        ]
        success_count += 1
        return jsonify(matches=matches), 200

    except Exception as e:
        # internal failure → 500
        fail_count += 1
        return jsonify(error={"http_status": 500, "message": str(e)}), 500
