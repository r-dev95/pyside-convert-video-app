
# build qrc
pyside6-rcc.exe .\lib\components\resources.qrc -o .\lib\components\resources_rc.py
# build ui
pyside6-uic.exe .\lib\components\layout.ui -o .\lib\components\layout.py
pyside6-uic.exe .\lib\components\video_layout.ui -o .\lib\components\video_layout.py

# fix import
(Get-Content .\lib\components\layout.py) -replace 'import resources_rc', 'import lib.components.resources_rc' | Set-Content .\lib\components\layout.py
(Get-Content .\lib\components\video_layout.py) -replace 'import resources_rc', 'import lib.components.resources_rc' | Set-Content .\lib\components\video_layout.py
