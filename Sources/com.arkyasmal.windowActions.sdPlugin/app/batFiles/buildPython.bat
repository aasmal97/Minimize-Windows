cd %~dp0
cd ../windowsScripts
pip install -r requirements.txt
pyinstaller determineActiveWindows.py -F -n determineActiveWindows --distpath ../executables --workpath ../executables --specpath ../executables
cd ..
cd ..