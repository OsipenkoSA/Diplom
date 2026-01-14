from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event
from django.utils.html import escape


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # формирование дня с событиями в td
    def formatday(self, day, events):
        # Фильтруем события для текущего дня и сортируем по времени начала
        events_per_day = (
            events
            .filter(start_time__day=day)
            .order_by('start_time')  # Сортировка по времени (от раннего к позднему)
        )

        event_items = []  # Список для HTML‑элементов

        for event in events_per_day:
            # Проверяем наличие start_time
            if not event.start_time:
                continue

            # Форматируем время с ведущими нулями (09:05, а не 9:5)
            hour = f"{event.start_time.hour:02d}"
            minute = f"{event.start_time.minute:02d}"

            # Экранируем данные для защиты от XSS
            first_name = escape(event.user.first_name)
            name = escape(event.user)
            title = escape(event.title)

            # Собираем <li> с отступами для читаемости HTML
            item = (
                f'<li style="border-bottom: 1px solid #DAA520;">'
                f'{hour}:{minute} {first_name} {name} {title}'
                f'</li>'
            )
            event_items.append(item)

        # Объединяем элементы без лишних пробелов
        events_html = ''.join(event_items)

        # Формируем ячейку таблицы
        if day != 0:
            return f"""
            <td>
                <span class='date'>{day}</span>
                <ul>{events_html}</ul>
            </td>
            """
        return '<td></td>'

    # формирование недели в tr
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    # формирование месяца в таблицу
    def formatmonth(self, withyear=True):
        events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal
