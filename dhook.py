#!/usr/bin/python3

from urllib.request import Request, urlopen
from urllib.parse import urlencode
import json
import sys
import getopt

def get_api_manager(api_base_url):
    def post(endpoint, parameters=None):
        url = api_base_url + endpoint
        # print(url)
        request = Request(url, urlencode(parameters).encode('utf-8') if parameters else None)
        request.add_header("User-Agent","WebhookExecutor (http://isogen.net/, 1.0)")
        site = urlopen(request)
        return site.read().decode('utf-8')
    return post

class DiscordWebhook:
    name   = None
    avatar = None

    def __init__(self, webhook_url):
        self.manager = get_api_manager(webhook_url)
        self.update()

    def update(self):
        try:
            webhook = json.loads(self.manager(""))
            self.__dict__.update(**webhook)
        except:
            raise Exception("Invalid Webhook Exception")

    def send(self, content):
        params = {
            "content":content,
            "username":self.name
        }
        if self.avatar:
            params['avatar_url'] = self.avatar

        self.manager("", params)


if __name__ == "__main__":
    webhook_id      = None
    webhook_token   = None
    webhook_content = None
    webhook_avatar  = None
    webhook_name    = None
    webhook_filename= None


    optlist, args = getopt.getopt(sys.argv[1:], 'i:t:a:n:f:', ["help"])

    for option, value in optlist:
        print(option)
        if option == "-i":
            webhook_id = value
        elif option == "-t":
            webhook_token = value
        elif option == "-a":
            webhook_avatar = value
        elif option == "-n":
            webhook_name = value
        elif option == "-f":
            webhook_filename = value
        elif option == "--help":
            print("\n".join([
                "dhook: CLI Discord Webhook Executor",
                "  Use: dhook -i<webhook id> -t<webhook token> <content>",
                "  OPTIONS:",
                "    -a<image url>    (Sets the avatar image of the message to the image at this url.)",
                "    -n<name>         (Sets the name of the webhook when posting message.)",
            ]))
            exit(0)
    try:
        webhook_content = args[0]
    except:
        print("Must provide message content.")
        exit(1)

    if not webhook_id:
        print("Must provide webhook id.")
        exit(1)

    if not webhook_token:
        print("Must provide webhook token.")
        exit(1)
    try:
        webhook = DiscordWebhook("https://discordapp.com/api/webhooks/{}/{}".format(webhook_id, webhook_token))
    except Exception as e:
        print(e)
        print("Invalid Webhook")
        exit(1)
    if webhook_name:
        webhook.name = webhook_name

    if webhook_avatar:
        webhook.avatar = webhook_avatar

    webhook.send(webhook_content)