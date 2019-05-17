#coding:utf8
import sys
from PyQt4 import QtGui

def window():
   app = QtGui.QApplication(sys.argv)
   w = QtGui.QWidget()
	
   b1 = QtGui.QPushButton(w)
   b2 = QtGui.QPushButton(w)
   b3 = QtGui.QPushButton(w)
   select = QtGui.QComboBox(w)
   select.addItem('First Fit')
   select.addItem('Best Fit')
   select.addItem('Worst Fit')
   f1 = QtGui.QPixmap('f1.png')
   p1 = QtGui.QPixmap('p1.png')
   r1 = QtGui.QPixmap('r1.png')
   b1.setIcon(QtGui.QIcon(f1))
   b2.setIcon(QtGui.QIcon(p1))
   b3.setIcon(QtGui.QIcon(r1))
   b1.move(180,100)
   b2.move(130,100)
   b3.move(80,100)
   select.move(110,50)
	
   w.setGeometry(10,10,300,200)
   w.setWindowTitle('PyQt')
   w.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   window()
