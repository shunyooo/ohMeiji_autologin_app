#!/usr/bin/env python
# coding: utf-8
from selenium import webdriver
import configparser
import selenium_agent

config = configparser.ConfigParser()
config.read('config.ini')

class ohMeijiAgent():
	def __init__(self,user_id,user_pass,browser_name,config_sel):
		self.__browser = self.__getBrowser(browser_name,config_sel)
		self.__id = user_id
		self.__pass = user_pass

	def __getBrowser(self,browser_name,config_sel):
		b = config_sel['driver_dir']
		path = b+config_sel[browser_name]

		if browser_name == "Chrome":
			options = self.__getChromeOptions()
			browser = webdriver.Chrome(executable_path = path, chrome_options = options)
		elif browser_name == "Firefox":
			browser = webdriver.Firefox(executable_path = path)
		elif browser_name == "PhantomJS":
			browser = webdriver.PhantomJS(executable_path = path)

		# 暗黙的な待機
		browser.implicitly_wait(3)
		browser.maximize_window()
		#ms = browser.get_window_size()
		#rate = 0.7
		#browser.set_window_size(ms['width']*rate,ms['height']*rate)

		return browser

	def __getChromeOptions(self):
		# 保存を促すポップが出ないように。
		prefs = {
			 "chrome.switches": "--disable-extensions --disable-extensions-file-access-check --disable-extensions-http-throttling --disable-infobars --enable-automation --start-maximized",
			 "credentials_enable_service":False,
			 "profile.password_manager_enabled": False
			 }
		options = webdriver.ChromeOptions()
		options.add_experimental_option("prefs", prefs)
		return options


	def login(self):
		browser = self.__browser
		ID = self.__id
		PASS = self.__pass

		# トップページにアクセス
		url_top = "https://oh-o2.meiji.ac.jp/portal/index"
		browser.get(url_top)
		print("トップページにアクセスしました")

		# ログインページにアクセス
		e = browser.find_element_by_css_selector(".login a")
		print("ログインページ > ",e.get_attribute('href'))
		e.click()
		print("遷移後ログインページ > ",browser.current_url)

		# id,passの入力
		# テキストボックスに文字を入力
		e = browser.find_element_by_name("ACCOUNTUID")
		e.clear()
		e.send_keys(ID)
		e = browser.find_element_by_name("PASSWORD")
		e.clear()
		e.send_keys(PASS)

		# フォームを送信
		frm = browser.find_element_by_css_selector(".form_container form")
		frm.submit()
		print("情報を入力してログインボタンを押しました")

	def goClassWeb(self):
		classweb_url = "https://oh-o2.meiji.ac.jp/portal/oh-o_meiji/classweb"
		self.__browser.get(classweb_url)
		print("classwebにアクセスしました")


if __name__ == '__main__':
	print(config)
	cm = config['ohMeiji'] # ohMeijiの設定
	cs = config['selenium']  # seleniumのドライバ設定
	agent = ohMeijiAgent(cm['ID'],cm['PASS'],cm['browser'],cs)
	agent.login()


	#agent.goClassWeb()



