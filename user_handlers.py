from dispatcher import dispatcher
from user_events import UserLoggedIn, UserRegistered


def send_welcome_email(event: UserRegistered):
    print(f"Sending welcome email to {event.email}")


def log_login(event: UserLoggedIn):
    print(f"User {event.user_id} has logged in")


# Subscribe to the UserRegistered and UserLoggedIn events by registering handlers
dispatcher.register(UserRegistered, send_welcome_email)
dispatcher.register(UserLoggedIn, log_login)
