cd ..
rm -rf build
rm -rf dist
rm -rf release
rm -rf venv

python3 -m venv venv
./venv/bin/python3 -m pip install --upgrade pip
./venv/bin/python3 -m pip install -r requirements.txt
./venv/bin/python3 -m pip install pyinstaller
./venv/bin/pyinstaller main.py --clean --onefile --noconsole \
--add-data "./media/*:media" \
--icon media/icon.ico \
--splash media/icon.png \
--name pong

mv dist release
rm -rf build
rm -rf dist
rm -rf venv
rm -rf pong.spec