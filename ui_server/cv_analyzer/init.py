from .linked_in_scrapper import Linked_in_scraper


def scrape_linkedin_profile(profile_link):
    linkedin_page = Linked_in_scraper(profile_link)
    return linkedin_page.scrape_one_profile(profile_link)


def get_linkedin_profile(link):
    return scrape_linkedin_profile(link)



