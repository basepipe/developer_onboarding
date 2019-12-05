choco install git -y
choco install pycharm -y
choco install python2 -y
choco install ffmpeg -y
choco install slack -y
choco install imagemagick -y
choco install wget -y
if not exist "%HOMEPATH%\PycharmProjects" mkdir "%HOMEPATH%\PycharmProjects"
git clone https://github.com/basepipe/developer_onboarding.git %HOMEPATH%\PycharmProjects\developer_onboarding
cd %HOMEPATH%\PycharmProjects\developer_onboarding
pip install -r requirements.txt
cd %HOMEPATH%\PycharmProjects\developer_onboarding\src\bin
python setup.py