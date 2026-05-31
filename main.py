import sys
import json

def run_backend_sync():
    data = {"node": 6087, "status": "online"}
    print(f"Syncing node data: {json.dumps(data)}")

if __name__ == '__main__':
    run_backend_sync()