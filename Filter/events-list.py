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

    return unique_events

events_data = [
    {"title": "Rocket de Laval vs. Belleville Senators", "date": "Dec 6", "time": "Wed • 7:00pm" },
    {"title": "Montreal Canadiens vs. Los Angeles Kings", "date": "Dec 7", "time": "Thu • 7:00pm" },
    {"title": "Rocket de Laval vs. Belleville Senators", "date": "Dec 6", "time": "Wed • 7:00pm" },
    {"title": "Rocket de Laval vs. Hartford Wolf Pack", "date": "Dec 8", "time": "Fri • 7:00pm"}
]

events = [Event(event["title"], event["date"], event["time"]) for event in events_data]

filtered_events = filter_duplicate_events(events)
