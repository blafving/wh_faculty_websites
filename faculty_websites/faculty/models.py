from django.db import models
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

class Department(models.Model):
    def __str__(self):
        return self.full_name
    full_name = models.CharField(max_length=50)
    four_letter_code = models.CharField('Four Letter Code', max_length=4)
    faculty_url = models.URLField()
    staff_url = models.URLField()
    phd_url = models.URLField()
    



# class Faculty(models.Model):
#     departments = models.
#     def __init__(self):
#         self.departments = ['accounting', 'lgst', 'real-estate', 'bepp', 'mgmt', 
#         'statistics', 'fnce', 'marketing', 'hcmg', 'oid'
#         ]


class Pages(models.Model):
    def __init__(self):
        pass


    def fetch_page(self, url):
        '''
        sends an HTTP GET request to a URL and returns the response text.
        '''
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching '{url}': {e}")
            return None

    def scrape_websites(self, urls, max_threads=10):
        '''
        takes a list of URLs and an optional max_threads parameter. 
        It uses a ThreadPoolExecutor to manage the threads and fetch 
        the content of the web pages concurrently. The responses are 
        returned as a list of strings containing the HTML content of each web page.
        '''
        responses = []

        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            futures = {executor.submit(self.fetch_page, url): url for url in urls}

            for future in as_completed(futures):
                url = futures[future]
                try:
                    response_text = future.result()
                    if response_text is not None:
                        responses.append(response_text)
                except Exception as e:
                    print(f"Error processing '{url}': {e}")

        return responses


class Page(models.Model):
    pages = models.ForeignKey(Pages, on_delete=models.CASCADE)


