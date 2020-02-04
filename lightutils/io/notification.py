__all__ = ['send_email_notification']

import yagmail

yag = yagmail.SMTP(user="lightfight@qq.com", password="bvxvmqapqqpideah", host="smtp.qq.com", port="465")


def send_email_notification(to, subject, contents):
    """
    a function which can send an email
    :param to: the mailbox of recipient
    :param subject: the subject of the email
    :param contents: the content of email
    :return: True or False
    """
    try:
        yag.send(to=to, subject=subject, contents=contents)
        return True
    except Exception as e:
        return False
