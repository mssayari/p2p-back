# db_init.py
from app import create_app
from extensions import db
from models.user import User
from models.module import Module

app = create_app()


def insert_demo_modules():
    demo_modules = [
        {"id": 1, "icon": "static/modules/maths.png", "name": "Math", "slug": "mathematics"},
        {"id": 2, "icon": "static/modules/ai.png", "name": "AI", "slug": "artificial-intelligence"},
        {"id": 3, "icon": "static/modules/python.png", "name": "Python", "slug": "python"},
        {"id": 4, "icon": "static/modules/c-plus-plus.png", "name": "C++", "slug": "c-plus-plus"},
        {"id": 5, "icon": "static/modules/android.png", "name": "Android", "slug": "android"},
        {"id": 6, "icon": "static/modules/html.png", "name": "HTML", "slug": "html"},
    ]

    for module_data in demo_modules:
        module = Module(**module_data)
        db.session.add(module)

    db.session.commit()


with app.app_context():
    try:
        # purge the database
        db.drop_all()
        print("Tables dropped successfully!")
        db.create_all()
        print("Tables created successfully!")
        insert_demo_modules()
        print("Demo modules inserted successfully!")
    except Exception as e:
        print(f"Error creating tables: {e}")
