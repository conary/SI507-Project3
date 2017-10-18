from bs4 import BeautifulSoup
import unittest
import requests
import urllib.request
import urllib.parse
import urllib.error
import ssl
import csv


#########
## Instr note: the outline comments will stay as suggestions, otherwise it's too difficult.
## Of course, it could be structured in an easier/neater way, and if a student decides to commit to that, that is OK.

## NOTE OF ADVICE:
## When you go to make your GitHub milestones, think pretty seriously about all the different parts and their requirements, and what you need to understand. Make sure you've asked your questions about Part 2 as much as you need to before Fall Break!


######### PART 0 #########



# make a function for caching pattern
def get_from_cache(url,file_name):
    try:
        html = open(file_name,'r').read()
        f.close()
    except:
        html = requests.get(url).text # request object FIRST and use .text to convert it to a string
        f = open(file_name,'w')
        f.write(html)
        f.close()

    return (html) # return string of HTML data that we can then parse through

gallery_html = get_from_cache("http://newmantaylor.com/gallery.html","gallery.html")
soup = BeautifulSoup(gallery_html, 'html.parser')
        # .find() gives you the FIRST tag the parser sees
        # .find_all() gives a list of all the tags

image_texts = soup.find_all("img")

for i in image_texts:
    try:
        text = i['alt']
    except:
        text = "No alternative text provided!"
    print(text)
#title = a.find("h3").text.strip() # removes all hidden whitespaces

#texts = image_alt-texts[0]
#print(soup.prettify())
#print(soup.img)
#print(image_texts)




#first_image = image_texts[0]
#desc = first_image.get('alt', '')
##desc = first_image['alt']
#print(first_image)
#print(desc)








######### PART 1 #########

# Get the main page data...

# Try to get and cache main page data if not yet cached
# Result of a following try/except block should be that
# there exists a file nps_gov_data.html,
# and the html text saved in it is stored in a variable 
# that the rest of the program can access.

# We've provided comments to guide you through the complex try/except, but if you prefer to build up the code to do this scraping and caching yourself, that is OK.

main_html = get_from_cache("https://www.nps.gov/index.htm","nps_gov_data.html")





# Get individual states' data...

# Result of a following try/except block should be that
# there exist 3 files -- arkansas_data.html, california_data.html, michigan_data.html
# and the HTML-formatted text stored in each one is available
# in a variable or data structure 
# that the rest of the program can access.
#def get_state_from_cache(url,file_name):
# TRY: 
# To open and read all 3 of the files


try:
    arkansas_html = open("arkansas_data.html",'r').read()
    california_html = open("california_data.html", 'r').read()
    michigan_html = open("michigan_data.html",'r').read()

# But if you can't, EXCEPT:
except:
# Create a BeautifulSoup instance of main page data 

    soup = BeautifulSoup(main_html, 'html.parser')
    #print(soup.type)
    #print(soup.prettify)

# Access the unordered list with the states' dropdown
    ul = soup.find ("ul", {"class":"dropdown-menu SearchBar-keywordSearch"})   

# Get a list of all the li (list elements) from the unordered list, using the BeautifulSoup find_all method
    states = ul.find_all ("li") 
# Use a list comprehension or accumulation to get all of the 'href' attributes of the 'a' tag objects in each li, instead of the full li objects
    urls = []
    for state in states:
        url = state.find("a")["href"]
    #print(url)
        urls.append(url)
#print(urls)
# Filter the list of relative URLs you just got to include only the 3 you want: AR's, CA's, MI's, using the accumulator pattern & conditional statements
    final_urls = []
    for url in urls:
        if "/ar/" in url:
            final_urls.append(url)
        if "/ca/" in url:
            final_urls.append(url)
        if "/mi/" in url:
            final_urls.append(url)
    print(final_urls)
    
