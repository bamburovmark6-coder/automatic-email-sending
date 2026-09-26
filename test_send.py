import yagmail
from datetime import datetime

sender_email = "ВАШ_АДРЕС_ПОЧТЫ"
sender_password = "ВАШ_ПАРОЛЬ"
receiver_email = "АДРЕС_ПОЛУЧАТЕЛЯ"
subject = "ЭТО_ТЕМА_ПИСЬМА"
body = "ЭТО_ТЕКСТ_ПИСЬМА"

try:
    yag = yagmail.SMTP(user=sender_email, password=sender_password)
    yag.send(to=receiver_email, subject=subject, contents=body)
    print("✅ Тестовое письмо успешно отправлено!")
except Exception as e:
    print(f"❌ Ошибка при отправке: {e}")
finally:
    yag.close()