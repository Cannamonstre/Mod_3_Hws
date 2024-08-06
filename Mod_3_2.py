def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if not (recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net')):
        print(f'Unable to send a message. Check recipient.')
    elif not (sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net')):
        print(f'Unable to send a message. Check sender.')
    elif not ('@' in recipient and '@' in sender):
        print(f'Unable to send a message.')
    elif sender == recipient:
        print(f"Unable to send a message to yourself.")
    elif sender == 'university.help@gmail.com':
        print(f"Email has been successfully sent from {sender} to {recipient}")
    elif not sender == 'university.help@gmail.com':
        print(f"IRREGULAR SENDER! Letter has been sent from {sender} to {recipient}")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