# Create 3 URLs to access data from by appending those 3 href values to the main part of the NPS url. Save each URL in a variable.
    for state in final_urls:
        if "/ar/" in state:
            arkansas_url = "https://www.nps.gov" + state
        if "/ca/" in state:
            california_url = "https://www.nps.gov" + state
        if "/mi/" in state:
            michigan_url = "https://www.nps.gov" + state

    print(arkansas_url)
    print(california_url)
    print(michigan_url)

## To figure out what URLs you want to get data from (as if you weren't told initially)...
# As seen if you debug on the actual site. e.g. Maine parks URL is "http://www.nps.gov/state/me/index.htm", Michigan's is "http://www.nps.gov/state/mi/index.htm" -- so if you compare that to the values in those href attributes you just got... how can you build the full URLs?




# Finally, get the HTML data from each of these URLs, and save it in the variables you used in the try clause
# (Make sure they're the same variables you used in the try clause! Otherwise, all this code will run every time you run the program!)
    
    arkansas_html = get_from_cache(arkansas_url,"arkansas_data.html")
    california_html = get_from_cache(california_url, "california_data.html")
    michigan_html = get_from_cache(michigan_url, "michigan_data.html")
    

# And then, write each set of data to a file so this won't have to run again.

    #print(arkansas_html)
    #print(california_html)
    #print(michigan_html)



######### PART 2 #########

## Before truly embarking on Part 2, we recommend you do a few things:
ar_soup = BeautifulSoup(arkansas_html, 'html.parser')
ca_soup = BeautifulSoup(california_html, 'html.parser')
mi_soup = BeautifulSoup(michigan_html, 'html.parser')

# print(ar_soup.prettify())
# - Create BeautifulSoup objects out of all the data you have access to in variables from Part 1
# - Do some investigation on those BeautifulSoup objects. What data do you have about each state? How is it organized in HTML?

# HINT: remember the method .prettify() on a BeautifulSoup object -- might be useful for your investigation! So, of course, might be .find or .find_all, etc...

# HINT: Remember that the data you saved is data that includes ALL of the parks/sites/etc in a certain state, but you want the class to represent just ONE park/site/monument/lakeshore.

# We have provided, in sample_html_of_park.html an HTML file that represents the HTML about 1 park. However, your code should rely upon HTML data about Michigan, Arkansas, and Califoria you saved and accessed in Part 1.

# However, to begin your investigation and begin to plan your class definition, you may want to open this file and create a BeautifulSoup instance of it to do investigation on.

# Remember that there are things you'll have to be careful about listed in the instructions -- e.g. if no type of park/site/monument is listed in input, one of your instance variables should have a None value...


#print("Title", mi_soup.title)
#print("Some Text", mi_soup.get_text())


## Define your class NationalSite here:

class NationalSite:
    def __init__(self, bs):
        
        self.location = bs.find('h4').text
        print(self.location)
        if len(self.location) < 2:
            self.location = ''
            self.cache_fn = 'xx'
        else:
            self.cache_fn = self.location[-2] + self.location[-1]
        if bs.find('h2').text == '':
            self.type = 'None'
        else:
            self.type = bs.find('h2').text
        self.name = bs.find('h3').text
        try: 
            self.description = bs.find('p').text
        except:
            self.description = ''
        self.detail_url_part = bs.find('a').get('href')
        self.detail_url = "https://www.nps.gov" + self.detail_url_part + "index.htm"

        #print(self.name)
        #print(self.type)
        #print(self.location)
        #print(self.description)
        #print(self.detail_url)
        

    def __str__(self):
        return "{} | {}".format(
            self.name,
            self.location
            )
    def get_mailing_address(self): 
        detail_html = get_from_cache(self.detail_url, self.cache_fn)
        detail_soup = BeautifulSoup(detail_html, 'html.parser')
        #print(detail_soup.prettify())
        if detail_soup.find('div', class_="mailing-address") == '':
            return(" ")   
        address = detail_soup.find('div', class_="mailing-address")
        street = address.find('div', {'itemprop':'address'}).text.strip()
        address_line = street.replace('\n', '/')
        address_line_final = ''
        dup_count = 0
        for char in address_line:
            if char != '/':
                address_line_final = address_line_final + char
                dup_count = 0
            else:
                if dup_count == 0:
                    address_line_final = address_line_final + char
                    dup_count = dup_count + 1
        return address_line_final
        
    def __contains__(self, check):
        if check in self.name:
            return True
        else:
            return False







