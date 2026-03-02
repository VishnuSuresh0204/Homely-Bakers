# 🎂 HomelyCakes - Online Cake Booking System

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**HomelyCakes** is a premium Django-powered platform designed to bridge the gap between talented local bakers and cake enthusiasts. It offers a seamless, interactive experience for ordering customized cakes with real-time pricing and verified feedback.

---

## ✨ Premium Features

### 👤 For Customers

- **Visual Browsing**: Explore a curated collection of cakes with high-quality imagery.
- **Dynamic Customization**:
  - **Weight Selection**: Real-time price calculation for various weights (0.5kg to 5kg+).
  - **Special Add-ons**: Eggless options, low sugar, extra toppings, and more.
- **Order Tracking**: Comprehensive dashboard to monitor status from "Pending" to "Delivered".
- **Smart Feedback System**:
  - **Time-Locked Reviews**: Feedback can only be submitted after the delivery time.
  - **One-Per-Order**: Ensures authentic, unique reviews for every purchase.
  - **Full Control**: Edit or delete your feedback at any time.

### 👩‍🍳 For Bakers

- **Bakery Management**: Full CRUD operations for cake listings with support for multiple attributes.
- **Order Fulfillment**: Review detailed customization requests and manage delivery schedules.
- **Business Insights**: Access customer feedback specific to cake configurations to improve offerings.

### 🛠️ For Admin

- **User Governance**: Approve/reject baker registrations and manage user access.
- **Quality Control**: Oversee all feedback to ensure platform integrity.

---

## 🚀 Tech Stack

- **Backend**: Python / Django (Robust & Scalable)
- **Frontend**: Vanilla CSS (Premium Bellaria Theme), JavaScript (Real-time calculations)
- **Database**: SQLite (Development-ready)
- **Architecture**: MVC (Model-View-Controller)

---

## 🛠️ Installation & Setup

1. **Clone & Enter**:

   ```bash
   git clone https://github.com/VishnuSuresh0204/Homely-Bakers.git
   cd HomelyCakes
   ```

2. **Environment Setup**:

   ```bash
   python -m venv env
   .\env\Scripts\activate  # Windows
   source env/bin/activate # Linux/Mac
   ```

3. **Dependencies**:

   ```bash
   pip install django
   ```

4. **Database Initialization**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Launch**:
   ```bash
   python manage.py runserver
   ```
   Visit: `http://127.0.0.1:8000/`

---

## 📂 Project Structure

```text
HomelyCakes/
│
├── homelyproject/          # Root Project Config
├── cakeapp/                # Core Business Logic (Models, Views, Controllers)
├── templates/              # Beautifully crafted HTML layouts
├── static/                 # CSS, JS, and Media assets
└── README.md               # Project Documentation
```

---

_Developed with ❤️ for Homely Bakers._
