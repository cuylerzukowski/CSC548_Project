# Streamlit Contact Book Manager
A lightweight, Python-based tool for efficiently creating, organizing, and retrieving personal and professional contact information using a clean web interface.

## Overview
This application uses Streamlit to create a digital rolodex that manages your network. It allows for local data persistence via JSON, enabling users to add, update, search, and categorize contacts without requiring a complex database setup. The system includes robust search functionality and data backup options.

## Demo Video
https://youtu.be/Sl7ZCi4BEec

## Key Features
* **CRUD Operations:** Full capability to Create, Read, Update, and Delete contact entries
* **Smart Search:** Case-insensitive search that scans names, phone numbers, emails, addresses, and notes simultaneously
* **Categorization:** Tag contacts with specific labels (Family, Friend, Work, School, Other) for better organization
* **Data Persistence:** Automatically saves data to a local JSON file so information is never lost between sessions
* **One-Click Backup:** Export your entire contact list to a JSON file via the sidebar for safekeeping

## Data Fields Managed
The system stores and manages the following data points for each contact entry:

### 1. Primary Information
* **Name:** Serves as the unique identifier for the contact
* **Phone:** Contact number
* **Email:** Digital contact address

### 2. Contextual Information
* **Address:** Physical location or mailing address
* **Notes:** Free-text area for context (e.g., availability or specific details)

### 3. Classification
* **Category:** Dropdown selection to organize the contact type
    * *Options:* Family, Friend, Work, School, Other

## Installation

### Prerequisites
* Python 3.x installed on your machine
* Terminal or Command Prompt access

### Setup Steps
**Step 1: Install Dependencies**
Open your terminal and run the following command to install the required library:
```bash
pip install streamlit
```
**Step 2: Navigate to the ContactManager folder**
In the terminal run:
```bash
cd/Desktop/ContactManager
```
**Step 3: Run the project**
In the terminal run:
```bash
streamlit run Project.py
```

## File Structure

```text
ContactManager/
├── Project.py                      # Main Streamlit application
├── contacts.json                   # Local database file (auto-generated)
├── requirements.txt                # List of dependencies
├── Instruction.txt                 # Raw setup commands
└── README.md                       # This file
```

## Authors
Developed by Harrison Nordmeyer, Cuyler Zukowski, Daniel You
