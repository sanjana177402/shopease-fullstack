# 🛍️ ShopEase — Full Stack E-Commerce Platform

A full-stack e-commerce web application built with **Django REST Framework** (backend) and **HTML/CSS/JavaScript** (frontend), deployed on **Render** with **PostgreSQL** as the database.

🔗 **Live Demo:** [https://shopease-fullstack.onrender.com](https://shopease-fullstack.onrender.com)  
📦 **GitHub:** [https://github.com/sanjana177402/shopease-fullstack](https://github.com/sanjana177402/shopease-fullstack)

---

## 📌 Features

### 👤 Authentication
- User registration and login
- JWT token-based authentication
- Role support: `customer` and `admin`

### 🛒 Products
- Browse all products with images, price, and description
- Search products by name
- Filter by category
- Sort by price (low → high / high → low)
- Pagination (5 products per page)

### 📦 Categories
- Products organized into categories
- Filter products by category from the frontend

### 🛒 Cart
- Add products to cart
- Update quantity (increase/decrease)
- Remove items from cart
- Real-time total price calculation

### 💳 Orders
- Place orders from cart
- View order history with product images
- Order status tracking: `placed` → `shipped` → `delivered` → `cancelled`

### ❤️ Wishlist
- Add products to wishlist
- View and remove wishlist items

### 🔐 Admin
- Django admin panel for managing products, categories, orders
- Only admin users can create, update, or delete products
- Admin can update order status directly from the admin panel

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 5.2, Django REST Framework |
| Authentication | JWT (djangorestframework-simplejwt) |
| Database | PostgreSQL (via Render) |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Render (Web Service + PostgreSQL) |
| Media | Unsplash image URLs |

---

## 📁 Project Structure

```
shopease-fullstack/
│
├── ecommerce/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── users/              # User registration, login, JWT auth
├── products/           # Product CRUD with search, filter, sort
├── categories/         # Product categories
├── cart/               # Cart management
├── orders/             # Order placement and tracking
│
├── frontend/           # HTML/CSS/JS frontend
│   ├── index.html      # Products page
│   ├── register.html   # Register page
│   ├── login.html      # Login page
│   ├── cart.html       # Cart page
│   ├── orders.html     # Orders page
│   ├── payment.html    # Payment page
│   └── wishlist.html   # Wishlist page
│
├── requirements.txt
├── runtime.txt
└── README.md
```

---

## 🔗 API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/users/register/` | Register a new user |
| POST | `/users/login/` | Login and get JWT token |
| GET | `/users/me/` | Get logged-in user profile |

### Products
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/products/` | List all products (with search, filter, sort, pagination) |
| GET | `/products/:id/` | Get single product |
| POST | `/products/` | Admin: Create product |
| PUT | `/products/:id/` | Admin: Update product |
| DELETE | `/products/:id/` | Admin: Delete product |

### Categories
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/categories/` | List all categories |
| POST | `/categories/` | Admin: Create category |

### Cart
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/cart/?userId=` | View cart |
| POST | `/cart/add/` | Add item to cart |
| PUT | `/cart/update/` | Update item quantity |
| DELETE | `/cart/remove/:productId/` | Remove item from cart |

### Orders
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/orders/` | Place an order |
| GET | `/orders/?userId=` | Get user orders |
| GET | `/orders/:id/` | Get single order |
| GET | `/orders/admin/orders/` | Admin: Get all orders |
| PUT | `/orders/admin/orders/:id/status/` | Admin: Update order status |

---

## 🚀 Local Setup

### Prerequisites
- Python 3.11+
- PostgreSQL (or use SQLite for local dev)
- Git

### Steps

```bash
# 1. Clone the repo
git clone https://github.com/sanjana177402/shopease-fullstack.git
cd shopease-fullstack/ecommerce

# 2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create superuser
python manage.py createsuperuser

# 6. Run server
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to see the app!

---

## 🌐 Deployment

The app is deployed on **Render** as a Web Service with:
- **Gunicorn** as the WSGI server
- **PostgreSQL** as the production database (via Render managed DB)
- **Environment variable** `DATABASE_URL` for secure DB connection
- **Static files** served via Django

---

## 👩‍💻 Developed By

**Sanjana R**  
Full Stack Django Project — Internship 2025-26

---

## 📸 Pages

| Page | URL |
|------|-----|
| Products | `/` |
| Register | `/register/` |
| Login | `/login/` |
| Cart | `/page/cart/` |
| Orders | `/page/orders/` |
| Payment | `/payment/` |
| Wishlist | `/wishlist/` |
| Admin | `/admin/` |