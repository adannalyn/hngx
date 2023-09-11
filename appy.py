from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    if slack_name is None or track is None:
        return jsonify({"error": "Missing parameters"}), 400

    # Validate track to ensure it's "backend"
    if track != "backend":
        return jsonify({"error": "Invalid track parameter"}), 400

    # Get the current day of the week
    current_day = datetime.utcnow().strftime('%A')

    # Get the current UTC time with a +/-2 minute window
    current_time_utc = datetime.utcnow()
    utc_time = current_time_utc.strftime('%Y-%m-%d %H:%M:%S')

    # GitHub URLs
    github_file_url = "https://github.com/username/repo/blob/main/file_name.ext"
    github_repo_url = "https://github.com/username/repo"

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
