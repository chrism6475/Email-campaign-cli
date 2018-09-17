import requests
import json
import urllib

HEADERS = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Response-Type': 'application/json'
}

API_URL = 'https://christianmichel107.api-us1.com'
API_KEY = 'API'


# class for Mailing List. Will have functions to add mailing list
class SenderInfo:

    def __init__(self, sender_name, sender_address, sender_zip, sender_country, sender_url):
        self.sender_name = sender_name
        self.sender_address = sender_address
        self.sender_zip = sender_zip
        self.sender_country = sender_country
        self.sender_url = sender_url


class MailingList:

    def add_mailing_list(self, new_subscriptions):
        url_append = {
            'api_action': 'list_add',
            'api_key': API_KEY,
            'api_output': 'serialize'
        }
        url = API_URL + '/admin/api.php?' + urllib.parse.urlencode(url_append)
        print(new_subscriptions)
        data = {

            'name': self.list_name,
            'subscription_notify': 'chrism6475@gwu.edu',
            'subscription_notify': '',
            'unsubscription_notify': '',
            'to_name' : "Recipient",
            'carboncopy': '',
            'p_use_captcha': 1,
            'get_unsubscribe_reason': 1,
            'send_last_broadcast': 1,
            'require_name': 1,
            'sender_name': self.sender_name,
            'sender_addr1': self.sender_address,
            'sender_zip': self.sender_zip,
            'sender_city': self.sender_city,
            'sender_country': self.sender_country,
            'sender_url': self.sender_url,
            'sender_reminder': 'You subscribed on our web site'

        }

        request = requests.post(url, data=urllib.parse.urlencode(data), headers=HEADERS)

        if request.status_code == 200:
            print(request.content)
        else:
            print(request.status_code)

    def __init__(self, list_name, sender_name, sender_address, sender_city, sender_zip, sender_country, sender_url):
        self.list_name = list_name
        self.sender_name = sender_name
        self.sender_address = sender_address
        self.sender_city = sender_city
        self.sender_zip = sender_zip
        self.sender_country = sender_country
        self.sender_url = sender_url


class Message:

    def new_message(self, subject, message_text):

        data = {
            'api_action': 'message_add',
            'api_key': API_KEY,
            'format': 'text',
            'subject': subject,
            'fromemail': 'christianmichel107@gmail.com',
            'fromename': 'Christian Michel',
            'reply2': 'cmichel@arcadia.edu',
            'priority': '1',
            'charset':'utf-8',
            'encoding': 'quoted-printable',
            'htmlconstructor': 'editor',
            'html':'<strong>HTML</strong>',
            'htmlfetch':'http://somedomain.com/somepage.html',
            'htmlfetchwhen': 'send',
            'textconstructor':'external',
            'textfetch': 'http://yoursite.com',
            'textfetchwhen': 'send',
            'p[1]': 1,


        }

def main():

    # Request Distribution list from user:
    new_subscriptions = map(int, input().split(','))
    # Generate new mailing list
    list = MailingList('test', 'Christian Michel', 'NGC', 'Chicago','60647', 'USA', 'https://github.com/chrism6475')
    list.add_mailing_list(new_subscriptions)

    """data = {
        'type': 'single',
        'segmentid': 0,
        'bounceid': -1,
        'name': 'Coding_Assessment',
        'status': 0,
        'public': 0,
        'mailer_log_file': 4,
        'tracklinks': 'all',



    }
    response = requests.post(API_URL, data=data, timeout=5, headers=HEADERS)

    if response.status_code == 200:
        print(response.content)
        response_content = json.loads(response.content)
    else:
        print('error')
    """


if __name__ == '__main__':
    main()
