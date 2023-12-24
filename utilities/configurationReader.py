from configparser import ConfigParser


def read_configuration(category, key):
    config = ConfigParser()
    config.read("C:/Users/Benjamin Saint Elien/Documents/FrameworkAnalysis/virtual_env/configurations/config.ini")
    return config.get(category, key)