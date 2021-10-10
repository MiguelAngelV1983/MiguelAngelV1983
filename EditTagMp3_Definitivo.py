#RECUPERACION ACTIVIDAD 2 PROGRAMACION AVANZADA
#EDITOR DE TAGS MP3
#ALUMNO: MIGUEL A. VALVERDE GONZALEZ


#Importamos las librerias necesarias

import sys
import os

from PyQt6.QtCore import QDir, Qt
from PyQt6.QtWidgets import QFileDialog, QLabel
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QFormLayout
from PyQt6.QtWidgets import QStatusBar
from PyQt6.QtWidgets import QToolBar
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QHBoxLayout
from PyQt6.QtWidgets import QDialog

import eyed3

class View(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Editor de Tags')
        self.setFixedSize(700, 480)

        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)

        self.left_widget = QWidget(self._central_widget)
        self.left_widget.setGeometry(0,80,300,380)
        self.right_widget = QWidget(self._central_widget)
        self.right_widget.setGeometry(305,50,400,480)

        self.left_widget_top = QWidget(self.left_widget)
        self.left_widget_top.setGeometry(21,10,300,50)
        self.left_widget_bot = QWidget(self.left_widget)
        self.left_widget_bot.setGeometry(0,40,300,300)

        self._create_file_path_display()
        self._create_metadata_display()
        self._create_buttons()
        self._create_tool_bar()
        self._create_status_bar()
    

    #crear el visor de archivos y los metadatos
    def _create_file_path_display(self):
        self.file_path_display = QLineEdit(parent=self._central_widget)
        self.file_path_display.setGeometry(0,0,700,60)
        self.file_path_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.file_path_display.setReadOnly(True)

    def _create_metadata_display(self):
        self.hlayout_track_bpm = QHBoxLayout()
        self.form_layout_track = QFormLayout()
        self.form_layout_bpm = QFormLayout()

        self.display_title = QLineEdit()
        self.display_title.setFixedSize(200, 20)
        self.display_artist = QLineEdit()
        self.display_artist.setFixedSize(200, 20)
        self.display_album = QLineEdit()
        self.display_album.setFixedSize(200, 20)
        self.display_album_artist = QLineEdit()
        self.display_album_artist.setFixedSize(200, 20)
        self.display_genre = QLineEdit()
        self.display_genre.setFixedSize(200, 20)
        self.display_track = QLineEdit()
        self.display_track.setFixedSize(60, 20)
        self.display_release_date = QLineEdit()
        self.display_release_date.setFixedSize(200, 20)
        self.display_bpm = QLineEdit()
        self.display_bpm.setFixedSize(60, 20)
        self.display_publisher = QLineEdit()
        self.display_publisher.setFixedSize(200,20)
        
        self.hlayout_track_bpm.addLayout(self.form_layout_track)
        self.form_layout_track.addRow('Pista:', self.display_track)
        self.hlayout_track_bpm.addLayout(self.form_layout_bpm)
        self.form_layout_bpm.addRow('BPM:', self.display_bpm)
        self.left_widget_top.setLayout(self.hlayout_track_bpm)

        self.form_layout = QFormLayout()
        self.form_layout.addRow('Titulo:', self.display_title)
        self.form_layout.addRow('Artista:', self.display_artist)
        self.form_layout.addRow('Album:',  self.display_album)
        self.form_layout.addRow('Album artist:', self.display_album_artist)
        self.form_layout.addRow('Genero:', self.display_genre)
        self.form_layout.addRow('Fecha:', self.display_release_date)
        self.form_layout.addRow('Publicacion:', self.display_publisher)
        self.left_widget_bot.setLayout(self.form_layout)

    #crear barra de tareas y botones

    def _create_buttons(self):
        self.close_button = QPushButton('Cerrar',parent=self.right_widget)
        self.close_button.setGeometry(220,350,70,30)
        self.save_button = QPushButton('Guardar',parent=self.right_widget)
        self.save_button.setGeometry(300,350,70,30)
    
    def _create_tool_bar(self):
        self.tools = QToolBar()
        self.addToolBar(self.tools)
        
    def _create_status_bar(self):
        status = QStatusBar()
        status.showMessage("Activo")
        self.setStatusBar(status)
    
    #crear el texto del display  
    
    def set_display_text(self,file_path, title,artist,album,album_artist,genre,track,release_date,bpm,publisher):
        self.file_path_display.setText(file_path)
        self.display_title.setText(title)
        self.display_artist.setText(artist)
        self.display_album.setText(album)
        self.display_album_artist.setText(album_artist)
        self.display_genre.setText(str(genre))
        self.display_track.setText(str(track))
        self.display_release_date.setText(str(release_date))
        self.display_bpm.setText(str(bpm))
        self.display_publisher.setText(publisher)

    def display_text(self):
        return self.display_title.text(),self.display_artist.text(),self.display_album.text(),self.display_album_artist.text(),self.display_genre.text(),self.display_track.text(),self.display_release_date.text(),self.display_bpm.text(),self.display_publisher.text()
    
