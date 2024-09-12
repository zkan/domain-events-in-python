from dispatcher import DomainEvent


class UserRegistered(DomainEvent):
    def __init__(self, user_id: int, email: str):
        super().__init__()
        self.user_id = user_id
        self.email = email


class UserLoggedIn(DomainEvent):
    def __init__(self, user_id: int):
        super().__init__()
        self.user_id = user_id
