# -*- coding: utf-8 -*-
#!/usr/bin/env python

from PyQt5.QtCore import (QLineF, QPointF, QRectF, Qt, QTimer, QThread, QUrl)
from PyQt5.QtGui import (QBrush, QColor, QPainter, QLinearGradient, QIntValidator)
from PyQt5.QtWidgets import (QApplication, QWidget, QGraphicsView, QGraphicsScene, QGraphicsItem, 
                             QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QSlider, QFileDialog, QSizePolicy)

import matplotlib
matplotlib.use('Qt5Agg')
import numpy as np

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

import time

class Session():
    def __init__(self):
        self.records = []
        self.bestTime = None
        self.recordsAo5 = []
        self.bestAo5 = None
        self.recordsAo12 = []
        self.bestAo12 = None
        self.recordsAo100 = []
        self.bestAo100 = None
    
    def record(self, time):
        self.records.append(time)
        if len(self.records)>=5:
            self.recordsAo5.append(sum(sorted(self.records[-5:])[1:-1])/3)
        if len(self.records)>=12:
            self.recordsAo12.append(sum(sorted(self.records[-12:])[1:-1])/10)
        if len(self.records)>=100:
            self.recordsAo100.append(sum(sorted(self.records[-100:])[1:-1])/98)
        self.update_best()
    
    def update_best(self):
        if not self.bestTime or self.bestTime > self.records[-1]:
            self.bestTime = self.records[-1]
        if self.recordsAo5 and (not self.bestAo5 or self.bestAo5 > self.recordsAo5[-1]):
            self.bestAo5 = self.recordsAo5[-1]
        if self.recordsAo12 and (not self.bestAo12 or self.bestAo12 > self.recordsAo12[-1]):
            self.bestAo12 = self.recordsAo12[-1]
        if self.recordsAo100 and (not self.bestAo100 or self.bestAo100 > self.recordsAo100[-1]):
            self.bestAo100 = self.recordsAo100[-1]
    
    def show_figure(self, ax, show_graph):
        if show_graph[0] and self.records:
            ax.plot([100 - len(self.records) + i for i in range(len(self.records))], self.records, color = '#DFDFDF', linewidth = 0.6, 
                    label='Time  Best: {:.2f}'.format(round(self.bestTime,2)))
        if show_graph[4]:
            ax.plot([0,99], [self.bestTime, self.bestTime], color = '#DFDFDF', linestyle = '--', linewidth = 0.6)
        if show_graph[1] and self.recordsAo5:
            ax.plot([100 - len(self.recordsAo5) + i for i in range(len(self.recordsAo5))], self.recordsAo5, color = '#7FDFFF', linewidth = 0.6, 
                    label='Ao5   Best: {:.2f}'.format(round(self.bestAo5,2)))
        if show_graph[5]:
            ax.plot([0,99], [self.bestAo5, self.bestAo5], color = '#7FDFFF', linestyle = '--', linewidth = 0.6)
        if show_graph[2] and self.recordsAo12:
            ax.plot([100 - len(self.recordsAo12) + i for i in range(len(self.recordsAo12))], self.recordsAo12, color = '#007FFF', linewidth = 0.6, 
                    label='Ao12  Best: {:.2f}'.format(round(self.bestAo12,2)))
        if show_graph[6]:
            ax.plot([0,99], [self.bestAo12, self.bestAo12], color = '#0F7FFF', linestyle = '--', linewidth = 0.6)
        if show_graph[3] and self.recordsAo100:
            ax.plot([100 - len(self.recordsAo100) + i for i in range(len(self.recordsAo100))], self.recordsAo100, color = '#005FBF', linewidth = 0.6, 
                    label='Ao100 Best: {:.2f}'.format(round(self.bestAo100,2)))
        if show_graph[7]:
            ax.plot([0,99], [self.bestAo100, self.bestAo100], color = '#005FBF', linestyle = '--', linewidth = 0.6)
        ax.set_xlim([0,99])
        ax.set_xticklabels([])
        ax.set_ylim([0.0,30.0])
        ax.set_yticks(np.arange(0,31,10))
        ax.set_yticklabels([0,10,20,30], fontsize=6,fontfamily='monospace',color = "#DFDFDF")
        if any(show_graph[4:]):
            leg = ax.legend(loc = 'lower left', facecolor='#3F3F3F', framealpha = 0.8, prop={'size':4, 'family':'monospace'})
            for text in leg.get_texts():
                plt.setp(text, color="#DFDFDF")

