# Kangacook Test Server

This is the backend server for the Kangacook application, built with Django.

## Prerequisites

- Python 3.x
- pip (Python package installer)
- Virtual environment (optional but recommended)

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/jon-slva/kangacook-test-server.git
cd kangacook-test-server
```

### 2. Create and Activate a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages using pip.

```sh
pip install -r requirements.txt
```

### 4. Run the Server
Start the Django development server.

```
python3 manage.py runserver
```

The server will start at http://127.0.0.1:8000/ by default.


## Additional Information
### CORS Origin
CORS is only set to accept requests from these addresses:

```
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
```
