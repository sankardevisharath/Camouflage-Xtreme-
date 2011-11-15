#Camouflage Extreme 1.0

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os


import ui_Camou
import resources_rc
import Encryption
import Decryption
import Steg
import shutil

class Camou (QMainWindow,ui_Camou.Ui_MainWindow,Encryption.encryption,Decryption.decryption):
	def __init__(self,parent=None):
		super(Camou,self).__init__(parent)
		self.setupUi(self)
		self.updateUI()	
		self.extractToolButton.setEnabled(False)
	def updateUI(self):
		if self.tabWidget.currentIndex()==0 :
			enable=not ((self.fileLineEdit.text().isEmpty()) or (self.imageFileLineEdit.text().isEmpty()))
			self.hidetoolButton.setEnabled(enable)
			self.hideStatusLabel.setText("Ready")
		else:
			enable=not((self.efileLineEdit.text().isEmpty()) or (self.saveasLineEdit.text().isEmpty()) )
			self.extractToolButton.setEnabled(enable)
			self.extractStatusLabel.setText("Ready")
######Hide########
	@pyqtSignature("")
	def on_hidetoolButton_clicked(self):
		if self.passwordLineEdit.text()==self.cpasswordLineEdit.text():
			iname=self.imageFileLineEdit.text()
			
			if os.path.exists(iname)==False:
				self.hideStatusLabel.setText("*Enter a valid Image file name")
				self.imageFileLineEdit.setText("")
				self.imageFileLineEdit.setFocus(True)
				return
			fname=self.fileLineEdit.text()
			if os.path.exists(fname)==False:
				self.hideStatusLabel.setText("*Enter a valid File name")
				self.fileLineEdit.setText("")
				self.fileLineEdit.setFocus(True)
				return
			saveasfilename=QFileDialog.getSaveFileName(self,'save file ','/home')
			password=self.passwordLineEdit.text()
			self.encinit(password,fname)
			print 'Encryption done'
			saveasfilename=saveasfilename+self.opimageComboBox.currentText()
			
			if Steg.embed(str(iname),'./temp',str(saveasfilename),str(password))!=0:
				self.hideStatusLabel.setText("Data too long stored partially")
				print 'Data embeded'
			else:
				self.passwordLabel.setText("")
				self.hideStatusLabel.setText("Data encoded in image")
			self.fileLineEdit.setText("")
			self.passwordLineEdit.setText("")
			self.cpasswordLineEdit.setText("")
			self.imageFileLineEdit.setText("")
			self.opimageComboBox.setCurrentIndex(0)
			self.updateUI()
			
		else:
			self.passwordLabel.setText("*Password Mismatch")
			self.cpasswordLineEdit.setText("")
			self.passwordLineEdit.setText("")
			self.passwordLineEdit.setFocus(True)
			
			
	@pyqtSignature("QString")
	def on_fileLineEdit_textEdited(self,text):
		self.updateUI()
	@pyqtSignature("QString")
	def on_imageFileLineEdit_textEdited(self,text):
		self.updateUI()
	@pyqtSignature("")
	def on_browsePushButton_clicked(self):
		fname=QFileDialog.getOpenFileName(self,'Select File','/home')
		if len(fname)!=0:
			self.updateUI()		
		self.fileLineEdit.setText(fname)
		info=QFileInfo(fname)
	@pyqtSignature("")
	def on_browseImagePushButton_clicked(self):
		imagefilename=QFileDialog.getOpenFileName(self,'select file','/home',"Image file (*.jpg *.png *.bmp *.tiff)")
		self.imageFileLineEdit.setText(imagefilename)
		if len(imagefilename)!=0:
			self.updateUI()
######Extraction######		
	@pyqtSignature("")
	def on_extractToolButton_clicked(self):
		if self.epasswordLineEdit.text()==self.ecpasswordLineEdit.text():
			iname=self.efileLineEdit.text()
			if os.path.exists(iname)==False:
				self.extractStatusLabel.setText("Enter a valid file name to  decode")
				self.efileLineEdit.setText("")
				self.efileLineEdit.setFocus(True)
			password=self.epasswordLineEdit.text()
			Steg.extract(str(iname),'temp.txt',str(password))
			print 'extraction done'
			self.decinit(password,'temp.txt')
			print 'decryption done'
			opfile=open(self.saveasLineEdit.text(),'w')
			t=open('temp.txt','r+')
			shutil.copyfile('temp.txt',self.saveasLineEdit.text())
			os.remove('temp.txt')
			self.epasswordLabel.setText("")
			self.extractStatusLabel.setText("Data extracted")
			self.epasswordLineEdit.setText("")
			self.efileLineEdit.setText("")
			self.ecpasswordLineEdit.setText("")
			self.saveasLineEdit.setText("")
			self.updateUI()
		else:
			self.epasswordLabel.setText("Password Mismatch")
			self.ecpasswordLineEdit.setText("")
			self.epasswordLineEdit.setText("")
			
	@pyqtSignature("QString")
	def on_efileLineEdit_textEdited(self,text):
		self.updateUI()
	@pyqtSignature("")
	def on_ebrowsePushButton_clicked(self):
		imagefilename=QFileDialog.getOpenFileName(self,'select file','/home',"Image file (*.jpg *.png *.bmp *.tiff)")
		self.efileLineEdit.setText(imagefilename)
		if len(imagefilename)!=0:
			self.updateUI()
	@pyqtSignature("")
	def on_saveasPushButton_clicked(self):
		saveasfilename=QFileDialog.getSaveFileName(self,'save file ','/home')
		self.saveasLineEdit.setText(saveasfilename)
		if len(saveasfilename)!=0:
			self.updateUI()
	@pyqtSignature("QString")
	def on_saveasLineEdit_textEdited(self,text):
		self.updateUI()
if __name__=="__main__":
	app=QApplication(sys.argv)
	C=Camou()
	C.show()
	app.exec_()
