from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta = today - input_date
        return delta.days
    except ValueError:
        return "Невірний формат дати. Використовуйте 'YYYY-MM-DD'."
    
print(get_days_from_today("2021-07-09"))
print(get_days_from_today("2030-05-21"))
print(get_days_from_today("20-10-09"))  # Неправильний формат
