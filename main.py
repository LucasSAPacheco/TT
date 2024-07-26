import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registro de Dados e Análise")

        layout = QVBoxLayout()

        self.button = QPushButton("Gerar Gráfico")
        self.button.clicked.connect(self.gerar_grafico)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def gerar_grafico(self):
        try:
            data = {
                'Categoria': ['A', 'B', 'C', 'D'],
                'Valores': [23, 17, 35, 29]
            }
            df = pd.DataFrame(data)

            sns.barplot(x='Categoria', y='Valores', data=df)
            plt.title('Valores por Categoria')
            plt.xlabel('Categoria')
            plt.ylabel('Valores')
            plt.show()
        except Exception as e:
            print(f"Erro ao gerar gráfico: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
