
# billing_system.py

import json
from datetime import datetime, timedelta

class BillingManager:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, plan="free"):
        self.users[user_id] = {
            "plan": plan,
            "expiry": datetime.now() + timedelta(days=30 if plan == "pro" else 7)
        }

    def check_access(self, user_id):
        user = self.users.get(user_id)
        if not user:
            return False
        return datetime.now() < user["expiry"]

    def upgrade_to_pro(self, user_id):
        self.users[user_id]["plan"] = "pro"
        self.users[user_id]["expiry"] = datetime.now() + timedelta(days=30)

if __name__ == "__main__":
    bm = BillingManager()
    bm.add_user("user123", "pro")
    print("Access:", bm.check_access("user123"))
