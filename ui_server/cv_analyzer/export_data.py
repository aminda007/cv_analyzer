import csv


def writePersonalInfo(name,email,linkedin):
    with open('cv_analyzer/static/csv_data/personal_info.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow([name, email, linkedin])


def writePersonalInfoLinkedIn(name, occupation, summary, skills, experience, courses, organizations):
    with open('cv_analyzer/static/csv_data/link_personal_info.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow([name, occupation, summary, skills, experience, courses, organizations])


def getWordList(data):
    data = data.rstrip()
    data = data.lstrip()
    words = data.split(' ')
    catogary = words[0]
    # print(words)
    words1 = ''
    for i in words:
        if (',' in i):
            words1 += i
    words1 = words1 + words[-1]
    # print(words1)
    wordList = words1.split(',')
    # print(wordList)
    return wordList


def writeProjects(data):
    with open('cv_analyzer/static/csv_data/projects.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='<')
        data = data.lstrip()
        projects = data.split('@#')

        for project in projects:
            print('111111111111111111111111111111111111111111111111111111111111111\n')
            print(project)
            lines = project.split('\n')
            pname = ''
            lineSet = ''
            for line in lines:
                if '---' in line:
                    pname = line
                elif '--' in line:
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
                    # csv_writer.writerow(["svgf", ['xas', 'xsa', 'xsasa']])
                    csv_writer.writerow([pname[3:], newLineSet])
                    print('pname is--------------------------------'+pname)


def writeProjectsLinkedIn(data):
    with open('cv_analyzer/static/csv_data/link_projects.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='<')
        data = data.lstrip()
        projects = data.split('@#')

        for project in projects:
            print('111111111111111111111111111111111111111111111111111111111111111\n')
            print(project)
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
                    # csv_writer.writerow(["svgf", ['xas', 'xsa', 'xsasa']])
                    csv_writer.writerow([pname[3:], newLineSet])
                    print('pname is--------------------------------'+pname)


def write_skills(data):
    with open('cv_analyzer/static/csv_data/skills.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        data = data.split('\n')
        for line in data:
            if len(line) > 2:
                csv_writer.writerow(getSkillList(line))


def getSkillList(data):
    data = data.rstrip()
    data = data.lstrip()
    words = data.split(' ')
    catogary = words[0]
    # print(words)
    words1 = ''
    for i in words:
        if (',' in i):
            words1 += i
    words1 = words1 + words[-1]
    # print(words1)
    wordList = words1.split(',')
    newLineSet = ''
    for line in wordList:
        newLineSet += '^'
        newLineSet += line
    # print(wordList)
    return [catogary[2:], newLineSet]


def writeSkillsLinkedIn(data):
    with open('cv_analyzer/static/csv_data/link_skills.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        for lines in data:
            skill = lines.split('$')
            csv_writer.writerow(skill)
            print('111111111111111111111111111111111111111111111111111111111111111\n')
            print(skill)


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