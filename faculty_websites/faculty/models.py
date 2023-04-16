from django.db import models
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


class Person(models.Model):
    TYPES = [
        ('faculty', 'Faculty'),
        ('staff', 'Staff'),
        ('phd', 'PhD')
    ]
    
    name = models.CharField(max_length=50)
    email = models.EmailField()
    profile_url = models.URLField()
    type = models.CharField(max_length=10, choices=TYPES)

    def __str__(self):
        return self.name
    
    def __init__(self, department, name, type, email=None, profile_url=None):
        self.department = models.ForeignKey(Department, on_delete=models.CASCADE)
        self.name = name
        self.type = type
        self.email = email
        self.profile_url = profile_url

class Department(models.Model):
    name = models.CharField(max_length=50)
    four_letter_code = models.CharField('Four Letter Code', max_length=4)
    url = models.URLField()
    faculty_url = models.URLField()
    staff_url = models.URLField()
    phd_url = models.URLField()
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

    def get_staff_list(self):
        pass

    def get_phd_list(self):
        pass

    def get_faculty_list(self):

        pass

    def get_all_list(self):
        pass

class Membership(models.Model):

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Department, on_delete=models.CASCADE)
    type = 



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




