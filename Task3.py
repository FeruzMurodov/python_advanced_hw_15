from datetime import datetime, timedelta


def find_day_on_calendar():
    now = datetime.now()
    day_count = int(input("Enter the number of days: "))
    delta = timedelta(days=day_count)
    new_date = now + delta
    new_formatted_date = new_date.strftime('%Y-%m-%d')
    return new_formatted_date


if __name__ == '__main__':
    print(datetime.now())
    print(find_day_on_calendar())
