class Event:
    def __init__(self, title, date, time):
        self.title = title
        self.date = date
        self.time = time

def filter_duplicate_events(events):
    unique_events = []
    seen_events = set()

    for event in events:
        event_key = (event.title, event.date, event.time)

        if event_key not in seen_events:
            seen_events.add(event_key)
            unique_events.append(event)
