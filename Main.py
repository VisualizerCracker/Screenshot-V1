import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QScreen, QGuiApplication
from PyQt5.QtCore import QRect

class ScreenshotWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Create a button to take the screenshot
        screenshotButton = QPushButton('Take Screenshot', self)
        screenshotButton.clicked.connect(self.takeScreenshot)
        
        # Create a label to display the screenshot
        self.screenshotLabel = QLabel(self)
        
        # Set the layout
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(screenshotButton)
        self.layout().addWidget(self.screenshotLabel)
        
    def takeScreenshot(self):
        # Get the size of the primary screen
        screenGeometry = QGuiApplication.primaryScreen().geometry()
        
        # Set the area to capture
        captureArea = QRect(0, 0, screenGeometry.width()/2, screenGeometry.height()/2)
        
        # Take a screenshot of the specified area
        screenshot = QApplication.primaryScreen().grabWindow(0, captureArea.x(), captureArea.y(), captureArea.width(), captureArea.height())
        
        # Display the screenshot in the label
        self.screenshotLabel.setPixmap(screenshot)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = ScreenshotWidget()
    widget.show()
    sys.exit(app.exec_())
