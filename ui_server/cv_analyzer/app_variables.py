from .qa_model.keras_question_and_answering_system.library.utility.squad import SquADDataSet


class AppVariables:

    started = False
    seq2seq = None
    data_set = SquADDataSet(data_path=None)
    q_count = 0
