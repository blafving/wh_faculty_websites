# wh_faculty_websites

Need to blow up the db - stashed the contents in scratchpad.
Started to restructure under a new schema where a page will be associated with an Object, which can be of type
Department or Person, and Person can be either Faculty, Staff or PhD.

It looks like the django app would be extremely helpful in the longer term effort to build a faculty data application.


-----------------------
Alternate short-term path - use a notebook to crawl departments, find profiles, and identify personal websites with linear code. Save the process and export. Can continue to run the script repeatedly. 

notes: advertools does not crawl subdomains

## UPDATE

Now get_departments gets a list of subdomains

Next up:

- [ ] Crawl subdomains
build list of faculty from subdomain urls
find Personal Websites Links
retrieve Personal Website information