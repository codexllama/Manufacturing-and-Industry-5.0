An Industry 5.0 smart manufacturing platform integrating real-time production monitoring, workforce management, predictive maintenance, AI-powered insights, safety compliance, and intelligent automation.

📌 Overview

AutoPlant-OS is a smart manufacturing management platform designed around the principles of Industry 5.0, where humans, machines, data, and intelligent technologies work together.

The platform provides a unified digital environment for monitoring manufacturing operations, managing workers, tracking machines, handling maintenance activities, monitoring production, analyzing sensor data, and receiving intelligent alerts.

Unlike a traditional manufacturing dashboard, AutoPlant-OS focuses on the combination of:

👷 Human-centric workforce management

🤖 Intelligent machine monitoring

📊 Real-time production analytics

🔧 Predictive and preventive maintenance

🛡️ Safety and compliance monitoring

📦 Inventory and supply management

🔔 Automated alerts and notifications

🧠 AI-assisted decision support

🎙️ Voice-based interaction

⚡ Energy and operational monitoring

🔐 Role-based access control

🎯 Project Objectives

The primary objectives of AutoPlant-OS are to:

Digitize important manufacturing operations through a centralized platform.

Connect employees, machines, production activities, and operational data.

Provide real-time visibility into manufacturing processes.

Improve machine and equipment monitoring.

Track maintenance requests and machine downtime.

Improve workforce and attendance management.

Provide role-specific dashboards for workers, managers, and administrators.

Provide actionable alerts for operational issues.

Use AI-assisted features to support faster decision-making.

Demonstrate an Industry 5.0-oriented manufacturing ecosystem.

🏭 Core Features
1. Command Center

The Command Center acts as the central operational dashboard.

It provides visibility into:

Production status

Machine conditions

Active alerts

Workforce information

Maintenance activities

Operational metrics

AI-generated insights

The objective is to give plant personnel a single place to understand the current state of the manufacturing environment.

2. Vehicle Pipeline

The Vehicle Pipeline provides an overview of vehicles moving through the manufacturing process.

It can be used to monitor:

Production stages

Vehicle progress

Manufacturing status

Production flow

Bottlenecks

This helps provide visibility into the overall production pipeline.

3. Production Monitoring

AutoPlant-OS includes production monitoring capabilities for tracking manufacturing activity.

Production information can be used to understand:

Production quantities

Production status

Machine utilization

Manufacturing progress

Operational performance

Production data is stored in PostgreSQL and exposed through the FastAPI backend.

4. Machine Management

The platform maintains information about manufacturing machines and equipment.

Machine information includes:

Machine ID

Machine name

Department

Operational status

Example machine categories used in the project include:

Robotic systems

Spot welders

Press machines

Automated guided vehicles

Manufacturing equipment

5. Sensor Data Monitoring

AutoPlant-OS includes a dedicated sensor-data component for collecting and displaying machine-related sensor information.

Sensor data can support monitoring of operational parameters and help identify abnormal conditions.

The backend provides an API endpoint for sensor information:
GET /api/sensors

6. Predictive / Preventive Maintenance

The Maintenance module helps track equipment maintenance activities.

It provides information such as:

Maintenance requests

Machine involved

Maintenance status

Maintenance activities

Maintenance history

Backend endpoint:
GET /api/maintenance

7. Downtime Alerts

The system provides alerts when machines or manufacturing operations experience problems.

Examples include:

Machine downtime

Equipment faults

Temperature abnormalities

Critical inventory conditions

Operational warnings

Backend endpoint:
GET /api/alerts

8. Safety Compliance

Safety is an important component of the Industry 5.0 approach.

AutoPlant-OS includes a dedicated Safety Compliance section designed to help workers and managers monitor safety-related information.

The worker interface can also provide safety reminders and notifications.


9. Workforce Management

AutoPlant-OS provides workforce-management functionality for managing employees within the manufacturing environment.

The system supports three primary roles:

Role	Description

Worker	Access to worker-focused manufacturing information

Manager	Access to operational and management information

Admin	Administrative and user-management capabilities

The database contains employee information including:

Employee ID

Full name

Password

Role

Department

Status

10. Attendance Management

