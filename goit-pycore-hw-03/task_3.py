import re

def normalize_phone(phone_number):
    cleaned = re.sub(r'[^\d+]', '', phone_number)
    if cleaned.startswith('380'):
        cleaned = '+' + cleaned
    elif not cleaned.startswith('+'):
        cleaned = '+38' + cleaned
    
    return cleaned

examples = [
    "+38 067 999 88 77",     
    "80671234567",           
    "(050)8889900",      
    "044-555-66-77",         
    "   (093) 777 88 99   ", ]

for phone in examples:
    print(phone, "→", normalize_phone(phone))
