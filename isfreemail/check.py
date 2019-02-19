from .freeservers import FREE_MAIL_SERVERS


def is_free_mail(email):
    """
    Check if email address is from a free email service provider.
    Does not validate email address format and may return False if email address format is invalid.

    :param email: email address
    :return: True if given email address is from free email hosting provider, False otherwise.
    """
    parts = email.split('@')
    if len(parts) < 2:
        # looks like an invalid email address, we'll say it's not free email server
        return False
    mail_server = parts[-1].strip().lower()

    return mail_server in FREE_MAIL_SERVERS
