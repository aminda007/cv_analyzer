import csv


def importPersonalData():
    with open('cv_analyzer/static/csv_data/personal_info.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            return line


def importPersonalDataLinkedIn():
    with open('cv_analyzer/static/csv_data/link_personal_info.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            return line


def importPersonalData():
    with open('cv_analyzer/static/csv_data/personal_info.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            return line


def importProjectData():
    with open('cv_analyzer/static/csv_data/projects.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='<')
        # print('666666666666666666666666666666666666666666666666666666666')
        # print (csv_reader)
        return getProjects(csv_reader)


def getProjects(csv_reader):
    projects = []

    for line in csv_reader:
        project = []
        project.append(line[0])
        lines = line[1]
        lines = lines[1:]
        lines = lines.split('^')
        newLines = []
        for line in lines:
            line = line.lstrip()
            newLines.append(line)

        project.append(newLines)
        projects.append(project)
    # for project in projects:
    #     for line in project[1]:
            # print(line)
    return [projects]


def importProjectDataLinkedIn():
    with open('cv_analyzer/static/csv_data/link_projects.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='<')
        # print('666666666666666666666666666666666666666666666666666666666')
        # print (csv_reader)
        return getProjects(csv_reader)


def importSkillsLinkedIn():
    with open('cv_analyzer/static/csv_data/link_skills.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # print('666666666666666666666666666666666666666666666666666666666')
        # print (csv_reader)
        skills = []
        for line in csv_reader:
            skills.append(line)
            # print(line)
        return [skills]

def importSkillsData():
    with open('cv_analyzer/static/csv_data/skills.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # print('666666666666666666666666666666666666666666666666666666666')
        # print (csv_reader)
        return getProjects(csv_reader)

def importScoreData():
    with open('cv_analyzer/static/csv_data/score.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            return line


def importScoreDataLinkedIn():
    with open('cv_analyzer/static/csv_data/link_score.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            return line


def import_all_data():
    file = open('cv_analyzer/all.txt', 'r')
    text_input = file.read()
    return text_input

def import_endoresed_data():
    with open('cv_analyzer/static/csv_data/endoresed_data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            return line


def import_word_count():
    with open('cv_analyzer/static/csv_data/word_count.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            return line