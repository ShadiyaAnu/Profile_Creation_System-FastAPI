# Student Profile API

A FastAPI-based RESTful API for managing student profiles. The application allows users to create student profiles with validated information such as name, email, phone, and password. The profiles are stored in a PostgreSQL database.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation Instructions](#installation-instructions)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
  - [Create Profile](#create-profile)
- [Error Handling](#error-handling)


## Project Overview

This project is a student profile API built using **FastAPI** and **SQLAlchemy**, with **PostgreSQL** as the database. It validates input fields like name, email, phone, and password, applying custom validation rules. Passwords are validated to meet specific strength criteria, and duplicate email entries are checked. The API exposes a single endpoint to create student profiles.

## Installation Instructions

Follow the steps below to set up the project locally:

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/ShadiyaAnu/Profile_Creation_SystemSystem-FastAPI.git
```

### 2. Set Up the Environment

- Install **Python 3.8+** if not already installed.
- Create a virtual environment:

  ```bash
  python -m venv env
  ```
Activate the virtual environment:
Windows: env\Scripts\activate
macOS/Linux: source env/bin/activate

### 3. Install Dependencies

Install all required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL
- Ensure that you have PostgreSQL installed and running on your machine.
- Create a database for the project by executing the following SQL command in your PostgreSQL client:
```bash
CREATE DATABASE student_profiles;
```

### 5. Configure the Database

```bash
DATABASE_URL=postgresql://username:password@localhost:5432/student_profiles

```
Replace username and password with your actual PostgreSQL credentials.

### 6. Run the Application

```bash
uvicorn app.main:app --reload

```
Replace username and password with your actual PostgreSQL credentials.

# Api Documentation

## Base URL
http://127.0.0.1:8000/

## Endpoints Overview

Below is a list of all available API endpoints:

| HTTP Method | Endpoint          | Description                                 |
|-------------|-------------------|---------------------------------------------|
| `POST`      | `/profiles/`  | Creates a new student profile               |

---

## Detailed Endpoint Documentation

### `POST /profiles/`

This endpoint is used to create a new student profile in the system.

#### Request URL:
POST : http://127.0.0.1:8000/profiles/


#### Request Body:

The request body should contain the student's information to create a profile. Here's the expected format:

```json
{
    "name": "shadiya",
    "email": "shadiya@example.com",
    "phone": "5467397576",
    "password": "Shadiya123!"
}
```
#### Response Body:
```json
{
    "name": "shadiya",
    "email": "shadiya@example.com",
    "phone": "5467397576"
}
    
```

#### Error Responses:
```json
{
    "detail": "Password must be at least 8 characters long, contain one uppercase, one lowercase, one digit, and one special character."
}
```

## Postman Collection

To help you easily test the API, a **Postman collection** is included with sample input data.

### How to Import the Postman Collection:

1. Open **Postman**.
2. Click on **File** > **Import**.
3. Select the `Student Profile API.postman_collection.json` file included in the project.
4. Once imported, you can run the requests directly from the collection.

### Sample Data for `/profile/` Request:

**Request Body Example:**

```json
{
    "name": "shadiya",
    "email": "shadiya@example.com",
    "phone": "5467397576",
    "password": "Shadiya123!"
}
```