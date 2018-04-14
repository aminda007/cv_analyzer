import colorama


class Extractor:

    profile_data = {}

    def extract_info(self, data):

        intro = data['included'][-1]
        included = data['included']
        # print(intro)
        # print(data)
        # print(included)

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
                # print(i)
                # print(index)
                if (len(i) == 9):
                    # print(i)
                    # print(i['name'] + 'company**************************')
                    experience.append(i['name'])
                if (len(i) == 4):
                    if (i['$type'] == 'com.linkedin.voyager.identity.profile.Skill' ):
                        print(i)
                        skills.append(i['name'])
                if (len(i) == 6):
                    courses.append(i['name'])
                if (len(i) == 8):
                    # print(i)
                    organization_name.append(i['name'])
                    if 'description' in keys:
                        organization_discription.append(i['description'])
                    else:
                        organization_discription.append('')
            elif 'members' in keys:
                # print(i)
                project_name.append(i['title'])
                project_discription.append(i['description'])
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
            projectList += '   ' +colorama.Fore.LIGHTGREEN_EX+ (project_name[i] + ' :- \n' + '        ' +colorama.Fore.WHITE+ project_discription[i] + '\n'+ project_url[i] + '\n'+'\n');

        print('\n' + 'Name:       ' + firstName + ' ' + lastName + '\n---------------------------------------------------------------------------\n'
                'Occupation: ' + occupation + '\n---------------------------------------------------------------------------\n'
                'Summary:    ' + summary + '\n---------------------------------------------------------------------------\n'
                'Skills:     ' + skillsList[:-2] + '\n---------------------------------------------------------------------------\n'
                'Experience: ' + experienceList[:-2]+ '\n---------------------------------------------------------------------------\n'
                'Courses: ' + courseList[:-2]+ '\n---------------------------------------------------------------------------\n'
                'Organizations: ' + organizationList+ '\n---------------------------------------------------------------------------\n'
                'Projects: ' + projectList
              )

