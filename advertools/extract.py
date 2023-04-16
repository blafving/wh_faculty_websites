import advertools as adv
from urllib.parse import urlparse
import pandas as pd
import re
import os

DEPARTMENTS = 'https://www.wharton.upenn.edu/departments/'
DATA = 'data/'

def subdoms(url):
    '''
    Returns a list of domain and subdomains, filtering out www
    '''
    location = urlparse(url).netloc
    doms = location.split('.')
    if doms[0] == 'www':
        return doms[1:]
    return doms

def crawl_dept(dept_page):
    '''
    Takes a department page and returns a list of courses.
    '''
    name = subdoms(dept_page)[0]
    if os.path.exists('.'.join([name, 'jl'])):
        os.remove('.'.join([name, 'jl']))
    adv.crawl(dept_page, 
        '.'.join([name, 'jl']),
        follow_links=True,
    )
    df = pd.read_json('.'.join([name, 'jl']), lines=True)
    return (name, df)

def dept_links(links_str):
    '''
    Takes a string of department links and returns a list of links.
    '''
    return re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', links_str)

def get_departments(depts_page):
    """
    Get departments links from a department page.
    """
    os.remove('departments.jl')
    adv.crawl(depts_page, 
        'departments.jl',
        xpath_selectors={'department_links': '//h3//a'})    
    crawl_df = pd.read_json('departments.jl', lines=True)
    print('Crawl DF \n')
    print(str(crawl_df['department_links'][0]))
    return dept_links(crawl_df['department_links'][0])

dept_links = get_departments(DEPARTMENTS)

for dept in dept_links:
    dept_name, dept_df = crawl_dept(dept)

    
