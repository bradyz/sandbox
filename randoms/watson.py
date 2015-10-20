import time
from slackclient import SlackClient


token = "xoxb-12889087845-5Ji34EFPAgGSP0uqTzP6rQe2"


def do_stuff():
    sc = SlackClient(token)

    if not sc.rtm_connect():
        return

    while True:
        chat = sc.rtm_read()

        print(chat)

        if chat and "type" in chat[0] and chat[0]["type"] == "message":
            message = chat[0]["text"]

            if "reverse" in message:
                sc.rtm_send_message(chat[0]["channel"], "try reversed(my_arr)")
            elif "set" in message:
                sc.rtm_send_message(chat[0]["channel"], "my_set.add(val)")
            elif "dict" in message:
                sc.rtm_send_message(chat[0]["channel"], "my_key in my_dict")
            elif "lambda" in message:
                sc.rtm_send_message(chat[0]["channel"], "my_lambda = lambda x: x + 5")
            elif "thanks" in message and "watson" in message:
                sc.rtm_send_message(chat[0]["channel"], "no problem! :)")

        time.sleep(1)
    else:
        print("Connection Failed, invalid token?")

do_stuff()
