# License Plate Tracking System

A Python-based automation tool that processes vehicle license plate spreadsheets, validates data, and generates organized reports. This project demonstrates practical software development skills including file handling, spreadsheet automation, input validation, modular programming, and containerization with Docker.

---

## Features

* Process vehicle license plate records from spreadsheets
* Validate user input and data integrity
* Generate automated reports
* Create directories and manage files automatically
* Handle errors gracefully
* Modular and maintainable code structure
* Command-line interface (CLI)
* Docker support for consistent deployment

---

## Technologies Used

* Python 3
* OpenPyXL
* PyInputPlus
* Pathlib
* Docker
* Docker Compose
* Git
* GitHub

---

## Project Structure

```text
plate-reporting-system/
│
├── main.py                 # Application entry point
├── functions.py            # Core business logic
├── config.py               # Configuration settings
├── spreadsheets/           # Input spreadsheet files
├── reports/                # Generated reports
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/NaomiSoubhia/plate-reporting-system.git
cd plate-reporting-system
```

### Create a Virtual Environment

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Run the application locally:

```bash
python main.py
```

Follow the prompts displayed in the terminal to process spreadsheet data and generate reports.

---

## Running with Docker

### Build the Docker Image

```bash
docker build -t plate-reporting-system .
```

### Run the Container

```bash
docker run -it plate-reporting-system
```

### Mount Local Folders (Optional)

To allow the container to access local spreadsheets and save generated reports:

```bash
docker run -it \
-v $(pwd)/spreadsheets:/app/spreadsheets \
-v $(pwd)/reports:/app/reports \
plate-reporting-system
```

### Docker Compose

```bash
docker compose up --build
```

---

## CI/CD

[![pipeline status](https://gitlab.com/NaomiSoubhia-group/plate-data-reporter/badges/main/pipeline.svg)](https://gitlab.com/NaomiSoubhia-group/plate-data-reporter/-/commits/main)

GitLab CI validates Python files automatically and builds the Docker image.

## Example Workflow

1. Load a spreadsheet containing vehicle records.
2. Validate input data.
3. Process license plate information.
4. Generate a report automatically.
5. Save the report to the reports directory.

---

## Skills Demonstrated

This project showcases:

* Python Programming
* Spreadsheet Automation
* Data Validation
* Error Handling
* File and Directory Management
* Modular Software Design
* Command-Line Applications
* Docker Containerization
* Git Version Control
* Technical Documentation

---

## Challenges and Solutions

### Challenge: Managing File Paths Across Different Operating Systems

Different operating systems handle file paths differently.

**Solution:** Implemented Pathlib to create platform-independent paths and improve code readability.

### Challenge: Preventing Invalid User Input

User input can introduce errors and unexpected behavior.

**Solution:** Used PyInputPlus to validate inputs and improve application reliability.

### Challenge: Ensuring Consistent Execution Environments

Applications may behave differently depending on the machine configuration.

**Solution:** Containerized the application using Docker to ensure consistency across environments.

---

## Future Improvements

* Graphical User Interface (GUI)
* Database integration
* CSV and JSON export options
* Advanced filtering and search features
* Dashboard and analytics
* Automated email reporting
* Unit and integration testing

---

## Sample Use Case

A parking management team receives daily spreadsheets containing vehicle records. Instead of manually reviewing and organizing the data, this application automates processing, validates records, and generates reports in seconds, reducing manual effort and improving accuracy.

---

## Author

**Naomi Soubhia Doi**

Computer Programming Student at Georgian College

Interested in software development, automation, infrastructure, and building practical solutions that improve efficiency through technology.

---

## License

This project is licensed for educational and portfolio purposes.
