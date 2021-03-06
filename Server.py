import requests
import sys

class Server:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

    session = requests.Session()

    def get(self, url):
        try:
           response = self.session.get(url, headers=self.headers)
           if response.status_code == 200:
            return response
           else:
               sys.exit("Error message. Response code not 200")
        except Exception as e:
            print(e)
            sys.exit("Error message")
        except requests.exceptions.Timeout as e:
            #Maybe set up for a retry, or continue in a retry loop
            print(e)
            sys.exit("Error message")
        except requests.exceptions.TooManyRedirects as e:
            # Tell the user their URL was bad and try a different one
            print(e)
            sys.exit("Error message")
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            print(e)
            sys.exit("Error message")

