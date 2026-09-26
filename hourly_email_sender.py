import yagmail
from datetime import datetime
import time
import os

# ========== Настройки ==========
sender_email = "ВАШ_АДРЕС_ПОЧТЫ"
sender_password = "ВАШ_ПАРОЛЬ_ОТ_ПОЧТЫ_ЗДЕСЬ"
receiver_email = ["АДРЕС_ПОЛУЧАТЕЛЯ", "АДРЕС_ПОЛУЧАТЕЛЯ"]
subject = "ЭТО_ТЕМА_ПИСЬМА"
your_attachments = r"ПУТЬ_К_ВАШЕМУ_ФАЙЛУ"
body_text = "ЭТО_ТЕКСТ_ПИСЬМА"

# Проверка существования файла
if not os.path.exists(your_attachments):
    print(f"❌ Файл не найден по пути: {your_attachments}")
    exit(1)

# ========== Подключение к почте ==========
try:
    yag = yagmail.SMTP(user=sender_email, password=sender_password)
    print("✅ Успешно подключились к Gmail")
except Exception as e:
    print(f"❌ Не удалось подключиться к Gmail: {e}")
    exit(1)

# ========== Бесконечный цикл отправки ==========
try:
    while True:
        now = datetime.now().strftime('%Y-%m-%d %H:%M')
        body = f"{body_text}\n\nОтправлено автоматически в {now}."

        try:
            yag.send(
                to=receiver_email,
                subject=subject,
                contents=body,
                attachments=[your_attachments]
            )
            print(f"[{now}] ✅ Письмо успешно отправлено")
        except Exception as e:
            print(f"[{now}] ❌ Ошибка при отправке: {e}")

        time.sleep(3600)

except KeyboardInterrupt:
    print("\n⏹ Отправка остановлена вручную.")
finally:
    yag.close()
    print("🔒 Соединение с Gmail закрыто.")