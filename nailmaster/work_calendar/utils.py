from calendar import monthcalendar
from .models import Event


class Calendar:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def get_weeks(self):
        weeks = []
        month_days = monthcalendar(self.year, self.month)
        events = (
            Event.objects
            .filter(
                start_time__year=self.year,
                start_time__month=self.month
            )
            .select_related('user')
            .order_by('start_time')
        )
        for week in month_days:
            week_data = []
            for day in week:
                if day == 0:
                    week_data.append(None)
                else:
                    day_events = [
                        event for event in events
                        if event.start_time.day == day
                    ]
                    week_data.append({
                        'day': day,
                        'events': day_events
                    })
            weeks.append(week_data)
        return weeks
