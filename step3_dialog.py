from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
                             QListWidget, QListWidgetItem, QMessageBox)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont


class Step3Dialog(QDialog):
    """Dialog Wizard Halaman 3 — Pilih Komponen UI"""
    
    components_completed = Signal(dict)
    
    def __init__(self, parent=None, project_id=None):
        super().__init__(parent)
        self.project_id = project_id
        self.setWindowTitle("⚙️ Wizard — Halaman 3: Pilih Komponen UI")
        self.setMinimumWidth(800)
        self.setMinimumHeight(650)
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
                border: 2px solid #FFB74D;
                border-radius: 8px;
                color: #E0E0E0;
            }
            QListWidget::item {
                padding: 8px;
                border-bottom: 1px solid rgba(255, 183, 77, 0.2);
            }
            QListWidget::item:selected {
                background-color: rgba(255, 183, 77, 0.3);
            }
            QPushButton {
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                font-weight: bold;
                border: none;
                font-size: 13px;
                min-width: 80px;
            }
            QPushButton#addBtn, QPushButton#removeBtn {
                background: #FFB74D;
                max-width: 100px;
            }
            QPushButton#addBtn:hover, QPushButton#removeBtn:hover {
                background: #FFA726;
            }
            QPushButton#nextBtn {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #FFB74D,
                    stop:1 #FFA726
                );
            }
            QPushButton#nextBtn:hover {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #FFD54F,
                    stop:1 #FFB74D
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
        title = QLabel("⚙️ Pilih Komponen UI")
        title_font = QFont("Poppins", 18, QFont.Bold)
        title.setFont(title_font)
        title.setStyleSheet("color: #FFB74D;")
        main_layout.addWidget(title)
        
        # Deskripsi
        desc = QLabel("Pilih komponen UI yang sesuai dengan kebutuhan project Anda. "
                     "Anda dapat menambah atau menghapus komponen sesuai preferensi.")
        desc.setWordWrap(True)
        desc.setStyleSheet("color: #B0BEC5; font-size: 12px; margin-bottom: 10px;")
        main_layout.addWidget(desc)
        
        # Two-column layout
        columns_layout = QHBoxLayout()
        
        # Kolom kiri - Available
        left_layout = QVBoxLayout()
        left_layout.addWidget(QLabel("<b style='color: #FFB74D;'>Komponen Tersedia:</b>"))
        self.available_list = QListWidget()
        components = ['Button', 'Input Field', 'Textarea', 'Dropdown', 'Checkbox', 'Radio Button',
                     'Card', 'Modal', 'Navbar', 'Sidebar', 'Footer', 'Tooltip',
                     'Table', 'Pagination', 'Breadcrumb', 'Badge', 'Progress Bar', 'Slider',
                     'Avatar', 'Tag', 'Alert', 'Toast Notification', 'Tabs', 'Accordion']
        for comp in components:
            item = QListWidgetItem(f"□ {comp}")
            self.available_list.addItem(item)
        left_layout.addWidget(self.available_list)
        columns_layout.addLayout(left_layout)
        
        # Kolom tengah - buttons
        btn_layout = QVBoxLayout()
        btn_layout.addStretch()
        add_btn = QPushButton("➜ Tambah")
        add_btn.setObjectName("addBtn")
        add_btn.clicked.connect(self.add_component)
        remove_btn = QPushButton("⬅ Hapus")
        remove_btn.setObjectName("removeBtn")
        remove_btn.clicked.connect(self.remove_component)
        btn_layout.addWidget(add_btn)
        btn_layout.addWidget(remove_btn)
        btn_layout.addStretch()
        columns_layout.addLayout(btn_layout)
        
        # Kolom kanan - Selected
        right_layout = QVBoxLayout()
        right_layout.addWidget(QLabel("<b style='color: #FFB74D;'>Komponen Dipilih:</b>"))
        self.selected_list = QListWidget()
        right_layout.addWidget(self.selected_list)
        columns_layout.addLayout(right_layout)
        
        main_layout.addLayout(columns_layout)
        
        # Info
        info = QLabel("💡 Tip: Drag & drop dari kiri ke kanan untuk memilih komponen dengan cepat.")
        info.setStyleSheet("color: #FFB74D; font-size: 12px; font-style: italic;")
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
        
        next_btn = QPushButton("Berikutnya →")
        next_btn.setObjectName("nextBtn")
        next_btn.clicked.connect(self.on_next)
        
        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(prev_btn)
        button_layout.addWidget(next_btn)
        main_layout.addLayout(button_layout)
    
    def add_component(self):
        """Tambah komponen dari available ke selected"""
        for item in self.available_list.selectedItems():
            comp_name = item.text().replace("□ ", "").replace("■ ", "")
            if not any(comp_name in sel_item.text() for sel_item in [self.selected_list.item(i) for i in range(self.selected_list.count())]):
                new_item = QListWidgetItem(f"✓ {comp_name}")
                self.selected_list.addItem(new_item)
    
    def remove_component(self):
        """Hapus komponen dari selected"""
        for item in self.selected_list.selectedItems():
            self.selected_list.takeItem(self.selected_list.row(item))
    
    def on_previous(self):
        """Close the current step and let the parent handle navigation."""
        self.reject()

    def on_next(self):
        """Validasi dan lanjut ke halaman berikutnya"""
        if self.selected_list.count() == 0:
            QMessageBox.warning(self, "Validasi", "Pilih minimal 1 komponen!")
            return

        components = []
        for i in range(self.selected_list.count()):
            item = self.selected_list.item(i)
            components.append(item.text().replace("✓ ", ""))

        data = {
            'project_id': self.project_id,
            'components': components
        }
        self.components_completed.emit(data)
        self.accept()
