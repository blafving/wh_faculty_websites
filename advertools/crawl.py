import advertools as adv
from urllib.parse import urlparse
import pandas as pd
import re
import os

DEPARTMENTS = 'https://www.wharton.upenn.edu/departments/'

def get_departments(dept_page):
    """
    Get departments from a department page.
    """
    os.remove('departments.jl')
    adv.crawl(dept_page, 
        'departments.jl',
        xpath_selectors={'department_links': '//h3//a'})    
    crawl_df = pd.read_json('departments.jl', lines=True)
    print('Crawl DF \n')
    print(str(crawl_df['department_links'][0]))
    return dept_links(crawl_df['department_links'][0])

get_departments(DEPARTMENTS)

def dept_links(links_str):
    '''
    Takes a string of department links and returns a list of links.
    '''
    return re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', links_str)



def count_subdoms(url):
    location = urlparse(url).netloc
    print(location)
    if 'www' in location:
        return location.count('.') - 2
    else: 
        return location.count('.') - 1
    
    def df_list(cell):
        return cell.split('@@')
    
