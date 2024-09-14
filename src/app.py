
from backend.modules.app.app_data import AppData
from backend.modules.audio.audio_extractor_factory import get_audio_extractor
from backend.modules.transcription.transcriber_factory import get_transcriber
from backend.modules.summary.summarizer_factory import get_summarizer
import platform




import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QComboBox, QPushButton, QTextEdit, QLabel, QFileDialog

class SummarizerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle('Video Summarizer')
        self.setGeometry(100, 100, 800, 400)
        self.status = 'Ready'
        self.status_label = QLabel(f'Status: {self.status}')
        
        

        # Main layout
        main_layout = QHBoxLayout()

        # Left side layout
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.status_label)

        # File/URL input
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText('Enter file path or YouTube URL')
        self.browse_button = QPushButton('Browse')
        self.browse_button.clicked.connect(self.browse_file)
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.browse_button)
        left_layout.addWidget(QLabel('Use a file or a YouTube URL:'))
        left_layout.addLayout(input_layout)

        # Transcriber combo box
        self.transcriber_combo = QComboBox()
        self.populate_transcriber_options()
        left_layout.addWidget(QLabel('Transcriber:'))
        left_layout.addWidget(self.transcriber_combo)

        # Summarizer combo box
        self.summarizer_combo = QComboBox()
        self.summarizer_combo.addItems(['llama'])  # Add more options as needed
        left_layout.addWidget(QLabel('Summarizer:'))
        left_layout.addWidget(self.summarizer_combo)

        # Summarize button
        self.summarize_button = QPushButton('Summarize')
        self.summarize_button.clicked.connect(self.summarize)
        left_layout.addWidget(self.summarize_button)

        left_layout.addStretch(1)

        # Right side layout
    
        # Summary field
        right_layout = QVBoxLayout()
        self.summary_field = QTextEdit()
        self.summary_field.setReadOnly(True)
        right_layout.addWidget(QLabel('Summary:'))
        right_layout.addWidget(self.summary_field)

        # Add layouts to main layout
        main_layout.addLayout(left_layout, 1)
        main_layout.addLayout(right_layout, 2)

        self.setLayout(main_layout)
    
    def populate_transcriber_options(self):
        os_name = platform.system().lower()
        if os_name in ['linux', 'windows']:
            self.transcriber_combo.addItem('whisper')
        elif os_name == 'darwin':
            self.transcriber_combo.addItem('mlx')
    
    def browse_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Audio File", "", "Audio Files (*.mp3 *.wav *.ogg *.flac);;All Files (*)")
        if file_name:
            self.input_field.setText(file_name)
    def update_status(self, status):
        self.status = status
        self.status_label.setText(f'Status: {self.status}')
        QApplication.processEvents()  # Force GUI update

    def summarize(self):
        input_text = self.input_field.text()
        transcriber = self.transcriber_combo.currentText()
        summarizer = self.summarizer_combo.currentText()

        app_data = AppData()
        
        self.update_status('Extracting audio...')
        app_data.audio_extractor = get_audio_extractor(input_text)
        app_data.audio = app_data.audio_extractor.extract(audio_source=input_text)
        
        self.update_status('Transcribing...')
        app_data.transcriber = get_transcriber(transcriber_type=transcriber)
        app_data.transcription = app_data.transcriber.transcribe(audio=app_data.audio)
        
        self.update_status('Summarizing...')
        app_data.summarizer = get_summarizer()
        app_data.summary = app_data.summarizer.summarize(app_data.transcription)
        
        self.update_status('Done')

        summary = f"Summarizing {app_data.audio.audio_file}\nUsing transcriber: {transcriber}\nUsing summarizer: {summarizer}\nSummary: {app_data.summary.text}"
        self.summary_field.setText(summary)

def main():
    app = QApplication(sys.argv)
    ex = SummarizerApp()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
