from flask import Flask, request, jsonify
import datetime
import json
import webbrowser  # Import the webbrowser module for optional web browser opening

def get_info(slack_name, track):
    """Gets the required information and returns it in JSON format."""
    now = datetime.datetime.utcnow()
    utc_time = now.strftime("%Y-%m-%d %H:%M:%S")

    github_file_url = "https://github.com/your_username/repo/blob/main/backend_stage_one.py"
    github_repo_url = "https://github.com/your_username/repo"

    info = {
        "slack_name": slack_name,
        "current_day": now.strftime("%A"),
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return json.dumps(info)

app = Flask(__name__)

@app.route("/get_info", methods=["GET"])
def get_info_endpoint():
    slack_name = request.args.get("slack_name")
    track = request.args.get("track")

    info = get_info(slack_name, track)

    return info, 200

if __name__ == "__main__":
    # Optional: Open the browser when the script is run
    webbrowser.open("http://localhost:5000/get_info?slack_name=your_name&track=backend")
    app.run(debug=True)
