# /usr/bin/bash
python3 -m venv osrs_player
cd osrs_player
git clone https://github.com/killuhwhale/osrs_color.git
source bin/activate
cd osrs_color
pip3 install -r requirements.txt

