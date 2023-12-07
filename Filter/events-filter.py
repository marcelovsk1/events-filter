class Event:
    def __init__(self, title, date, startTime, endTime):
        self.title = title
        self.date = date
        self.startTime = startTime
        self.endTime = endTime

def filter_duplicate_events(events):
    unique_events = []
    seen_events = set()

    for event in events:
        event_key = ( event.date, event.startTime, event.endTime )

        if event_key not in seen_events:
            seen_events.add(event_key)
            unique_events.append(event)

    return unique_events

events_data = [
    {"title": "Rocket de Laval vs. Belleville Senators", "date": "Dec 6", "startTime": "Wed • 7:00pm", "endTime": "Wed • 11:59pm" },
    {"title": "Montreal Canadiens vs. Los Angeles Kings", "date": "Dec 7", "startTime": "Thu • 7:00pm", "endTime": "Thu • 10pm" },
    {"title": "Rocket de Laval vs. Belleville Senators", "date": "Dec 6", "startTime": "Wed • 7:00pm", "endTime": "Wed • 11pm" },
    {"title": "Rocket de Laval vs. Hartford Wolf Pack", "date": "Dec 8", "startTime": "Fri • 7:00pm", "endTime": "Wed • 9:30pm"}
]

events = [Event(event["title"], event["date"], event["startTime"], event["endTime"]) for event in events_data]

filtered_events = filter_duplicate_events(events)

for event in filtered_events:
    print(f"Title: {event.title}, Date: {event.date}, startTime: {event.startTime}, endTime: {event.endTime}")
