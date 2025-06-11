
# build qrc
pyside6-rcc.exe .\lib\ui\resources.qrc -o .\lib\ui\resources_rc.py
# build ui
pyside6-uic.exe .\lib\ui\layout.ui -o .\lib\ui\layout.py
pyside6-uic.exe .\lib\ui\video_layout.ui -o .\lib\ui\video_layout.py

# fix import
(Get-Content .\lib\ui\layout.py) -replace 'import resources_rc', 'import lib.ui.resources_rc' | Set-Content .\lib\ui\layout.py
(Get-Content .\lib\ui\video_layout.py) -replace 'import resources_rc', 'import lib.ui.resources_rc' | Set-Content .\lib\ui\video_layout.py
