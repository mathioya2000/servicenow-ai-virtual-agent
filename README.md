\# ServiceNow AI Virtual Agent



AI-powered employee support assistant using ServiceNow Knowledge Base and OpenAI.



\## Live Demo



https://servicenow-ai-virtual-agent.onrender.com



\## GitHub Repository



https://github.com/mathioya2000/servicenow-ai-virtual-agent



\---



\## Overview



This project demonstrates an enterprise AI virtual support assistant integrated with ServiceNow Knowledge Management.



Employees can ask natural-language IT support questions, and the assistant:



\- searches ServiceNow Knowledge Base articles

\- retrieves relevant knowledge content

\- uses AI to generate employee-friendly troubleshooting guidance

\- recommends when to escalate to incident creation

\- simulates a ServiceNow AI-powered employee support experience



Example:



\*\*Employee asks:\*\*



```text

My VPN is not connecting

```



\*\*System responds with:\*\*



\- likely issue diagnosis

\- troubleshooting guidance

\- knowledge article summary

\- escalation recommendation

\- professional employee-facing support response



\---



\## Business Value



Enterprise IT organizations need to reduce repetitive support tickets.



This solution demonstrates:



\- Incident deflection

\- Faster employee self-service

\- Better knowledge utilization

\- AI-assisted IT support

\- Reduced service desk workload

\- Improved employee experience



This reflects real enterprise ServiceNow use cases.



\---



\## Features



\### AI Virtual Support Assistant

Natural-language employee IT support interaction.



\### ServiceNow Knowledge Base Search

Queries live ServiceNow knowledge articles through REST API.



\### OpenAI Response Generation

Uses LLM reasoning to transform knowledge data into practical support guidance.



\### Incident Escalation Guidance

Advises when users should create incidents.



\### Professional Web UI

Simple web-based support assistant interface.



\### Live Cloud Deployment

Deployed publicly via Render.



\---



\## Architecture



```text

Employee Web UI

&#x20;     |

&#x20;     v

FastAPI Backend

&#x20;     |

&#x20;     +----------------------+

&#x20;     |                      |

&#x20;     v                      v

ServiceNow KB API        OpenAI API

&#x20;     |

&#x20;     v

Knowledge Articles

```



\---



\## Technology Stack



\- Python

\- FastAPI

\- ServiceNow REST API

\- OpenAI API

\- Jinja2

\- HTML/CSS/JavaScript

\- Uvicorn

\- Render Deployment



\---



\## Project Structure



```text

servicenow-ai-virtual-agent/

│

├── app/

│   ├── main.py

│   ├── ai\_engine.py

│   └── servicenow\_client.py

│

├── templates/

│   └── index.html

│

├── .env

├── .gitignore

├── requirements.txt

└── README.md

```



\---



\## Setup



\### Clone repository



```bash

git clone https://github.com/mathioya2000/servicenow-ai-virtual-agent.git

cd servicenow-ai-virtual-agent

```



\### Create virtual environment



```bash

python -m venv .venv

```



\### Activate environment



Windows:



```bash

.venv\\Scripts\\activate

```



\### Install dependencies



```bash

pip install -r requirements.txt

```



\### Configure environment variables



Create `.env`



```env

OPENAI\_API\_KEY=your\_openai\_key

SERVICENOW\_INSTANCE=https://your-instance.service-now.com

SERVICENOW\_USERNAME=admin

SERVICENOW\_PASSWORD=your\_password

```



\### Run locally



```bash

uvicorn app.main:app --reload

```



Open:



```text

http://127.0.0.1:8000

```



\---



\## Example Use Cases



\- VPN connection troubleshooting

\- password reset guidance

\- email access issues

\- onboarding support

\- software access support

\- device troubleshooting



\---



\## Interview Talking Points



This project demonstrates:



\- enterprise AI integration

\- REST API integration

\- ServiceNow Knowledge Management usage

\- practical LLM orchestration

\- employee self-service automation

\- production-style deployment

\- ITSM support automation thinking



\---



\## Future Enhancements



\- Incident auto-creation

\- chat conversation memory

\- authentication

\- employee identity awareness

\- approval workflows

\- multi-turn conversational context

\- ServiceNow Virtual Agent integration



\---



\## Author



Joseph Mwangi



ServiceNow + AI Portfolio Project

