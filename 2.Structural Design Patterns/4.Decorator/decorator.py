class Notification:
    def send(self):
        raise NotImplementedError


class EmailNotification(Notification):
    def send(self):
        return "Sending Email Notification"


class NotificationDecorator(Notification):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def send(self):
        return self._wrapped.send()


class SMSDecorator(NotificationDecorator):
    def send(self):
        return f"{self._wrapped.send()} + Sending SMS Notification"


class PushDecorator(NotificationDecorator):
    def send(self):
        return f"{self._wrapped.send()} + Sending Push Notification"


# Khởi tạo EmailNotification
notification = EmailNotification()

# Trang trí bằng SMSDecorator
notification = SMSDecorator(notification)

# Trang trí thêm bằng PushDecorator
notification = PushDecorator(notification)

print(notification.send())
# Result: Sending Email Notification + Sending SMS Notification + Sending Push Notification
