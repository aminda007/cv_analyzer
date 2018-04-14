from linked_in_scrapper import Linked_in_scraper


def scrape_linkedin_profile(profile_link):
    linkedin_page = Linked_in_scraper(profile_link)
    return linkedin_page.scrape_one_profile(profile_link)


def get_linkedin_profile(link):
    return scrape_linkedin_profile(link)


# get_linkedin_profile('https://www.linkedin.com/in/manura-jithmal-de-silva-988b385b/')
get_linkedin_profile('https://www.linkedin.com/in/aminda-abeywardana-6aa8b845/')
# get_linkedin_profile('https://www.linkedin.com/in/chamodsamarajeewa/')
# get_linkedin_profile('https://www.linkedin.com/in/ksuthagar/')
# get_linkedin_profile('https://www.linkedin.com/in/anuradha-sithuruwan-a971b7126/')
