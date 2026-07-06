#!/usr/bin/env python3
"""
Account save/create functionality for inlinegui.
Supports saving user info (Name, Email) from Mozilla Persona
or collecting via a simple form.
"""
import json
import os
from datetime import datetime

DATA_FILE = os.environ.get('INLINEGUI_DATA', 'accounts.json')

def load_accounts():
    """Load accounts from JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_accounts(accounts):
    """Save accounts to JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(accounts, f, indent=2)

def save_user_info(name, email):
    """Save user info from Mozilla Persona or similar auth."""
    accounts = load_accounts()
    if email in accounts:
        accounts[email]['name'] = name
        accounts[email]['updated_at'] = datetime.utcnow().isoformat()
    else:
        accounts[email] = {
            'name': name,
            'email': email,
            'created_at': datetime.utcnow().isoformat()
        }
    save_accounts(accounts)
    return accounts[email]

def get_create_account_html():
    """Return HTML for a simple account creation form (Stripe-inspired minimal style)."""
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Account - InlineGUI</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
               display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0;
               background: #f6f8fa; }
        .card { background: white; padding: 40px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                width: 100%; max-width: 360px; }
        h1 { font-size: 24px; margin-bottom: 8px; color: #24292e; }
        p.subtitle { color: #586069; margin-bottom: 24px; }
        input { width: 100%; padding: 10px 12px; margin-bottom: 16px; border: 1px solid #e1e4e8;
                border-radius: 6px; font-size: 14px; box-sizing: border-box; }
        input:focus { outline: none; border-color: #0366d6; box-shadow: 0 0 0 3px rgba(3,102,214,0.1); }
        button { width: 100%; padding: 10px 16px; background: #2da44e; color: white; border: none;
                 border-radius: 6px; font-size: 14px; font-weight: 600; cursor: pointer; }
        button:hover { background: #2c974b; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Create your account</h1>
        <p class="subtitle">Get started with InlineGUI</p>
        <form id="accountForm">
            <input type="text" id="name" placeholder="Full name" required>
            <input type="email" id="email" placeholder="Email address" required>
            <button type="submit">Create account</button>
        </form>
    </div>
</body>
</html>"""

if __name__ == '__main__':
    print("Account save/create module loaded.")
    print(f"Data file: {DATA_FILE}")
