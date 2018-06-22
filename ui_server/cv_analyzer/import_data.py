import csv


def importPersonalDataLinkedIn():
    with open('cv_analyzer/static/csv_data/link_personal_info.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            return line


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
    return [projects]


def importProjectDataLinkedIn():
    with open('cv_analyzer/static/csv_data/link_projects.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='<')
        return getProjects(csv_reader)


def importSkillsLinkedIn():
    with open('cv_analyzer/static/csv_data/link_skills.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        skills = []
        for line in csv_reader:
            skills.append(line)
        return [skills]


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
