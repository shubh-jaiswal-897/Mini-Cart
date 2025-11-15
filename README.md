,
>>>>>>> b8f2c646db683e3171d896c7c2b8ac63cd943a7c
=======
# Minicart

Minicart is a full-functional e-commerce website built with Django, inspired by platforms like Flipkart. It features user authentication, product catalog, shopping cart, checkout, and order management.

## Features

- **User Authentication**: Register, login, and logout functionality
- **Product Catalog**: Browse products by categories with search
- **Shopping Cart**: Add, remove, and update items in cart
- **Checkout**: Place orders with address and phone details
- **Order History**: View past orders
- **Admin Panel**: Manage products, categories, and orders
- **Responsive Design**: Bootstrap-based UI for mobile and desktop

## Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/shubh-jaiswal-897/Mini-Cart.git
   cd Mini-Cart
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

4. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

5. **Run database migrations**:
   ```
   python manage.py migrate
   ```

6. **Create a superuser** (for admin access):
   ```
   python manage.py createsuperuser
   ```
   Follow the prompts to set username, email, and password.

7. **Run the development server**:
   ```
   python manage.py runserver
   ```

8. **Access the site**:
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Usage

- **As a User**:
  - Register a new account or login.
  - Browse products by category or search.
  - Add products to cart, view cart, and proceed to checkout.
  - View your order history.

- **As an Admin**:
  - Login to `/admin/` with superuser credentials.
  - Add/edit categories and products.
  - Manage orders and users.

## Admin Credentials

- **Username**: admin
- **Password**: admin123

*Note: Change the password after first login for security.*

## Technologies Used

- **Backend**: Django 5.2.8
- **Database**: SQLite (default)
- **Frontend**: HTML, CSS, Bootstrap 5.3.0
- **Icons**: Font Awesome

## Project Structure

```
minicart/
├── minicart/          # Project settings
├── store/             # Main app
│   ├── models.py      # Database models
│   ├── views.py       # View functions
│   ├── urls.py        # URL patterns
│   ├── templates/     # HTML templates
│   └── static/        # CSS, JS files
├── templates/         # Global templates
├── static/            # Static files
├── manage.py          # Django management script
└── README.md          # This file
```

## Contributing

Feel free to fork the repository and submit pull requests for improvements.

## License

This project is open-source and available under the MIT License.
=======
,
>>>>>>> b8f2c646db683e3171d896c7c2b8ac63cd943a7c
