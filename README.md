🚀 Full-Stack Product Manager Dashboard

An intuitive and secure full-stack application for managing product inventory. The backend is built on the high-performance FastAPI framework, paired with a dynamic React.js frontend. This setup provides robust CRUD operations backed by secure JWT authentication.

✨ Key Features

Category
Features
🛡️ Security & Performance
Authentication

🔑 User Registration & Login
Secure Password Hashing (bcrypt)

🌐 JWT Token Generation
Protected API Routes via Token Verification

Product Management
➕ Add New Products

Full CRUD (Create, Read, Update, Delete)
📋 List & View Details
Frontend support for Sorting & Filtering

<img width="1034" height="399" alt="image" src="https://github.com/user-attachments/assets/6f7d9745-83bd-43ac-b97b-07c387bb06db" />

🧱 Project Structure

The project is logically separated into backend (FastAPI) and frontend (React).

backend/

backend/
├── main.py             # Core FastAPI Application & Routing
├── auth_models.py      # SQLAlchemy Schema for Users
├── auth_schemas.py     # Pydantic Schemas for Auth Payloads
├── utils_auth.py       # JWT and Hashing Utilities
├── database_models.py  # SQLAlchemy Schema for Products
├── database.py         # DB Connection and Session Handling
└── requirements.txt    # Python dependencies


frontend/

frontend/
├── src/App.js          # Main Component and Layout
├── src/login.js        # Login View
├── src/register.js     # Registration View
├── src/ProtectedRoute.js # Auth Wrapper for Routes
├── src/components/     # UI components (Forms, Tables, etc.)
└── package.json        # Node dependencies




🛠️ Installation and Setup

Follow these steps to get the application running locally.

1. 📂 Clone the Repository

git clone [https://github.com/YOUR_USERNAME/YOUR_REPO.git](https://github.com/YOUR_USERNAME/YOUR_REPO.git)
cd your-repo

2. 🐍 Backend Setup (FastAPI)
cd backend
# Create & activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# source venv/Scripts/activate # Windows

# Install dependencies
pip install -r requirements.txt

# Run the server with auto-reload
uvicorn main:app --reload

URL
Description
API Server
http://localhost:8000
Swagger Docs
http://localhost:8000/docs

3. ⚛️ Frontend Setup (React)
cd ../frontend

# Install node modules
npm install

# Start the development server
npm start

URL
http://localhost:3000

🔗 API Endpoints
All product management routes require authentication (Authorization: Bearer <token>).
Authentication

<img width="905" height="712" alt="image" src="https://github.com/user-attachments/assets/dca656e7-cc5f-45a8-963a-400d74c2bbff" />


☁️ Scalability & Production Planning

The current architecture is solid, but for production deployment, consider:
Security: Always store the SECRET_KEY in environment variables and enforce HTTPS.
Database: Migrate from SQLite to PostgreSQL for better reliability and performance.
Microservices: Decouple Authentication and Product Management into separate services.
Deployment: Dockerize the application for consistent, easy deployment across environments.

Caching: Integrate Redis to cache frequently accessed product data.
