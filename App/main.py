#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------
# Telegram : @DIBIBl , @TDTDI ,@ruks3
# Coded by ruks
# YouTube : https://youtube.com/channel/UCUNbzQRjfAXGCKI1LY72DTA
# Instagram : https://instagram.com/_v_go?utm_medium=copy_link
# github : https://github.com/muntazir-halim
# ---------------------
from kivy.lang import Builder
from kivymd.app import MDApp
import kivymd_extensions.akivymd
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.screen import Screen
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.core.window import Window
from kivymd.uix.label import MDLabel, MDIcon
import py_compile,webbrowser,json
import base64, marshal, zlib
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.properties import BooleanProperty
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox

class MenuScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass  
class ItemConfirm(OneLineAvatarIconListItem):
    pass
class ConfirmDialog(MDDialog):
    pass
       
sm = ScreenManager()   
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
# - code by ruks -
class App(MDApp):
    active = BooleanProperty(False)
    def __init__(self, **kwargs):
         super().__init__(**kwargs)
         Window.bind(on_keyboard=self.events)
         self.manager_open = False
         self.screen = Builder.load_file('frontend/main.kv')
    def build(self):
        self.title = "Encrypt python by ruks"
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.theme_style = "Light"
        return self.screen        
    def on_pyc(self):
         self.file_manager = MDFileManager(
         exit_manager=self.exit_manager,
         select_path=self.pyc_path,)
         self.file_manager.ext = [".py"]
         self.file_manager.show('/sdcard')       
         self.manager_open = True         
    def pyc_path(self, path):
         self.exit_manager()
         try:
         	py_compile.compile(path)
         	toast('تم تشفير الملف')
         except:
         	toast('Erorr')
        # - code by ruks -   
    def on_base32(self):
    	self.file_manager = MDFileManager(
	            exit_manager=self.exit_manager,
	            select_path=self.base32_path,)  	
    	self.file_manager.ext = [".py"]
    	self.file_manager.show('/sdcard')       
    	self.manager_open = True    	   	
    def base32_path(self, path):       
        self.exit_manager()
        toast(path)
        try:
	        file = open(path, "r").read()        
	        Enc=base64.b32encode(file.encode("ascii"))
	        da = str(json.loads(open("data/da.json", "r").read())["base32"])
	        path_y=str(path.split(".")[0])
	        with open(path_y+"-ruks.py", 'w') as x:
	        	x.write(f"{da}{Enc}))")
	        toast('تم تشفير الملف')	        	
        except:
        	toast('Erorr')       	
    def on_base16(self):
    	self.file_manager = MDFileManager(
	            exit_manager=self.exit_manager,
	            select_path=self.base16_path,)  	
    	self.file_manager.ext = [".py"]
    	self.file_manager.show('/sdcard')       
    	self.manager_open = True    	   	
    def base16_path(self, path):       
        self.exit_manager()
        toast(path)
        try:
	        file = open(path, "r").read()        
	        Enc=base64.b16encode(file.encode("ascii"))
	        da = str(json.loads(open("data/da.json", "r").read())["base16"])
	        path_y=str(path.split(".")[0])
	        with open(path_y+"-ruks.py", 'w') as x:
	        	x.write(f"{da}{Enc}))")
	        toast('تم تشفير الملف')	        	
        except:
        	# - code by ruks -
        	toast('Erorr')         	
    def on_base64(self):
    	self.file_manager = MDFileManager(
	            exit_manager=self.exit_manager,
	            select_path=self.base64_path,)  	
    	self.file_manager.ext = [".py"]
    	self.file_manager.show('/sdcard')       
    	self.manager_open = True    	   	
    def base64_path(self, path):       
        self.exit_manager()
        toast(path)
        try:
	        file = open(path, "r").read()        
	        Enc=base64.b64encode(file.encode("ascii"))
	        da = str(json.loads(open("data/da.json", "r").read())["base64"])
	        path_y=str(path.split(".")[0])
	        with open(path_y+"-ruks.py", 'w') as x:
	        	x.write(f"{da}{Enc}))")
	        toast('تم تشفير الملف')	        	
        except:
        	toast('Erorr')        
    def on_marshal(self):
         self.file_manager = MDFileManager(
         exit_manager=self.exit_manager,
         select_path=self.marshal_path,)
         self.file_manager.ext = [".py"]
         self.file_manager.show('/sdcard')       
         self.manager_open = True 
    def marshal_path(self, path):
    	self.exit_manager()  
    	try:
    		file = open(path, "r").read()
    		en = compile(file, '<ruks>', 'exec')
    		enc = marshal.dumps(en)
    		da = str(json.loads(open("data/da.json", "r").read())["marshal"])
    		path_y=str(path.split(".")[0])
    		with open(path_y+"-ruks.py", 'w') as x:
    			x.write(f"{da}{enc}))")
    		toast('تم تشفير الملف')
    	except:
    		# - code by ruks -
    		toast('Erorr')    		
    def on_zlib(self):
         self.file_manager = MDFileManager(
         exit_manager=self.exit_manager,
         select_path=self.zlib_path,)
         self.file_manager.ext = [".py"]
         self.file_manager.show('/sdcard')       
         self.manager_open = True 
    def zlib_path(self, path):
    	self.exit_manager()
    	try:
    		file = open(path, "r").read()
    		co=compile(file,"ru",'exec')
    		mr=marshal.dumps(co)
    		zl = zlib.compress(mr)
    		enc = str(base64.b64encode(zl))
    		da = str(json.loads(open("data/da.json", "r").read())["zlib"])
    		path_y=str(path.split(".")[0])
    		with open(path_y+"-ruks.py", 'w') as x:
    			x.write(f"{da}{enc}))))")
    		toast('تم تشفير الملف')
    		# - code by ruks -
    	except:
    		toast('Erorr') 
    def on_lambda(self):
         self.file_manager = MDFileManager(
         exit_manager=self.exit_manager,
         select_path=self.lambda_path,)
         self.file_manager.ext = [".py"]
         self.file_manager.show('/sdcard')       
         self.manager_open = True 	
    def lambda_path(self, path):
    	self.exit_manager()
    	try:
    		file = open(path, "r").read()
    		en=repr(zlib.compress(file.encode('utf-8')))	    			  		  	
    		da = str(json.loads(open("data/da.json", "r").read())["lambda"])
    		cmb=(f"{da}{en},compile))")
    		path_y=str(path.split(".")[0])      
    		with open(path_y+"-ruks.py", 'w') as x:
    			x.write(cmb)    		 		
    		toast('تم تشفير الملف')
    	except:
    		toast('Erorr')    		
		# - code by ruks -
    def confirmation_lambda(self, *args):
        self.dialog = ConfirmDialog()
        self.dialog.open()
    def score_limit(self, *args, **kwargs):
        self.ruks_layers =self.check_active('check')
        toast(self.ruks_layers)
        self.file_manager = MDFileManager(
         exit_manager=self.exit_manager,
         select_path=self.lambda_path_layers,)
        self.file_manager.ext = [".py"]
        self.file_manager.show('/sdcard') 
        self.manager_open = True 
        self.dialog.dismiss()
        self.dialog = None  
        self.active = False
    def check_active(self, group):  
        for cb in MDCheckbox.get_widgets(group):
            if cb.active:
                self.active = True
                return cb.score
        self.active = False
        return None 		 	 			
    def lambda_path_layers(self, path):
    	self.exit_manager()
    	for i in range(int(self.ruks_layers)):     	
	    	try:
	    		file = open(path, "r").read()
	    		en=repr(zlib.compress(file.encode('utf-8')))	    			  		  	
	    		da = str(json.loads(open("data/da.json", "r").read())["lambda"])
	    		cmb=(f"{da}{en},compile))")	    		
	    		with open(path, 'w') as x:
	    			x.write(cmb)    		 			    		
	    	except:
	    		toast('Erorr')
    	toast('تم تشفير الملف')    
    	# - code by ruks -	
    def show_confirmation_marshal(self, *args):
        self.dialog = ConfirmDialog()
        self.dialog.open()
    def score_limit(self, *args, **kwargs):
        self.ruks_layers =self.check_active('check')
        toast(self.ruks_layers)
        self.file_manager = MDFileManager(
         exit_manager=self.exit_manager,
         select_path=self.marshal_path_layers,)
        self.file_manager.ext = [".py"]
        self.file_manager.show('/sdcard') 
        self.manager_open = True 
        self.dialog.dismiss()
        self.dialog = None  
        self.active = False
    def check_active(self, group):  
        for cb in MDCheckbox.get_widgets(group):
            if cb.active:
                self.active = True
                return cb.score
        self.active = False
        return None 		 	 			
    def marshal_path_layers(self, path): 
    	self.exit_manager()
    	for i in range(int(self.ruks_layers)):
	    	try:
	    		file = open(path, "r").read()
	    		en = compile(file, '<ruks>', 'exec')
	    		enc = marshal.dumps(en)
	    		da = str(json.loads(open("data/da.json", "r").read())["marshal"])	    		
	    		with open(path, 'w') as x:
	    			x.write(f"{da}{enc}))")	    		
	    	except:
	    		toast('Erorr')
    	toast('تم تشفير الملف')
    	# - code by ruks -
    def exit_manager(self, *args): 
        self.manager_open = False
        self.file_manager.close()
    def events(self, instance, keyboard, keycode, text, modifiers): 
    	if keyboard in (1001, 27):
    		if self.manager_open:
    		   self.file_manager.back()
    		   return True  

App().run()
