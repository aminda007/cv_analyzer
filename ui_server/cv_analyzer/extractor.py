import colorama
from .export_data import *

class Extractor:

    profile_data = {}

    def extract_info(self, data):

        included = data['included']
        firstName = ''
        lastName = ''
        occupation = ''
        summary = ''
        courses = []
        skills = []
        experience = []
        organization_name = []
        organization_discription = []
        project_name = []
        project_discription = []
        project_url = []

        for index, i in enumerate(included):
            keys = i.keys()
            if 'summary' in keys:
                firstName = i['firstName']
                lastName = i['lastName']
                occupation = i['headline']
                summary = i['summary']
            elif 'name' in keys:
                if (len(i) == 9):
                    experience.append(i['name'])
                if (len(i) == 4):
                    if (i['$type'] == 'com.linkedin.voyager.identity.profile.Skill' ):
                        skills.append(i['name'])
                if (len(i) == 6):
                    courses.append(i['name'])
                if (len(i) == 8):
                    organization_name.append(i['name'])
                    if 'description' in keys:
                        organization_discription.append(i['description'])
                    else:
                        organization_discription.append('')
            elif 'members' in keys:
                project_name.append(i['title'])
                if 'description' in keys:
                    project_discription.append(i['description'])
                else:
                    project_discription.append('')
                if 'url' in keys:
                    project_url.append(i['url'])
                else:
                    project_url.append('')


        skillsList = ''
        for i in skills:
            skillsList += (i + ', ');

        experienceList = ''
        for i in experience:
            experienceList += (i + ', ');

        courseList = ''
        for i in courses:
            courseList += (i + ', ');

        organizationList = '\n'
        for i in range(len(organization_name)):
            organizationList += '   '+(organization_name[i] + ' :- \n'+'        '+organization_discription[i]+'\n');

        projectList = '\n'
        for i in range(len(project_name)):
            projectList += '@#---' +(project_name[i] + '\n' + '--' + project_discription[i] + '\n--'+ project_url[i] +'\n');

        writePersonalInfoLinkedIn(firstName + ' ' + lastName, occupation, summary, skillsList[:-2], experienceList[:-2], courseList[:-2], organizationList)
        writeProjectsLinkedIn(projectList)
        write_all_data(firstName+lastName+' '+occupation+' '+summary+' '+skillsList[:-2]+' '+experienceList[:-2]+' '+courseList[:-2]+' '+organizationList+' '+projectList)