The Attendance module is designed to monitor workforce attendance.

Attendance information can be retrieved through:

GET /api/attendance

The system can be extended to support:

Check-in

Check-out

Shift tracking

Attendance history

Worker availability

11. Task Management

Tasks can be assigned and monitored through the task-management component.

Backend endpoint:

GET /api/tasks

Tasks can be associated with users and used to monitor operational responsibilities.

12. Inventory & Supply

The Inventory & Supply module provides visibility into manufacturing materials and supplies.

The interface is designed to support monitoring of:

Stock levels

Critical materials

Supply conditions

Reordering requirements

This helps connect manufacturing operations with supply-chain visibility.

13. Helpdesk AI

The platform includes an AI-assisted Helpdesk concept designed to provide users with assistance regarding plant operations.

Potential use cases include:

Answering operational questions

Providing system guidance

Helping workers locate information

Supporting troubleshooting

Providing contextual assistance


14. AI Insights

AutoPlant-OS contains an AI Insights section intended to transform operational data into useful information for decision support.

Possible insights include:

Machine anomalies

Production issues

Maintenance requirements

Operational trends

Safety-related observations

Inventory warnings


15. AI Voice Features

Voice interaction is included as part of the project's Industry 5.0 approach.

The system can provide voice-based notifications and assistance.

The project also explores the use of AI APIs such as Groq for intelligent voice/assistant functionality.

Example use cases:

"Check machine status"

"Show active alerts"

"Give me today's production status"

"Which machines require maintenance?"


16. Energy Monitoring

The Energy Monitor component is intended to provide visibility into energy usage within the manufacturing environment.

This can help organizations monitor:

Energy consumption

Operational efficiency

Equipment usage

Potential energy-saving opportunities

👥 Role-Based Access

AutoPlant-OS is designed around role-based access.

👷 Factory Worker

Workers can access worker-focused functionality such as:

Worker dashboard

Safety information

Assigned tasks

Attendance

Machine/production information relevant to their work
Voice reminders


👨‍💼 Manager

Managers can access operational information such as:

Plant dashboard

Production monitoring

Machine status

Maintenance

Alerts

Workforce information

Analytics


🛠️ Administrator

Administrators can manage system-level information such as:

Users

Roles

Departments

Workforce records

System information

🏗️ System Architecture

AutoPlant-OS follows a three-layer architecture:

                    ┌─────────────────────────┐
                    │       USER INTERFACE    │
                    │                         │
                    │ HTML / CSS / JavaScript │
                    └────────────┬────────────┘
                                 │
                                 │ REST API
                                 ▼
                    ┌─────────────────────────┐
                    │       BACKEND           │
                    │                         │
                    │ FastAPI + Python        │
                    └────────────┬────────────┘
                                 │
                                 │ SQL
                                 ▼
                    ┌─────────────────────────┐
                    │       DATABASE          │
                    │                         │
                    │ PostgreSQL              │
                    └─────────────────────────┘


💻 Technology Stack

Layer	Technology

Frontend	HTML5

Styling	CSS3

Client-side Logic	JavaScript

Backend	Python

API Framework	FastAPI

Server	Uvicorn

Database	PostgreSQL 18

Database Driver	psycopg2

Environment Configuration	python-dotenv

Development Environment	Visual Studio Code

AI Integration	Groq API concept/integration
📁 Project Structure

The project currently follows a simple structure:

AutoPlant-OS/

│

├── autoplant-os-light-theme.html

│

├── backend/

│   └── main.py

│

├── .env

│

├── .venv/

│

└── run.bat

autoplant-os-light-theme.html

The main frontend application containing:

UI

Styling

Dashboard

Login interface

Role-based screens

JavaScript functionality

Charts

Tables

Interactive components

backend/main.py

The FastAPI backend responsible for:

API endpoints

PostgreSQL connectivity

Login authentication

Database queries

Data retrieval

Serving the frontend


.env

Stores database configuration and other environment-specific settings.

Example:

DB_HOST=localhost

DB_PORT=5432

DB_NAME=your_database

DB_USER=postgres

DB_PASSWORD=your_password

Do not commit .env to GitHub.

.venv

Python virtual environment containing the project's Python dependencies.

run.bat

