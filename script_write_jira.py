import json
body = {"fields": {"project": {"key": "PJ"}, "summary": "Growth Office PJotaEmiteLP sync", "description": "Integrate Jira with Claw3D for pipeline and Lead->Task automation.", "issuetype": {"name": "Task"}}}
with open(r"C:\Users\alyss\.openclaw\workspace\jira_issue.json", "w", encoding="utf-8") as f:
    json.dump(body, f)
