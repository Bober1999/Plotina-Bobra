from random import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
question = QLabel('Какой национальности не существует?')
trf = QLabel('Правильно/Неправильно')
otvet = QLabel('Смурфы')
answer = QPushButton('Ответить')
RadioGroupBox = QGroupBox('Варианты ответов') 
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чулымцы')
rbtn_3 = QRadioButton('Смурфы')
rbtn_4 = QRadioButton('Алеуты')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

layout_ans1.addWidget(trf)
layout_ans1.addWidget(otvet, alignment = Qt.AlignVCenter)
trf.hide()
otvet.hide()
layout_ans1.addWidget(answer, alignment = Qt.AlignCenter)
layout_ans1.addWidget(question, alignment = Qt.AlignCenter)
layout_ans2.addWidget(rbtn_1, alignment = Qt.AlignCenter)
layout_ans2.addWidget(rbtn_2, alignment = Qt.AlignCenter)
layout_ans3.addWidget(rbtn_3, alignment = Qt.AlignCenter)
layout_ans3.addWidget(rbtn_4, alignment = Qt.AlignCenter)


RadioGroupBox.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question, alignment =(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(answer, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)


def show_result():
    trf.show()
    otvet.show()
    rbtn_1.hide()
    rbtn_2.hide() 
    rbtn_3.hide()
    rbtn_4.hide()
    answer.setText('Следующий вопрос')
def show_question():
    trf.hide()
    otvet.hide()
    rbtn_1.show()
    rbtn_2.show()
    rbtn_3.show()
    rbtn_4.show()
    answer.setText('Ответить')
    #RadioGroupBox.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    #RadioGroupBox.setExclusive(True)
def start_test():
    if 'Ответить' == answer.text():
        show_result()        
    else:
        show_question()

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(question, right_answer, wrong1, wrong2, wrong3):
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    question.setText(question)
    otvet.setText(right_answer)
    show_question()

answer.clicked.connect(start_test)
main_win.setLayout(layout_card)
main_win.show()
app.exec()

