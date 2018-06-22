import urllib

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from .export_data import *
from .import_data import import_all_data
from .scoring_template import write_total_score

def scrape_linkedin(pro_url):

    chrome_options = Options()
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=chrome_options)

    usrName = 'redleafpro@gmail.com'
    pssWrd = "asasas12"


    driver.get("https://www.linkedin.com/uas/login?")
    driver.find_element_by_name('session_key').send_keys(usrName)
    driver.find_element_by_class_name('password').send_keys(pssWrd)
    driver.find_element_by_class_name('btn-primary').click()
    time.sleep(3)
    driver.get(pro_url)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2)");
    time.sleep(5)
    driver.find_element_by_class_name('pv-skills-section__additional-skills').click()
    time.sleep(1)

    # getting skills and endorsements
    skills_div = driver.find_element_by_id("skill-categories-expanded")
    skills = skills_div.find_elements_by_xpath("//*[contains(@class, 'Sans-17px-black-100%-semibold') or contains(@class, 'pv-skill-category-entity__endorsement-count Sans-15px-black-70%')]")
    try:
        pro_pic = driver.find_element_by_xpath("//*[contains(@class, 'pv-top-card-section__photo presence-entity__image EntityPhoto-circle-9 ember-view')]")
        pro_pic_src = pro_pic.get_attribute("style")
        pro_pic_src_splitted = pro_pic_src.split('"')
        pro_pic_src_refined = pro_pic_src_splitted[1]
        urllib.request.urlretrieve(pro_pic_src_refined, "cv_analyzer/static/images/profile_pictures"+pro_url[27:]+".png")
    except:
        urllib.request.urlretrieve("http://www.davidniklasson.com/in.png", "cv_analyzer/static/images/profile_pictures"+ pro_url[27:]+".png")
        print("no pro pic found")
    # driver.close()

    newSkills = []
    skill_ok = 0
    skill_line = ''
    scrapped_data = ''
    total_endoresed = 0

    for skill in skills:
        if 'Sans-17px-black-100%-semibold' in skill.get_attribute("class"):
            skill_ok += 1
            if skill_ok == 2:
                skill_ok = 1
                newSkills.append(skill_line)
                skill_line = ''
            skill_line = skill.text + '$'
            scrapped_data += skill.text + ' '
        if 'pv-skill-category-entity__endorsement-count Sans-15px-black-70%' in skill.get_attribute("class"):
            skill_line += skill.text
            total_endoresed += int(skill.text)

    endoresed_marks = min(max(int(total_endoresed/250*100), 20), 100)
    writeSkillsLinkedIn(newSkills)
    write_endoresed_data(endoresed_marks)
    updata_all_data(scrapped_data)
    write_total_score(import_all_data().lower().split())

    return True