import configparser
# import os

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")
# config.read(os.path.abspath(os.curdir)+'//configurations/config.ini')  # reads file in config.ini file


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('commonInfo', 'baseURL')
        # 'commonInfo' is the name given on the config.ini file and the value we want to return is 'baseURL'
        return url

    @staticmethod
    def get_user_email():
        email = config.get('commonInfo', 'email')
        return email

    @staticmethod
    def get_user_password():
        password = config.get('commonInfo', 'password')
        return password
