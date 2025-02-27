# Flask MongoDB CRUD API

This is a Flask-based REST API that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource.

## Features
- Flask for API development
- MongoDB for database storage
- RESTful endpoints for user management
- Docker for easy deployment

## Prerequisites
Ensure you have the following installed on your machine:
- Python 3.8+
- pip (Python package manager)
- Docker & Docker Compose
- MongoDB (if running locally)

---

## 🚀 Setting Up Locally (Without Docker)

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Kalparatna/Fask-mogngo-crud.git
cd <project-folder>
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv env
source env/bin/activate  # For macOS/Linux
env\Scripts\activate    # For Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Configure Environment Variables**
Create a `.env` file in the project root and add:
```ini
FLASK_APP=run.py
FLASK_ENV=development
MONGO_URI=mongodb://localhost:27017/userdb
```

### **5️⃣ Start MongoDB (If Not Using Docker)**
Make sure MongoDB is running locally.
```bash
mongod --dbpath /path/to/your/db/folder
```

### **6️⃣ Run the Flask Application**
```bash
python run.py
```

---

## 🚀 Running With Docker

### **1️⃣ Build and Start Docker Containers**
```bash
docker-compose up --build
```
This will start:
- A Flask API container
- A MongoDB container

### **2️⃣ Check Running Containers**
```bash
docker ps
```

### **3️⃣ Access the API**
The API will be available at:
```
http://localhost:5000
```

---

## 🛠️ API Endpoints

### **1️⃣ Create a User (POST)**
```http
POST /users
```
**Request Body:**
```json
{
  "name": "Alice",
  "email": "alice@example.com",
  "password": "securepassword"
}
```

### **2️⃣ Get All Users (GET)**
```http
GET /users
```

### **3️⃣ Get a User by ID (GET)**
```http
GET /users/{id}
```

### **4️⃣ Update a User (PUT)**
```http
PUT /users/{id}
```
**Request Body:**
```json
{
  "name": "Alice Johnson",
  "email": "alice.johnson@example.com"
}
```

### **5️⃣ Delete a User (DELETE)**
```http
DELETE /users/{id}
```

---

## ✅ Testing the API with Postman
- Open **Postman**.
- Create new requests for each endpoint.
- Use **raw JSON** format for POST and PUT requests.

---
