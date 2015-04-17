import guidefault
import sys
import xlwt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidget,QPushButton,QHBoxLayout,QVBoxLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QTableWidgetItem
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# Output Tab
class OutputTab(guidefault.DefaultTab):

    def __init__(self):
        """
            Constructor
            """
        super().__init__()
        self.initGraph()
    

    def initGraph(self):
        """
            Create an output screen containing one table, three line edit widgets and six buttons
            The first line edit widget will display the name for the warehouse
            The second line edit widget will display the total Optimal Cost
            The third line edit widget will display the total Non-Distance Optimal Cost
            The fourth line edit widget will display the total optimal distance
            the fifth line edit widget will display the total weight
            The "Export to excel sheet" button exports the data in the table to a new spreadsheet
        """
        self.resize(800,500)
        self.move(300,200)
        self.setWindowTitle('<output tab>')

        self.labelOne=QLabel('Warehouse', self)
        self.line=QLineEdit(self)
        self.labelTwo=QLabel('Total Optimal Cost',self)
        self.lineTwo=QLineEdit(self)
        self.labelThree=QLabel('Total Non-Distance Optimal Cost',self)
        self.lineThree=QLineEdit(self)
        self.labelFour=QLabel('Total Optimal Distance',self)
        self.lineFour=QLineEdit(self)
        self.labelFive=QLabel('Total Weight',self)
        self.lineFive=QLineEdit(self)

        hBox=QHBoxLayout()
        hBox.addStretch()
        hBox.addWidget(self.labelOne)
        hBox.addStretch(1)
        hBox.addWidget(self.line)
        hBoxTwo=QHBoxLayout()
        hBoxTwo.addStretch()
        hBoxTwo.addWidget(self.labelTwo)
        hBoxTwo.addStretch(1)
        hBoxTwo.addWidget(self.lineTwo)
        hBoxThree=QHBoxLayout()
        hBoxThree.addStretch()
        hBoxThree.addWidget(self.labelThree)
        hBoxThree.addStretch(1)
        hBoxThree.addWidget(self.lineThree)
        hBoxFour=QHBoxLayout()
        hBoxFour.addStretch()
        hBoxFour.addWidget(self.labelFour)
        hBoxFour.addStretch(1)
        hBoxFour.addWidget(self.lineFour)
        hBoxFive=QHBoxLayout()
        hBoxFive.addStretch()
        hBoxFive.addWidget(self.labelFive)
        hBoxFive.addStretch(1)
        hBoxFive.addWidget(self.lineFive)
        vBox=QVBoxLayout()
        vBox.addStretch()
        vBox.addLayout(hBox)
        vBox.addLayout(hBoxTwo)
        vBox.addLayout(hBoxThree)
        vBox.addLayout(hBoxFour)
        vBox.addLayout(hBoxFive)

        self.table=QTableWidget(1000,9,self)
        self.table.setHorizontalHeaderLabels(['district','site 1', 'site 2', 'actual distance','optimal distance','weight','truck size','optimal cost', 'Non-Distance optimal cost'])
        self.table.setColumnWidth(0,100)
        self.table.setColumnWidth(1,100)
        self.table.setColumnWidth(2,100)
        self.table.setColumnWidth(3,100)
        self.table.setColumnWidth(4,100)
        self.table.setColumnWidth(5,100)
        self.table.setColumnWidth(6,100)
        self.table.setColumnWidth(7,100)
        self.table.setColumnWidth(8,150)

        hBoxSix=QHBoxLayout()
        hBoxSix.addWidget(self.table)
        vBox.addLayout(hBoxSix)

        self.buttonOne=QPushButton('Export to excel sheet',self)
        self.buttonOne.clicked.connect(self.createExcelSheet)

        hBoxSeven=QHBoxLayout()
        hBoxSeven.addStretch(1)
        hBoxSeven.addWidget(self.buttonOne)
        vBox.addStretch(1)
        vBox.addLayout(hBoxSeven)

        self.setLayout(vBox)
        self.show()

    def showtable(self,theList,theName):
        """
            Displays the data on the table
            Displays the name of the warehouse
            Calculates the sum of the optimal distance and displays it
            Calculates the sum of the total weight and displays it
            Calcualtes the sum of the optimal cost and displays it
            Calcualtes the sum of the non-distance cost and displays it
        """
        self.theList=theList
        self.warehouseName=theName
        rowAdjust = 0

        for k in range(len(self.theList)):
            self.theList=self.theList[k]
            
            
            # Displays the data on the table
            for i in range(len(self.theList)):
                for j in range(len(self.theList[i])):
                    self.table.setItem(i,j,QTableWidgetItem(str(self.theList[i][j])[:11]))
            for i in range(len(self.theList)):
                self.table.setItem(i,3,QTableWidgetItem(str(self.theList[i][3])[:7]))
            for i in range(len(self.theList)):
                self.table.setItem(i,4,QTableWidgetItem(str(self.theList[i][4])[:7]))
            for i in range(len(self.theList)):
                self.table.setItem(i,5,QTableWidgetItem(str(self.theList[i][5])[:7]))
            for i in range(len(self.theList)):
                self.table.setItem(i,6,QTableWidgetItem(str(self.theList[i][6])[:7]))
            for i in range(len(self.theList)):
                self.table.setItem(i,7,QTableWidgetItem(str(self.theList[i][7])[:7]))
            for i in range(len(self.theList)):
                self.table.setItem(i,8,QTableWidgetItem(str(self.theList[i][8])[:7]))
        

            # Calculates the sum of the optimal distance and displays the value in the fourth line edit widget
            totalDistance=0
            for i in range(len(self.theList)):
                totalDistance=totalDistance+self.theList[i][4]
            self.lineFour.setText(str(totalDistance)[:7])

            # Calculates the sum of the total weight and displays the value in the fifth line edit widget
            totalWeight=0
            for i in range(len(self.theList)):
                totalWeight=totalWeight+self.theList[i][5]
            self.lineFive.setText(str(totalWeight)[:7])

            # Calculates the sum of the optimal cost and displays the value in the second line edit widget
            totalCost=0
            for i in range(len(self.theList)):
                totalCost=totalCost+self.theList[i][7]
            self.lineTwo.setText(str(totalCost)[:7])

            # Calculates the sum of non-distance optimal cost and displays the value in the third line edit widget
            totalCostOne=0
            for i in range(len(self.theList)):
                totalCostOne=totalCostOne+theList[i][8]
            self.lineThree.setText(str(totalCostOne)[:7])

            # Displays the name of the warehouse in the first line edit widget
            self.line.setText(self.warehouseName)

    def createExcelSheet(self,theList):
        """
            Exports the data in the table to a new Excel spreasheet
            The new Excel spreasheet is saved as "outputsheet.xls"
        """
        self.theList=theList
        
        workbook=xlwt.Workbook()
        worksheet=workbook.add_sheet('output')

        bold=xlwt.easyxf('font:bold 1')
        worksheet.write(0,0,'Total Optimal Cost',bold)
        worksheet.write(0,2,'Total Non-Distance Optimal Cost',bold)
        worksheet.write(0,4,'Total Optimal Distance',bold)
        worksheet.write(0,6,'Total Weight',bold)
        worksheet.write(1,0,'District',bold)
        worksheet.write(1,1,'Site 1',bold)
        worksheet.write(1,2,'Site 2',bold)
        worksheet.write(1,3,'Actual Distance',bold)
        worksheet.write(1,4,'Optimal Distance',bold)
        worksheet.write(1,5,'Weight',bold)
        worksheet.write(1,6,'Truck Size',bold)
        worksheet.write(1,7,'Optimal Cost',bold)
        worksheet.write(1,8,'Non-Distance Optimal Cost',bold)

        worksheet.col(0).width=256*20
        worksheet.col(1).width=256*20
        worksheet.col(2).width=256*30
        worksheet.col(3).width=256*20
        worksheet.col(4).width=256*20
        worksheet.col(5).width=256*20
        worksheet.col(6).width=256*20
        worksheet.col(7).width=256*20
        worksheet.col(8).width=256*25


        for k in range(len(self.theList)):
            self.theList=self.theList[k]
        
            # Displays the data in the table in the spreadsheet
            for i in range(len(self.theList)):
                for j in range(len(self.theList[i])):
                    worksheet.write(i+2,j,theList[i][j])

            # Calculates the total optimal cost and displays it
            totalOptimalCost=0
            for i in range(len(self.theList)):
                totalOptimalCost=totalOptimalCost+self.theList[i][7]
            worksheet.write(0,1,totalOptimalCost)

            # Calcualtes the total non-distance optimal cost and displays it
            totalNonDistanceOptimalCost=0
            for i in range(len(self.theList)):
                totalNonDistanceOptimalCost=totalNonDistanceOptimalCost+theList[i][8]
            worksheet.write(0,3,totalNonDistanceOptimalCost)
        
            # Calculates the total optimal distance and displays it
            totalOptimalDistance=0
            for i in range(len(self.theList)):
                totalOptimalDistance=totalOptimalDistance+theList[i][4]
            worksheet.write(0,5,totalOptimalDistance)
        
            # Calculates the total truck weight and displays it
            totalTruckWeight=0
            for i in range(len(self.theList)):
                totalTruckWeight=totalTruckWeight+self.theList[i][5]
            worksheet.write(0,7,totalTruckWeight)

            # Saves the new Excel spreadsheet as "outputsheet.xls"
            workbook.save('outputsheet.xls')









