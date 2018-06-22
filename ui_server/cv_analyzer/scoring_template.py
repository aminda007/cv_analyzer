import csv
from .models import Skills


# return a score according to the given priority
def get_score(skill_priority):
    if skill_priority == 'High':
        return 30
    elif skill_priority == 'Very High':
        return 25
    elif skill_priority == 'Medium':
        return 20
    elif skill_priority == 'Very Low':
        return 15
    else:
        return 10


# get the total scores from given skills for model for each section
def get_total_section_score(category):
    skills = Skills.objects.filter(category=category)
    total_score = 0
    for item in skills:
        score = get_score(item.priority)
        total_score = total_score + score
    print(category+str(total_score))
    return total_score


def write_total_score(lists):

    score_front_end = 0
    score_back_end = 0
    score_quality_assurance = 0
    score_business_analysis = 0
    score_database = 0

    # remove duplicates from word list
    word_list = list(set(lists))
    # iterate through word list and give a score to each section for the uploaded resume
    for item in word_list:
        skills = Skills.objects.filter(skill=item)
        if len(skills) > 0:
            skill = skills[0]
            skill_priority = skill.priority
            skill_category = skill.category
            if skill_category == 'Front-end':
                score_front_end = score_front_end + get_score(skill_priority)
            elif skill_category == 'Back-end':
                score_back_end = score_back_end + get_score(skill_priority)
            elif skill_category == 'Quality Assurance':
                score_quality_assurance = score_quality_assurance + get_score(skill_priority)
            elif skill_category == 'Business Analysis':
                score_business_analysis = score_business_analysis + get_score(skill_priority)
            else:
                score_database = score_database + get_score(skill_priority)

    # get the total scores from given skills for model for each section as a percentage
    scores_front_end = int((score_front_end / get_total_section_score('Front-end'))*100)
    scores_back_end = int((score_back_end / get_total_section_score('Back-end'))*100)
    scores_quality_assurance = int((score_quality_assurance / get_total_section_score('Quality Assurance'))*100)
    scores_business_analysis = int((score_business_analysis / get_total_section_score('Business Analysis'))*100)
    scores_database = int((score_database / get_total_section_score('Database'))*100)

    # total score get by average of section scores
    score_total = int((scores_front_end + scores_back_end + scores_quality_assurance + scores_business_analysis + scores_database) / 5)

    with open('cv_analyzer/static/csv_data/link_score.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow([scores_front_end, scores_back_end, scores_quality_assurance, scores_business_analysis, scores_database, score_total])
        print("section score writing finished...")