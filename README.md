# DJANGO-EVENT-CRM
An event booking and review CRM

GET /api/v1/users/  - Get all users
POST /api/v1/users/  - Create a new user
GET  /api/v1/users/:userid - Get user by id
PUT  /api/v1/users/:userid - Update user by id
DELETE  /api/v1/users/:userid - Delete User by id

GET /api/v1/events/  - Get all events
POST /api/v1/events/  - Create a new event
GET  /api/v1/events/:eventid - Get event by id
PUT  /api/v1/events/:eventid - Update event by id
DELETE  /api/v1/events/:eventid - Delete Event by id

GET /api/v1/reviews/  - Get all reviews
POST /api/v1/reviews/  - Create a new review { Takes user and event in request.body }
GET  /api/v1/reviews/:reviewid - Get review by id
PUT  /api/v1/reviews/:reviewid - Update review by id
DELETE  /api/v1/reviews/:reviewid - Delete review by id

GET /api/v1/bookings/  - Get all bookings
POST /api/v1/bookings/  - Create a new booking { Takes user and event in request.body }
GET  /api/v1/bookings/:bookingid - Get booking by id
DELETE  /api/v1/bookings/:bookingid - Delete booking by id
