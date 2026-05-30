# URL Shortener

The URL Shortener is built using FastAPI and SQLite that generates short URLs, redirects users to the original URL, supports automatic expiration, reuses existing unexpired URLs, and handles short-code collisions.

## Features

* Generate short URLs from long URLs
* Redirect users using the short URL
* Automatic URL expiration after 30 days
* Reuse existing short URLs for unexpired links
* Collision detection and handling
* SQLite database storage
* Interactive API documentation with Swagger UI

## Tech Stack

* Python
* FastAPI
* SQLite
* Pydantic
* Uvicorn
* Git & GitHub

## Project Structure

```text
url-shortener/
│
├── main.py
├── database.py
├── schemas.py
├── utils.py
├── requirements.txt
├── README.md
└── .gitignore
```

## API Endpoints

### Home

```http
GET /
```

Response:

```json
{
  "message": "URL Shortener API"
}
```

### Create Short URL

```http
POST /shorten
```

Request Body:

```json
{
  "url": "https://www.google.com"
}
```

Response:

```json
{
  "short_code": "4Ln8Fd",
  "short_url": "http://127.0.0.1:8000/4Ln8Fd",
  "expires_at": "2026-06-29",
  "message": "New short URL created"
}
```

### Redirect

```http
GET /{short_code}
```

Example:

```http
GET /4Ln8Fd
```

Redirects the user to the original URL.

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd url-shortener
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

to access the Swagger API documentation.

## Future Improvements

* Custom aliases
* Analytics dashboard
* QR code generation
* User authentication
* Deployment with PostgreSQL

## Author

Venkata Vamsi Reddy Yeruva

IIT Hyderabad
