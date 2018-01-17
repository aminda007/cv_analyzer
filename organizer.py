from bs4 import BeautifulSoup
# import json.simple.JSONObject;
# import  urllib
import json

def organize():
    html = open('cv.html', 'r', buffering=1).read()
    print(html)
    # import codecs
    # f = codecs.open("cv.html", 'rb', 'utf-8')
    soup1 = BeautifulSoup(f.read()).get_text()
    print(soup1)
    # page = urllib.request.urlopen("./cv.html").read()
    # print(page)
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find_all('span', style=True)
    font_array = []
    line_array = []
    for data in div:
        style_set = data["style"]
        if 'font' in style_set:
            font_size = style_set.split(':')[-1].replace('px','').replace(';','')
            line = {}
            line['font'] = font_size
            line['text'] = data.text.replace('\n',' ').rstrip()
            # print(line['text'])
            # print(line['font'])
            font_array.append(font_size)
            line_array.append(line)
    # print(line_array)


    # convert string array into int array
    font_array_int = []
    for i in font_array:
        i = int(i)
        font_array_int.append(i)

    # find font size of body using sort
    sorted_font_array = sorted(font_array_int, key = font_array_int.count)
    font_body = sorted_font_array[-1]

    # find font size of name using sort and max
    max_array = sorted(font_array_int)
    font_name  = str(max_array[-1])
    print(font_array)
    print(max_array)
    print(font_name)
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
        else:
            cv['linkedin'] = "Not available"


    font_subheading = 0
    for line in line_array:
        font = int(line['font'])
        if (font < font_heading and font > font_body):
            font_subheading =  font


    heading_started = False
    heading_ended = False
    sub_heading_started = False
    sub_heading_ended = False
    body_started = False
    body_ended = False
    heading = {}
    subheading = {}
    body = {}
    heading_array = []
    sub_heading_array = []
    body_array = []
    print('font heading')
    print(font_heading)
    for line in line_array:
        font = int(line['font'])
        line = line['text']

        # print('111111111111111111111111111111111111111111111111')
        print('font is '+str(font))
        if (font == font_heading):
            if heading_started:
                print('inside heading')
                heading["sub_heading"] = sub_heading_array
                # print(heading)
                heading_array.append(heading)
                print(heading_array)
            heading = {}
            heading["heading"] = line
            heading_started = True
            # print(heading)
        if heading_started:
            if (font == font_subheading):
                if sub_heading_started:
                    subheading["body"] = body_array
                    sub_heading_array.append(subheading)
                sub_heading = {}
                subheading["subheading"] = line
                body_array = []
                sub_heading_started = True
            if (font == font_body):
                body = {}
                body['line'] = line
                body_array.append(body)

    print(sub_heading_array)
    heading["sub_heading"] = sub_heading_array
    heading_array.append(heading)

    cv['data']= heading_array
    json_data = json.dumps(cv)
    # print(json_data)

    print('\nName:                  ' + cv['name'])
    print('Email:                 ' + cv['email'])
    print('LinkedIn Profile URL:  '+cv['linkedin'])