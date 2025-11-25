from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        days_until_birthday = (birthday_this_year - today).days
        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Олег", "birthday": "1992.10.25"},
    {"name": "Анна", "birthday": "1995.10.26"},
    {"name": "Сергій", "birthday": "1980.10.27"},
    {"name": "Юлія", "birthday": "1991.11.01"},
]


birthdays = get_upcoming_birthdays(users)
print("Кого привітати цього тижня і в який день:")
for person in birthdays:
    print(f"{person['name']}: {person['congratulation_date']}")
