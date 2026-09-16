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

3. Production Monitoring

AutoPlant-OS includes production monitoring capabilities for tracking manufacturing activity.

Production information can be used to understand:

Production quantities

Production status

Machine utilization

Manufacturing progress

Operational performance

Production data is stored in PostgreSQL and exposed through the FastAPI backend.

4. Sensor Data Monitoring

AutoPlant-OS includes a dedicated sensor-data component for collecting and displaying machine-related sensor information.

Sensor data can support monitoring of operational parameters and help identify abnormal conditions.

The backend provides an API endpoint for sensor information:
GET /api/sensors

5. Predictive / Preventive Maintenance

The Maintenance module helps track equipment maintenance activities.

It provides information such as:

Maintenance requests

Machine involved

Maintenance status

Maintenance activities

Maintenance history

Backend endpoint:
GET /api/maintenance

6. Downtime Alerts

The system provides alerts when machines or manufacturing operations experience problems.

Examples include:

Machine downtime

Equipment faults

Temperature abnormalities

Critical inventory conditions

Operational warnings

Backend endpoint:
GET /api/alerts

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
