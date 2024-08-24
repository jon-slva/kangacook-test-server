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
### Running Tests
To run the tests, use the following command:

```
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
```


## The Late Submission

If you are reading this, I want to apologize - had a serious family emergency this week and had to step away from this. It's been a very difficult year of searching very hard and applying and networking every day all day since graduating from my bootcamp in December. I'm doing career switch not just because I needed to, but because I love technology. I know if someone gives me a chance, my great past experience and my hard work and dedication, and drive to always learn new things will not let you down. I've never used Django before and haven't used python in a long time, and I am already proud of myself for making this server work. Thank you for the challenge. I really hope to join your team. Sorry for the late submission, I hope you'll understand. Thank you so much for the consideration and I hope you have an amazing weekend!