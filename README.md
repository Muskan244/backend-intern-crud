# 📚 Blog API

A **FastAPI-based Blog CRUD API** with authentication, likes, and comments. Includes Postman collection for testing authorized and unauthorized requests.

---

## 🚀 Features
- **User Authentication** (Register, Login) with JWT
- **Blog CRUD** (Create, Read, Update, Delete)
- **Like** a blog (only once per user)
- **Comment** on blogs
- **Postman Collection** included for easy testing

---

## 🛠 Tech Stack
- **FastAPI** - Web framework
- **SQLAlchemy** - ORM for database operations
- **SQLite** - Database
- **Passlib** - Password hashing
- **python-jose** - JWT creation and verification
- **Pydantic** - Data validation

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/backend-intern-crud.git
cd backend-intern-crud
````

### 2️⃣ Create & activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate      # Mac/Linux
.venv\Scripts\activate         # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set up environment variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./test.db
```

### 5️⃣ Run database migrations (if needed)

```bash
# For SQLite (tables auto-created in dev mode)
```

### 6️⃣ Start the FastAPI server

```bash
python -m uvicorn src.main:app --reload
```

Server will be running at:
📌 `http://127.0.0.1:8000`

---

## 📬 API Endpoints

### Authentication

| Method | Endpoint             | Description         |
| ------ | -------------------- | ------------------- |
| POST   | `/api/auth/register` | Register a new user |
| POST   | `/api/auth/login`    | Login & get JWT     |

### Blogs

| Method | Endpoint          | Description    |
| ------ | ----------------- | -------------- |
| POST   | `/api/posts/`     | Create a blog  |
| GET    | `/api/posts/`     | Get all blogs  |
| GET    | `/api/posts/{id}` | Get blog by ID |
| PUT    | `/api/posts/{id}` | Update blog    |
| DELETE | `/api/posts/{id}` | Delete blog    |

### Likes

| Method | Endpoint               | Description |
| ------ | ---------------------- | ----------- |
| POST   | `/api/posts/{id}/like` | Like a blog |

### Comments

| Method | Endpoint                   | Description              |
| ------ | -------------------------- | ------------------------ |
| POST   | `/api/posts/{id}/comment`  | Add comment to a blog    |
| GET    | `/api/posts/{id}/comments` | Get all comments on blog |

---

## 🧪 Testing with Postman

1. Open **Postman**
2. Import the file:
   **`Blog API Assignment.postman_collection.json`**
3. Test authorized vs unauthorized requests.

---
