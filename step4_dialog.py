from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QFormLayout, QLabel, QLineEdit, 
                             QComboBox, QPushButton, QScrollArea, QWidget, QMessageBox, QCheckBox)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont


class Step4Dialog(QDialog):
    """Dialog Wizard Halaman 4 — Konfigurasi API & Database"""
    
    finished_setup = Signal(dict)
    
    def __init__(self, parent=None, project_id=None):
        super().__init__(parent)
        self.project_id = project_id
        self.setWindowTitle("🔧 Wizard — Halaman 4: Konfigurasi API & Database")
        self.setMinimumWidth(750)
        self.setMinimumHeight(700)
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
            QLineEdit {
                background-color: rgba(255, 255, 255, 0.05);
                border: 2px solid #9A83FF;
                border-radius: 8px;
                color: #E0E0E0;
                padding: 8px;
                font-size: 13px;
            }
            QLineEdit:focus {
                border: 2px solid #BB86FC;
                background-color: rgba(154, 131, 255, 0.1);
            }
            QComboBox {
                background-color: rgba(255, 255, 255, 0.05);
                border: 2px solid #9A83FF;
                border-radius: 8px;
                color: #E0E0E0;
                padding: 6px;
                font-size: 13px;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 25px;
                border-left: 1px solid #9A83FF;
            }
            QCheckBox {
                color: #E0E0E0;
                spacing: 8px;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid #9A83FF;
                border-radius: 4px;
                background: transparent;
            }
            QCheckBox::indicator:checked {
                background: #9A83FF;
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
            QPushButton#finishBtn {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #9A83FF,
                    stop:1 #7C63D8
                );
            }
            QPushButton#finishBtn:hover {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #BB86FC,
                    stop:1 #9A83FF
                );
            }
            QPushButton#prevBtn, QPushButton#cancelBtn {
                background: #555555;
            }
            QPushButton#prevBtn:hover, QPushButton#cancelBtn:hover {
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
        title = QLabel("🔧 Konfigurasi API & Database")
        title_font = QFont("Poppins", 18, QFont.Bold)
        title.setFont(title_font)
        title.setStyleSheet("color: #9A83FF;")
        main_layout.addWidget(title)
        
        # Deskripsi
        desc = QLabel("Atur konfigurasi database dan API framework untuk backend project Anda. "
                     "Anda dapat mengubah konfigurasi ini nanti jika diperlukan.")
        desc.setWordWrap(True)
        desc.setStyleSheet("color: #B0BEC5; font-size: 12px; margin-bottom: 10px;")
        main_layout.addWidget(desc)
        
        # Form dengan scroll
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")
        scroll_widget = QWidget()
        scroll_widget.setStyleSheet("background: transparent;")
        form = QFormLayout(scroll_widget)
        form.setSpacing(12)
        
        # Database Section
        form.addRow(QLabel("<b style='color: #9A83FF; font-size: 14px;'>📊 Konfigurasi Database</b>"))
        
        self.db_type = QComboBox()
        self.db_type.addItems(['PostgreSQL', 'MySQL', 'MongoDB', 'Firebase', 'SQLite', 'Redis'])
        form.addRow(QLabel("<b>Tipe Database:</b>"), self.db_type)
        
        self.db_host = QLineEdit()
        self.db_host.setPlaceholderText("localhost atau IP address")
        self.db_host.setText("localhost")
        form.addRow(QLabel("<b>Host:</b>"), self.db_host)
        
        self.db_port = QLineEdit()
        self.db_port.setPlaceholderText("Port database")
        self.db_port.setText("5432")
        form.addRow(QLabel("<b>Port:</b>"), self.db_port)
        
        self.db_name = QLineEdit()
        self.db_name.setPlaceholderText("Nama database")
        form.addRow(QLabel("<b>Database Name:</b>"), self.db_name)
        
        self.db_user = QLineEdit()
        self.db_user.setPlaceholderText("Username")
        form.addRow(QLabel("<b>Username:</b>"), self.db_user)
        
        self.db_pass = QLineEdit()
        self.db_pass.setEchoMode(QLineEdit.Password)
        self.db_pass.setPlaceholderText("Password")
        form.addRow(QLabel("<b>Password:</b>"), self.db_pass)
        
        # API Section
        form.addRow(QLabel(""))
        form.addRow(QLabel("<b style='color: #9A83FF; font-size: 14px;'>🌐 Konfigurasi API</b>"))
        
        self.api_framework = QComboBox()
        self.api_framework.addItems(['FastAPI', 'Flask', 'Django', 'Node.js Express', 'Spring Boot'])
        self.api_framework.setCurrentText('FastAPI')
        form.addRow(QLabel("<b>Framework:</b>"), self.api_framework)
        
        self.auth_type = QComboBox()
        self.auth_type.addItems(['JWT Token', 'OAuth 2.0', 'Session-based', 'Custom'])
        form.addRow(QLabel("<b>Tipe Autentikasi:</b>"), self.auth_type)
        
        # Security Section
        form.addRow(QLabel(""))
        form.addRow(QLabel("<b style='color: #9A83FF; font-size: 14px;'>🔒 Keamanan</b>"))
        
        self.enable_ssl = QCheckBox("Enable SSL/HTTPS")
        self.enable_ssl.setChecked(True)
        form.addRow(self.enable_ssl)
        
        self.api_key = QLineEdit()
        self.api_key.setPlaceholderText("Generate atau masukkan API key (opsional)")
        form.addRow(QLabel("<b>API Key (Opsional):</b>"), self.api_key)
        
        scroll.setWidget(scroll_widget)
        main_layout.addWidget(scroll)
        
        # Info
        info = QLabel("💡 Tip: Simpan API key Anda di tempat yang aman dan jangan bagikan kepada siapa pun.")
        info.setStyleSheet("color: #9A83FF; font-size: 12px; font-style: italic;")
        main_layout.addWidget(info)
        
        # Buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        cancel_btn = QPushButton("Batal")
        cancel_btn.setObjectName("cancelBtn")
        cancel_btn.clicked.connect(self.reject)
        
        prev_btn = QPushButton("← Sebelumnya")
        prev_btn.setObjectName("prevBtn")
        prev_btn.clicked.connect(self.on_previous)
        
        finish_btn = QPushButton("✓ Selesai")
        finish_btn.setObjectName("finishBtn")
        finish_btn.clicked.connect(self.on_finish)
        
        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(prev_btn)
        button_layout.addWidget(finish_btn)
        main_layout.addLayout(button_layout)
    
    def on_previous(self):
        """Close the current step and let the parent handle navigation."""
        self.reject()

    def on_finish(self):
        """Validasi dan selesaikan wizard"""
        if not self.db_name.text().strip():
            QMessageBox.warning(self, "Validasi", "Nama database tidak boleh kosong!")
            return
        if not self.db_user.text().strip():
            QMessageBox.warning(self, "Validasi", "Username database tidak boleh kosong!")
            return

        data = {
            'project_id': self.project_id,
            'database': {
                'type': self.db_type.currentText(),
                'host': self.db_host.text(),
                'port': self.db_port.text(),
                'name': self.db_name.text(),
                'user': self.db_user.text(),
            },
            'api': {
                'framework': self.api_framework.currentText(),
                'auth_type': self.auth_type.currentText(),
                'ssl_enabled': self.enable_ssl.isChecked(),
                'api_key': self.api_key.text() if self.api_key.text() else 'auto'
            }
        }
        self.finished_setup.emit(data)
        self.accept()
