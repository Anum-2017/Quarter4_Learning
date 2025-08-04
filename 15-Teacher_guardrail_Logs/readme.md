# 🧑‍🏫 Teacher Agent with Input Guardrail Trigger

## 🔑 OpenAI Key Setup & Log Tracing Guide

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
   3. Navigate to the Traces section to view execution details and API activity, including any triggered guardrails like InputGuardrailTripwireTriggered.
      
---

## Exercise:

**Objective:** Make a teacher agent and make an input guardrail trigger.
**Prompt:** I want to change my class timings 

**Outcome:** After running the above prompt an InputGuardrailTripwireTriggered in except should be called. See the outcome in LOGS

---

<img width="959" height="546" alt="1" src="https://github.com/user-attachments/assets/d1e37158-9496-4da8-8109-9027a170f7eb" />

<img width="799" height="433" alt="3" src="https://github.com/user-attachments/assets/5847669f-45dd-4792-90a6-4159dcc06c82" />

<img width="828" height="425" alt="4" src="https://github.com/user-attachments/assets/a05839c3-27b3-4ef1-afb8-d50880e02ff4" />

<img width="830" height="437" alt="5" src="https://github.com/user-attachments/assets/e0f87eac-bef1-4063-bdb9-41533a9586e5" />
