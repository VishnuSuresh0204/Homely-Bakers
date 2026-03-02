# HomelyCakes - Online Cake Booking System

HomelyCakes is a Django-based web application that connects local bakers with customers. Customers can browse a variety of cakes, customize their orders based on weight and special instructions, and provide feedback after delivery.

## Features

### For Customers

- **Browse Cakes**: Explore a wide range of cakes with detailed descriptions and pricing.
- **Cake Customization**:
  - Select weight (500g, 1kg, 2kg, etc.) with automatic price scaling.
  - Add customization options (Eggless, Less Sugar, Extra Toppings, etc.).
- **Smart Pricing**: Real-time price updates based on weight and quantity before booking.
- **Booking Management**: Track order status (Pending, Accepted, Paid).
- **Secure Feedback**:
  - Provide feedback only once per order.
  - Submit feedback only after the scheduled delivery time has passed.
  - Edit or Delete feedback at any time.

### For Bakers

- **Product Management**: Add, update, and manage cake listings.
- **Order Management**: Accept or Reject incoming bookings.
- **Order Visibility**: View detailed customization requirements for every order.
- **Feedback Review**: See what customers are saying about specific cake configurations.

### For Admin

- **Overall Monitoring**: Manage bakers and users.
- **Feedback Oversight**: View all reviews across the platform.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Real-time pricing)
- **Database**: SQLite (Default Django)
- **Version Control**: Git

## Setup and Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd HomelyCakes
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv env
   .\env\Scripts\activate
   ```

3. **Install dependencies**:
   _(Ensure you have a requirements.txt, or install Django manually)_

   ```bash
   pip install django
   ```

4. **Apply Migrations**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Open `http://127.0.0.1:8000/` in your browser.

## Project Structure

- `homelyproject/`: Main Django project directory.
- `cakeapp/`: Core app containing models, views, and business logic.
- `templates/`: HTML templates for Admin, Baker, and User modules.
- `static/`: CSS, JS, and Images.
