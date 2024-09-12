from typing import Callable, List, Dict, Type


# Domain Event Base Class
class DomainEvent:
    def __init__(self):
        self.name = self.__class__.__name__


# Event Dispatcher to register and notify event handlers
class EventDispatcher:

    def __init__(self):
        self._handlers: Dict[Type[DomainEvent], List[Callable]] = {}

    def register(self, event_type: Type[DomainEvent], handler: Callable):
        """Register a handler for a specific domain event."""
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)

    def dispatch(self, event: DomainEvent):
        """Dispatch an event to all its registered handlers."""
        handlers = self._handlers.get(type(event), [])
        for handler in handlers:
            handler(event)


# Create an instance of EventDispatcher
dispatcher = EventDispatcher()
