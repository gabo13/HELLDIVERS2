# HELLDIVERS2
Virtual Keyboard

## Telepítés:

1. A Microsoft Store-ból töltsd le a python-t
2. Nyisd meg a PowerShell-t
3. Írd be: python -V
Ha normálisan települt akkor kiírja a verzióinformációt
4.Telepítsd a git szoftvert innen:
https://git-scm.com/downloads
5. Navigálj oda ahova le akarod tölteni a githubról a HELLDIVERS2 mappát
6. Írd be: git clone https://github.com/gabo13/HELLDIVERS2.git
7. Hozzál létre egy független virtulális környezetet:
python -m venv venv
8. Aktiváld a virtuális környezetet:
bin\scripts\activate.ps1
Itt lehet egy kis gond hogy nem engedi futtatni a fenti scriptet, ehhez [alt + x] powershell futtatása rendszergazdaként.
Írd be: Set-ExecutionPolicy RemoteSigned
Ezek után visszatérhetsz a másik powershell ablakhoz és újra kiadhatod a parancsot.
Ha minden ok akkor a prompt előtt "(venv)".
9. Egy kömyvtár telepítése a virtuális környezetbe, írd be: pip install pywin32
10. Futtathatod a scriptet:
python helldivers2.py 