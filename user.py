from dispatcher import EventDispatcher
from user_events import UserLoggedIn, UserRegistered


# Domain Entity Example
class User:
    def __init__(self, user_id: int, email: str, dispatcher: EventDispatcher):
        self.user_id = user_id
        self.email = email
        self._dispatcher = dispatcher

    def register(self):
        print(f"Registering user {self.user_id}")
        event = UserRegistered(self.user_id, self.email)
        self._dispatcher.dispatch(event)

    def login(self):
        print(f"User {self.user_id} logging in")
        event = UserLoggedIn(self.user_id)
        self._dispatcher.dispatch(event)
