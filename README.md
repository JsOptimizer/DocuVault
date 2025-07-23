# DocuVault

A secure, modular backend API for document management, built with Flask.

---

## 🧩 Project Overview

DocuVault is a robust backend system designed to securely manage, organize, and version documents for teams, companies, and individuals. It provides:

- User authentication and role-based permissions
- File upload/download with folder structures (like Google Drive)
- Document versioning
- Activity/audit logging
- Admin dashboard endpoints

---

## 🚀 Target Users

- **Organizations** needing internal document sharing and version control
- **Freelancers/Individuals** managing personal or legal documents
- **Third-party integrations** (React, Next.js, Flutter, etc.)

---

## ⚙️ Core Features

### ✅ Authentication & Authorization

- JWT-based authentication (access & refresh tokens)
- Role-based permissions: Admin, Editor, Viewer
- User registration, login, password reset

### 📂 Document Management

- Upload documents (PDF, Word, images, etc.)
- Folder support (nested structure)
- Document versioning
- File download
- Soft delete & restore

### 👤 User Roles

- **Admin:** Full access, user/role management
- **Editor:** Upload, update, delete docs
- **Viewer:** Read/download only

### 🧾 Activity Logs

- Track all user activities (upload, delete, login, etc.)
- Admin endpoint for audit logs

### 📊 Admin Endpoints

- User statistics
- Storage usage
- Most accessed documents

---

## 🏗️ System Architecture

- Modular Flask app (see `flaskr/` directory)
- RESTful API endpoints
- Configurable via environment variables
- Dockerfile & Compose for local/dev/prod

---

## 📁 Project Structure

```
duc_velo_backenc/
├── compose.yaml
├── Dockerfile
├── flaskr/
│   ├── __init__.py
│   ├── extension/
│   │   ├── __init__.py
│   │   └── core.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── document.py
│   │   └── user.py
│   ├── repositories/
│   │   └── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── auth.py
│   ├── schema/
│   │   └── __init__.py
│   ├── services/
│   │   └── __init__.py
│   └── utils/
│       └── __init__.py
├── instance/
├── Pipfile
├── Pipfile.lock
├── pyproject.toml
├── README.Docker.md
├── README.md
└── requirements.txt
```

---

## 🛠️ Setup & Installation

### 1. Clone the repository

```bash
git clone <repo-url>
cd duc_velo_backenc
```

### 2. Environment Variables

Create a `.env` file in the project root (or use `instance/config.py`). Example:

```env
SECRET_KEY=your-secret-key
POSTGRES_USER=youruser
POSTGRES_PASSWORD=yourpassword
POSTGRES_DB=docuvault
```

- The `instance/` folder is used for instance-specific configuration (e.g., `config.py`).
- For Docker, environment variables can be set in the `compose.yaml` file.

### 3. Local Development (without Docker)

```bash
pip install -r requirements.txt
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

### 4. Using Docker

Build and run with Docker Compose:

```bash
docker compose up --build
```

- API: http://localhost:5000
- Adminer (DB UI): http://localhost:8080

---

## 🧪 Testing

- Use `pytest` or `unittest` (to be implemented)

---

## 📚 API Endpoints Overview

| Method | Endpoint               | Description             | Auth |
| ------ | ---------------------- | ----------------------- | ---- |
| POST   | /auth/register         | Register a new user     | ❌   |
| POST   | /auth/login            | Login and get JWT token | ❌   |
| POST   | /auth/refresh          | Refresh token           | ✅   |
| GET    | /documents/            | List all user documents | ✅   |
| POST   | /documents/            | Upload document         | ✅   |
| GET    | /documents/<id>        | Get document by ID      | ✅   |
| DELETE | /documents/<id>        | Soft delete document    | ✅   |
| PUT    | /documents/<id>        | Update metadata/version | ✅   |
| GET    | /admin/logs            | View activity logs      | 🔒   |
| GET    | /admin/users           | View all users          | 🔒   |
| PUT    | /admin/users/<id>/role | Change user role        | 🔒   |

- `✅` = Authenticated
- `🔒` = Admin only

---

## 📝 Development Notes

- Modularize features using Flask Blueprints (see `flaskr/routes/`)
- Use Marshmallow for request/response validation
- Use Alembic for DB migrations
- Store files locally in dev, S3 in production
- All config via `.env` or `instance/config.py`

---

## 🐳 Docker & Deployment

- Build: `docker build -t docuvault .`
- Run: `docker compose up --build`
- Deploy: Push image to your registry and deploy as needed

---

## 📄 References

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker's Python guide](https://docs.docker.com/language/python/)
- [12-Factor App](https://12factor.net/)

---

## License

MIT (or specify your license)
