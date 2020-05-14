from dataclasses import dataclass, field

from twilio.rest import Client


@dataclass
class SMSNotifications:
    account_sid: str
    auth_token: str
    from_number: str
    client: Client = field(init=False)

    def __post_init__(self):
        self.client = Client(self.account_sid, self.auth_token)

    def send(self, body: str, to_number: str):
        message = self.client.messages.create(
            body=body, from_=self.from_number, to=to_number
        )
        print(f"Message with sid: {message.sid} to {to_number} sent.")
