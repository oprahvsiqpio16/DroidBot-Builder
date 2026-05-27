#!/usr/bin/env python3
import os
import sys
import json
import subprocess
import requests
import time

def build_apk(bot_token, chat_id, app_name):
    """
    بناء APK باستخدام GitHub Actions عن بعد
    """
    github_token = os.environ.get("GITHUB_TOKEN")
    repo = "YOUR_USERNAME/DroidBot-Builder"
    
    url = f"https://api.github.com/repos/{repo}/dispatches"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {github_token}",
        "Content-Type": "application/json"
    }
    
    data = {
        "event_type": "build-apk",
        "client_payload": {
            "bot_token": bot_token,
            "chat_id": chat_id,
            "app_name": app_name
        }
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 204:
        print("✅ تم بدء البناء بنجاح")
        return True
    else:
        print(f"❌ فشل: {response.status_code}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("الاستخدام: python build_apk.py <TOKEN> <CHAT_ID> <APP_NAME>")
        sys.exit(1)
    
    token = sys.argv[1]
    chat_id = sys.argv[2]
    app_name = sys.argv[3]
    
    build_apk(token, chat_id, app_name)
