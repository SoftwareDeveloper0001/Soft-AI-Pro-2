from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
                             QListWidget, QListWidgetItem, QMessageBox, QFileDialog)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont, QIcon
import os


class Step2Dialog(QDialog):
    """Dialog Wizard Halaman 2 — Upload Figma Design"""
    
    design_completed = Signal(dict)
    
    def __init__(self, parent=None, project_id=None):
        super().__init__(parent)
        self.project_id = project_id
        self.setWindowTitle("🎨 Wizard — Halaman 2: Upload Figma Design")
        self.setMinimumWidth(700)
        self.setMinimumHeight(600)
        self.setStyleSheet(self.get_stylesheet())
        self.setup_ui()
        
    def get_stylesheet(self):
        return """
            QDialog {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #0a0e27,
                    stop:1 #1a1f3a
                );
            }
            QListWidget {
                background-color: rgba(255, 255, 255, 0.03);
                border: 2px solid #81C784;
                border-radius: 8px;
                color: #E0E0E0;
            }
            QListWidget::item {
                padding: 8px;
                border-bottom: 1px solid rgba(129, 199, 132, 0.2);
            }
            QListWidget::item:selected {
                background-color: rgba(129, 199, 132, 0.3);
            }
            QPushButton {
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                font-weight: bold;
                border: none;
                font-size: 13px;
                min-width: 100px;
            }
            QPushButton#uploadBtn {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #81C784,
                    stop:1 #66BB6A
                );
            }
            QPushButton#uploadBtn:hover {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #A5D6A7,
                    stop:1 #81C784
                );
            }
            QPushButton#nextBtn {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #81C784,
                    stop:1 #66BB6A
                );
            }
            QPushButton#nextBtn:hover {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #A5D6A7,
                    stop:1 #81C784
                );
            }
            QPushButton#prevBtn {
                background: #555555;
            }
            QPushButton#prevBtn:hover {
                background: #666666;
            }
            QPushButton#cancelBtn {
                background: #555555;
            }
            QPushButton#cancelBtn:hover {
                background: #666666;
            }
            QLabel {
                color: #E0E0E0;
            }
        """
    
    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(30, 30, 30, 30)
        
        # Header
        title = QLabel("🎨 Upload Desain Figma")
        title_font = QFont("Poppins", 18, QFont.Bold)
        title.setFont(title_font)
        title.setStyleSheet("color: #81C784;")
        main_layout.addWidget(title)
        
        # Deskripsi
        desc = QLabel("Upload minimal 10 halaman design Figma untuk analisis lebih lanjut. "
                     "Anda dapat mengupload file .fig atau screenshot PNG/JPG.")
        desc.setWordWrap(True)
        desc.setStyleSheet("color: #B0BEC5; font-size: 12px; margin-bottom: 10px;")
        main_layout.addWidget(desc)
        
        # File list
        self.file_list = QListWidget()
        main_layout.addWidget(QLabel("<b>File yang Diupload:</b>"))
        main_layout.addWidget(self.file_list)
        
        # Info
        info = QLabel("💡 Tip: Gunakan file dengan resolusi tinggi untuk hasil analisis yang lebih akurat.")
        info.setStyleSheet("color: #FFB74D; font-size: 12px; font-style: italic;")
        main_layout.addWidget(info)
        
        # Upload button
        upload_btn = QPushButton("📁 Pilih & Upload File")
        upload_btn.setObjectName("uploadBtn")
        upload_btn.clicked.connect(self.handle_upload)
        main_layout.addWidget(upload_btn)
        
        # Buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        cancel_btn = QPushButton("Batal")
        cancel_btn.setObjectName("cancelBtn")
        cancel_btn.clicked.connect(self.reject)
        
        prev_btn = QPushButton("← Sebelumnya")
        prev_btn.setObjectName("prevBtn")
        prev_btn.clicked.connect(self.on_previous)
        
        next_btn = QPushButton("Berikutnya →")
        next_btn.setObjectName("nextBtn")
        next_btn.clicked.connect(self.on_next)
        
        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(prev_btn)
        button_layout.addWidget(next_btn)
        main_layout.addLayout(button_layout)
    
    def handle_upload(self):
        """Handle file upload"""
        files, _ = QFileDialog.getOpenFileNames(
            self,
            'Pilih File Figma',
            os.path.expanduser('~'),
            'Figma Files (*.fig);;Images (*.png *.jpg *.jpeg);;All Files (*)'
        )
        
        for file in files:
            file_name = os.path.basename(file)
            if not any(file_name in self.file_list.item(i).text() for i in range(self.file_list.count())):
                item = QListWidgetItem(f"✓ {file_name}")
                item.setData(Qt.UserRole, file)
                self.file_list.addItem(item)
    
    def on_previous(self):
        """Close the current step and let the parent handle navigation."""
        self.reject()

    def on_next(self):
        """Validasi dan lanjut ke halaman berikutnya"""
        if self.file_list.count() < 10:
            QMessageBox.warning(self, "Validasi", "Minimum 10 file design harus diupload!")
            return

        files = []
        for i in range(self.file_list.count()):
            item = self.file_list.item(i)
            files.append(item.data(Qt.UserRole))

        data = {
            'project_id': self.project_id,
            'pages': files,
            'pages_count': self.file_list.count()
        }
        self.design_completed.emit(data)
        self.accept()
