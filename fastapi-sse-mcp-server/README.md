# FernAI Backend

This is the **FastAPI Backend** for the **FernAI Web Application**.

## Getting Started

Follow these steps to set up and run the backend locally.

### 1️⃣ Navigate to the Backend Directory

```sh
cd backend
```

### 2️⃣ Set Up a Virtual Environment

```sh
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows (use Git Bash or cmd)
```

### 3️⃣ Install Dependencies

```sh
pip3 install -r requirements.txt
```

### 4️⃣ Run the FastAPI Server

```sh
fastapi dev app/main.py
```

The server should now be running at [http://127.0.0.1:8000](http://127.0.0.1:8000).
