# 🔑 OpenAI Key Setup & Log Tracing Guide

This guide helps you set up your OpenAI API key securely and view logs/traces for your application using the OpenAI Developer Dashboard.

## 🚀 Getting Started

### 1️⃣ Generate Your OpenAI API Key
   1. Visit the OpenAI Documentation Dashboard (https://platform.openai.com/docs/overview)
   2. Log in or sign up for an OpenAI account.
   3. In the left sidebar, click on "API Keys" under the Dashboard section.
   4. Click on "Create new secret key".
   5. Copy the generated key and paste it in your `.env` file as shown below:

```python
OPENAI_API_KEY=your_openai_secret_key_here
```

### 2️⃣ Enable Logging & Traces
In your RunConfig setup, make sure to remove or comment out the following line if it exists:

```python
tracing_disabled=True
```

In your main.py, load the environment variables:

```python
from dotenv import load_dotenv
load_dotenv()
```

This ensures your OpenAI key from `.env` is accessible in the code.

---

## 🔍 View Execution Logs

 After running your application:
   1. Go to the OpenAI Platform Dashboard
   2. From the sidebar, click Logs
   3. Navigate to the Traces section to view execution details and API activity

---

<img width="799" height="334" alt="Screenshot 2025-07-30 214143" src="https://github.com/user-attachments/assets/b16f47d1-1756-4ef7-9d3e-bd2eeed549a6" />

<img width="797" height="428" alt="Screenshot 2025-07-30 214728" src="https://github.com/user-attachments/assets/aa99f3ab-62a1-446c-9958-84202231358e" />
