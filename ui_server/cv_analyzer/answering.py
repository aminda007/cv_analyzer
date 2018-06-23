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

        print('inside get_qna_list')
        data_set = SquADDataSet(data_path=None)
        data_set.load_model(data_path='cv_analyzer/static/demo/data/SQuAD/custom4.json')
        qa_list = []

        for qa_item in data_set.to_tree():
            data = []
            context = qa_item[0]
            print('qa title')
            print(context)
            item_array = []
            for question in qa_item[1]:
                question_array = []
                print('qa question')
                print(question[0])
                question_array.append(question[0])
                print('qa answer')
                print(question[1])
                question_array.append(question[1])
                item_array.append(question_array)
            # item_array.append(answer_array)
            data.append(context)
            data.append(item_array)
            qa_list.append(data)
            print(len(qa_list))
            print('qa 1 st item')
            print(qa_list[0])
        return json.dumps(qa_list[0:5])

    @staticmethod
    def get_random_qna():

        print('inside get_qna_list')
        data_set = SquADDataSet(data_path=None)
        data_set.load_model(data_path='cv_analyzer/static/demo/data/SQuAD/custom4.json')
        qa_list = []

        for qa_item in data_set.to_tree():
            data = []
            context = qa_item[0]
            print('qa title')
            print(context)
            item_array = []
            for question in qa_item[1]:
                question_array = []
                print('qa question')
                print(question[0])
                question_array.append(question[0])
                print('qa answer')
                print(question[1])
                question_array.append(question[1])
                item_array.append(question_array)
            # item_array.append(answer_array)
            data.append(context)
            data.append(item_array)
            qa_list.append(data)
            print(len(qa_list))
            print('qa 1 st item')
            print(qa_list[0])
        return qa_list[randint(0, len(qa_list)-1)]

    def get_qna(self):
        try:
            q = self.get_random_qna()
            print("555555555555555555")
            print(q)
            context = q[0]
            print(context)
            question_array = q[1]
            first_item = question_array[0]
            question = first_item[0]
            answer = first_item[1]
            return context, question, answer
        except:
            return self.get_qna()
