from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout,
    QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Qt


class WelcomePage(QWidget):
    """Halaman selamat datang sederhana dengan tombol navigasi pojok kanan."""

    def __init__(self, navigate_callback=None):
        super().__init__()
        self._navigate_callback = navigate_callback
        self.init_ui()

    def init_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(28, 28, 28, 28)
        layout.setSpacing(12)

        # Top bar with spacer and navigation button (right corner)
        top_bar = QHBoxLayout()
        top_bar.setContentsMargins(0, 0, 0, 0)
        top_bar.setSpacing(6)

        top_bar.addItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.nav_button = QPushButton("Menu")
        self.nav_button.setFixedHeight(36)
        self.nav_button.setStyleSheet("""
            QPushButton { background: qlineargradient(x1:0,y1:0,x2:1,y2:0, stop:0 #7C3AED, stop:1 #5B21B6); color: white; border-radius: 8px; padding: 6px 12px; font-weight: bold; }
            QPushButton:hover { background: qlineargradient(x1:0,y1:0,x2:1,y2:0, stop:0 #A78BFA, stop:1 #7C3AED); }
        """)
        self.nav_button.clicked.connect(self._on_navigate_clicked)

        top_bar.addWidget(self.nav_button)
        layout.addLayout(top_bar)

        # Centered welcome text
        welcome = QLabel("Selamat Datang")
        welcome.setAlignment(Qt.AlignCenter)
        welcome.setStyleSheet("color: white; font-size: 36px; font-weight: 800;")
        layout.addStretch()
        layout.addWidget(welcome)

        subtitle = QLabel("Selamat datang di Soft AI Pro — mulai dari sini untuk membuat proyek baru atau mengelola yang sudah ada.")
        subtitle.setWordWrap(True)
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color: #D1D5DB; font-size: 12pt;")
        layout.addWidget(subtitle)
        layout.addStretch()

    def _on_navigate_clicked(self) -> None:
        if callable(self._navigate_callback):
            try:
                self._navigate_callback()
            except Exception:
                # avoid bubbling errors; caller should handle exceptions
                pass

    def set_navigation_callback(self, callback) -> None:
        """Set callback yang dipanggil ketika tombol navigasi diklik."""
        self._navigate_callback = callback