Intended to provide a convenient way to start the application.

🗄️ Database

AutoPlant-OS uses PostgreSQL as its relational database.

The current database design contains the following major tables:

users

departments

machines

attendance

tasks

maintenance_requests

production

sensor_data

alerts

Database Relationships

A simplified representation:

                 ┌──────────────┐
                 │ departments  │
                 └──────┬───────┘
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
       ┌──────────┐          ┌──────────┐
       │  users   │          │ machines │
       └────┬─────┘          └────┬─────┘
            │                     │
       ┌────┼─────┐          ┌────┼─────────────┐
       ▼    ▼     ▼          ▼    ▼             ▼
  attendance tasks      production sensor_data alerts
                             
                         maintenance_requests
🔌 API Endpoints

The FastAPI backend currently provides endpoints for the major system modules.

System
GET /

Serves the AutoPlant-OS frontend.

GET /api/test

Tests whether the backend is running.

Authentication
POST /api/login

Used for employee login.

Example request:

{
  "employee_id": "EMP-001",
  "password": "password"
}
Users
GET /api/users

Returns user information.

GET /api/users/{user_id}

Returns information for a specific user.

Machines
GET /api/machines

Returns machine information from PostgreSQL.

Departments
GET /api/departments

Returns department information.

Attendance
GET /api/attendance

Returns attendance information.

Tasks
GET /api/tasks

Returns task information.

Maintenance
GET /api/maintenance

Returns maintenance requests.

Production
GET /api/production

Returns production information.

Sensors
GET /api/sensors

Returns sensor data.

Alerts
GET /api/alerts

Returns active/system alerts.

⚙️ Installation & Setup

1. Clone the Repository
2. 
git clone https://github.com/YOUR-USERNAME/AutoPlant-OS.git

Move into the project directory:

cd AutoPlant-OS

2. Create a Virtual Environment

Windows:

python -m venv .venv

Activate it:

.venv\Scripts\activate

You should see:

(.venv)

in your terminal.

3. Install Dependencies

Install the required Python packages:

python -m pip install fastapi uvicorn psycopg2-binary python-dotenv

4. Configure PostgreSQL

Install PostgreSQL and create the AutoPlant-OS database.

Create a database, for example:

autoplant_os

Then configure the database credentials in .env.

Example:

DB_HOST=localhost

DB_PORT=5432

DB_NAME=autoplant_os

DB_USER=postgres

DB_PASSWORD=your_password

▶️ Running the Application

Open PowerShell in:

E:\AutoPlant-OS\backend

Make sure the virtual environment is activated.

Then run:

python -m uvicorn main:app --reload

The backend should start at:

http://127.0.0.1:8000

Open:

http://127.0.0.1:8000

in your browser.

🧪 Testing the Backend

You can verify that FastAPI is running by opening:

http://127.0.0.1:8000/api/test

A successful response should indicate that the AutoPlant-OS backend is working.

You can also test the users API:

http://127.0.0.1:8000/api/users

and the machines API:

http://127.0.0.1:8000/api/machines

🔐 Security

The current project is primarily an academic/prototype implementation.

Before using AutoPlant-OS in a real production environment, additional security measures should be implemented.

Recommended improvements include:

Password hashing

Secure authentication tokens

HTTPS

Environment-variable protection

Input validation

API authorization

Database access restrictions

Audit logging

Rate limiting

Secure session management

Role-based API authorization

Database passwords and API keys should never be committed to GitHub.

📊 Industry 5.0 Approach

AutoPlant-OS is designed around several important Industry 5.0 principles.

Human-Centric

Workers remain an important part of the manufacturing system rather than being treated simply as data points.

The system provides:

Worker dashboards

Safety information

Voice assistance

Task management

Attendance monitoring

Sustainable

The platform includes an Energy Monitor concept to support visibility into energy consumption and operational efficiency.

Resilient

Machine monitoring, maintenance tracking, alerts, and production visibility help the plant respond to operational problems.

Intelligent

AI-assisted functionality can help transform manufacturing data into actionable information.

🔄 Example System Workflow

A typical workflow can be represented as:

Employee Login

      │
      
      ▼
      
