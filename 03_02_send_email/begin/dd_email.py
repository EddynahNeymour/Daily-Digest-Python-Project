import dd_content
import datetime

class DailyDigestEmail:

    def __init__(self):
        self.content = {'quote': {'include': True, 'content': dd_content.get_random_quote()},
                        'sale': {'include': True, 'content': dd_content.get_sale_events()},
                        'instagram': {'include': True, 'content': dd_content.get_instagram_trends()},
                        'article': {'include': True, 'content': dd_content.get_skincare_article()}}

    def send_email(self):
        pass

    """
    Generate email message body as Plaintext and HTML.
    """
    def format_message(self):
        ##############################
        ##### Generate Plaintext #####
        ##############################
        text = f'*~*~*~*~* Daily Digest - {datetime.date.today().strftime("%d %b %Y")} *~*~*~*~*\n\n'

        # format random quote
        if self.content['quote']['include'] and self.content['quote']['content']:
            text += '*~*~* Quote of the Day *~*~*\n\n'
            text += f'"{self.content["quote"]["content"]["quote"]}" - {self.content["quote"]["content"]["author"]}\n\n'

        # format sale events
        if self.content['sale']['include'] and self.content['sale']['content']:
            text += f'*~*~* Dates for {self.content["sale"]["content"]["city"]}, {self.content["sale"]["content"]["country"]} *~*~*\n\n'
            for events in self.content['sale']['content']['periods']:
                text += f'{events["timestamp"].strftime("%d %b %H%M")} - {events["dates"]}\u00B0C | {events["description"]}\n'
            text += '\n'

        # format Instagram trends
        if self.content['instagram']['include'] and self.content['instagram']['content']:
            text += '*~*~* Top Ten Instagram Trends *~*~*\n\n'
            for trend in self.content['instagram']['content'][0:10]: # top ten
                text += f'{trend["name"]}\n'
            text += '\n'

        # format fashion article
        if self.content['fashion']['include'] and self.content['fashion']['content']:
            text += '*~*~* Daily Fashion Scoop *~*~*\n\n'
            text += f'{self.content["fashion"]["content"]["title"]}\n{self.content["fashion"]["content"]["extract"]}'
        
        #########################
        ##### Generate HTML #####
        #########################
        html = f"""<html>
    <body>
    <center>
        <h1>Daily Digest - {datetime.date.today().strftime('%d %b %Y')}</h1>
        """

        # format random quote
        if self.content['quote']['include'] and self.content['quote']['content']:
            html += f"""
        <h2>Quote of the Day</h2>
        <i>"{self.content['quote']['content']['quote']}"</i> - {self.content['quote']['content']['author']}
        """

        # format sale events
        if self.content['sale']['include'] and self.content['sale']['content']:
            html += f"""
        <h2>events for {self.content['sale']['content']['city']}, {self.content['sale']['content']['country']}</h2> 
        <table>
                    """

            for events in self.content['sale']['content']['periods']:
                html += f"""
            <tr>
                <td>
                    {events['timestamp'].strftime('%d %b %H%M')}
                </td>
                <td>
                    <img src="{events['icon']}">
                </td>
                <td>
                    {events['temp']}\u00B0C | {events['description']}
                </td>
            </tr>
                        """               

            html += """
            </table>
                    """

        # format Instagram trends
        if self.content['instagram']['include'] and self.content['instagram']['content']:
            html += """
        <h2>Top Ten Instagram Trends</h2>
                    """

            for trend in self.content['instagram']['content'][0:10]: # top ten
                html += f"""
        <b><a href="{trend['url']}">{trend['name']}</a></b><p>
                        """

        # format Fashion article
        if self.content['fashion']['include'] and self.content['fashion']['content']:
            html += f"""
        <h2>Daily Fashion Scoop</h2>
        <h3><a href="{self.content['fashion']['content']['url']}">{self.content['fashion']['content']['title']}</a></h3>
        <table width="800">
            <tr>
                <td>{self.content['fashion']['content']['extract']}</td>
            </tr>
        </table>
                    """

        # footer
        html += """
    </center>
    </body>
</html>
                """

        return {'text': text, 'html': html}

if __name__ == '__main__':
    email = DailyDigestEmail()

    ##### test format_message() #####
    print('\nTesting email body generation...')
    message = email.format_message()

    # print Plaintext and HTML messages
    print('\nPlaintext email body is...')
    print(message['text'])
    print('\n------------------------------------------------------------')
    print('\nHTML email body is...')
    print(message['html'])

    # save Plaintext and HTML messages to file
    with open('message_text.txt', 'w', encoding='utf-8') as f:
        f.write(message['text'])
    with open('message_html.html', 'w', encoding='utf-8') as f:
        f.write(message['html'])