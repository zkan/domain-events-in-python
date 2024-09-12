from user import User
from user_handlers import dispatcher


# Create a user and trigger domain events
user = User(user_id=1, email="user@example.com", dispatcher=dispatcher)
user.register()  # This triggers the UserRegistered event and sends the welcome email
user.login()     # This triggers the UserLoggedIn event and logs the login

# ------------- Different domain -------------

import analytics_handlers


# When a user logs in again, it will dispatch an event to analytics domain
user.login()
