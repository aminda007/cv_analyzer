import csv

def read_csv(file_name):
    with open('cv_analyzer/static/csv_data/'+file_name+'.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            return line[0]

def get_score(word_list, db_list, special_words):
    word_list = list(set(word_list))
    score = 0
    for item in word_list:
        if item in special_words:
            score += 2
        elif item in db_list:
            score += 1
    word_tokens = db_list.split()
    max_score = min(int(score/len(word_tokens)*100), 100)
    return max_score

def write_total_score(word_list, filename,
                      programming_special_words='xxxx', software_special_words='xxxx',
                      engineering_special_words='xxxx', finance_special_words='xxxx',
                      management_special_words='xxxx', art_special_words='xxxx',):

    db_programming = read_csv('db_programming')
    db_software = read_csv('db_software')
    db_engineering = read_csv('db_engineering')
    db_finance = read_csv('db_finance')
    db_management = read_csv('db_management')
    db_art = read_csv('db_art')

    score_programming = get_score(word_list, db_programming, programming_special_words)
    score_software = get_score(word_list, db_software, software_special_words)
    score_engineering = get_score(word_list, db_engineering, engineering_special_words)
    score_finance = get_score(word_list, db_finance, finance_special_words)
    score_management = get_score(word_list, db_management, management_special_words)
    score_art = get_score(word_list, db_art, art_special_words)

    score_total = int((score_programming+score_software+score_engineering+score_finance+score_management+score_art)/6)

    with open('cv_analyzer/static/csv_data/'+filename+'.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow([score_programming, score_software, score_engineering, score_finance, score_management, score_art, score_total])

write_total_score(["java", "emacs", "lisp", "go!"], "java")