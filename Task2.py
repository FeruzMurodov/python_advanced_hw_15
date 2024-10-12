from datetime import datetime


def display_current_time():
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    result = f'Time: {formatted_date}\nWeekday: {now.strftime('%A')}\nWeek number: {now.isocalendar()[1]}'
    print(now)
    print(result)


if __name__ == '__main__':
    display_current_time()