## Recommendation: to test the class, at various points, uncomment the following code and invoke some of the methods / check out the instance variables of the test instance saved in the variable sample_inst:

#f = open("sample_html_of_park.html",'r')
#soup_park_inst = BeautifulSoup(f.read(), 'html.parser') # an example of 1 BeautifulSoup instance to pass into your class
#sample_inst = NationalSite(soup_park_inst)
#print(sample_inst)
#print(sample_inst.get_mailing_address())
#f.close()





######### PART 3 #########

# Create lists of NationalSite objects for each state's parks.
#arkansas_natl_sites
#california_natl_sites
#michigan_natl_sites
# HINT: Get a Python list of all the HTML BeautifulSoup instances that represent each park, for each state.
#print("Here comes mi_soup")
#print(mi_soup.prettify())
#print(mi_soup.type)

#print("Herer comes mi_parks")
#print(mi_parks.prettify())


def createSiteList(state_parks):
    i=0
    site_list = []
    sites = state_parks.find_all('li', class_="clearfix")
    for park in sites:
        print("This is Park Nunber", i)
        #print(park)
        i = i + 1
        park_soup = BeautifulSoup(str(park), 'html.parser')
        site_obj = NationalSite(park_soup)
        site_list.append(site_obj)
    return site_list 

michigan_natl_sites = createSiteList(mi_soup.find('ul', {'id':'list_parks'}))
arkansas_natl_sites =  createSiteList(ar_soup.find('ul', {'id':'list_parks'}))
california_natl_sites = createSiteList(ca_soup.find('ul', {'id':'list_parks'}))
for i in michigan_natl_sites:
    print ("I am a Michigan site: " + str(i))
for i in arkansas_natl_sites:
    print("I am an Arkansas site: " + str(i))
for i in california_natl_sites:
    print("I am a California site: " + str(i))










##Code to help you test these out:
# for p in california_natl_sites:
# 	print(p)
# for a in arkansas_natl_sites:
# 	print(a)
# for m in michigan_natl_sites:
# 	print(m)



######### PART 4 #########

## Remember the hints / things you learned from Project 2 about writing CSV files from lists of objects!

## Note that running this step for ALL your data make take a minute or few to run -- so it's a good idea to test any methods/functions you write with just a little bit of data, so running the program will take less time!

## Also remember that IF you have None values that may occur, you might run into some problems and have to debug for where you need to put in some None value / error handling!

# outfile = open("arkansas.csv", "w")
# outfile.write('"Name", "Location", "Type", "Address", "Description"\n')
# for site_obj in arkansas_natl_sites:
#     print(site_obj.name)
#     print(site_obj.location)
#     print(site_obj.type)
#     print(site_obj.get_mailing_address())
#     print(site_obj.description)

#     outfile.write('"{}", "{}"\n'.format(site_obj.name, site_obj.location))


def createCSV(file_name, national_sites):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        q = 0
        writer.writerow(['Name', 'Location', 'Type', 'Address', 'Description'])
        for obj in national_sites:
            print("row" + str(q))
            q = q + 1
            description_clean = obj.description.strip()
            description_final = description_clean.replace('\n', '/')
            writer.writerow([obj.name, obj.location, obj.type, obj.get_mailing_address(), description_final])

createCSV("michigan.csv", michigan_natl_sites)
createCSV("arkansas.csv", arkansas_natl_sites)
createCSV("california.csv", california_natl_sites)