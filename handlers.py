from datetime import datetime
import dateutil.parser

def format_ts(ts):
    dt = dateutil.parser.isoparse(ts)
    return dt.strftime("%d %b %Y, %I:%M %p")

def handle_push(payload):
    if "head_commit" not in payload:
        return None

    return {
        "author": payload["pusher"]["name"],
        "action": "PUSH",
        "to_branch": payload["ref"].split("/")[-1],
        "timestamp": format_ts(payload["head_commit"]["timestamp"]),
        "created_at": datetime.utcnow()
    }

def handle_pr(payload):
    pr = payload.get("pull_request")
    if not pr:
        return None

    action = "MERGE" if pr.get("merged") else "PULL_REQUEST"

    return {
        "author": pr["user"]["login"],
        "action": action,
        "from_branch": pr["head"]["ref"],
        "to_branch": pr["base"]["ref"],
        "timestamp": format_ts(pr["created_at"]),
        "created_at": datetime.utcnow()
    }
