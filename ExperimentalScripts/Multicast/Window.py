import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QGridLayout, QMainWindow, QLabel
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer

app = QApplication(sys.argv)

# Création de la fenêtre principale
window = QMainWindow()

# Création de la zone de texte non modifiable qui prend toute la place
textEdit = QTextEdit()
textEdit.setReadOnly(True)

# Fonction à exécuter toutes les 5 secondes
def updateTextEdit():
    textEdit.append("Text added at " + str(datetime.now()))

# Création du timer
timer = QTimer()
timer.setInterval(5000) # 5000 milliseconds = 5 secondes
timer.timeout.connect(updateTextEdit)
timer.start()
 

# Création de la zone de texte plus petite dans le coin inférieur droit
label = QLabel("Plus petite zone de texte")

# utilisation d'un layout pour organiser les widgets
layout = QGridLayout()
layout.addWidget(textEdit, 0, 0, 1, 3)
layout.addWidget(label, 1, 2)

# Création d'un widget central pour contenir le layout
centralWidget = QWidget()
centralWidget.setLayout(layout)

# Affectation du widget central à la fenêtre principale
window.setCentralWidget(centralWidget)

# Afficher la fenêtre
window.show()

sys.exit(app.exec_())