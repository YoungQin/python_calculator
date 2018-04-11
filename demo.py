'''
仿windows 10 计算器 面向对象版
'''
from tkinter import *
import random
#实例化窗口
root = Tk()

class mian():
	
	# 设置窗口大小
	def __init__(self,h,g,title):
		root.maxsize(h, g)
		root.minsize(h, g)
		root.title(title)
		# 设置初始透明度
		self.nums = 1
		# 设置第一个数
		self.x = ''
		# 设置运算方法
		self.z = ''
		# 设置第二个数
		self.y = ''
		# 设置是否按下运算符
		self.istrue = False
		# 设置初始颜色
		self.colo = ''
		#是否已经运算
		self.click = False
		#设置计算公式
		# self. result = self.x + self.z + self.y
		#设置结果集
		self.result =''
	
	
	# 设置窗口颜色
	root_show = Frame(width=300, height=30)
	
	
	def set_label(self):
		# 设置窗口颜色
		root_show = Frame(width=300, height=30)
		# 编辑2个label
		head_bott = Label(root_show, bg='#555555', fg='#ffffff', text='标准计算器', font=("微软雅黑", 18), anchor='w', width=100)
		hei_label = Label(root_show, bg='#555555', fg='#ffffff', text='0', font=("微软雅黑", 20), anchor='se', height=2,
		                  borderwidth=20, width=100)
		self.hei = hei_label
		head_bott.pack()
		hei_label.pack()
		root_show.pack()
	
	def set_span(self):
		# 设置键盘和主界面
		frame_bord = Frame(width=350, height=400, bg='#cccccc')
		
		button_c = Button(frame_bord, text='C', bd='4', width=6, height=2, font=('微软雅黑', 13), bg='#787878',
		                  fg='#ffffff', command=lambda:self.fun_c()).grid(row=0, column=0)
		button_ce = Button(frame_bord, text='CE', bd='4', width=6, height=2, font=('微软雅黑', 13), bg='#787878',
		                   fg='#ffffff', command=lambda: self.fun_ce()).grid(row=0, column=1)
		button_del = Button(frame_bord, text='←', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#787878',
		                    fg='#ffffff', command=lambda: self.fun_t()).grid(row=0, column=2)
		button_fu = Button(frame_bord, text='±', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#787878',
		                   fg='#ffffff', command=lambda: self.fun_fu()).grid(row=0, column=3)
		button_1 = Button(frame_bord, text='1', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#000000',
		                  fg='#ffffff', command=lambda: print('C')).grid(row=1, column=0)
		button_2 = Button(frame_bord, text='2', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#000000',
		                  fg='#ffffff', command=lambda: print('C')).grid(row=1, column=1)
		button_3 = Button(frame_bord, text='3', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#000000',
		                  fg='#ffffff', command=lambda: print('C')).grid(row=1, column=2)
		button_chu = Button(frame_bord, text='/', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#333333',
		                    fg='#ffffff', command=lambda: self.chu()).grid(row=1, column=3)
		button_4 = Button(frame_bord, text='4', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#000000',
		                  fg='#ffffff', command=lambda: print('C')).grid(row=2, column=0)
		button_5 = Button(frame_bord, text='5', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#000000',
		                  fg='#ffffff', command=lambda: print('C')).grid(row=2, column=1)
		button_6 = Button(frame_bord, text='6', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#000000',
		                  fg='#ffffff', command=lambda: print('C')).grid(row=2, column=2)
		button_cheng = Button(frame_bord, text='*', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#333333',
		                      fg='#ffffff', command=lambda: self.cheng()).grid(row=2, column=3)
		button_7 = Button(frame_bord, text='7', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#000000',
		                  fg='#ffffff', command=lambda: print('C')).grid(row=3, column=0)
		button_8 = Button(frame_bord, text='8', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#000000',
		                  fg='#ffffff', command=lambda: print('C')).grid(row=3, column=1)
		button_9 = Button(frame_bord, text='9', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#000000',
		                  fg='#ffffff', command=lambda: print('C')).grid(row=3, column=2)
		button_jia = Button(frame_bord, text='+', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#333333',
		                    fg='#ffffff', command=lambda: self.jia()).grid(row=3, column=3)
		button_dian = Button(frame_bord, text='.', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#000000',
		                     fg='#ffffff', command=lambda:self.dian()).grid(row=4, column=0)
		button_0 = Button(frame_bord, text='0', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#000000',
		                  fg='#ffffff', command=lambda: print('C')).grid(row=4, column=1)
		button_deng = Button(frame_bord, text='=', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#333333',
		                     fg='#ffffff', command=lambda: self.deng()).grid(row=4, column=2)
		button_jian = Button(frame_bord, text='-', bd='4', width=6, height=2, font=('微软雅黑', 13, 'bold'), bg='#333333',
		                     fg='#ffffff', command=lambda: self.jian()).grid(row=4, column=3)
		self.bord = frame_bord
		# 显示主页面
		frame_bord.pack()


	
	# 点方法
	def dian(self):
		#如果
		if self.z:
			if self.y.find('.') == -1 :
				self.y = self.y+'.'
				self.show('y')
		else :
			if self.x.find('.') == -1:
				self.x = self.x+'.'
				self.show('x')
	
	
	#正负方法
	def fun_fu(self):
		if self.z  :
			if   (self.y == '' or  str(self.y)[0] == '0'):
				return
			
			if str(self.y)[0] == '-' :
				self.y = str(self.y)[1:]
			else:
				self.y = '-' +  str(self.y)
			self.show('y')
		else:
			if (self.x == '' or  str(self.x)[0] =='0') :
				return
			if str(self.x)[0] == '-':
				self.x = str(self.x)[1:]
			else :
				self.x = '-' + str(self.x)
			self.show('x')
		return
	#退格方法
	def fun_t(self):
		
		if self.click:
			return
		
		if self.z :
			#如果长度有2个多
			if len(str(self.y)) >=2 :
				self.y = self.y[0:-1]
			#反之只有1个长度
			else :
				self.y = '0'
			show = 'y'
		else :
			#同上

			if len(str(self.x)) >=2 :
				self.x = self.x[0:-1]
			else :
				self.x = '0'
			show = 'x'
		self.show(show)
		
	#ce 方法
	def fun_ce(self):
		if self.z:
			self.y = '0'
			show = 'y'
		else :
			self.x = '0'
			show = 'x'
		self.show(show)
	
	#c方法
	def fun_c(self):
		self.x = '0'
		self.z = ''
		self.y = ''
		self.click = False
		self.show('x')
		return
	
			
		#运算方法
	def yun(self,text):

		# 判断是否是运算状态
		if self.click:
			#如果计算完后再次点击运算符号
			if text in '+-*/':
				self.x = str(self.result)
				self.z = text
				self.y = ''
				self.click = False
				self.show('x')
				return
			#判断是不是等号 text 为等号会报错
			if text =='=':
				text = self.z
			#除数不能为0
			if text =='/' and str(self.y) =='0':
				self.result = '0'
				self.show('*=')
				return
			
			
			result = str(self.result) +  text +  str(self.y)
			#处理结果 返回结果集
			self.result = eval(result)
			#解决余数为浮点数 1.0的 情况
			if self.result and  str(self.result)[-1] == '0'   and str(self.result)[-2] == '.':
				self.result = int(self.result)
			self.show('*=')
			return
		
		
			
		#如果直接点击运算符号
		if self.x =='' and  self.y =='' and text :
			self.x='0'
			self.z =text
			self.y =''
			self.show('z')
			return
		#第一个数字填写后 才能填写运算符号
		if self.x != '':
			#正常运算 添加运算符
			if text in  '+-*/' and  self.z == '' and self.y == '' :
				self.z = text
				self.show('z')
				return
			#还没运算完 在进行运算符操作
			elif  text != '=' and self.z :#and self.y
				if self.z == '/' and str(self.y) == '0':
					self.fun_c()
				
				if len(str(self.y)) < 1  :
					self.z = text
					self.show('z')
					return
				
				strs = str(self.x) + str(self.z) + str(self.y)
				strs = eval(strs)
				if strs and  str(strs)[-1] == '0' and str(strs)[-2] == '.':
					strs = int(strs)
				self.x = "%g"%strs
				self.z = text
				self.y = ''
				self.show('z')
				return

			
		#如果2个运算数字都存在 则开始进行运算
		if self.x and self.y:
			#除数不能为0
			if self.y =='0' and self.z == '/':
				self.result = '0'
				self.show('*=')
				# self.click = True
				return
			#如果运算等式成立 按等于号
			if text =='=':
				strs = str(self.x) + str(self.z) + str(self.y)
				self.result = eval(strs)
				if self.result and str(self.result)[-1] == '0' and str(self.result)[-2] == '.':
					self.result = int(self.result)
				self.show('')
				self.click = True
				return

		
	#鼠标移入方法
	def Mouse_Entry(self,e):
		global colo
		colo = e.widget['bg']
		nums = str(random.randint(0, 1000000))
		if len(nums) != '6':
			nums = nums.ljust(6, str(random.randint(0, 9)))
		e.widget['bg'] = '#' + nums
	
	#鼠标移出事件
	def Mouse_Uot(self,e):
		global colo
		e.widget['bg'] = colo
		pass
	
	#鼠标滚轮事件
	def Mouse_on(self,e):
		if e.delta == -120 and self.nums > 0.11:
			self.nums -= 0.1
			root.attributes("-alpha", self.nums)  # 窗口透明度70 %
		elif e.delta == 120 and self.nums < 1:
			self.nums += 0.1
			root.attributes("-alpha", self.nums)
		
	# 显示
	def show(self,sign):
		show = ''
		if sign =='x':
			self.hei['text'] = str(self.x)
		elif sign == 'z':
			self.hei['text'] = str(self.x) + '\n' + str(self.z)
		elif sign == 'y':
			self.hei['text'] = str(self.x) + self.z + '\n' + str(self.y)
		elif sign == '*=':
			
			show = self.result
			if len(str(show)) >18:
				show = str("%g" %show)
				

			self.hei['text'] = show
		else:
			result = self.result
			if len(str(result)) > 18:
				result = str("%g" % result)
				
			show = str(self.x) + str(self.z) + str(self.y) + '=' + '\n' +str(result).rjust(9,' ')
			self.hei['text'] = show
			
	#鼠标点击事件
	def Mouse_click(self,e):
		#获取点击的值
		text = e.widget['text']
		
		# 输入的值最高为15为数
		if len(str(self.x)) > 16 or len(str(self.y)) > 16:
			# print(self.click)
			# print(type(self.x), '000011111')
			# print(type(self.y), '000011111', self.y)
			if self.z:
				self.y = "%g" % float(self.y)
			else:
				self.x = "%g" % float(self.x)
			
			pass
		
		# print(text,type(text))
		print(self.x,self.y,self.z)
		#如果是减好 就是减号方法
		if text in '+-*/=':
			self.yun(text)
			return
		#c 方法
		if  text == 'C':
			self.fun_c()
			return
		#ce方法
		if text == 'CE':
			self.fun_ce()
			return
		#小数点方法
		if text =='.' :
			self.dian()
			return
		#退格方法
		if text == '←':
			self.fun_t()
			return
		#正负方法
		if text  == '±':
			self.fun_fu()
			return
		#如果在新点一个数字 则取消运算状态
		if self.click  and text not in '+-*/=':
			self.click = False
			self.x = ''
			self.y = ''
			self.z = ''

			
		#如果输入的不是数字键 则暂停
		if text not in '1234567890':
			return
		
		
		
		#如果数值的开头为0   不能出现连续以0开头的数值
		if    (str(self.y)[0:1] == '0'  or  str(self.x)[0:1] =='0') and  self.z ==''  :
			if self.z :
				self.y = text
				show = 'y'
			else :
				self.x = text
				show = 'x'
			self.show(show)
			return
		elif self.y[0:1] == '0'  and   self.z !='' :
			self.y = text
			show = 'y'
			self.show(show)
			return
		
		
		#如果显示的是0 和输入的是0
		if  self.hei['text'] == '0' and text != '0'  :
			if self.z :
				self.y =text
				show = 'y'
			else :
				self.x = text
				show = 'x'
			self.show(show)
			return
		
		#如果有标点符号 则显示 第二个数字 反之 显示第一个
		if self.z :
			self.y += text
			si = 'y'
		else:
			self.x += text
			si ='x'
		self.show(si)
		
		# print(self.x,self.z,self.y)
		
	

	#调用事件
	def call_fun(self):
		self.bord.bind_class('Button', '<Enter>', self.Mouse_Entry)
		self.bord.bind_class('Button', '<Leave>', self.Mouse_Uot)
		self.bord.bind_class('Button', '<Button-1>', self.Mouse_click)
		root.bind('<MouseWheel>', self.Mouse_on )

		
		
		

mian =  mian(320,500,'计算器')
mian.set_label()
mian.set_span()
mian.call_fun()
root.mainloop()