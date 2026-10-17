# Restaurant Menu Management System

A complete Django beginner project for managing a restaurant's menu items, chefs, and categories.

## Quick Start

### 1. Install Django
```bash
pip install -r requirements.txt
```

### 2. Setup Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Admin User
```bash
python manage.py createsuperuser
# Username: admin
# Email: admin@example.com
# Password: (enter password)
```

### 4. Run Server
```bash
python manage.py runserver
```

### 5. Visit Application
- **Home:** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin/

## Features

✅ Menu Items Management
✅ Chef Management
✅ Category Management
✅ Admin Panel with Search & Filtering
✅ Responsive Design
✅ Form Validation

## Project Structure

```
Restaurant_Project/
├── manage.py
├── requirements.txt
├── README.md
├── Restaurant_prj/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── menu/
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── urls.py
    ├── admin.py
    ├── templates/menu/
    │   ├── base.html
    │   ├── home.html
    │   ├── menu_list.html
    │   ├── menu_detail.html
    │   ├── menu_item_form.html
    │   ├── chef_list.html
    │   ├── chef_form.html
    │   └── category_list.html
    └── migrations/
```

## URLs

| URL | Purpose |
|-----|---------|
| `/` | Home page |
| `/menu-list/` | All menu items |
| `/menu-detail/` | Item details |
| `/add-menu-item/` | Add item form |
| `/chef-list/` | All chefs |
| `/add-chef/` | Add chef form |
| `/category-list/` | All categories |
| `/admin/` | Admin panel |

## Next Steps

1. Add data via admin panel
2. Explore the application
3. Modify templates and styles
4. Add new features

Enjoy! 🍽️
