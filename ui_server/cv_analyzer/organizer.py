from bs4 import BeautifulSoup
# import json.simple.JSONObject;
# import  urllib
from pathlib import Path
import json
from .export_data import *
from .scoring_template import write_total_score

def organize():
    # html = open('cv.txt', 'rb', buffering=1).read(1000000)
    # with open('cv.txt','r') as content:
    #     html = content.read()
    # html = open('cv.txt', 'rt', encoding='utf-8')
    # html = open('cv.txt', 'rb')
    # html = open('cv.txt','r').readlines()
    # for line in html:
    #     print (line)
    # html.close()
    # html = Path('cv.txt').read_text()

    file = open('cv_analyzer/cv.txt', 'at')
    file.write('afdsghjgfdsafghjkhgfdsfghj')
    file.close()

    file = open('cv_analyzer/cv.txt', 'r')
    text_input  = file.read()
    write_total_score(text_input.split(),'score')
    file.close()

    html = open('cv_analyzer/cv.txt', 'rb', buffering=1).read(1000000)
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS\n"+str(soup))
    div = soup.find_all('span', style=True)
    print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD\n"+str(div))
    font_array = []
    line_array = []
    for data in div:
        # print('data is' + str(data))
        style_set = data["style"]
        if 'font' in style_set:
            font_size = style_set.split(':')[-1].replace('px', '')

            lines = data.text.split('\n')
            for ln in lines:
                if ln != '':
                    line = {}
                    line['font'] = font_size
                    line['text'] = ln.strip()
                    line_array.append(line)
                    # print(line)
            font_array.append(font_size)

    # print(font_array)
    # convert string array into int array
    font_array_int = []
    for i in font_array:
        i = int(i)
        font_array_int.append(i)
    # print(font_array_int)

    # find font size of body using sort
    sorted_font_array = sorted(font_array_int, key = font_array_int.count)
    font_body = sorted_font_array[-1]
    # print(sorted_font_array)

    # find font size of name using sort and max
    max_array = sorted(font_array_int)
    font_name  = str(max_array[-1])

    #
    # identify font size of headings
    font_heading = 0
    for line in line_array:
        if 'Education' in line['text']:
            font_heading = int(line['font'])
            break
    # get name from cv
    cv = {}
    for lines in line_array:
        line = lines['text']
        font = lines['font']
        if (font == font_name):
            cv['name'] =  line
        if ('@' in line):
            cv['email'] = line
        if ('linkedin' in line):
            cv['linkedin'] = line


    font_subheading = 0
    for line in line_array:
        font = int(line['font'])
        if (font < font_heading and font > font_body):
            font_subheading =  font


    heading_started = False
    sub_heading_started = False
    heading = {}
    subheading = {}
    body = {}
    heading_array = []
    sub_heading_array = []
    body_array = []

    for line in line_array:
        font = int(line['font'])
        line = line['text']
        print('***********************************************************************')
        print('init font is '+str(font))
        print('init text is '+str(line))
        print('init heading is '+str(heading_array))
        print('init sub_heading is '+str(sub_heading_array))
        print('init body is '+str(body_array))

        if (font == font_heading):

            if heading_started:
                print('inside heading')
                sub_heading["body"] = body_array
                sub_heading_array.append(sub_heading)
                heading["sub_heading"] = sub_heading_array
                print('final heading iiiisss'+str(heading))
                heading_array.append(heading)


                # print(heading_array)
            sub_heading_array = []
            sub_heading = {}
            body = {}
            body_array = []
            heading = {}
            heading["heading"] = line
            heading_started = True
            # print('heading iiiisss'+str(heading))

        elif (font == font_subheading):
            print('inside sub heading')
            if sub_heading_started:
                sub_heading["body"] = body_array
                sub_heading_array.append(sub_heading)
            sub_heading = {}
            sub_heading["subheading"] = line
            body_array = []
            sub_heading_started = True

        elif (font == font_body):
            print('inside body')
            body = {}
            body['line'] = line
            body_array.append(body)
            print('inside body')

    # print(sub_heading_array)
    sub_heading["body"] = body_array
    sub_heading_array.append(sub_heading)
    heading["sub_heading"] = sub_heading_array
    heading_array.append(heading)

    cv['data']= heading_array
    json_data = json.dumps(cv)
    print(json_data)

    def get_heading_data(type):
        heading_data = []
        for i in cv['data']:
            if (type in i['heading']):
                heading_data = i['sub_heading']
        data_set = ''
        for j in heading_data:
            try:
                data_set =  data_set + '\n' +'      @#---'+ j['subheading']
            except KeyError:
                print('')
            for k in j['body']:
                try:
                    data_set =  data_set +'\n' + '              --' + k['line']
                except KeyError:
                    print('')

        return data_set

    # print('\nName:                  ' + cv['name'])
    # print('Email:                 ' + cv['email'])
    # print('LinkedIn Profile URL:  '+cv['linkedin'])
    writePersonalInfo( cv['name'], cv['email'], cv['linkedin'])
    print('Education:             '+get_heading_data('ducation'))
    print('Experience:            '+get_heading_data('xperience'))
    writeProjects(get_heading_data('xperience'))
    # print('Skills:                '+get_heading_data('kills'))
    write_skills(get_heading_data('kills'))
    print('Achievement:           '+get_heading_data('chievement'))
