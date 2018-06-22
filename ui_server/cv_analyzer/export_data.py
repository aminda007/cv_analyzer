import csv


def writePersonalInfo(name,email,linkedin):
    with open('cv_analyzer/static/csv_data/personal_info.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow([name, email, linkedin])


def writePersonalInfoLinkedIn(name, occupation, summary, skills, experience, courses, organizations):
    with open('cv_analyzer/static/csv_data/link_personal_info.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow([name, occupation, summary, skills, experience, courses, organizations])


def writeProjectsLinkedIn(data):
    with open('cv_analyzer/static/csv_data/link_projects.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='<')
        data = data.lstrip()
        projects = data.split('@#')

        for project in projects:
            lines = project.split('\n')
            pname = ''
            lineSet = ''
            for line in lines:
                if '---' in line:
                    pname = line
                elif line != '':
                    if '--' in line:
                        line
                    else:
                        line = '--' + line
                    lineSet += line
            lineSet = lineSet.lstrip()
            lineSet = lineSet.split('--')
            newLineSet = ''
            for line in lineSet:
                line = line.lstrip()
                line = line.rstrip()
                if line != '':
                    newLineSet += '^'
                    newLineSet += line
            if pname != '':
                if len(newLineSet) != 0:
                    csv_writer.writerow([pname[3:], newLineSet])


def writeSkillsLinkedIn(data):
    with open('cv_analyzer/static/csv_data/link_skills.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        for lines in data:
            skill = lines.split('$')
            csv_writer.writerow(skill)
            # print('111111111111111111111111111111111111111111111111111111111111111\n')
            # print(skill)


def write_all_data(data):
    file = open('cv_analyzer/all.txt', 'w')
    file.write(data)
    file.close()


def updata_all_data(data):
    file = open('cv_analyzer/all.txt', 'a')
    file.write(data)
    file.close()

def write_endoresed_data(data):
    with open('cv_analyzer/static/csv_data/endoresed_data.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow([data])

def write_word_count(count):
    with open('cv_analyzer/static/csv_data/word_count.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow([count])