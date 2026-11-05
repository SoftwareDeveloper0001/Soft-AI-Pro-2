from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QFormLayout, QLabel, QLineEdit,
                             QTextEdit, QCheckBox, QPushButton, QScrollArea, QWidget, QMessageBox,
                             QComboBox, QListWidget, QListWidgetItem)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont


class Step1Dialog(QDialog):
    """Dialog Wizard Halaman 1 — Informasi Project."""

    project_created = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("🚀 Wizard — Halaman 1: Informasi Project")
        self.setMinimumWidth(700)
        self.setMinimumHeight(650)
        self.setStyleSheet(self.get_stylesheet())
        self.features = []
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
            QLineEdit, QTextEdit, QComboBox, QListWidget {
                background-color: rgba(255, 255, 255, 0.05);
                border: 2px solid #4FC3F7;
                border-radius: 8px;
                color: #E0E0E0;
                padding: 8px;
                font-size: 13px;
            }
            QLineEdit:focus, QTextEdit:focus, QComboBox:focus, QListWidget:focus {
                border: 2px solid #00D4FF;
                background-color: rgba(79, 195, 247, 0.1);
            }
            QCheckBox {
                color: #E0E0E0;
                spacing: 8px;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid #4FC3F7;
                border-radius: 4px;
                background: transparent;
            }
            QCheckBox::indicator:checked {
                background: #4FC3F7;
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
            QPushButton#nextBtn {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #4FC3F7,
                    stop:1 #00B8D4
                );
            }
            QPushButton#nextBtn:hover {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #00D4FF,
                    stop:1 #00E5FF
                );
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

        title = QLabel("📋 Informasi Project")
        title_font = QFont("Poppins", 18, QFont.Bold)
        title.setFont(title_font)
        title.setStyleSheet("color: #4FC3F7;")
        main_layout.addWidget(title)

        desc = QLabel("Isi informasi dasar project Anda. Data ini akan digunakan untuk analisis design selanjutnya.")
        desc.setWordWrap(True)
        desc.setStyleSheet("color: #B0BEC5; font-size: 12px; margin-bottom: 10px;")
        main_layout.addWidget(desc)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")
        scroll_widget = QWidget()
        scroll_widget.setStyleSheet("background: transparent;")
        form = QFormLayout(scroll_widget)
        form.setSpacing(12)

        self.project_name = QLineEdit()
        self.project_name.setPlaceholderText("Contoh: E-Commerce Platform")
        form.addRow(QLabel("<b>Nama Project:</b>"), self.project_name)

        self.project_desc = QTextEdit()
        self.project_desc.setPlaceholderText("Jelaskan tujuan dan fitur utama...")
        self.project_desc.setMaximumHeight(100)
        form.addRow(QLabel("<b>Deskripsi:</b>"), self.project_desc)

        form.addRow(QLabel("<b style='color: #4FC3F7; font-size: 13px;'>Fitur yang Diinginkan:</b>"))

        self.feature_name_input = QLineEdit()
        self.feature_name_input.setPlaceholderText("Contoh: User Authentication")
        self.feature_priority = QComboBox()
        self.feature_priority.addItems(["Low", "Medium", "High"])

        feature_form = QHBoxLayout()
        feature_form.addWidget(self.feature_name_input)
        feature_form.addWidget(self.feature_priority)
        form.addRow("Fitur baru:", feature_form)

        add_feature_btn = QPushButton("Tambah Fitur")
        add_feature_btn.clicked.connect(self.add_feature)
        form.addRow(add_feature_btn)

        self.feature_list = QListWidget()
        self.feature_list.setMaximumHeight(130)
        form.addRow(QLabel("<b>Daftar Fitur:</b>"), self.feature_list)

        self.platform = QLineEdit()
        self.platform.setPlaceholderText("Web, Mobile, Desktop")
        form.addRow(QLabel("<b>Target Platform:</b>"), self.platform)

        self.budget = QLineEdit()
        self.budget.setPlaceholderText(r"$5000-$10000")
        form.addRow(QLabel("<b>Budget (Opsional):</b>"), self.budget)

        scroll.setWidget(scroll_widget)
        main_layout.addWidget(scroll)

        button_layout = QHBoxLayout()
        button_layout.addStretch()

        cancel_btn = QPushButton("Batal")
        cancel_btn.setObjectName("cancelBtn")
        cancel_btn.clicked.connect(self.reject)

        next_btn = QPushButton("Simpan & Lanjut →")
        next_btn.setObjectName("nextBtn")
        next_btn.clicked.connect(self.on_next)

        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(next_btn)
        main_layout.addLayout(button_layout)

    def add_feature(self):
        """Add a feature to the list and keep compatibility with older tests."""
        feature_name = self.feature_name_input.text().strip()
        if not feature_name:
            QMessageBox.warning(self, "Validasi", "Nama fitur tidak boleh kosong!")
            return

        if any(existing["name"].lower() == feature_name.lower() for existing in self.features):
            QMessageBox.warning(self, "Validasi", "Fitur sudah ada dalam daftar.")
            return

        priority = self.feature_priority.currentText()
        self.features.append({"name": feature_name, "priority": priority})

        item = QListWidgetItem(f"{feature_name} ({priority})")
        self.feature_list.addItem(item)
        self.feature_name_input.clear()
        self.feature_priority.setCurrentIndex(0)

    def remove_feature(self):
        row = self.feature_list.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Validasi", "Pilih fitur yang ingin dihapus terlebih dahulu.")
            return
        self.feature_list.takeItem(row)
        if row < len(self.features):
            del self.features[row]

    def save_project(self):
        """Validate and emit the created project payload."""
        if not self.project_name.text().strip():
            QMessageBox.warning(self, "Validasi", "Nama project tidak boleh kosong!")
            return None
        if not self.project_desc.toPlainText().strip():
            QMessageBox.warning(self, "Validasi", "Deskripsi project tidak boleh kosong!")
            return None

        data = {
            'project_name': self.project_name.text().strip(),
            'project_desc': self.project_desc.toPlainText().strip(),
            'features': [item['name'] for item in self.features],
            'platform': self.platform.text().strip(),
            'budget': self.budget.text().strip(),
            'project_id': 'proj_' + self.project_name.text().strip().replace(' ', '_').lower()
        }
        self.project_created.emit(data)
        self.accept()
        return data

    def on_next(self):
        """Validasi dan lanjut ke halaman berikutnya."""
        self.save_project()

    def open_step2(self):
        """Backward-compatible alias for older flow references."""
        self.on_next()

