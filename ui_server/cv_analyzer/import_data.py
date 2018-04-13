import csv


def importPersonalData():
    with open('cv_analyzer/static/csv_data/personal_info.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            return line


def importLanguageData():
    with open('cv_analyzer/static/csv_data/programming_languages.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            return line


def importLibrariesData():
    with open('cv_analyzer/static/csv_data/libraries.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            return line


def importFrameworksData():
    with open('cv_analyzer/static/csv_data/frameworks.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            return line


def importDatabaseData():
    with open('cv_analyzer/static/csv_data/database.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            return line


def importPersonalData():
    with open('cv_analyzer/static/csv_data/personal_info.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            return line

def importMobile():
    with open('cv_analyzer/static/csv_data/mobile.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            return line


def importIDE():
    with open('cv_analyzer/static/csv_data/ides.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            return line


def importVersionData():
    with open('cv_analyzer/static/csv_data/version.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            return line


def importOSData():
    with open('cv_analyzer/static/csv_data/os.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            return line


def importProjectData():
    with open('cv_analyzer/static/csv_data/projects.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='<')
        print('666666666666666666666666666666666666666666666666666666666')
        print (csv_reader)
        projects = []

        for line in csv_reader:
            project = []
            project.append(line[0])
            lines= line[1]
            lines= lines[1:]
            lines = lines.split('^')
            newLines = []
            for line in lines:
                line = line.lstrip()
                newLines.append(line)


            project.append(newLines)
            projects.append(project)
        for project in projects:
            for line in project[1]:
                print(line)
        return [projects]
# importPersonalData()