class Display(QGraphicsItem):
    def __init__(self, width=800, height=450):
        super(Display, self).__init__()
        self.width = width
        self.height = height
        
        self.session = Session()
        
        self.status = 0
        self.time = 0.0
        self.stayTime = 0.0
        self.starTime = None
    
    def keyPress(self):
        if self.status == 0:
            self.status = 1
            return False
        elif self.status == 2:
            
            ############
            ### STOP ###
            ############
            
            self.status = 3
            self.time = time.time() - self.startTime
            self.session.record(self.time)
            return True
    
    def keyRelease(self):
        if self.status == 1:
            if self.stayTime >= 0.3:
                
                #############
                ### START ###
                #############
                
                self.status = 2
                self.time = 0.0
                self.startTime = time.time()
            else:
                self.status = 0
                self.stayTime = 0.0
        if self.status == 3:
            self.status = 0
            self.stayTime = 0.0
            
        
    def update_time(self):
        if self.status == 1:
            self.stayTime += 1/60
        elif self.status == 2:
            self.time += 1/60
        
        self.update()
    
    def paint(self, painter, option, widget):
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(63,63,63))
        painter.drawRect(0,0,self.width,self.height)
        font = painter.font()
        font.setFamily('monospace')
        painter.setFont(font)
        if self.status == 1:
            if self.stayTime < 0.3:
                painter.setPen(QColor(223,63,63))
            else:
                painter.setPen(QColor(63,223,63))
        else:
            painter.setPen(QColor(223,223,223))
        font.setPixelSize(270)
        painter.setFont(font)
        painter.drawText(QRectF(0,60,500,270),Qt.AlignRight,str(int(self.time)))
        font.setPixelSize(180)
        painter.setFont(font)
        if self.status == 2:
            painter.drawText(QRectF(500,150,300,180),Qt.AlignLeft, '.'+str(int((self.time-int(self.time))*10)))
        else:
            painter.drawText(QRectF(500,150,300,180),Qt.AlignLeft, '.'+str('{:02d}'.format(int((self.time-int(self.time))*100))))
        
    def boundingRect(self):
        return QRectF(0,0,self.width,self.height)

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.graphicsView = QGraphicsView()
        scene = QGraphicsScene(self.graphicsView)
        scene.setSceneRect(0, 0, 800, 450)
        self.graphicsView.setScene(scene)
        self.display = Display()
        scene.addItem(self.display)
        self.graphicsView.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        
        self.show_graph = [True for _ in range(8)]
        self.fig, self.ax = plt.subplots(facecolor = "#3F3F3F", figsize=(2.5, 2))
        self.ax.set_aspect(1.5)
        self.ax.set_facecolor("#3F3F3F")
        for child in self.ax.get_children():
            if isinstance(child, matplotlib.spines.Spine):
                child.set_color("#DFDFDF")
                child.set_linewidth(0.5)
        self.ax.tick_params(color="#DFDFDF", width = 0.5, bottom = False)
        
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setFixedSize(500,200)
        self.canvas.setParent(self)
        
        self.ax.cla()
        self.display.session.show_figure(self.ax, self.show_graph)
        
        self.timer = QTimer(self)
        self.timer.setInterval(16)
        self.timer.timeout.connect(self.update_time)
        self.timer.start()
        
        
        style='''
            QPushButton{
                background-color: transparent;
                color:#7F7F7F;
                border:2px solid #7F7F7F;
                border-radius: 4px;
                font:bold 16px;
                font-family: monospace;
            }
            QPushButton:checked{
                background-color:transparent;
                color:#3FAFFF;
                border:2px solid #3FAFFF;
            }
            '''
        
        #           name,               label,          size,       check,          connect
        self.button('showTime',         'Time',         120,  24,   True, True,     'showTime',         style)
        self.button('showAo5',          'Ao5',          120,  24,   True, True,     'showAo5',          style)
        self.button('showAo12',         'Ao12',         120,  24,   True, True,     'showAo12',         style)
        self.button('showAo100',        'Ao100',        120,  24,   True, True,     'showAo100',        style)
        self.button('showBestTime',     'Best Time',    120,  24,   True, True,     'showBestTime',     style)
        self.button('showBestAo5',      'Best Ao5',     120,  24,   True, True,     'showBestAo5',      style)
        self.button('showBestAo12',     'Best Ao12',    120,  24,   True, True,     'showBestAo12',     style)
        self.button('showBestAo100',    'Best Ao100',   120,  24,   True, True,     'showBestAo100',    style)
        
        buttonsLayout = QGridLayout()
        buttonsLayout.setHorizontalSpacing(8)
        buttonsLayout.setVerticalSpacing(12)
        buttonsLayout.addWidget(self.showTimeButton, 1, 0)
        buttonsLayout.addWidget(self.showAo5Button, 2, 0)
        buttonsLayout.addWidget(self.showAo12Button, 3, 0)
        buttonsLayout.addWidget(self.showAo100Button, 4, 0)
        buttonsLayout.addWidget(self.showBestTimeButton, 1, 1)
        buttonsLayout.addWidget(self.showBestAo5Button, 2, 1)
        buttonsLayout.addWidget(self.showBestAo12Button, 3, 1)
        buttonsLayout.addWidget(self.showBestAo100Button, 4, 1)
        buttonsLayout.setRowStretch(0,1)
        buttonsLayout.setRowStretch(5,1)
        
        propertyLayout = QHBoxLayout()
        propertyLayout.addWidget(self.canvas)
        propertyLayout.addLayout(buttonsLayout)
        propertyLayout.addStretch(0)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.graphicsView)
        mainLayout.addLayout(propertyLayout)
        mainLayout.addStretch(0)
        self.setLayout(mainLayout)
        self.setWindowTitle("CUBE TIMER")
        
    def button(self, name, label, width, height, checkable, checked, clicked, style):
        exec("self.%sButton = QPushButton('%s', self)"      % (name, label))
        exec("self.%sButton.setStyleSheet(style)"           % (name))
        exec("self.%sButton.setFixedSize(%d, %d)"           % (name, width, height))
        if checkable:
            exec("self.%sButton.setCheckable(True)"         % (name))
            exec("self.%sButton.setChecked(%r)"             % (name, checked))
        exec("self.%sButton.clicked.connect(self.%s)"       % (name, clicked))
        
    def label(self, name, label_, width, center):
        exec("self.%sLabel = QLabel('%s', self)"                % (name, label_))
        if width:
            exec("self.%sLabel.setFixedWidth(%d)"             % (name, width))
        if center:
            exec("self.%sLabel.setAlignment(Qt.AlignCenter)"    % (name))
    
    def showTime(self, isChecked):
        self.show_graph[0] = isChecked
        self.update_figure()
    
    def showAo5(self, isChecked):
        self.show_graph[1] = isChecked
        self.update_figure()
    
    def showAo12(self, isChecked):
        self.show_graph[2] = isChecked
        self.update_figure()
    
    def showAo100(self, isChecked):
        self.show_graph[3] = isChecked
        self.update_figure()
    
    def showBestTime(self, isChecked):
        self.show_graph[4] = isChecked
        self.update_figure()
    
    def showBestAo5(self, isChecked):
        self.show_graph[5] = isChecked
        self.update_figure()
    
    def showBestAo12(self, isChecked):
        self.show_graph[6] = isChecked
        self.update_figure()
    
    def showBestAo100(self, isChecked):
        self.show_graph[7] = isChecked
        self.update_figure()
    
    def keyPressEvent(self, event):
        recorded = self.display.keyPress()
        
        if recorded:
            self.update_figure()
        
    def keyReleaseEvent(self, event):
        self.display.keyRelease()
    
    def update_time(self):
        self.display.update_time()
    
    def update_figure(self):
        self.ax.cla()
        self.display.session.show_figure(self.ax, self.show_graph)
        self.canvas.draw()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    pal = mainWindow.palette()
    pal.setColor(mainWindow.backgroundRole(), QColor(63,63,63))
    mainWindow.setPalette(pal)
    mainWindow.show()
    sys.exit(app.exec_())