
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from PyQt5.QtGui import QFont
from random import shuffle , randint



class Quetion():
    def __init__(self, text, right_answer, wrong1, wrong2, wrong3 ):
        self.text = text
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


quetions_list = []
quetions_list.append(Quetion('Як перекладається слово змінна ?' , "variable" , "vacation" , "varition" , "zminna"))
quetions_list.append(Quetion("28 ударов ножом!!!" , "Ты действовал наверняка не так ли" , "Отвали" , "??" , "Я ухожу"))
quetions_list.append(Quetion("Сосал?" , "Ты?" , "Свали" , "Да" , "Нет"))
quetions_list.append(Quetion("Доту2 любишь?" , "Да" , "Нет" , "Нет" , "Нет"))
quetions_list.append(Quetion("Сосал?" , "Ты?" , "Свали" , "Да" , "Нет"))


app = QApplication([])

window = QWidget()
window.resize(400, 200)
window.setWindowTitle('Memory Card')

question = QLabel("Запитання")
answer1 = QRadioButton("Відповідь 1")
answer2 = QRadioButton("Відповідь 2")
answer3 = QRadioButton("Відповідь 3")
answer4 = QRadioButton("Відповідь 4")
GroupBox = QGroupBox("Назва групи")
Button = QPushButton("Відповідь")

RadioGroup = QButtonGroup()
RadioGroup.addButton(answer1)
RadioGroup.addButton(answer2)
RadioGroup.addButton(answer3)
RadioGroup.addButton(answer4)

ResultGroupBox = QGroupBox("Результат")
result = QLabel("Тут буде результат", alignment=Qt.AlignCenter)
correct =QLabel("ТУт буде правильна відповідь", alignment=Qt.AlignCenter)
result_lineV1 = QVBoxLayout()
result_lineV1.addWidget(result, alignment=Qt.AlignCenter)
result_lineV1.addWidget(correct, alignment=Qt.AlignCenter)
ResultGroupBox.setLayout(result_lineV1)
ResultGroupBox.hide()

font = QFont("Times New Roman", 20, QFont.Bold)
font1 = QFont("Times New Roman", 14)
question.setFont(font)

lineH1 = QHBoxLayout()
lineV1 = QVBoxLayout()
lineV2 = QVBoxLayout()

lineV1.addWidget(answer1, alignment=Qt.AlignCenter)
lineV1.addWidget(answer2, alignment=Qt.AlignCenter)
lineV2.addWidget(answer3, alignment=Qt.AlignCenter)
lineV2.addWidget(answer4, alignment=Qt.AlignCenter)

lineH1.addLayout(lineV1)
lineH1.addLayout(lineV2)
GroupBox.setLayout(lineH1)

main_lineH1 = QHBoxLayout()
main_lineH2 = QHBoxLayout()
main_lineH3 = QHBoxLayout()

main_lineH1.addWidget(question, alignment=Qt.AlignCenter)
main_lineH2.addWidget(GroupBox, alignment=Qt.AlignCenter)
main_lineH2.addWidget(ResultGroupBox, alignment=Qt.AlignCenter)
main_lineH3.addWidget(Button, alignment=Qt.AlignCenter)

main_lineV1 = QVBoxLayout()
main_lineV1.addLayout(main_lineH1, stretch=2)
main_lineV1.addLayout(main_lineH2, stretch=8)
main_lineV1.addStretch(1)
main_lineV1.addLayout(main_lineH3, stretch=1)
main_lineV1.setSpacing(5)

window.setLayout(main_lineV1)

def show_result():
    GroupBox.hide()
    ResultGroupBox.show()
    Button.setText("Наступне запитання")

def show_question():
    GroupBox.show()
    ResultGroupBox.hide()
    Button.setText("Відповідь")
    RadioGroup.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [answer1, answer2, answer3, answer4]

def asker(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.text)
    correct.setText("Правильна відповідь: " + q.right_answer)
    show_question()

def next_question():
    random = randint(0, len(quetions_list) - 1)
    q = quetions_list[random]
    asker(q)

def check_answer():
    if RadioGroup.checkedButton() is None:
        return
    if answers[0].isChecked():
        result.setText("Молодець.Правильно.")
    else:
        result.setText("Невірно!")
    show_result()
    rating = window.score/window.total*100
    print('все ответы', window.total)
    print('правильные ответы', window.total)
    print('процентики', rating, '%')
def button_OK():
    if Button.text() == "Відповідь":
        check_answer()
    else:
        next_question()

window.score = 0
window.total = 0
Button.clicked.connect(button_OK)
next_question()


window.show()
app.exec_()