Role Verification

      │
      
      ├───────────────┐
      
      ▼               ▼
      
   Worker          Manager/Admin
   
      │               │
      
      ▼               ▼
      
Worker Dashboard   Plant Dashboard

      │               │
      
      └───────┬───────┘
      
              ▼
              
       Manufacturing Data
       
              │
              
      ┌───────┼────────┐
      
      ▼       ▼        ▼
      
   Machines Production Sensors
   
      │       │        │
      
      └───────┼────────┘

              ▼
              
          FastAPI
          
              │
              
              ▼
              
         PostgreSQL
         
              │
              
              ▼
              
      Analytics / Alerts
      
              │
              
              ▼
              
         AI Insights

         
📈 Future Enhancements

The following features can be added as the project evolves:

🔐 JWT-based authentication

🔑 Secure password hashing

📱 Responsive mobile interface

🤖 Advanced predictive-maintenance models

🧠 Machine-learning-based anomaly detection

🎙️ More advanced voice assistant functionality

📡 Real IoT sensor integration

📊 Advanced Power BI integration

📈 Historical production analytics

⚡ Real-time energy monitoring

📦 Automated inventory management

🔔 WebSocket-based real-time notifications

☁️ Cloud deployment

🐳 Docker containerization

📋 Detailed audit logs

🔄 Automated backup and recovery

🛠️ Development Roadmap

Phase 1

├── Frontend UI

├── Dashboard

└── Role-based screens



Phase 2

├── PostgreSQL database

├── Database schema

└── Initial data



Phase 3

├── FastAPI backend

├── REST APIs

└── Frontend-backend integration


Phase 4

├── Authentication

├── Workforce management

├── Machine monitoring

└── Production monitoring


Phase 5

├── Maintenance

├── Alerts

├── Sensors

└── Analytics


Phase 6

├── AI assistance

├── Voice features

├── AI insights

└── Industry 5.0 enhancements


Phase 7

├── Security improvements

├── Testing

├── Deployment

└── Production optimization


🧪 Testing

Testing can be performed at multiple levels.

Frontend Testing

Verify:

Login interface

Navigation

Dashboard components

Role-based screens

Tables

Charts

Alerts

Voice features

Backend Testing

Verify:

API availability

Login requests

Database connections

API responses

Error handling

Database Testing


Verify:

User records

Machine records

Department relationships

Attendance

Tasks

Maintenance

Production

Sensor data

Alerts


👨‍💻 Development Environment

Recommended development setup:

Operating System : Windows

IDE               : Visual Studio Code

Frontend          : HTML / CSS / JavaScript

Backend           : Python + FastAPI

Server            : Uvicorn

Database          : PostgreSQL 18

Database Tool     : pgAdmin


🤝 Contributing

Contributions and suggestions are welcome.

A typical contribution workflow:

git checkout -b feature/new-feature

Make your changes, test them, then:

git add .
git commit -m "Add new feature"
git push origin feature/new-feature

Then create a Pull Request.

📜 License

This project can be distributed under an appropriate open-source license such as the MIT License.

If this repository is being submitted as an academic project, the license can be adjusted according to the institution/project requirements.

👥 Project Team

AutoPlant-OS is an academic/project implementation focused on demonstrating how Industry 5.0 concepts can be applied to smart automotive manufacturing.

The project brings together:

Human Workforce

       +
       
Manufacturing Machines

       +
       
IoT / Sensor Data

       +
       
Production Data

       +
       
Artificial Intelligence

       +
       
Analytics

       +
       
Automation

       =
       
AutoPlant-OS


⭐ Why AutoPlant-OS?

Traditional manufacturing systems often operate with separate systems for:

Production

Workers

Machines

Maintenance

Inventory

Safety

Analytics

AutoPlant-OS aims to bring these functions together into a single smart manufacturing platform.

The ultimate vision is:

Connect people, machines, data, and intelligence to create a more connected, responsive, and human-centric manufacturing environment.

📌 Project Status

Status: 🚧 Active Development

AutoPlant-OS currently has the core frontend, FastAPI backend, PostgreSQL database, API integration, role-based application structure, machine monitoring, workforce data, and multiple manufacturing modules established. Further integration and production-level security enhancements are ongoing.
