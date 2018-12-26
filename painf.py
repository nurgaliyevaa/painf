# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu 
from PyQt5.QtWidgets import QMenuBar, QAction, QFileDialog
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen
from PyQt5.QtWidgets import QColorDialog, QLabel
from PyQt5 import QtWidgets, QtGui, QtCore
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        TOP = 400
        LEFT = 400
        HEIGHT = 1440
        WIDTH = 820
        # Размеры окна
        
        self.setWindowTitle("Painf")
        self.setGeometry(TOP, LEFT, HEIGHT, WIDTH)
        # Создание окна
        
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.bgColor = Qt.white
        self.image.fill(self.bgColor)
        # Создание заднего фона
        
        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black
        # Дефолтные настройки кисти
        
        self.lastPoint = QPoint() 
        # Создание точки
        # Пригодится для использования мыши
        
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        brushMenu = mainMenu.addMenu("Brush Size")
        brushColorMenu = mainMenu.addMenu("Brush Color")
        toolsMenu = mainMenu.addMenu("More tools")
        bgColorMenu = mainMenu.addMenu("Background Color")
        # Создание различных настроек меню
        
        saveAction = QAction("Save", self)
        # Действие "сохранить"
        saveAction.setShortcut("Ctrl+S")
        # Создание горячей клавиши
        fileMenu.addAction(saveAction)
        # Добавление действия в меню
        saveAction.triggered.connect(self.save)
        # Запуск действия
    
        clearAction = QAction("Clear", self)
        # Действие "очистить"
        clearAction.setShortcut("Ctrl+C")
        # Создание горячей клавиши
        fileMenu.addAction(clearAction)
        # Добавление действия в меню
        clearAction.triggered.connect(self.clear)
        # Запуск действия
        
        threepxAction = QAction("3px", self)
        # Действие "толщина кисти - 3"
        threepxAction.setShortcut("Ctrl+3")
        # Создание горячей клавиши
        brushMenu.addAction(threepxAction)
        # Добавление действия в меню
        threepxAction.triggered.connect(self.threePx)
        # Запуск действия
        
        fivepxAction = QAction("5px", self)
        # Действие "толщина кисти - 5"
        fivepxAction.setShortcut("Ctrl+5")
        # Создание горячей клавиши
        brushMenu.addAction(fivepxAction)
        # Добавление действия в меню
        fivepxAction.triggered.connect(self.fivePx)
        # Запуск действия
        
        sevenpxAction = QAction("7px", self)
        # Действие "толщина кисти - 7"
        sevenpxAction.setShortcut("Ctrl+7")
        # Создание горячей клавиши
        brushMenu.addAction(sevenpxAction)
        # Добавление действия в меню
        sevenpxAction.triggered.connect(self.sevenPx)
        # Запуск действия
        
        ninepxAction = QAction("9px", self)
        # Действие "толщина кисти - 9"
        ninepxAction.setShortcut("Ctrl+9")
        # Создание горячей клавиши
        brushMenu.addAction(ninepxAction)
        # Добавление действия в меню
        ninepxAction.triggered.connect(self.ninePx) 
        # Запуск действия
        
        twelvepxAction = QAction("12px", self)
        # Действие "толщина кисти - 12"
        twelvepxAction.setShortcut("Ctrl+2")
        # Создание горячей клавиши
        brushMenu.addAction(twelvepxAction)
        # Добавление действия в меню
        twelvepxAction.triggered.connect(self.twelvePx)
        # Запуск действия
        
        fifteenpxAction = QAction("15px", self)
        # Действие "толщина кисти - 15"
        fifteenpxAction.setShortcut("Ctrl+4")
        # Создание горячей клавиши
        brushMenu.addAction(fifteenpxAction)
        # Добавление действия в меню
        fifteenpxAction.triggered.connect(self.fifteenPx)  
        # Запуск действия
        
        eighteenpxAction = QAction("18px", self) 
        # Действие "толщина кисти - 18"   
        eighteenpxAction.setShortcut("Ctrl+6")
        # Создание горячей клавиши
        brushMenu.addAction(eighteenpxAction)
        # Добавление действия в меню
        eighteenpxAction.triggered.connect(self.eighteenPx) 
        # Запуск действия
            
        twentyonepxAction = QAction("21px", self)
        # Действие "толщина кисти - 21"
        twentyonepxAction.setShortcut("Ctrl+8")
        # Создание горячей клавиши
        brushMenu.addAction(twentyonepxAction)
        # Добавление действия в меню
        twentyonepxAction.triggered.connect(self.twentyonePx) 
        # Запуск действия

    
        blackAction = QAction("Black", self)
        # Действие "цвет кисти - черный"        
        blackAction.setShortcut("Shift+D")
        # Создание горячей клавиши
        brushColorMenu.addAction(blackAction)
        # Добавление действия в меню
        blackAction.triggered.connect(self.blackColor)
        # Запуск действия
        
        whiteAction = QAction("White", self)
        # Действие "цвет кисти - белый"        
        whiteAction.setShortcut("Shift+W")
        # Создание горячей клавиши
        brushColorMenu.addAction(whiteAction)
        # Добавление действия в меню
        whiteAction.triggered.connect(self.whiteColor)
        # Запуск действия
        
        yellowAction = QAction("Yellow", self)
        # Действие "цвет кисти - желтый"        
        yellowAction.setShortcut("Shift+Y")
        # Создание горячей клавиши
        brushColorMenu.addAction(yellowAction)
        # Добавление действия в меню
        yellowAction.triggered.connect(self.yellowColor)
        # Запуск действия
        
        redAction = QAction("Red", self)
        # Действие "цвет кисти - красный"        
        redAction.setShortcut("Shift+R")
        # Создание горячей клавиши
        brushColorMenu.addAction(redAction)
        # Добавление действия в меню
        redAction.triggered.connect(self.redColor)
        # Запуск действия
        
        greenAction = QAction("Green", self)
        # Действие "цвет кисти - зеленый"        
        greenAction.setShortcut("Shift+G")
        # Создание горячей клавиши
        brushColorMenu.addAction(greenAction)
        # Добавление действия в меню
        greenAction.triggered.connect(self.greenColor) 
        # Запуск действия
        
        blueAction = QAction("Blue", self)
        # Действие "цвет кисти - синий"        
        blueAction.setShortcut("Shift+B")
        # Создание горячей клавиши
        brushColorMenu.addAction(blueAction)
        # Добавление действия в меню
        blueAction.triggered.connect(self.blueColor)
        # Запуск действия
        
        brownAction = QAction("Brown", self)
        # Действие "цвет кисти - коричевый"        
        brownAction.setShortcut("Shift+W")
        # Создание горячей клавиши
        brushColorMenu.addAction(brownAction)
        # Добавление действия в меню
        brownAction.triggered.connect(self.brownColor)
        # Запуск действия
        
        chooseColorAction = QAction("Choose color", self)
        chooseColorAction.setShortcut("Shift+C")
        # Создание горячей клавиши
        brushColorMenu.addAction(chooseColorAction)
        # Добавление действия в меню
        chooseColorAction.triggered.connect(self.chooseColor)
        # Вызов диалогового окна для выбора цвета

        brushAction = QAction("Brush", self)
        brushAction.setShortcut("Ctrl+H")
        # Создание горячей клавиши
        toolsMenu.addAction(brushAction)
        # Добавление действия в меню
        brushAction.triggered.connect(self.brush)   
        # Выбор кисти
        
        penAction = QAction("pen", self)
        penAction.setShortcut("Ctrl+P")
        # Создание горячей клавиши
        toolsMenu.addAction(penAction)
        # Добавление действия в меню
        penAction.triggered.connect(self.pen)   
        # Выбор кисти
        
        eraserAction = QAction("Eraser", self)
        eraserAction.setShortcut("Ctrl+E")
        # Создание горячей клавиши
        toolsMenu.addAction(eraserAction)
        # Добавление действия в меню
        eraserAction.triggered.connect(self.eraser)
        # Выбор ластика
        
        self.coords = QLabel(self)
        self.coords.setText("Coords:None, None")
        self.coords.move(10, 790)
        self.show()
        # Создание лэйбла с координатами
        
        blackBgAction = QAction("Black", self)
        # Действие "цвет заднего фона - черный"
        bgColorMenu.addAction(blackBgAction)
        # Добавление действия в меню
        blackBgAction.triggered.connect(self.blackBgColor)
        # Запуск действия
                
        
        whiteBgAction = QAction("White", self)
        # Действие "цвет заднего фона - белый"        
        bgColorMenu.addAction(whiteBgAction)
        # Добавление действия в меню
        whiteBgAction.triggered.connect(self.whiteBgColor)
        # Запуск действия
        
        yellowBgAction = QAction("Yellow", self)
        # Действие "цвет заднего фона - желтый"        
        bgColorMenu.addAction(yellowBgAction)
        # Добавление действия в меню
        yellowBgAction.triggered.connect(self.yellowBgColor)
        # Запуск действия
        
        redBgAction = QAction("Red", self)
        # Действие "цвет заднего фона - красный"        
        bgColorMenu.addAction(redBgAction)
        # Добавление действия в меню
        redBgAction.triggered.connect(self.redBgColor)
        # Запуск действия
        
        greenBgAction = QAction("Green", self)
        # Действие "цвет заднего фона - зеленый"        
        bgColorMenu.addAction(greenBgAction)
        # Добавление действия в меню
        greenBgAction.triggered.connect(self.greenBgColor) 
        # Запуск действия
        
        blueBgAction = QAction("Blue", self)
        # Действие "цвет заднего фона - синий"        
        bgColorMenu.addAction(blueBgAction)
        # Добавление действия в меню
        blueBgAction.triggered.connect(self.blueBgColor)
        # Запуск действия
        
        brownBgAction = QAction("Brown", self)
        # Действие "цвет заднего фона - коричневый"        
        bgColorMenu.addAction(brownBgAction)
        # Добавление действия в меню
        brownBgAction.triggered.connect(self.brownBgColor) 
        # Запуск действия
        
        chooseBgColorAction = QAction("Choose color", self)
        bgColorMenu.addAction(chooseBgColorAction)
        # Добавление действия в меню
        chooseBgColorAction.triggered.connect(self.chooseBgColor) 
        # Вызов диалогового окна для выбора цвета
        

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
     # Если была нажата левая кнопка мыши lastPoint станет коордиеатой действия
            
    def mouseMoveEvent(self, event):
        self.coords.setText("Coords:{}, {}".format(event.x(), event.y()))
        # Обозначения коорднат курсора
        
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            # Если была нажата левая кнопка мыши и drawing == True, то создаем ручку
            self.lastPoint = event.pos()
            self.update()
    
    def mouseReleaseEvent(self, event):    
        if event.button == Qt.LeftButton:
            self.drawing = False
        # Если отпустить кнопку мыши, то рисование прекратится
            
            
    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())
        # Процесс рисования
        
    def save(self):
        filePath = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);; ALL Files('.'!)")
        if filePath == "":
            return
        self.image.save(filePath)
        # Реализация метода "save"
        
    def clear(self):
        self.image.fill(Qt.white)
        self.update()
        # Реализация метода "clear"
        
    def threePx(self):
        self.brushSize = 3
        # Изменение толщины кисти на 3
    
    def fivePx(self):
        self.brushSize = 5
        # Изменение толщины кисти на 5
        
    def sevenPx(self):
        self.brushSize = 7
        # Изменение толщины кисти на 7
        
    def ninePx(self):
        self.brushSize = 9
        # Изменение толщины кисти на 9
        
    def twelvePx(self):
        self.brushSize = 12
        # Изменение толщины кисти на 12
    
    def fifteenPx(self):
        self.brushSize = 15
        # Изменение толщины кисти на 15
    
    def eighteenPx(self):
        self.brushSize = 18
        # Изменение толщины кисти на 18 
        
    def twentyonePx(self):
        self.brushSize = 21    
        # Изменение толщины кисти на 21
    
    def blackColor(self):
        self.brushColor = Qt.black
        # Изменение цвета кисти на черный
        
    def whiteColor(self):
        self.brushColor = Qt.white
        # Изменение цвета кисти на белый
    
    def yellowColor(self):
        self.brushColor = Qt.yellow 
        # Изменение цвета кисти на желтый
        
    def greenColor(self):
        self.brushColor = Qt.green 
        # Изменение цвета кисти на зеленый
        
    def redColor(self):
        self.brushColor = Qt.red
        # Изменение цвета кисти на красный
        
    def blueColor(self):
        self.brushColor = Qt.blue
        # Изменение цвета кисти на синий
        
    def brownColor(self):
        self.brushColor = Qt.brown    
        # Изменение цвета кисти на коричневый
    
    def chooseColor(self):
        color = QColorDialog.getColor()
        # Открытие диалогового окна и выбор цвета кисти
        if color.isValid():
            self.brushColor = color
        # Присваивание выбраного цвета кисти
    
    def blackBgColor(self):
        self.brushColor = Qt.black
        self.image.fill(self.bgColor)
        self.update()
        # Изменение цвета заднего фона на черный
        
    def whiteBgColor(self):
        self.bgColor = Qt.white
        self.image.fill(self.bgColor)
        self.update()
        # Изменение цвета заднего фона на белый
    
    def yellowBgColor(self):
        self.bgColor = Qt.yellow 
        self.image.fill(self.bgColor)
        self.update()
        # Изменение цвета заднего фона на желтый
        
    def greenBgColor(self):
        self.bgColor = Qt.green 
        self.image.fill(self.bgColor)
        self.update()
        # Изменение цвета заднего фона на зеленый
        
    def redBgColor(self):
        self.bgColor = Qt.red
        self.image.fill(self.bgColor)
        self.update()
        # Изменение цвета заднего фона на красный
        
    def blueBgColor(self):
        self.bgColor = Qt.blue
        self.image.fill(self.bgColor)
        self.update()
        # Изменение цвета заднего фона на синий
        
    def brownBgColor(self):
        self.bgColor = Qt.brown 
        self.image.fill(self.bgColor)
        # Изменение цвета заднего фона на коричневый
    
    def chooseBgColor(self):
        color = QColorDialog.getColor()
        # Открытие диалогового окна и выбор цвета заднего фона
        if color.isValid():
            self.bgColor = color
        self.image.fill(self.bgColor)
        self.update()
        # Присваивание выбраного цвета заднему фону 
    
    
    def brush(self):
        self.brushColor = Qt.black
        # Выбор кисти
        
    def pen(self):
        self.brushColor = Qt.blue
        self.brushSize = 3
        # Выбор ручки
    def eraser(self):
        self.brushColor = Qt.white
        # Выбор ластика
    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()