def write_notification(email: str, message=''):
    with open('log.txt', mode='w') as email_file:
        content = f'Email: {email} - msg: {message}'
        email_file.write(content)