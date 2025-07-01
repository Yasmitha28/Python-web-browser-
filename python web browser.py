import sys
from PyQt5.QtWidgets
import QApplications,QMainWindow
from PyQt5.QtWebEngineWidgets
import QWebEngineView
from PyQt5.QtCore
import QUrl
app=QApplication(sys.argv)
Window=QMainWindow()
Window.setWindowTitle("Simple Browser")
Window.setGeometry(100,100,800,600)
browser=QWebEngineView()
browser.setUrl(QUrl("https://www.google.com"))
Window.setCentralWidget(browser)
Window.show()
sys.exit(app.exec_())
