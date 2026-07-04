# 🛍️ Mahnuva Fashion – POS & Inventory Management System

A real-world **Point of Sale (POS) and Inventory Management System** developed using **Django** for **Mahnuva Fashion**, designed to manage products, suppliers, stock, and daily sales operations efficiently.

This system centralizes all business operations into a single platform for smooth retail management.

---

## 🚀 Core Features

### 🔐 Authentication System

* Secure login system for system access
* Single-user operation (Admin/Operator only)
* Session-based authentication

---

### 📦 Inventory Management

* Add, update, and delete products
* Organize products by **categories**
* View complete product listings
* Real-time **stock tracking**

---

### 🗂 Category Management

* Create and manage product categories
* Helps organize inventory efficiently

---

### 🚚 Supplier Management

* Add and manage suppliers
* Maintain supplier records
* Link suppliers with inventory workflow

---

### 💰 Point of Sale (POS) System

* Interactive POS interface
* Add products to cart and process sales
* Automatically updates stock after each sale

---

### 🧾 Sales & Billing

* Generate **receipts** for each transaction
* Store transaction details in the system
* Maintain clean billing workflow

---

### 📊 Sales Tracking & Reports

* View **sales history**
* Sales summary dashboard
* Track daily/overall transactions

---

### 📉 Stock Monitoring

* Dedicated stock view page
* Helps prevent stock shortages
* Easy overview of inventory levels

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS (Django Templates)
* **Database:** SQLite
* **Architecture:** MVT (Model-View-Template)

---

## 📁 Project Structure

```id="a1b2c3"
POS_IMS_System/
│
├── auth_app/        # Authentication system
├── inventory/       # Products, categories, stock
├── sales/           # POS, receipts, sales history
├── suppliers/       # Supplier management
├── templates/       # UI templates
├── db.sqlite3       # Database
├── manage.py
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash id="b7x92k"
git clone <your-repo-link>
cd POS_IMS_System
```

### 2. Create virtual environment

```bash id="k29xpl"
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash id="m3pq8z"
pip install -r requirements.txt
```

### 4. Run migrations

```bash id="z91dka"
python manage.py migrate
```

### 5. Create admin user

```bash id="u7x4dn"
python manage.py createsuperuser
```

### 6. Start server

```bash id="p0q8ls"
python manage.py runserver
```

---

## 🌐 System Usage

* Main system: `http://127.0.0.1:8000/`
* Admin panel: `http://127.0.0.1:8000/admin/`

Login using your admin credentials to access:

* Inventory
* POS system
* Supplier management
* Sales history

---

## 🏢 Real-World Application

This system was developed for **Mahnuva Fashion**, a retail business, to:

* Digitize manual sales processes
* Maintain accurate inventory records
* Track supplier relationships
* Generate receipts and sales history
* Improve operational efficiency

---

## 🔮 Future Improvements

* Multi-user role system (cashier, manager)
* Advanced analytics dashboard
* Barcode scanning integration
* REST API (Django REST Framework)
* Frontend upgrade (React / Next.js)

---

## 👨‍💻 Author

Developed as a real-world project to solve business problems using Django and full-stack development practices.

---

## 📄 License

This project is intended for educational and organizational use.

---
