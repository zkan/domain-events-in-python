from user import User
from user_handlers import dispatcher


if __name__ == "__main__":
    # Create a user and trigger domain events
    user = User(user_id=1, email="user@example.com", dispatcher=dispatcher)

    # This triggers the UserRegistered event and sends the welcome email
    user.register()
    # This triggers the UserLoggedIn event and logs the login
    user.login()

    print(dispatcher._handlers)
    print("--------------------------")

    # ------------- Different domain -------------

    import analytics_handlers


    # When a user logs in again, it will dispatch an event to analytics domain
    user.login()

    print(dispatcher._handlers)
