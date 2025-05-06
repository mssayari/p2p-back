# P2P Backend

A **Flask-based API** for Our P2P startup managing users, tutors, bookings, messages, and modules. This project provides endpoints for user authentication, tutor management, booking creation, messaging, and more.

---

## Features

- **User Authentication**: Register, login, logout, and refresh tokens.
- **Tutor Management**: View tutors, filter by skills, and update tutor details.
- **Booking System**: Create, view, confirm, and cancel bookings.
- **Messaging System**: Send and retrieve messages between users.
- **Modules Management**: Retrieve available modules.
- **Static File Serving**: Serve avatars and module-related static files.

---

## Technologies Used

- **Python**: Core programming language.
- **Flask**: Web framework for building the API.
- **Flask-JWT-Extended**: For authentication and token management.
- **Flask-CORS**: To handle cross-origin requests.
- **SQLAlchemy**: ORM for database interactions.
- **Werkzeug**: For password hashing and validation.

---

## Installation
1. Go to the project directory: 
2Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   - Configure your database in the `Config` class in `config.py`.
   - Run migrations (if applicable) or initialize the database.

4. Run the application:
   ```bash
   python app.py
   ```

---

## API Endpoints

### **Authentication**
- `POST /auth/login`: Login and retrieve access/refresh tokens.
- `POST /auth/register`: Register a new user.
- `POST /auth/logout`: Logout the user.
- `POST /auth/refresh`: Refresh the access token.

### **Users**
- `PUT /users/update`: Update user details.
- `DELETE /users/delete`: Delete the current user.
- `GET /tutors`: Retrieve all tutors.
- `GET /tutors/<tutor_id>`: Retrieve a specific tutor.
- `GET /tutors/skills/<skill_id>`: Retrieve tutors by skill.

### **Bookings**
- `POST /bookings`: Create a new booking.
- `GET /bookings`: Retrieve bookings for the current user.
- `GET /bookings/<booking_id>`: Retrieve a specific booking.
- `PUT /bookings/<booking_id>/confirm`: Confirm a booking.
- `PUT /bookings/<booking_id>/cancel`: Cancel a booking.

### **Messages**
- `POST /messages`: Send a message.
- `GET /messages`: Retrieve all messages with tutors.
- `GET /messages/<user_id>`: Retrieve messages with a specific user.

### **Modules**
- `GET /modules/all`: Retrieve all available modules.

### **General**
- `GET /`: Welcome message.
- `GET /protected`: Access a protected route.
- `GET /avatars/<filename>`: Retrieve user avatars.
- `GET /static/modules/<filename>`: Retrieve module-related static files.

---

## Database Models

### **User**
- Stores user details, including name, email, password, and tutor-specific fields like skills, rate, and availability.

### **Booking**
- Represents a booking between a student and a tutor, with fields for date, time, price, and status.

### **Message**
- Represents messages exchanged between users, with fields for sender, receiver, content, and read status.

### **Module**
- Represents a skill or subject area, with fields for name, slug, and icon.