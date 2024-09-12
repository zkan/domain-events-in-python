from dispatcher import dispatcher
from user_events import UserLoggedIn


def track_login(event: UserLoggedIn):
    print(f"Tracking login for user {event.user_id}")


dispatcher.register(UserLoggedIn, track_login)
