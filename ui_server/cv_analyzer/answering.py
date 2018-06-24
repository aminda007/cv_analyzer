import json
from .qa_model.keras_question_and_answering_system.library.seq2seq import Seq2SeqQA
from .qa_model.keras_question_and_answering_system.library.utility.squad import SquADDataSet
from .app_variables import AppVariables
from random import randint


class Answering:

    @staticmethod
    def get_answer(question_context, question):
        print("started: "+str(AppVariables.started))
        if AppVariables.started:
            print("Already initiated")
        else:
            AppVariables.seq2seq = Seq2SeqQA()
            AppVariables.started = True
            AppVariables.seq2seq.load_model(model_dir_path='cv_analyzer/static/demo/models')

        answer = AppVariables.seq2seq.reply(question_context, question)
        return answer

    @staticmethod
    def get_qna_list():
        with open('cv_analyzer/static/demo/data/SQuAD/custom4.json') as json_data:
            file = json.load(json_data)
        qa_list = []
        for qa_item in file['data']:
            paragraphs = qa_item['paragraphs']
            paragraph = paragraphs[0]
            context = paragraph['context']
            qas = paragraph['qas']
            data = []
            item_array = []
            for question in qas:
                question_array = []
                answers = question['answers']
                answer = answers[0]
                ques = question['question']
                question_array.append(ques)
                question_array.append(answer['text'])
                item_array.append(question_array)
            data.append(context)
            data.append(item_array)
            qa_list.append(data)
        return json.dumps(qa_list)

    @staticmethod
    def get_random_qna():
        with open('cv_analyzer/static/demo/data/SQuAD/custom4.json') as json_data:
            file = json.load(json_data)
        qa_list = []
        for qa_item in file['data']:
            title = qa_item['title']
            if title == AppVariables.qna_category:
                paragraphs = qa_item['paragraphs']
                paragraph = paragraphs[0]
                context = paragraph['context']
                qas = paragraph['qas']
                data = []
                item_array = []
                for question in qas:
                    question_array = []
                    answers = question['answers']
                    answer = answers[0]
                    ques = question['question']
                    question_array.append(ques)
                    question_array.append(answer['text'])
                    item_array.append(question_array)
                data.append(context)
                data.append(item_array)
                qa_list.append(data)
        return qa_list[randint(0, len(qa_list)-1)]

    def get_qna(self):
        try:
            q = self.get_random_qna()
            context = q[0]
            question_array = q[1]
            first_item = question_array[0]
            question = first_item[0]
            answer = first_item[1]
            return context, question, answer
        except:
            return self.get_qna()
