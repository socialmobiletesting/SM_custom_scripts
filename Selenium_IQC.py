import datetime
import threading

import select
import json
import logging
import subprocess
import platform
import sys

from appium.webdriver.common.appiumby import AppiumBy
from framework_constants.framework_constants import *
#import pandas as pd
import os
import zipfile
from zipfile import ZipFile
import shutil
from shutil import make_archive

from selenium.webdriver.support.wait import WebDriverWait
from utilities.libraries.timelib import get_current_time
import unicodedata
#import PIL
#from PIL import Image
#from PIL.ExifTags import TAGS
#import paramiko
import re
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.ie.service import Service as IeService
from selenium.webdriver.ie.options import Options as IeOptions
# from msedge.selenium_tools import EdgeOptions
# from msedge.selenium_tools import EdgeService
from selenium.webdriver.common.by import By
import time
from utilities.libraries.config import root_path
from db_conn import MYSQLDBConn
import glob
import openpyxl
from db_conn import update_device_status
import socket
from client_variables import *
import pyautogui

#import pandas as pd
from openpyxl.styles import Side, Alignment
from openpyxl.styles import PatternFill, Font, Border
from openpyxl.styles.differential import DifferentialStyle
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def webdriver_start(serial=""):
    """
    This function is used to start the chrome webdriver
    :return:
    """
    import configparser
    config = configparser.ConfigParser()
    print("loading config proos")
    path = get_root_directory_path()
    directory_path = os.path.join(path, 'config.properties')
    config.read(directory_path)
    print("Sections:", config.sections())
    chrome_path = config.get('lib_config', 'web_driver_start')

    if "Chrome" in serial:
        print("Chrome")
        # driver = webdriver.Chrome(executable_path='start chrome')
        # driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe")
        s = Service(f'{chrome_path}')
        opt = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=s, options=opt)
        driver.maximize_window()
    elif "FireFox" in serial:
        print("FireFox")
        driver = webdriver.Firefox(executable_path='start firefox')
    elif "Edge" in serial:
        print("Edge")
        driver = webdriver.Edge(executable_path='start microsoft-edge:')
    print(driver)
    return driver