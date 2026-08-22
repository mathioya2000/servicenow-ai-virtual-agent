# ServiceNow AI Virtual Agent

AI-powered employee self-service assistant using ServiceNow Knowledge Management and OpenAI.

## Live Demo

[Open the ServiceNow AI Virtual Agent](https://servicenow-ai-virtual-agent.onrender.com)

## Overview

This project demonstrates an enterprise AI support assistant integrated with ServiceNow Knowledge Management.

Employees can ask natural-language IT support questions, and the assistant:

- Searches ServiceNow Knowledge Base articles
- Retrieves relevant knowledge content
- Generates employee-friendly troubleshooting guidance
- Recommends when to escalate an issue to incident creation
- Simulates an AI-powered ServiceNow employee-support experience

## Example

**Employee asks:**

```text
My VPN is not connecting.
```

**The system responds with:**

- Likely issue diagnosis
- Troubleshooting guidance
- Relevant knowledge article summary
- Escalation recommendation
- Professional employee-facing response

## Business Value

Enterprise service desks handle many repetitive support requests. This project demonstrates how AI and ServiceNow Knowledge Management can provide:

- Incident deflection
- Faster employee self-service
- Better knowledge utilization
- AI-assisted IT support
- Reduced service desk workload
- Improved employee experience

## Features

### AI Virtual Support Assistant

Provides natural-language IT support interactions for employees.

### ServiceNow Knowledge Base Search

Queries ServiceNow Knowledge Base articles through the REST API.

### AI Response Generation

Transforms retrieved knowledge content into practical, employee-friendly support guidance.

### Incident Escalation Guidance

Recommends when the employee should create or escalate an incident.

### Web Interface

Provides a simple browser-based employee-support experience.

### Cloud Deployment

The demonstration application is deployed through Render.

## Architecture

```text
Employee Web Interface
          |
          v
    FastAPI Backend
       /       \
      v         v
ServiceNow KB   OpenAI API
     API
      |
      v
Knowledge Articles
```

## Technology Stack

- ServiceNow Knowledge Management
- ServiceNow REST API
- Python
- FastAPI
- OpenAI API
- Jinja2
- HTML, CSS, and JavaScript
- Uvicorn
- Render

## Project Structure

```text
servicenow-ai-virtual-agent/
├── app/
│   ├── main.py
│   ├── ai_engine.py
│   └── servicenow_client.py
├── templates/
│   └── index.html
├── .gitignore
├── requirements.txt
└── README.md
```

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/mathioya2000/servicenow-ai-virtual-agent.git
cd servicenow-ai-virtual-agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment on Windows

```text
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a local `.env` file:

```text
OPENAI_API_KEY=your_openai_key
SERVICENOW_INSTANCE=https://your-instance.service-now.com
SERVICENOW_USERNAME=integration_user
SERVICENOW_PASSWORD=your_secure_password
```

Never commit the `.env` file or real credentials. Use a dedicated ServiceNow integration account with only the permissions required by the application.

### 6. Run locally

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

## Example Use Cases

- VPN connection troubleshooting
- Password-reset guidance
- Email-access problems
- Employee onboarding support
- Software-access support
- Device troubleshooting
- Hospital employee IT support

## Skills Demonstrated

- ServiceNow Knowledge Management
- ServiceNow REST API integration
- Employee self-service automation
- ITSM support automation
- Knowledge-based incident deflection
- AI response orchestration
- FastAPI development
- Cloud deployment
- Secure credential configuration
- Technical documentation

## Future Enhancements

- Automatic incident creation
- Multi-turn conversation memory
- Employee authentication
- Employee identity awareness
- Approval workflows
- ServiceNow Virtual Agent integration
- Conversation and resolution analytics

## Project Status

Portfolio demonstration project for ServiceNow administration, support analysis, Knowledge Management, API integration, and AI-powered employee self-service.

## Author

Joseph Mwangi  
ServiceNow Certified Application Developer (CAD)  
[GitHub Profile](https://github.com/mathioya2000) | [Portfolio](https://mathioya2000.github.io)
