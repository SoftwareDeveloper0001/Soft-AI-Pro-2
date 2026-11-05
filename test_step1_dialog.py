"""
Test Script untuk Step 1 Dialog
Jalankan untuk test apakah fitur berfungsi dengan baik
"""

import sys
from PySide6.QtWidgets import QApplication
from step1_dialog import Step1Dialog

def test_step1_dialog():
    """Test Step 1 Dialog"""
    app = QApplication(sys.argv)
    
    dialog = Step1Dialog()
    
    # Test 1: Add features programmatically
    print("=" * 50)
    print("TEST STEP 1 DIALOG")
    print("=" * 50)
    
    # Simulate adding features
    print("\n✅ TEST 1: Adding features...")
    dialog.feature_name_input.setText("User Authentication")
    dialog.feature_priority.setCurrentIndex(2)  # High
    dialog.add_feature()
    print(f"   Feature added: {dialog.features}")
    
    dialog.feature_name_input.setText("Payment Gateway")
    dialog.feature_priority.setCurrentIndex(1)  # Medium
    dialog.add_feature()
    print(f"   Total features: {len(dialog.features)}")
    
    # Show dialog
    print("\n✅ TEST 2: Showing dialog...")
    print("   >>> Dialog ditampilkan, silakan test secara manual")
    print("   >>> Klik 'Tambah Fitur' untuk menambah fitur")
    print("   >>> Klik 'Lanjut Lihat Fitur' untuk lihat summary")
    print("   >>> Klik tombol di bawah untuk simpan & lanjut")
    
    dialog.exec()
    
    print("\n✅ TEST 3: Dialog closed")
    print(f"   Final features: {dialog.features}")

if __name__ == "__main__":
    test_step1_dialog()
