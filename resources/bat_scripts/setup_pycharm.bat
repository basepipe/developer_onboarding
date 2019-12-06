if not exist "%HOMEPATH%\PycharmProjects" mkdir "%HOMEPATH%\PycharmProjects"
git clone https://github.com/basepipe/cglumberjack.git %HOMEPATH%\PycharmProjects\cglumberjack
git clone https://github.com/basepipe/developer_onboarding.git %HOMEPATH%\PycharmProjects\developer_onboarding
cd %HOMEPATH%\PycharmProjects\developer_onboarding
pip install -r requirements.txt
python %HOMEPATH%\PycharmProjects\developer_onboarding\src\bin\pycharm_setup.py