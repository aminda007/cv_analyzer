import csv


def writePersonalInfo(name,email,linkedin):
    with open('cv_analyzer/static/csv_data/personal_info.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow([name, email, linkedin])


def getWordList(data):
    data = data.rstrip()
    words = data.split(' ')
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


def writeLanguages(data):
    with open('cv_analyzer/static/csv_data/programming_languages.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(getWordList(data))


def writeLibraries(data):
    with open('cv_analyzer/static/csv_data/libraries.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(getWordList(data))


def writeFrameworks(data):
    with open('cv_analyzer/static/csv_data/frameworks.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(getWordList(data))


def writeDatabase(data):
    with open('cv_analyzer/static/csv_data/database.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(getWordList(data))


def writeMobile(data):
    with open('cv_analyzer/static/csv_data/mobile.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(getWordList(data))


def writeIDE(data):
    with open('cv_analyzer/static/csv_data/ides.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(getWordList(data))


def writeVersion(data):
    with open('cv_analyzer/static/csv_data/version.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(getWordList(data))


def writeOS(data):
    with open('cv_analyzer/static/csv_data/os.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(getWordList(data))


def writeProjects(data):
    with open('cv_analyzer/static/csv_data/projects.csv', 'w',newline='') as csv_file:
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

