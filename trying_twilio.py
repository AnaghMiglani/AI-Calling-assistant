import os
from twilio.rest import Client

from dotenv import load_dotenv
load_dotenv()


def _get_client_and_config():
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    twilio_from = os.getenv("TWILIO_PHONE_NUMBER")
    hosted_web = os.getenv("HOSTED_WEB")

    if not account_sid or not auth_token:
        raise RuntimeError("TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN must be set in the environment")

    client = Client(account_sid, auth_token)
    return client, twilio_from, hosted_web


def call_sleep(number):
    client, twilio_from, hosted_web = _get_client_and_config()
    url_base = hosted_web

    call = client.calls.create(
        url=f"{url_base}/api/say",
        to=number,
        from_=twilio_from,
    )

    print("sleeping", call.sid)


def call_wake(number):
    client, twilio_from, hosted_web = _get_client_and_config()
    url_base = hosted_web

    call = client.calls.create(
        url=f"{url_base}/api/wake",
        to=number,
        from_=twilio_from,
    )

    print("waking", call.sid)