#Creamos una clase modelo para cargar y guardar los archivos

class Model:       
    
    def __init__(self):
        pass

    def load_file(self,file_path):
        self.file_path=file_path
        self.audiofile = eyed3.load(self.file_path)
        self.release_date = self.audiofile.tag.release_date
        self.album_artist = self.audiofile.tag.album_artist
        self.track = self.audiofile.tag.track_num[0]
        self.artist = self.audiofile.tag.artist
        self.album = self.audiofile.tag.album
        self.title = self.audiofile.tag.title
        self.genre = self.audiofile.tag.genre
        self.bpm = self.audiofile.tag.bpm
        self.publisher = self.audiofile.tag.publisher
        return self.title,self.artist,self.album,self.album_artist,self.genre,self.track,self.release_date,self.bpm,self.publisher

    def save_file(self,title,artist,album,album_artist,genre,track,release_date,bpm,publisher):
        self.audiofile.tag.title = title
        self.audiofile.tag.artist = artist
        self.audiofile.tag.album = album
        self.audiofile.tag.album_artist = album_artist
        self.audiofile.tag.genre = genre
        self.audiofile.tag.release_date = release_date
        self.audiofile.tag.publisher = publisher
        try:
           int(bpm)
        except ValueError:
           self.audiofile.tag.bpm = 00
        else:
            self.audiofile.tag.bpm = int(bpm)
        
        try:
           int(track)
        except ValueError:
           self.audiofile.tag.track_num = 00
        else:
            self.audiofile.tag.track_num = int(track)
        
        self.audiofile.tag.save()

#clase controlador para crear el contenedor con las funciones de conectar, cargar y guardar archivos
class Controller:  

    def __init__(self,view,Model):
        self._view = view
        self._Model = Model
        self._connect_signals()
    
    def _connect_signals(self):
        self._view.save_button.clicked.connect(self._save)
        self._view.close_button.clicked.connect(self._view.close)
        self._view.tools.addAction('Salir', self._view.close)
        self._view.tools.addAction('Cargar', self._load)

    def _load(self):
        '''A la hora de realizar la carga del fichero controlo si se produce un mensaje de error y lo muestro'''
        try:
            file = QFileDialog.getOpenFileName(self, 'Buscar Archivo', QDir.homePath(), "All Files (*);;Music Mp3 Files (*.mp3)")
            if file:
                print("Archivo seleccionado: ", file)
        except:
            print("Error en la carga de datos.")

    
    def _save(self):
        '''Repito el control de errores de la funcion anterior'''
        try:
            self.text_save_file = self._view.display_text()
            for i in range(0,8):
                self._Model.save_file(self.text_save_file[i])
        except:
            print("Error al guardar los datos, por favor, revise todos los parametros.")


        #self._model.save_file(self.text_save_file[0],self.text_save_file[1],self.text_save_file[2],self.text_save_file[3],self.text_save_file[4],self.text_save_file[5],self.text_save_file[6],self.text_save_file[7],self.text_save_file[8])

#clase para cargar los textos

class Load_Dialog(QDialog):

    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle('Cargar Fichero')
        self.dlg_v_layout = QVBoxLayout()
        form_layout = QFormLayout()
        self.load_file = QLineEdit()
        self.error_label = QLabel()
        form_layout.addRow('Ruta del archivo:', self.load_file)
        self.dlg_v_layout.addLayout(form_layout)
        self.dlg_v_layout.addWidget(self.error_label)
        buttons_h_layout = QHBoxLayout()
        button_cancel = QPushButton('Cancelar')
        self.button_ok = QPushButton('Aceptar')
        buttons_h_layout.addWidget(button_cancel)
        buttons_h_layout.addWidget(self.button_ok)
        self.dlg_v_layout.addLayout(buttons_h_layout)
        self.setLayout(self.dlg_v_layout)
        button_cancel.clicked.connect(self._clear)
        button_cancel.clicked.connect(self.close)
        self.button_ok.clicked.connect(self._load)
    
    def _load_file_dialog(self):
        dlg= Load_Dialog(self._view) 
        dlg.exec()
        self.file = dlg.file_path_dialog
        try:
            if len(self.file)>0:
                self.text_load_file = self._Model.load_file(self.file) 
                self._view.set_display_text(self.file,self.text_load_file[0],self.text_load_file[1],self.text_load_file[2],self.text_load_file[3],self.text_load_file[4],self.text_load_file[5],self.text_load_file[6],self.text_load_file[7],self.text_load_file[8]) 
            pass
        except:
            print("Error de carga de ficheros.")

    def _clear(self):
        self.load_file.clear()
        self.file_path_dialog = self.load_file.text()        

#funcion principal
def main():
    Tag_editor = QApplication(sys.argv)

    view = View()  
    model = Model()
    controller = Controller(view,model)

    view.show()

    sys.exit(Tag_editor.exec())

if __name__ == '__main__':
    main()