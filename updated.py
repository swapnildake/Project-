import mysql.connector
import random
from tkinter.ttk import *
from tkinter import messagebox as mb
from tkinter import ttk
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import cv2
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import requests
import json
import time
import tkinter
import PIL.Image, PIL.ImageTk
import smtplib
import os.path
import threading
from functools import partial


#packages required for mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



#---------------------------------------------------------------------------------------------  












						
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(side=BOTTOM,fill=BOTH, expand=1)
        
        load = Image.open("store6.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
#App(tkinter.Tk(), "Tkinter and OpenCV")
class Dake:

	def __init__(self,root,):
		self.root=root
		self.root.title("Kirana Store Management")
		self.root.geometry("1520x800+0+0")
		self.root.configure(bg="red")
		bn="#353535"#272822"
		title=Label(self.root,text="                       KIRANA STORE",fg='white',bg="#424242",bd=30,relief=GROOVE,font=("times new roman",20,"bold"))
		title.pack(side=TOP,fill=X)
		#time1=Label(self.root,text="15:50:41",fg='red',bg="#272822",font=("times new roman",20,"bold"))
		#title.pack(side=TOP)
		#side=TOP,fill=X
		#title.grid(row=0,column=1,columnspan=2,pady=3)
		

#===========================================Methods==================================================================	
		
		
		def box():	
			ct=1
			fg_of_box='red'
			for i in range(20):
				
				if (ct%2==0):
					doar='on'
					fg_of_box='red'
				else: 
					doar='off'
					fg_of_box='green'
				ct=ct+1
				time.sleep(1)

				#print(time)

			

				title_frame=Frame(self.root,bd=10,relief=RIDGE,bg='#272822')
				title_frame.place(x=1182,y=30,width=78,height=78)
				box_char=''
				box_char1=""
				tm=time.time()

				if(doar=='on'):
					on=Label(title_frame,text=tm,fg=fg_of_box,bg='#272822',font=('times of roman',15,'bold')).pack(pady=10)
				else:
					off=Label(title_frame,text=box_char1,fg=fg_of_box,bg='#272822',font=('times of roman',20,'bold')).pack(pady=10)


				title_frame1=Frame(self.root,bd=10,relief=RIDGE,bg='#272822')
				title_frame1.place(x=260,y=30,width=78,height=78)

				
				if(doar=='on'):
					on=Label(title_frame1,text=box_char1,fg=fg_of_box,bg='#272822',font=('times of roman',20,'bold')).pack(pady=10)
				else:
					off=Label(title_frame1,text=box_char,fg='red',bg='#272822',font=('times of roman',20,'bold')).pack(pady=10)

				self.title_frame2=Frame(self.root,bd=10,relief=RIDGE,bg='#272822')
				self.title_frame2.place(x=340,y=30,width=78,height=78)

				
				if(doar=='on'):
					on=Label(self.title_frame2,text=box_char,fg=fg_of_box,bg='#272822',font=('times of roman',20,'bold')).pack(pady=10)
				else:
					off=Label(self.title_frame2,text=box_char1,fg='red',bg='#272822',font=('times of roman',20,'bold')).pack(pady=10)

				title_frame3=Frame(self.root,bd=10,relief=RIDGE,bg='#272822')
				title_frame3.place(x=420,y=30,width=78,height=78)

			
				if(doar=='on'):
					on=Label(title_frame3,text=box_char1,fg=fg_of_box,bg='#272822',font=('times of roman',20,'bold')).pack(pady=10)
				else:
					off=Label(title_frame3,text=box_char,fg='red',bg='#272822',font=('times of roman',20,'bold')).pack(pady=10)

				title_frame4=Frame(self.root,bd=10,relief=RIDGE,bg='#272822')
				title_frame4.place(x=1104,y=30,width=78,height=78)

				
				if(doar=='on'):
					on=Label(title_frame4,text=box_char,fg=fg_of_box,bg='#272822',font=('times of roman',20,'bold')).pack(pady=10)
				else:
					off=Label(title_frame4,text=box_char1,fg='red',bg='#272822',font=('times of roman',20,'bold')).pack(pady=10)


				title_frame4=Frame(self.root,bd=10,relief=RIDGE,bg='#272822')
				title_frame4.place(x=1026,y=30,width=78,height=78)

			
				if(doar=='on'):
					on=Label(title_frame4,text=box_char1,fg=fg_of_box,bg='#272822',font=('times of roman',20,'bold')).pack(pady=10)
				else:
					off=Label(title_frame4,text=box_char,fg='red',bg='#272822',font=('times of roman',20,'bold')).pack(pady=10)
		t5=threading.Thread(target=box)
		t5.start()

		"""title_frame4=Frame(self.root,bd=10,relief=RIDGE,bg='#272822')
		title_frame4.place(x=948,y=30,width=78,height=78)


		title_frame4=Frame(self.root,bd=10,relief=RIDGE,bg='#272822')
		title_frame4.place(x=870,y=30,width=78,height=78)"""

		


		def backCol():
			self.root.configure(bg='red')


		def product_data():
			mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="lakan")
			mycursor = mydb.cursor()
			sql = "SELECT * FROM storekirana2"#brand,product,day,month,year,qty,wt) VALUES (%s, %s, %s, %s, %s, %s, %s)"									
			mycursor.execute(sql)
			self.product_count1=0
			self.product_count2=0
			self.product_count3=0

			wheat_brand1=['Morya','Celebration','Twitter','Olympic']

			wheat_brand2=['Mahalaxmi','Dimond','Swastic','Vasant']
			
			wheat_brand3=['Tini','Mini','Indrayani','Basmati']
			self.p=0
			self.p1=0
			self.p2=0
			self.p3=0
			self.p4=0
			self.p5=0
			self.p6=0
			self.p7=0
			self.p8=0
			self.p9=0
			self.p10=0
			self.p11=0	

			for i in mycursor:
				if i[3]=='Jan' and i[2]==2 and i[4]==2016:
					if i[1]=='Wheat':
						self.product_count1=self.product_count1+i[7]
					if i[1]=='Jawar':
						self.product_count2=self.product_count2+i[7]
					if i[1]=='Rice':
						self.product_count3=self.product_count3+i[7]


				
		
					if i[0]==wheat_brand1[0]:
						self.p=self.p+i[7]

					if i[0]==wheat_brand1[1]:
						self.p1=self.p1+i[7]

					if i[0]==wheat_brand1[2]:
						self.p2=self.p2+i[7]
					
					if i[0]==wheat_brand1[3]:
						self.p3=self.p3+i[7]



				
		
					if i[0]==wheat_brand2[0]:
						self.p4=self.p4+i[7]

					if i[0]==wheat_brand2[1]:
						self.p5=self.p5+i[7]

					if i[0]==wheat_brand2[2]:
						self.p6=self.p6+i[7]
					
					if i[0]==wheat_brand2[3]:
						self.p7=self.p7+i[7]


				
		
					if i[0]==wheat_brand3[0]:
						self.p8=self.p8+i[7]

					if i[0]==wheat_brand3[1]:
						self.p9=self.p9+i[7]

					if i[0]==wheat_brand3[2]:
						self.p10=self.p10+i[7]
					
					if i[0]==wheat_brand3[3]:
						self.p11=self.p11+i[7]


		product_data()
						


		def pichart():
			fig = plt.figure()
			ax = fig.add_axes([0,0,1,1])
			ax.axis('equal')
			remaining_space=1000-(self.product_count1+self.product_count2+self.product_count3)
			langs = ['Wheat','Jawar','Rice','Remaining Space']
			pd = [self.product_count1,self.product_count2,self.product_count3,remaining_space]
			ax.pie(pd, labels = langs,autopct='%1.2f%%')
			plt.show()

		

		def histogram():
			fig,ax = plt.subplots(1,1)
			a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
			ax.hist(a, bins = [0,25,50,75,100])
			ax.set_title("histogram of result")
			ax.set_xticks([0,25,50,75,100])
			ax.set_xlabel('marks')
			ax.set_ylabel('no. of students')
			plt.show()

		def boxPlot():
			pass
			#fig = plt.figure()
			# Create an axes instance
			#ax = fig.add_axes([0,0,1,1])
			# Create the boxplot
			#bp = ax.boxplot(data_to_plot)
			#plt.show()

		def scatter():
			girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
			boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
			grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
			fig=plt.figure()
			ax=fig.add_axes([0,0,1,1])
			ax.scatter(grades_range, girls_grades, color='r')
			ax.scatter(grades_range, boys_grades, color='b')
			ax.set_xlabel('Grades Range')
			ax.set_ylabel('Grades Scored')
			ax.set_title('scatter plot')
			plt.show()
		def contours():
			xlist = np.linspace(-3.0, 3.0, 100)
			ylist = np.linspace(-3.0, 3.0, 100)
			X, Y = np.meshgrid(xlist, ylist)
			Z = np.sqrt(X**2 + Y**2)
			fig,ax=plt.subplots(1,1)
			cp = ax.contourf(X, Y, Z)
			fig.colorbar(cp) # Add a colorbar to a plot
			ax.set_title('Filled Contours Plot')
			#ax.set_xlabel('x (cm)')
			ax.set_ylabel('y (cm)')
			plt.show()
		def coll():
			pass
			


		
		
		self.capturee=0
		def stop_capture():
			self.capturee=1
			cap_vid=Button(self.button_Frame,text="►",width=10,fg="white",font=("times new rooman",16,"bold"),relief=RAISED,bd=2,bg="#272822",command=Start_cap)
			cap_vid.grid(row=0,column=1,columnspan=2,pady=3,sticky="w")

		self.import_export=1	


		
		def cap():
			


			face_cascade = cv2.CascadeClassifier('stop.xml')
			a=cv2.VideoCapture(0)
			count=1
			self.cb=1
			while self.capturee==0:
				title_frame=Frame(self.root,bd=10,relief=RIDGE,bg='red')#272822
				title_frame.place(x=100,y=30,width=78,height=78)
				count+=1
				check,frame=a.read()
				gray_image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
				
				faces=face_cascade.detectMultiScale(gray_image,scaleFactor=1.05,minNeighbors=5)

				print(type(faces))

				print(faces)


				import mysql.connector

				mydb = mysql.connector.connect(
				  host="localhost",
				  user="root",
				  passwd="",
				  database="lakan"
				)

				mycursor = mydb.cursor()

				n = mycursor.execute('select * from store')
				c = mycursor.fetchall()
				ca="Basmati"
				for i in c:
					if i[0]==ca:
						n1=i[2]
				mc=mydb.cursor()
				if len(faces)==0:
					print("Serching..... ")
				else:
					print("Prodct Found")
					#on=Label(self.title_frame2,text="ooooo",fg='green',bg='#272822',font=('times of roman',20,'bold')).pack(pady=10)
					
					title_frame=Frame(self.root,bd=10,relief=RIDGE,bg='green')
					title_frame.place(x=100,y=30,width=78,height=78)
					if self.import_export==1:
						j=(n1+self.cb)
					if self.import_export==0:
						j=n1-(self.cb)
					self.cb=self.cb+1
					print("Product Count",j)
					bas='Basmati'

					sql ="UPDATE store SET qty = %s WHERE brand = %s"
					var=(j,bas)
					mc.execute(sql,var)
					time.sleep(5)
				mydb.commit()
				time.sleep(2)
			self.capturee=0
			
			a.release()
			cv2.destroyAllWindows()	

		def Start_cap():
			t1=threading.Thread(target=cap)
			t1.start()
			cap_vid=Button(self.button_Frame,text="■",width=10,fg="white",font=("times new rooman",15,"bold"),relief=RAISED,bd=2,bg="#272822",command= stop_capture  )
			cap_vid.grid(row=0,column=1,columnspan=2,pady=3,sticky="w")

		

		def exits():
			self.root.destroy()

		def no_emp():
			mb.showinfo("Emp","Number of Employee: 26")
		def do_nothing():
			mb.showinfo("Nothing","Ther is no implimentation for me yet	!")
			
		def hel():
			help(ttk)
		self.log=0
		self.aa=1

		def is_user_correct():
			mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="lakan")

			mycursor = mydb.cursor()
		
			m_uname=self.log_uname_in.get()
			m_password=self.log_password_in.get()
		
			print(m_uname)
			print(m_password)
			sql = "SELECT * FROM usersignupdata"
													
			mycursor.execute(sql)

			for i in mycursor:
				if m_uname==i[0]:
					if m_password==i[5]:
						self.log=1
						self.aa=0
						print(i[4])
						kk()
					#else: 
					#	mb.showinfo("Error","Incorrect Password")
				#else: 
				#	mb.showinfo("Error","Incorrect Username")


		def get_up():
			mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="lakan")

			mycursor = mydb.cursor()
		
			m_mobile_number=self.mobile_number_in.get()
		
			print("Mobile Number: m",m_mobile_number)
			sql = "SELECT * FROM usersignupdata"
													
			mycursor.execute(sql)

			for i in mycursor:
				if m_mobile_number==i[3]:
						geted_u=i[0]
						geted_p=i[5]
						msg='your username:'+geted_u+' and password:'+geted_p
						print(msg)

						URL = 'https://www.sms4india.com/api/v1/sendCampaign'

						# get request
						def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
						  req_params = {
						  'apikey':'QBYOM7F7XIO0V7HS8W7ZF0M0RYY3VMND',
						  'secret':'1ZBPCHICFV8LTQMS',
						  'usetype':'stage',
						  'phone': m_mobile_number,
						  'message':msg,
						  'senderid':'no'
						  }
						  return requests.post(reqUrl, req_params)

						# get response
						response = sendPostRequest(URL, '', '', 'stage', '', '', '' )

						print("response.text")

						


#========== Forget Password =====================================================================================
		def forgetPassword():
			self.Manage_Frame=Frame(self.root,bd=10,relief=RIDGE,bg="#363636")
			self.Manage_Frame.place(x=520,y=140,width=500,height=650)

			forget_frame=Frame(self.Manage_Frame,bd=0,relief=RIDGE,bg="#303030")
			forget_frame.place(x=80,y=150,width=350,height=300)


			first_title=Label(forget_frame,text="Forget Password",fg='white',bg="#272822",bd=10,width=20,relief=GROOVE,font=("times new roman",20,"bold"))
			first_title.grid(row=0,column=1,columnspan=2,pady=3)

			self.mobile_number_in=tk.StringVar(self.Manage_Frame)

			mobile_number=Label(forget_frame,text="Mobile Number:",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			mobile_number.grid(row=4,columnspan=2,pady=3,sticky='w')
			in_mobile_number=Entry(forget_frame,fg="white",textvariable=self.mobile_number_in,font=("times new rooman",15,"bold"),bg="#272822")
			in_mobile_number.grid(row=4,column=2,columnspan=2,pady=3)

			rec_type=Label(forget_frame,text="Get on:",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			rec_type.grid(row=5,columnspan=2,pady=3,sticky='w')

			btn_get_up=Button(forget_frame,text="Mobile",width=10,fg="white",font=("times new rooman",15,"bold"),relief=RAISED,bd=2,bg="#272822",command=get_up)
			btn_get_up.grid(row=5,column=1,columnspan=2,pady=3)

			btn_get_up=Button(forget_frame,text="Email",width=10,fg="white",font=("times new rooman",15,"bold"),relief=RAISED,bd=2,bg="#272822",command=get_up)
			btn_get_up.grid(row=5,column=2,columnspan=2,pady=3,sticky="E")




			
			self.button_Frame=Frame(self.Manage_Frame,bd=10,relief=RIDGE,bg="#363636")
			self.button_Frame.place(x=40,y=515,width=410,height=70)

			login=Button(self.button_Frame,text="Login",width=10,fg="white",font=("times new rooman",15,"bold"),relief=RAISED,bd=2,bg="#272822",command=lo)
			login.grid(row=0,column=1,columnspan=2,pady=3,sticky="w")

			signup=Button(self.button_Frame,text="SignUp",width=10,fg="white",font=("times new rooman",15,"bold"),relief=RAISED,bd=2,bg="#272822",command=si)
			signup.grid(row=0,column=3,columnspan=2,pady=3,sticky="w")

			exit=Button(self.button_Frame,text="Exit",width=10,fg="white",font=("times new rooman",15,"bold"),relief=RAISED,bd=2,bg="#272822",command=exits)
			exit.grid(row=0,column=6,columnspan=2,pady=3,sticky="w")
#===============================================================================forget password=======






		
#====================login=================================================================================
		def lo():
			self.Manage_Frame=Frame(self.root,bd=10,relief=RIDGE,bg="#363636")
			self.Manage_Frame.place(x=520,y=140,width=500,height=650)

			login_Frame=Frame(self.Manage_Frame,bd=0,relief=RIDGE,bg="#303030")
			login_Frame.place(x=80,y=150,width=350,height=300)


			first_title=Label(login_Frame,text="Login",fg='white',bg="#363636",bd=10,relief=GROOVE,font=("times new roman",40,"bold"))
			first_title.grid(row=0,column=1,columnspan=2,pady=3)

			self.log_uname_in=tk.StringVar(self.Manage_Frame)
			self.log_password_in=tk.StringVar(self.Manage_Frame)

			user=Label(login_Frame,text="User Name:",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			user.grid(row=4,columnspan=2,pady=3,sticky='w')
			in_user=Entry(login_Frame,fg="white",textvariable=self.log_uname_in,font=("times new rooman",15,"bold"),bg="#272822")
			in_user.grid(row=4,column=2,columnspan=2,pady=15,padx=15)

			password=Label(login_Frame,text="Password",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			password.grid(row=5,columnspan=2,pady=3,sticky="w")
			in_password=Entry(login_Frame,fg="white",show='*',textvariable=self.log_password_in,font=("times new rooman",15,"bold"),bg="#272822")
			in_password.grid(row=5,column=2,columnspan=2,pady=3)

			btn_forget_password=Button(login_Frame,text="Forget Password",font=("times new rooman",15,"bold"),bg='#272822',fg="white",bd=2,command=forgetPassword)
			btn_forget_password.grid(row=6,column=1,columnspan=2,pady=60)


			
			self.button_Frame=Frame(self.Manage_Frame,bd=10,relief=RIDGE,bg="#363636")
			self.button_Frame.place(x=40,y=515,width=410,height=70)

			login=Button(self.button_Frame,text="Login",width=10,fg="white",font=("times new rooman",15,"bold"),relief=RAISED,bd=2,bg="#272822",command=is_user_correct)
			login.grid(row=0,column=1,columnspan=2,pady=3,sticky="w")

			signup=Button(self.button_Frame,text="SignUp",width=10,fg="white",font=("times new rooman",15,"bold"),relief=RAISED,bd=2,bg="#272822",command=si)
			signup.grid(row=0,column=3,columnspan=2,pady=3,sticky="w")

			exit=Button(self.button_Frame,text="Exit",width=10,fg="white",font=("times new rooman",15,"bold"),relief=RAISED,bd=2,bg="#272822",command=exits)
			exit.grid(row=0,column=6,columnspan=2,pady=3,sticky="w")

#=================================================================login==================================
		
		self.rand_otp=45
		self.mobile_number='456654565'
		self.str2="ldkfj"
		def getOTP():
			
			m_mobile=self.mobile_in.get()
			print("mobile Number:",m_mobile)

			self.rand_otp=random.randint(1000,2000)
			print("from dake kirana store: your OTP is: ",self.rand_otp)
			self.mobile_number=m_mobile

			URL = 'https://www.sms4india.com/api/v1/sendCampaign'

			str1='from dake kirana store: your OTP is:'
			self.str2=str1+str(self.rand_otp)
			print("message: ",self.str2)

			# get request
			def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
			  req_params = {
			  'apikey':'QBYOM7F7XIO0V7HS8W7ZF0M0RYY3VMND',
			  'secret':'1ZBPCHICFV8LTQMS',
			  'usetype':'stage',
			  'phone': self.mobile_number,
			  'message':self.str2,
			  'senderid':'no'
			  }
			  return requests.post(reqUrl, req_params)

			# get response
			response = sendPostRequest(URL, '', '', 'stage', '', '', '' )

			print("response.text")

		def getOTP_OnMail():
			
			m_email=self.email_in.get()
			self.rand_otp=random.randint(1000,2000)
			msg="OTP:"
			msg1=str(self.rand_otp)
			print(self.rand_otp)

			#sender_email='smfcmahidhoni123456@gmail.com'
			reciever_email='lakan1998hpk@gmail.com'
			#password='mahi@1998'

			#msg="ky ky bhavad"
			server=smtplib.SMTP("smtp.gmail.com",587)
			server.starttls()
			#print(os.environ.get('PASSWORD'))
			#p=os.environ.get('PASSWORD')
			server.login('smfcmahidhoni123456@gmail.com','mahi@1998')
			server.sendmail('smfcmahidhoni123456@gmail.com',m_email,msg1)
			print("OTP is sent on ",m_email)
		

			
						

					



		def getSignupData():
			mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="lakan")

			mycursor = mydb.cursor()
			
			m_fname=self.fname_in.get()
			m_lname=self.lname_in.get()
			m_uname=self.uname_in.get()
			m_mobile=self.mobile_in.get()
			m_email=self.email_in.get()
			m_password1=self.password1_in.get()
			m_password2=self.password2_in.get()
			m_password_hint=self.password_hint_in.get()
			m_adhar=self.adhar_in.get()
			m_address=self.address_in.get()
			m_OTP=self.OTP_in.get()
			print("si  rand_otp",self.rand_otp)

			print("m_OTP=",m_OTP)

			if(str(self.rand_otp)==m_OTP):
				print("success")
				sql = "INSERT INTO usersignupdata (username,fname,lname,mobile_number,email_id,password1,password2,password_hint,adhar_number,address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
				val=(m_uname,m_fname,m_lname,m_mobile,m_email,m_password1,m_password2,m_password_hint,m_adhar,m_address)									
				mycursor.execute(sql, val)
				mydb.commit()
				mb.showinfo("Succefull ! ","Welcome")
			else:
				print("Unsuccess")
				mb.showinfo("Error ! ","Please Enter Correct OTP")




			



#==================signup===========================================================================
		def si():
			self.Manage_Frame=Frame(self.root,bd=5,relief=RIDGE,bg="#363636")
			self.Manage_Frame.place(x=520,y=140,width=500,height=650)

			signup_Frame=Frame(self.Manage_Frame,bd=0,relief=RIDGE,bg="#303030")
			signup_Frame.place(x=40,y=20,width=410,height=600)


			self.fname_in=tk.StringVar(self.Manage_Frame)
			self.lname_in=tk.StringVar(self.Manage_Frame)
			self.uname_in=tk.StringVar(self.Manage_Frame)
			self.mobile_in=tk.StringVar(self.Manage_Frame)
			self.email_in=tk.StringVar(self.Manage_Frame)
			self.password1_in=tk.StringVar(self.Manage_Frame)
			self.password2_in=tk.StringVar(self.Manage_Frame)
			self.password_hint_in=tk.StringVar(self.Manage_Frame)
			self.adhar_in=tk.StringVar(self.Manage_Frame)
			self.address_in=tk.StringVar(self.Manage_Frame)
			self.OTP_in=tk.StringVar(self.Manage_Frame)


			first_title=Label(signup_Frame,text="SignUp",fg='white',bg="#272822",bd=10,relief=GROOVE,font=("times new roman",10,"bold"))
			first_title.grid(row=0,column=1,columnspan=2,pady=3)

			fname=Label(signup_Frame,text="First Name:*",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			fname.grid(row=1,columnspan=2,pady=3,sticky='w')
			in_fname=Entry(signup_Frame,textvariable = self.fname_in,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			in_fname.grid(row=1,column=2,columnspan=2,pady=3)

			lname=Label(signup_Frame,text="Last Name:*",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			lname.grid(row=2,columnspan=2,pady=3,sticky='w')
			in_lname=Entry(signup_Frame,textvariable = self.lname_in,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			in_lname.grid(row=2,column=2,columnspan=2,pady=3)

			uname=Label(signup_Frame,text="User Name:*",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			uname.grid(row=3,columnspan=2,pady=3,sticky='w')
			in_uname=Entry(signup_Frame,textvariable = self.uname_in,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			in_uname.grid(row=3,column=2,columnspan=2,pady=3)	

			mobile=Label(signup_Frame,text="Mobile Number:*",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			mobile.grid(row=4,columnspan=2,pady=3,sticky='w')
			in_mobile=Entry(signup_Frame,textvariable = self.mobile_in,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			in_mobile.grid(row=4,column=2,columnspan=2,pady=3)

			email=Label(signup_Frame,text="Email Id:*",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			email.grid(row=5,columnspan=2,pady=3,sticky='w')
			in_email=Entry(signup_Frame,textvariable = self.email_in,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			in_email.grid(row=5,column=2,columnspan=2,pady=3)
			
			password1=Label(signup_Frame,text="Password:*",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			password1.grid(row=6,columnspan=2,pady=3,sticky='w')
			in_password1=Entry(signup_Frame,textvariable = self.password1_in,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			in_password1.grid(row=6,column=2,columnspan=2,pady=3)

			password2=Label(signup_Frame,text="Renter Password:*",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			password2.grid(row=7,columnspan=2,pady=3,sticky='w')
			in_password2=Entry(signup_Frame,textvariable = self.password2_in,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			in_password2.grid(row=7,column=2,columnspan=2,pady=3)

			password_hint=Label(signup_Frame,text="Password Hint:",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			password_hint.grid(row=8,columnspan=2,pady=3,sticky='w')
			in_password_hint=Entry(signup_Frame,textvariable = self.password_hint_in,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			in_password_hint.grid(row=8,column=2,columnspan=2,pady=3)

			adhar=Label(signup_Frame,text="Adhar Number:*",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			adhar.grid(row=9,columnspan=2,pady=3,sticky='w')
			in_adhar=Entry(signup_Frame,textvariable = self.adhar_in,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			in_adhar.grid(row=9,column=2,columnspan=2,pady=3)

			address=Label(signup_Frame,text="Address:*",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			address.grid(row=10,columnspan=2,pady=3,sticky='w')
			in_address=Entry(signup_Frame,textvariable = self.address_in,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			in_address.grid(row=10,column=2,columnspan=2,pady=3)

			otp_type=Label(signup_Frame,text="Get OTP on :*",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			otp_type.grid(row=11,columnspan=2,pady=3,sticky='w')

			btn_otp_onMail=Button(signup_Frame,text="Mail",width=10,fg="white",font=("times new rooman",15,"bold"),relief=RAISED,bd=2,bg="#272822",command=getOTP_OnMail)
			btn_otp_onMail.grid(row=11,column=1,columnspan=2,pady=3,sticky="E")


			btn_otp=Button(signup_Frame,text="Mobile",width=10,fg="white",font=("times new rooman",15,"bold"),relief=RAISED,bd=2,bg="#272822",command=getOTP)
			btn_otp.grid(row=11,column=2,columnspan=2,pady=3,sticky="E")

			

			otp=Label(signup_Frame,text="Enter OTP*",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			otp.grid(row=12,columnspan=2,pady=3,sticky='w')
			in_otp=Entry(signup_Frame,textvariable = self.OTP_in,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			in_otp.grid(row=12,column=2,columnspan=2,pady=3)


			self.button_Frame=Frame(self.Manage_Frame,bd=10,relief=RIDGE,bg="#363636")
			self.button_Frame.place(x=40,y=515,width=410,height=70)

			login=Button(self.button_Frame,text="Login",width=10,fg="white",font=("times new rooman",15,"bold"),relief=RAISED,bd=2,bg="#272822",command=lo)
			login.grid(row=0,column=1,columnspan=2,pady=3,sticky="w")

			signup=Button(self.button_Frame,text="SignUp",width=10,fg="white",font=("times new rooman",15,"bold"),relief=RAISED,bd=2,bg="#272822",command=getSignupData)
			signup.grid(row=0,column=3,columnspan=2,pady=3,sticky="w")

			exit=Button(self.button_Frame,text="Exit",width=10,fg="white",font=("times new rooman",15,"bold"),relief=RAISED,bd=2,bg="#272822",command=self.root.destroy)
			exit.grid(row=0,column=6,columnspan=2,pady=3,sticky="w")
#==================================================================== signup =========================




#===========================================Methods======================================================	



		

		


		print("self.log",self.log)
		if(self.log==0):
			lo()
		else:
			si()
		print("start:..",self.log)

		def product_menu(product_name):
			mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="lakan")
			mycursor = mydb.cursor()
			sql = "SELECT * FROM storekirana2"#brand,product,day,month,year,qty,wt) VALUES (%s, %s, %s, %s, %s, %s, %s)"									
			mycursor.execute(sql)
			total_product=0
			total_b1=0
			total_b2=0
			total_b3=0
			total_b4=0


			print("Product Name: ",product_name)
			if product_name=='Wheat':
				wheat_brand=['Morya','Celebration','Twitter','Olympic']
			if product_name=='Jawar':
				wheat_brand=['Mahalaxmi','Dimond','Swastic','Vasant']
			if product_name=='Rice':
				wheat_brand=['Tini','Mini','Indrayani','Basmati']


			
			for i in mycursor:
				if(i[2]==11 and i[3]=='Dec' and i[4]==2017):
					if i[1]==product_name:# and i[4]==2016:
						if i[0]==wheat_brand[0]:
							total_b1=total_b1+i[7]

						if i[0]==wheat_brand[1]:
							total_b2=total_b1+i[7]

						if i[0]==wheat_brand[2]:
							total_b3=total_b1+i[7]
						
						if i[0]==wheat_brand[3]:
							total_b4=total_b1+i[7]
				


			#signup_Frame=Frame(self.root,bd=0,relief=RIDGE,bg="red")
			#signup_Frame.place(x=0,y=0,width=410,height=600)

			self.Manage_Frame=Frame(self.root,bd=5,bg="#363636")
			self.Manage_Frame.place(x=530,y=400,width=460,height=200)

			product_label=Label(self.Manage_Frame,text=product_name,fg="white",font=("times new rooman",15,"bold"),bg='#363636').grid(row=0,column=0,padx=3,pady=3)
			product_label=Label(self.Manage_Frame,text="Stock",fg="white",font=("times new rooman",15,"bold"),bg='#363636').grid(row=0,column=1,padx=3,pady=3)


			product_label=Label(self.Manage_Frame,text=wheat_brand[0],fg="white",font=("times new rooman",15,"bold"),bg='#363636').grid(row=1,column=0,padx=3,pady=3)
			product_label=Label(self.Manage_Frame,text=wheat_brand[1],fg="white",font=("times new rooman",15,"bold"),bg='#363636').grid(row=2,column=0,padx=3,pady=3)
			product_label=Label(self.Manage_Frame,text=wheat_brand[2],fg="white",font=("times new rooman",15,"bold"),bg='#363636').grid(row=3,column=0,padx=3,pady=3)
			product_label=Label(self.Manage_Frame,text=wheat_brand[3],fg="white",font=("times new rooman",15,"bold"),bg='#363636').grid(row=4,column=0,padx=3,pady=3)

			product_label=Label(self.Manage_Frame,text=total_b1,fg="white",font=("times new rooman",15,"bold"),bg='black').grid(row=1,column=1,padx=3,pady=3)
			product_label=Label(self.Manage_Frame,text=total_b2,fg="white",font=("times new rooman",15,"bold"),bg='black').grid(row=2,column=1,padx=3,pady=3)
			product_label=Label(self.Manage_Frame,text=total_b3,fg="white",font=("times new rooman",15,"bold"),bg='black').grid(row=3,column=1,padx=3,pady=3)
			product_label=Label(self.Manage_Frame,text=total_b4,fg="white",font=("times new rooman",15,"bold"),bg='black').grid(row=4,column=1,padx=3,pady=3)

			print(wheat_brand[0]," :",total_b1)
			print(wheat_brand[1]," :",total_b2)
			print(wheat_brand[2]," :",total_b3)
			print(wheat_brand[3]," :",total_b4)


			print(i[0]," hell////////",i[7])






		

		self.aa=1
		def kk():		
			def bgRed():
				self.Sec_Frame.config(bg='red')
				self.Third_Frame.config(bg='red')
			def bgBlue():
				self.Sec_Frame.config(bg='#dceffb')
				self.Third_Frame.config(bg='#dceffb')
			def bgYellow():
				self.Sec_Frame.config(bg='yellow')
				self.Third_Frame.config(bg='yellow')

			def bgBlack():
				self.Sec_Frame.config(bg='black')
				self.Third_Frame.config(bg='black')
			def bgGreen():
				self.Sec_Frame.config(bg='#ffedd1')
				self.Third_Frame.config(bg='#ffedd1')

			def randColor():
				r = lambda: random.randint(0,255)
				print('#%02X%02X%02X' % (r(),r(),r()))
				col='#%02X%02X%02X' % (r(),r(),r())
				self.Sec_Frame.config(bg=col)
				self.Third_Frame.config(bg=col)



		

				
	#============MenuBar======================================================================================
			
			self.menubar = Menu(self.root)
			self.filemenu = Menu(self.menubar, tearoff=0,bg="#272822",fg='white')
			self.filemenu.add_command(label="No. of Employee",font=("times new rooman",15,"bold"), command=no_emp)
			self.filemenu.add_separator()
			
			self.filemenu.add_command(label="Logout",font=("times new rooman",15,"bold"), command=lo)
			self.filemenu.add_separator()
			self.filemenu.add_separator()
			self.filemenu.add_command(label="Quit",font=("times new rooman",15,"bold"), command=self.root.quit)
			self.filemenu.add_separator()
			self.menubar.add_cascade(label=":", menu=self.filemenu,font=("times new rooman",30,"bold"))
				
			self.charts = Menu(self.menubar, tearoff=0,bg="#272822",fg='white')
			self.charts.add_command(label="Histogram",font=("times new rooman",15,"bold"), command=histogram)
			self.charts.add_separator()
			self.charts.add_command(label="Pi Chart",font=("times new rooman",15,"bold"), command=pichart)
			self.charts.add_separator()
			
			#self.charts.add_command(label="Box Chart",font=("times new rooman",15,"bold"), command=boxPlot)
			#self.charts.add_separator()
			#self.charts.add_command(label="Contours", font=("times new rooman",15,"bold"),command=contours)
			#self.charts.add_separator()
			#self.charts.add_command(label="Scatter Chart",font=("times new rooman",15,"bold"), command=scatter)
			#self.charts.add_separator()
			#self.menubar.add_cascade(label="Charts", menu=self.charts,font=("times new rooman",60,"bold"))

			
			self.theme = Menu(self.menubar, tearoff=0,bg="#272822",fg='white')
			self.theme.add_command(label="Red",font=("times new rooman",15,"bold"), command=bgRed)
			self.theme.add_separator()
			self.theme.add_command(label="blue",font=("times new rooman",15,"bold"), command=bgBlue)
			self.theme.add_separator()
			self.theme.add_command(label="Dark",font=("times new rooman",15,"bold"), command=bgBlack)
			self.theme.add_separator()
			self.theme.add_command(label="Sun", font=("times new rooman",15,"bold"),command=bgYellow)
			self.theme.add_separator()
			self.theme.add_command(label="Green",font=("times new rooman",15,"bold"), command=bgGreen)
			self.theme.add_separator()
			self.theme.add_command(label="Random",font=("times new rooman",15,"bold"), command=randColor)
			self.theme.add_separator()
			self.menubar.add_cascade(label="Themes", menu=self.theme,font=("times new rooman",60,"bold"))


			self.products = Menu(self.menubar, tearoff=0,bg="#272822",fg='white')

			prod1=partial(product_menu,"Wheat")
			prod2=partial(product_menu,"Jawar")
			prod3=partial(product_menu,"Rice")


			self.products.add_command(label="Wheat",font=("times new rooman",15,"bold"), command=prod1)
			self.products.add_separator()
			self.products.add_command(label="Jawar",font=("times new rooman",15,"bold"), command=prod2)
			self.products.add_separator()
			self.products.add_command(label="Rice",font=("times new rooman",15,"bold"), command=prod3)
			self.products.add_separator()
		
			self.menubar.add_cascade(label="Products", menu=self.products,font=("times new rooman",60,"bold"))


			self.root.config(menu=self.menubar)

	#============================================================================ MenuBar  ======================











	#========================================== Frame 2 =======================================================
			self.Sec_Frame=Frame(self.root,bd=10,relief=RIDGE,bg=bn)#"#66D9EF")
			self.Sec_Frame.place(x=520,y=140,width=500,height=660)


	
			"""canvas22 = Canvas(self.Sec_Frame, width = 300, height = 300)      
			canvas22.pack()      
			img22 = PhotoImage(file="store8.png") 	     
			canvas22.create_image(0,0,image=img22)"""



			

			scroll_x=Scrollbar(self.Sec_Frame,orient=HORIZONTAL,bg='red')
			scroll_y=Scrollbar(self.Sec_Frame,orient=VERTICAL,bg='red')
			ttk.Style().configure("Treeview", background="black",fieldbackground="black",foreground="white")
			self.s_table=ttk.Treeview(self.Sec_Frame,columns=("brand","product","day",'month','year','qty','wt'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
			scroll_x.pack(side=BOTTOM,fill=X)
			scroll_y.pack(side=RIGHT,fill=Y)
			scroll_x.config(command=self.s_table.xview)
			scroll_y.config(command=self.s_table.yview)
			self.s_table.heading("brand",text="Brand")
			self.s_table.heading("product",text="Product")
			self.s_table.heading("day",text="Day")
			self.s_table.heading("month",text="Month")
			self.s_table.heading("year",text="Year")
			self.s_table.heading("qty",text="Qty")
			self.s_table.heading("wt",text="Wieght")


			self.s_table['show']='headings'
			self.s_table.column("brand",width="60")
			self.s_table.column("product",width="60")
			self.s_table.column("day",width="60")
			self.s_table.column("month",width="60")
			self.s_table.column("year",width="60")
			self.s_table.column("qty",width="60")
			self.s_table.column("wt",width="60")

			self.s_table.pack()

			

			self.button_Frame=Frame(self.Sec_Frame,bd=10,relief=RIDGE,bg=bn)
			self.button_Frame.place(x=0,y=480,width=470,height=60)




			self.import_export=1
			def Import():
				self.import_export=1
				stop_capt=Button(self.button_Frame,text="Export",width=10,fg="white",font=("times new rooman",15,"bold"),relief=RAISED,bd=2,bg="#272822",command=Export)
				stop_capt.grid(row=0,column=3,columnspan=2,pady=3,sticky="w")
			def Export():
				self.import_export=0
				stop_capt=Button(self.button_Frame,text="Import",width=11,fg="white",font=("times new rooman",15,"bold"),relief=RAISED,bd=2,bg="#272822",command=Import)
				stop_capt.grid(row=0,column=3,columnspan=2,pady=3,sticky="w")



			cap_vid=Button(self.button_Frame,text="►",width=12,fg="white",font=("times new rooman",15,"bold"),relief=RAISED,bd=2,bg="#272822",command=Start_cap)
			cap_vid.grid(row=0,column=1,columnspan=2,padx=3,sticky="w")

			stop_capt=Button(self.button_Frame,text="Import",width=11,fg="white",font=("times new rooman",15,"bold"),relief=RAISED,bd=2,bg="#272822",command=Import)
			stop_capt.grid(row=0,column=3,columnspan=2,padx=3,sticky="w")
			
			show_satus=Button(self.button_Frame,text="Show",width=11,fg="white",font=("times new rooman",15,"bold"),relief=RAISED,bd=2,bg="#272822",command=self.fetch)
			show_satus.grid(row=0,column=6,columnspan=2,padx=3,sticky="w")

			#show_satus=Button(self.button_Frame,text="Show",width=10,fg="white",font=("times new rooman",15,"bold"),relief=RAISED,bd=2,bg="#272822",command=self.fetch)
			#show_satus.grid(row=0,column=6,columnspan=2,pady=3,sticky="w")


	#==========================================Frame 2=======================================================
		


	#==========================================Frame 3========================================================

				
	
			
			self.Third_Frame=Frame(self.root,bd=10,relief=RIDGE,bg=bn)#"#AE81FF")
			self.Third_Frame.place(x=1010,y=100,width=410,height=600)

			self.button_Frame1=Frame(self.Third_Frame,bd=10,relief=RIDGE,bg=bn)
			self.button_Frame1.place(x=0,y=520,width=390,height=60)


			show_satus=Button(self.button_Frame1,text="             ",fg="black",font=("times new rooman",14,"bold"),bg="red",command=self.bar)
				#show.grid(row=8,column=3,columnspan=2,pady=3,sticky="w")
			show_satus.grid(row=0,column=0,padx=12)

			show_satus=Button(self.button_Frame1,text="             ",fg="black",font=("times new rooman",14,"bold"),bg="yellow",command=self.yellow_bar)
				#show.grid(row=8,column=3,columnspan=2,pady=3,sticky="w")
			show_satus.grid(row=0,column=2,padx=12)





			show_satus=Button(self.button_Frame1,text='             ',fg="black",font=("times new rooman",14,"bold"),bg="green",command=self.green_bar)
				#show.grid(row=8,column=3,columnspan=2,pady=3,sticky="w")
			show_satus.grid(row=0,column=3,padx=12)


#=================================Report by Date===========================================

			
			menu_frame=Frame(self.root,bd=10,relief=RIDGE,bg=bn)#"#AE81FF")
			menu_frame.place(x=5,y=150,width=500,height=600)

			def selected_date():

				mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="lakan")
				mycursor = mydb.cursor()
				sql = "SELECT * FROM storekirana2"#brand,product,day,month,year,qty,wt) VALUES (%s, %s, %s, %s, %s, %s, %s)"									
				mycursor.execute(sql)


				selected_month=months.get()

				if days.get()=='Day':
					selected_day='Day'
				else:
					selected_day=int(days.get())
				if years.get()=='Year':
					selected_year='Year'
				else:
					selected_year=int(years.get())
		

				is_monthwise=0
				is_yearwise=0
				is_daywise=0

				if selected_month!='Month':
					is_monthwise=1

				if selected_day!='Day':
					is_daywise=1

				if selected_year!='Year':
					is_yearwise=1



				n_gemini=0
				n_sarkhi=0
				n_sutti=0
				n_dawat=0
				n_joon=0


				n_dimond=0
				n_swastic=0
				n_vasant=0
				n_tini=0
				n_mini=0

				n_mahalaxmi=0
				n_morya=0
				n_twiteer=0
				n_indrayani=0
				n_celebratic=0
				n_olympic=0


				if is_monthwise==1 and is_yearwise==1 and is_daywise==1:
					print("Day wise") 
					for j in mycursor:
						if j[2]==selected_day and j[3]==selected_month and j[4]==selected_year:
							print(j)

							if j[0]=='Dimond':
								n_dimond=j[5]+n_dimond
							if j[0]=='Swastic':
								n_swastic=j[5]+n_swastic
							if j[0]=='Vasant':
								n_vasant=j[5]+n_vasant
							if j[0]=='Tini':
								n_tini=j[5]+n_tini
							if j[0]=='Mini':
								n_mini=j[5]+n_mini
							if j[0]=='Morya':
								n_morya=j[5]+n_morya
							if j[0]=='Twitter':
								n_twiteer=j[5]+n_twiteer
							if j[0]=='Olympic':
								n_olympic=j[5]+n_olympic
							if j[0]=='Indrayani':
								n_indrayani=j[5]+n_indrayani
							if j[0]=='Celebratic':
								n_celebratic=j[5]+n_celebratic
							if j[0]=='Mahalaxmi':
								n_mahalaxmi=j[5]+n_mahalaxmi



					print(" no. of ----:",n_dawat,n_sutti,n_gemini)


		
					fig = plt.figure()
					ax = fig.add_axes([0,0,1,1])
					ax.axis('equal')
					remaining_space=2000-(n_dimond+n_swastic+n_vasant+n_tini+n_mini+n_morya+n_twiteer+n_olympic+n_indrayani+n_celebratic+n_mahalaxmi)
					langs = ['Dimond','Swastic','Vasant','Tini','Mini','Morya',"Twitter",'Olympic','Indrayani','Celebratic','Mahalaxmi','Remaining']
					pd = [n_dimond,n_swastic,n_vasant,n_tini,n_mini,n_morya,n_twiteer,n_olympic,n_indrayani,n_celebratic,n_mahalaxmi,remaining_space]
					ax.pie(pd, labels = langs,autopct='%1.2f%%')
					plt.show()

				#Variable assignment
					total_of_brand1=n_dimond
					total_of_brand2=n_swastic
					total_of_brand3=n_vasant
					total_of_brand4=n_tini
					total_of_brand5=n_mini
					total_of_brand6=n_morya
					total_of_brand7=n_twiteer
					total_of_brand8=n_olympic
					total_of_brand9=n_indrayani
					total_of_brand10=n_celebratic
					total_of_brand11=n_mahalaxmi

					brand1='Dimond:'
					brand2='Swastic:'
					brand3='Vasant:'
					brand4='Tini:'
					brand5='Mini:'
					brand6='Morya:'
					brand7='Twitter:'
					brand8='Olympic:'
					brand9='Indrayani:'
					brand10='Celebratic:'
					brand11='Mahalaxmi:'

					msg = MIMEMultipart() 
					
			
						
					msg1="Todays Report"+" Dimond:"+str(n_dimond)+"Swastic:"+str(n_swastic)
					f = open('D:\\Report.txt','w')
					f.write('Report: NCY KIRANA \n')
					f.write('\nDimond  :  '+str(n_dimond))
					f.write('\nSwastic  :  '+str(n_swastic))
					f.write('\nVasant  :  '+str(n_vasant))
					f.write('\nTini  :  '+str(n_tini))
					f.write('\nMini  :  '+str(n_mini))
					f.write('\nmorya  :  '+str(n_morya))
					f.write('\nTwitter  :  '+str(n_twiteer))
					f.write('\nOlympic  :  '+str(n_olympic))
					f.write('\nCelebratic  :  '+str(n_celebratic))
					f.write('\nMahalaxmi  :  '+str(n_mahalaxmi))
				
					f.close()




					
					fromaddr = "smfcmahidhoni123456@gmail.com"
					toaddr = "swapnildake8@gmail.com"
					   
				
					msg = MIMEMultipart() 
					  
					 
					msg['From'] = fromaddr 
					  
					 
					msg['To'] = toaddr 
					  
					# storing the subject  
					msg['Subject'] = "Todays Report:"
					  
				
					body = "Report :"
					file_location="D:\\Report.txt"
					filename=os.path.basename(file_location)
					  
					
					msg.attach(MIMEText(body, 'plain')) 
					  
				  
					
					attachment = open(file_location, "rb") 
					  
					
					p = MIMEBase('application', 'octet-stream') 
					  
					 
					p.set_payload((attachment).read()) 
				
					encoders.encode_base64(p) 
					   
					p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
					  
					
					msg.attach(p) 
					  
					
					s = smtplib.SMTP('smtp.gmail.com', 587) 
					  
					
					s.starttls() 
					  
					
					s.login(fromaddr, "mahi@1998") 
					  
		 
					text = msg.as_string() 
					  
					
					s.sendmail(fromaddr, toaddr,text) 
					
					s.quit() 





				

				if is_monthwise==1 and is_yearwise==1 and is_daywise==0:
					print("Mont wise")
					for j in mycursor:
						if j[3]==selected_month:
							#print(j)
							if j[0]=='Dimond':
								n_dimond=j[5]+n_dimond
							if j[0]=='Swastic':
								n_swastic=j[5]+n_swastic
							if j[0]=='Vasant':
								n_vasant=j[5]+n_vasant
							if j[0]=='Tini':
								n_tini=j[5]+n_tini
							if j[0]=='Mini':
								n_mini=j[5]+n_mini
							if j[0]=='Morya':
								n_morya=j[5]+n_morya
							if j[0]=='Twitter':
								n_twiteer=j[5]+n_twiteer
							if j[0]=='Olympic':
								n_olympic=j[5]+n_olympic
							if j[0]=='Indrayani':
								n_indrayani=j[5]+n_indrayani
							if j[0]=='Celebratic':
								n_celebratic=j[5]+n_celebratic
							if j[0]=='Mahalaxmi':
								n_mahalaxmi=j[5]+n_mahalaxmi



					total_of_brand1=n_dimond
					total_of_brand2=n_swastic
					total_of_brand3=n_vasant
					total_of_brand4=n_tini
					total_of_brand5=n_mini
					total_of_brand6=n_morya
					total_of_brand7=n_twiteer
					total_of_brand8=n_olympic
					total_of_brand9=n_indrayani
					total_of_brand10=n_celebratic
					total_of_brand11=n_mahalaxmi

					brand1='Dimond:'
					brand2='Swastic:'
					brand3='Vasant:'
					brand4='Tin:'
					brand5='Mini:'
					brand6='Morya:'
					brand7='Twitter:'
					brand8='Olympic:'
					brand9='Indrayani:'
					brand10='Celebratic:'
					brand11='Mahalaxmi:'


				print("Gemini:",n_gemini)
				print("Joon:",n_joon)
				print("Sarkhi:",n_sarkhi)
				print("Sutti:",n_sutti)
				print("Dawat:",n_dawat)		




				width_report_lb=20
				height_report_lb=1
				padx_report_lb=1
				pady_report_lb=2



				if is_monthwise==0 and is_yearwise==1 and is_daywise==0:
					print("year wise")
					#Variable assignment

					for j in mycursor:
						if j[4]==selected_year:
							#print(j)
							if j[0]=='Dimond':
								n_dimond=j[5]+n_dimond
							if j[0]=='Swastic':
								n_swastic=j[5]+n_swastic
							if j[0]=='Vasant':
								n_vasant=j[5]+n_vasant
							if j[0]=='Tini':
								n_tini=j[5]+n_tini
							if j[0]=='Mini':
								n_mini=j[5]+n_mini
							if j[0]=='Morya':
								n_morya=j[5]+n_morya
							if j[0]=='Twitter':
								n_twiteer=j[5]+n_twiteer
							if j[0]=='Olympic':
								n_olympic=j[5]+n_olympic
							if j[0]=='Indrayani':
								n_indrayani=j[5]+n_indrayani
							if j[0]=='Celebratic':
								n_celebratic=j[5]+n_celebratic
							if j[0]=='Mahalaxmi':
								n_mahalaxmi=j[5]+n_mahalaxmi



					total_of_brand1=n_dimond
					total_of_brand2=n_swastic
					total_of_brand3=n_vasant
					total_of_brand4=n_tini
					total_of_brand5=n_mini
					total_of_brand6=n_morya
					total_of_brand7=n_twiteer
					total_of_brand8=n_olympic
					total_of_brand9=n_indrayani
					total_of_brand10=n_celebratic
					total_of_brand11=n_mahalaxmi

					brand1='Dimond:'
					brand2='Swastic:'
					brand3='Vasant:'
					brand4='Tin:'
					brand5='Mini:'
					brand6='Morya:'
					brand7='Twitter:'
					brand8='Olympic:'
					brand9='Indrayani:'
					brand10='Celebratic:'
					brand11='Mahalaxmi:'



				if  is_daywise==1  and is_monthwise==0 and is_yearwise==0:
					mb.showinfo("Error","Choose Correct Date")
					#Variable assignment
					total_of_brand1=n_gemini
					total_of_brand2=n_sarkhi
					total_of_brand3=n_sutti
					total_of_brand4=n_dawat
					total_of_brand5=n_joon

					brand1='Gemini:'
					brand2='Joon:'
					brand3='Sarkhi:'
					brand4='Sutti:'
					brand5='Dawat'

				if  is_daywise==1  and is_monthwise==1 and is_yearwise==0:
					mb.showinfo("Error","Choose Correct Date")
					#Variable assignment
					total_of_brand1=n_gemini
					total_of_brand2=n_sarkhi
					total_of_brand3=n_sutti
					total_of_brand4=n_dawat
					total_of_brand5=n_joon

					brand1='Gemini:'
					brand2='Joon:'
					brand3='Sarkhi:'
					brand4='Sutti:'
					brand5='Dawat'

				if  is_daywise==1  and is_monthwise==0 and is_yearwise==1:
					mb.showinfo("Error","Choose Correct Date")
					#Variable assignment
					total_of_brand1=n_gemini
					total_of_brand2=n_sarkhi
					total_of_brand3=n_sutti
					total_of_brand4=n_dawat
					total_of_brand5=n_joon

					brand1='Gemini:'
					brand2='Joon:'
					brand3='Sarkhi:'
					brand4='Sutti:'
					brand5='Dawat'

				if  is_daywise==0  and is_monthwise==1 and is_yearwise==0:
					mb.showinfo("Error","Choose Correct Date")
					#Variable assignment
					total_of_brand1=n_gemini
					total_of_brand2=n_sarkhi
					total_of_brand3=n_sutti
					total_of_brand4=n_dawat
					total_of_brand5=n_joon

					brand1='Gemini:'
					brand2='Joon:'
					brand3='Sarkhi:'
					brand4='Sutti:'
					brand5='Dawat'


				l1=Label(menu_frame,text=brand1,width=width_report_lb,height=height_report_lb,)
				l1.grid(row=3,column=1,padx=padx_report_lb,pady=pady_report_lb)	
				l1=Label(menu_frame,text=total_of_brand1,width=width_report_lb,height=height_report_lb,)
				l1.grid(row=3,column=2,padx=padx_report_lb,pady=pady_report_lb)	

				l1=Label(menu_frame,text=brand2,width=width_report_lb,height=height_report_lb,)
				l1.grid(row=4,column=1,padx=padx_report_lb,pady=pady_report_lb)	
				l1=Label(menu_frame,text=total_of_brand2,width=width_report_lb,height=height_report_lb,)
				l1.grid(row=4,column=2,padx=padx_report_lb,pady=pady_report_lb)	


				l1=Label(menu_frame,text=brand3,width=width_report_lb,height=height_report_lb,)
				l1.grid(row=5,column=1,padx=padx_report_lb,pady=pady_report_lb)	
				l1=Label(menu_frame,text=total_of_brand3,width=width_report_lb,height=height_report_lb,)
				l1.grid(row=5,column=2,padx=padx_report_lb,pady=pady_report_lb)	


				l1=Label(menu_frame,text=brand4,width=width_report_lb,height=height_report_lb,)
				l1.grid(row=6,column=1,padx=padx_report_lb,pady=pady_report_lb)	
				l1=Label(menu_frame,text=total_of_brand4,width=width_report_lb,height=height_report_lb,)
				l1.grid(row=6,column=2,padx=padx_report_lb,pady=pady_report_lb)	

				l1=Label(menu_frame,text=brand5,width=width_report_lb,height=height_report_lb,)
				l1.grid(row=7,column=1,padx=padx_report_lb,pady=pady_report_lb)	
				l1=Label(menu_frame,text=total_of_brand5,width=width_report_lb,height=height_report_lb,)
				l1.grid(row=7,column=2,padx=padx_report_lb,pady=pady_report_lb)	

				l1=Label(menu_frame,text=brand6,width=width_report_lb,height=height_report_lb,)
				l1.grid(row=8,column=1,padx=padx_report_lb,pady=pady_report_lb)	
				l1=Label(menu_frame,text=total_of_brand6,width=width_report_lb,height=height_report_lb,)
				l1.grid(row=8,column=2,padx=padx_report_lb,pady=pady_report_lb)	

				l1=Label(menu_frame,text=brand7,width=width_report_lb,height=height_report_lb,)
				l1.grid(row=9,column=1,padx=padx_report_lb,pady=pady_report_lb)	
				l1=Label(menu_frame,text=total_of_brand7,width=width_report_lb,height=height_report_lb,)
				l1.grid(row=9,column=2,padx=padx_report_lb,pady=pady_report_lb)	

				l1=Label(menu_frame,text=brand8,width=width_report_lb,height=height_report_lb,)
				l1.grid(row=10,column=1,padx=padx_report_lb,pady=pady_report_lb)	
				l1=Label(menu_frame,text=total_of_brand8,width=width_report_lb,height=height_report_lb,)
				l1.grid(row=10,column=2,padx=padx_report_lb,pady=pady_report_lb)

				l1=Label(menu_frame,text=brand9,width=width_report_lb,height=height_report_lb,)
				l1.grid(row=11,column=1,padx=padx_report_lb,pady=pady_report_lb)	
				l1=Label(menu_frame,text=total_of_brand9,width=width_report_lb,height=height_report_lb,)
				l1.grid(row=11,column=2,padx=padx_report_lb,pady=pady_report_lb)	

				l1=Label(menu_frame,text=brand10,width=width_report_lb,height=height_report_lb,)
				l1.grid(row=12,column=1,padx=padx_report_lb,pady=pady_report_lb)	
				l1=Label(menu_frame,text=total_of_brand10,width=width_report_lb,height=height_report_lb,)
				l1.grid(row=12,column=2,padx=padx_report_lb,pady=pady_report_lb)	

				l1=Label(menu_frame,text=brand11,width=width_report_lb,height=height_report_lb,)
				l1.grid(row=13,column=1,padx=padx_report_lb,pady=pady_report_lb)	
				l1=Label(menu_frame,text=total_of_brand11,width=width_report_lb,height=height_report_lb,)
				l1.grid(row=13,column=2,padx=padx_report_lb,pady=pady_report_lb)	






			width_for_combobox=15
			height_for_combobox=20
			padx_for_combobox=10

			months = tk.StringVar() 
			monthchoosen = ttk.Combobox(menu_frame, width =width_for_combobox , height=height_for_combobox, textvariable = months) 
  
			# Adding combobox drop down list 
			monthchoosen['values'] = ('Month','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep', 
                          'Oct','Nov','Dec') 
  
			monthchoosen.grid(column = 2, row = 1, padx=padx_for_combobox) 
			monthchoosen.current(0)

			days = tk.StringVar() 
			daychoosen = ttk.Combobox(menu_frame, width = width_for_combobox, height=height_for_combobox , textvariable = days) 
  
			# Adding combobox drop down list for days
			daychoosen['values'] = ('Day','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17',
				'18','19','20','21','22','23','24','25','26','27','28','29','30','31')
  
			daychoosen.grid(column = 1, row = 1,padx=padx_for_combobox) 
			daychoosen.current(0)

			years = tk.StringVar() 
			daychoosen = ttk.Combobox(menu_frame, width = width_for_combobox, height=height_for_combobox , textvariable = years) 
  
			# Adding combobox drop down list for years
			daychoosen['values'] = ('Year','2016','2017','2018','2019','2020')
  
			daychoosen.grid(column = 3, row = 1,padx=padx_for_combobox) 
			daychoosen.current(0)
			def Clear():
				rf=Frame(menu_frame,bg=bn).place(x=0,y=60,width=470,height=520)

			button=Button(menu_frame,text="Generate Report",command=selected_date,width=20).grid(column=1,row=2,padx=10,pady=10)
			button=Button(menu_frame,text="Clear",command=Clear,width=20).grid(column=2,row=2,padx=10,pady=10)
			
			#l=Label(rf,text='This is Report Frame').pack(side=BOTTOM,fill=BOTH, expand=1)
	#==========================================Report By Date    =========================================================
			
			

			
			

			#self.p=50
	def bar(self): 

		#self.progress_f1=Frame(self.Third_Frame,bg=red).place(x=0,y=0,width=50,height=500)
		"""
		if self.p<70:
			basmati=Label(self.Third_Frame,text="Basmati:",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			basmati.grid()#row=1,columnspan=2,pady=3,sticky="w")
					
			self.progress=Progressbar(self.Third_Frame, orient = HORIZONTAL, length = 200, mode = 'determinate')
			self.progress.grid()#row=1,column=2,columnspan=2,pady=3)
			self.progress['value'] = self.p

		if self.p1<70:
			gimini=Label(self.Third_Frame,text="Gimini",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			gimini.grid()#row=2,columnspan=2,pady=3,sticky="w")
				
			self.progress1=Progressbar(self.Third_Frame, orient = HORIZONTAL, length = 200, mode = 'determinate') 
			self.progress1.grid()#row=2,column=2,columnspan=2,pady=3)
			self.progress['value'] = self.p1

		if self.p2<70:
			quinoa=Label(self.Third_Frame,text="QUINOA",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			quinoa.grid()#row=3,columnspan=2,pady=3,sticky="w")
				
			self.progress2=Progressbar(self.Third_Frame, orient = HORIZONTAL, length = 200, mode = 'determinate') 
			self.progress2.grid()#row=3,column=2,columnspan=2,pady=3)			
			self.progress['value'] = self.p2
		
		if self.p3<70:

			indiana=Label(self.Third_Frame,text="Indiana:",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			indiana.grid()#row=4,columnspan=2,pady=3,sticky="w")
			
				
			self.progress3=Progressbar(self.Third_Frame, orient = HORIZONTAL, length = 200, mode = 'determinate') 
			self.progress3.grid()#row=4,column=2,columnspan=2,pady=3)
			self.progress['value'] = self.p3

		if self.p4<70:
			nutrillet=Label(self.Third_Frame,text="Nutrillet:",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			nutrillet.grid()#row=5,columnspan=2,pady=3,sticky="w")
					
			self.progress4=Progressbar(self.Third_Frame, orient = HORIZONTAL, length = 200, mode = 'determinate') 
			self.progress4.grid()#row=5,column=2,columnspan=2,pady=3)
			self.progress['value'] = self.p4

		if self.p5<70:
			nago=Label(self.Third_Frame,text="Nago:",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			nago.grid()#row=6,columnspan=2,pady=3,sticky="w")
					
			self.progress5=Progressbar(self.Third_Frame, orient = HORIZONTAL, length = 200, mode = 'determinate') 
			self.progress5.grid()#row=6,column=2,columnspan=2,pady=3)
			self.progress['value'] = self.p5

		if self.p6<70:

			ramajeyam=Label(self.Third_Frame,text="Ramajeyam:",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
					
			self.progress6=Progressbar(self.Third_Frame, orient = HORIZONTAL, length = 200, mode = 'determinate') 
			self.progress6.grid()#row=7,column=2,columnspan=2,pady=3)
			self.progress['value'] = self.p6

		if self.p7<70:

			rajaram=Label(self.Third_Frame,text="Rajaram:",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			rajaram.grid()#row=8,columnspan=2,pady=3,sticky="w")
					
			self.progress7=Progressbar(self.Third_Frame, orient = HORIZONTAL, length = 200, mode = 'determinate') 
			self.progress7.grid()#row=8,column=2,columnspan=2,pady=3)
			self.progress['value'] = self.p7

		if self.p8<70:

			sakhi=Label(self.Third_Frame,text="Sakhi:",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			sakhi.grid()#row=9,columnspan=2,pady=3,sticky="w")
					
			self.progress8=Progressbar(self.Third_Frame, orient = HORIZONTAL, length = 200, mode = 'determinate') 
			self.progress8.grid()#row=9,column=2,columnspan=2,pady=3)
			self.progress['value'] = self.p8

		if self.p9<70:

			zonee=Label(self.Third_Frame,text="Zonee:",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			zonee.grid()#row=10,columnspan=2,pady=3,sticky="w")
					
			self.progress9=Progressbar(self.Third_Frame, orient = HORIZONTAL, length = 200, mode = 'determinate') 
			self.progress9.grid()#row=10,column=2,columnspan=2,pady=3)
			self.progress['value'] = self.p9

		if self.p10<70:

			nirma=Label(self.Third_Frame,text="Nirma:",fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			nirma.grid()#row=11,columnspan=2,pady=3,sticky="w")
				
				
			self.progress10=Progressbar(self.Third_Frame, orient = HORIZONTAL, length = 200, mode = 'determinate') 
			self.progress10.grid()#row=11,column=2,columnspan=2,pady=3)
			self.progress['value'] = self.p10
		"""


		wheat_brand1=['Morya','Celebration','Twitter','Olympic']
		wheat_brand2=['Mahalaxmi','Dimond','Swastic','Vasant']
		wheat_brand3=['Tini','Mini','Indrayani','Basmati']
		

		self.red_frame=Frame(self.Third_Frame,bd=10,bg='#353535')#"#AE81FF")
		self.red_frame.place(x=0,y=0,width=195,height=520)

		self.red_frame1=Frame(self.Third_Frame,bd=10,bg='#353535')#"#AE81FF")
		self.red_frame1.place(x=195,y=0,width=195,height=520)

		title_for_zone=Label(self.red_frame,text='   ',fg="white",font=("times new rooman",15,"bold"),bg="red").grid()
		title_for_zone=Label(self.red_frame1,text='   ',fg="white",font=("times new rooman",15,"bold"),bg="red").grid()
		if self.p<30:
			basmati=Label(self.red_frame,text=wheat_brand1[0],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			basmati.grid()#row=1,columnspan=2,pady=3,sticky="w")
			ramajeyam=Label(self.red_frame1,text=self.p,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
					
			

		if self.p1<30:
			gimini=Label(self.red_frame,text=wheat_brand1[1],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			gimini.grid()#row=2,columnspan=2,pady=3,sticky="w")
			ramajeyam=Label(self.red_frame1,text=self.p1,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
				
			
		if self.p2<30:
			quinoa=Label(self.red_frame,text=wheat_brand1[2],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			quinoa.grid()#row=3,columnspan=2,pady=3,sticky="w")
			ramajeyam=Label(self.red_frame1,text=self.p2,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
				
			
		if self.p3<30:

			indiana=Label(self.red_frame,text=wheat_brand1[3],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			indiana.grid()#row=4,columnspan=2,pady=3,sticky="w")
			ramajeyam=Label(self.red_frame1,text=self.p3,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
			
				

		if self.p4<30:
			nutrillet=Label(self.red_frame,text=wheat_brand2[0],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			nutrillet.grid()#row=5,columnspan=2,pady=3,sticky="w")
			ramajeyam=Label(self.red_frame1,text=self.p4,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
					
			

		if self.p5<30:
			nago=Label(self.red_frame,text=wheat_brand2[1],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			nago.grid()#row=6,columnspan=2,pady=3,sticky="w")
			ramajeyam=Label(self.red_frame1,text=self.p5,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
					
			

		if self.p6<30:

			ramajeyam=Label(self.red_frame,text=wheat_brand2[2],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
			ramajeyam=Label(self.red_frame1,text=self.p6,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
		
		if self.p7<30:

			rajaram=Label(self.red_frame,text=wheat_brand2[3],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			rajaram.grid()#row=8,columnspan=2,pady=3,sticky="w")
			rajaram=Label(self.red_frame1,text=self.p7,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			rajaram.grid()#row=8,columnspan=2,pady=3,sticky="w")
					
					
		
		if self.p8<30:

			sakhi=Label(self.red_frame,text=wheat_brand3[0],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			sakhi.grid()#row=9,columnspan=2,pady=3,sticky="w")
			sakhi=Label(self.red_frame1,text=self.p8,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			sakhi.grid()#row=9,columnspan=2,pady=3,sticky="w")

		if self.p9<30:

			zonee=Label(self.red_frame,text=wheat_brand3[1],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			zonee.grid()#row=10,columnspan=2,pady=3,sticky="w")
			zonee=Label(self.red_frame1,text=self.p9,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			zonee.grid()#row=10,columnspan=2,pady=3,sticky="w")
		
		
		if self.p10<30:

			nirma=Label(self.red_frame,text=wheat_brand3[2],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			nirma.grid()#row=11,columnspan=2,pady=3,sticky="w")

			nirma=Label(self.red_frame1,text=self.p10,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			nirma.grid()#row=11,columnspan=2,pady=3,sticky="w")
			
		if self.p11<30:

			nirma=Label(self.red_frame,text=wheat_brand3[3],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			nirma.grid()#row=11,columnspan=2,pady=3,sticky="w")

			nirma=Label(self.red_frame1,text=self.p11,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			nirma.grid()#row=11,columnspan=2,pady=3,sticky="w")
			

	def yellow_bar(self):

		wheat_brand1=['Morya','Celebration','Twitter','Olympic']
		wheat_brand2=['Mahalaxmi','Dimond','Swastic','Vasant']
		wheat_brand3=['Tini','Mini','Indrayani','Basmati']

		self.yellow_frame=Frame(self.Third_Frame,bd=10,bg='#353535')#"#AE81FF")
		self.yellow_frame.place(x=0,y=0,width=195,height=520)

		self.yellow_frame1=Frame(self.Third_Frame,bd=10,bg='#353535')#"#AE81FF")
		self.yellow_frame1.place(x=195,y=0,width=195,height=520)


		title_for_zone=Label(self.yellow_frame,text='   ',fg="white",font=("times new rooman",15,"bold"),bg="yellow").grid()
		title_for_zone=Label(self.yellow_frame1,text='   ',fg="white",font=("times new rooman",15,"bold"),bg="yellow").grid()
		if self.p<70 and self.p>31:
			basmati=Label(self.yellow_frame,text=wheat_brand1[0],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			basmati.grid()#row=1,columnspan=2,pady=3,sticky="w")
			ramajeyam=Label(self.yellow_frame1,text=self.p,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
					
			

		if self.p1<70 and self.p1>31:
			gimini=Label(self.yellow_frame,text=wheat_brand1[1],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			gimini.grid()#row=2,columnspan=2,pady=3,sticky="w")
			ramajeyam=Label(self.yellow_frame1,text=self.p1,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
				
			
		if self.p2<70 and self.p2>31:
			quinoa=Label(self.yellow_frame,text=wheat_brand1[2],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			quinoa.grid()#row=3,columnspan=2,pady=3,sticky="w")
			ramajeyam=Label(self.yellow_frame1,text=self.p2,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
				
			
		if self.p3<70 and self.p3>31:

			indiana=Label(self.yellow_frame,text=wheat_brand1[3],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			indiana.grid()#row=4,columnspan=2,pady=3,sticky="w")
			ramajeyam=Label(self.yellow_frame1,text=self.p3,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
			
				

		if self.p4<70 and self.p4>31:
			nutrillet=Label(self.yellow_frame,text=wheat_brand2[0],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			nutrillet.grid()#row=5,columnspan=2,pady=3,sticky="w")
			ramajeyam=Label(self.yellow_frame1,text=self.p4,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
					
			

		if self.p5<70 and self.p5>31:
			nago=Label(self.yellow_frame,text=wheat_brand2[1],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			nago.grid()#row=6,columnspan=2,pady=3,sticky="w")
			ramajeyam=Label(self.yellow_frame1,text=self.p5,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
					
			

		if self.p6<70 and self.p6>31:

			ramajeyam=Label(self.yellow_frame,text=wheat_brand2[2],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
			ramajeyam=Label(self.yellow_frame1,text=self.p6,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
		
		if self.p7<70 and self.p7>31:

			rajaram=Label(self.yellow_frame,text=wheat_brand2[3],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			rajaram.grid()#row=8,columnspan=2,pady=3,sticky="w")
			rajaram=Label(self.yellow_frame1,text=self.p7,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			rajaram.grid()#row=8,columnspan=2,pady=3,sticky="w")
					
					
		
		if self.p8<70 and self.p8>31:

			sakhi=Label(self.yellow_frame,text=wheat_brand3[0],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			sakhi.grid()#row=9,columnspan=2,pady=3,sticky="w")
			sakhi=Label(self.yellow_frame1,text=self.p8,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			sakhi.grid()#row=9,columnspan=2,pady=3,sticky="w")

		if self.p9<70 and self.p9>31:

			zonee=Label(self.yellow_frame,text=wheat_brand3[1],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			zonee.grid()#row=10,columnspan=2,pady=3,sticky="w")
			zonee=Label(self.yellow_frame1,text=self.p9,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			zonee.grid()#row=10,columnspan=2,pady=3,sticky="w")
		
		
		if self.p10<70 and self.p10>31:

			nirma=Label(self.yellow_frame,text=wheat_brand3[2],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			nirma.grid()#row=11,columnspan=2,pady=3,sticky="w")

			nirma=Label(self.yellow_frame1,text=self.p10,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			nirma.grid()#row=11,columnspan=2,pady=3,sticky="w")

		if self.p11<70 and self.p11>31:

			nirma=Label(self.yellow_frame,text=wheat_brand3[3],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			nirma.grid()#row=11,columnspan=2,pady=3,sticky="w")

			nirma=Label(self.yellow_frame1,text=self.p11,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			nirma.grid()#row=11,columnspan=2,pady=3,sticky="w")

	def green_bar(self):

		wheat_brand1=['Morya','Celebration','Twitter','Olympic']
		wheat_brand2=['Mahalaxmi','Dimond','Swastic','Vasant']
		wheat_brand3=['Tini','Mini','Indrayani','Basmati']

		self.green_frame=Frame(self.Third_Frame,bd=10,bg='#353535')#"#AE81FF")
		self.green_frame.place(x=0,y=0,width=195,height=520)

		self.green_frame1=Frame(self.Third_Frame,bd=10,bg='#353535')#"#AE81FF")
		self.green_frame1.place(x=195,y=0,width=195,height=520)

		title_for_zone=Label(self.green_frame,text='   ',fg="white",font=("times new rooman",15,"bold"),bg="green").grid()
		title_for_zone=Label(self.green_frame1,text='   ',fg="white",font=("times new rooman",15,"bold"),bg="green").grid()
		if self.p<100 and self.p>71:
			basmati=Label(self.green_frame,text=wheat_brand1[0],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			basmati.grid()#row=1,columnspan=2,pady=3,sticky="w")
			ramajeyam=Label(self.green_frame1,text=self.p,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
					
			

		if self.p1<100 and self.p1>71:
			gimini=Label(self.green_frame,text=wheat_brand1[1],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			gimini.grid()#row=2,columnspan=2,pady=3,sticky="w")
			ramajeyam=Label(self.green_frame1,text=self.p1,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
				
			
		if self.p2<100 and self.p2>71:
			quinoa=Label(self.green_frame,text=wheat_brand1[2],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			quinoa.grid()#row=3,columnspan=2,pady=3,sticky="w")
			ramajeyam=Label(self.green_frame1,text=self.p2,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
				
			
		if self.p3<100 and self.p3>71:

			indiana=Label(self.green_frame,text=wheat_brand1[3],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			indiana.grid()#row=4,columnspan=2,pady=3,sticky="w")
			ramajeyam=Label(self.green_frame1,text=self.p3,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
			
				

		if self.p4<100 and self.p4>71:
			nutrillet=Label(self.green_frame,text=wheat_brand2[0],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			nutrillet.grid()#row=5,columnspan=2,pady=3,sticky="w")
			ramajeyam=Label(self.green_frame1,text=self.p4,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
					
			

		if self.p5<100 and self.p5>71:
			nago=Label(self.green_frame,text=wheat_brand2[1],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			nago.grid()#row=6,columnspan=2,pady=3,sticky="w")
			ramajeyam=Label(self.green_frame1,text=self.p5,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
					
			

		if self.p6<100 and self.p6>71:

			ramajeyam=Label(self.green_frame,text=wheat_brand2[2],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
			ramajeyam=Label(self.green_frame1,text=self.p6,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			ramajeyam.grid()#row=7,columnspan=2,pady=3,sticky="w")
		
		if self.p7<100 and self.p7>71:

			rajaram=Label(self.green_frame,text=wheat_brand2[3],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			rajaram.grid()#row=8,columnspan=2,pady=3,sticky="w")
			rajaram=Label(self.green_frame1,text=self.p7,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			rajaram.grid()#row=8,columnspan=2,pady=3,sticky="w")
					
					
		
		if self.p8<100 and self.p8>71:

			sakhi=Label(self.green_frame,text=wheat_brand3[0],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			sakhi.grid()#row=9,columnspan=2,pady=3,sticky="w")
			sakhi=Label(self.green_frame1,text=self.p8,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			sakhi.grid()#row=9,columnspan=2,pady=3,sticky="w")

		if self.p9<100 and self.p9>71:

			zonee=Label(self.green_frame,text=wheat_brand3[1],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			zonee.grid()#row=10,columnspan=2,pady=3,sticky="w")
			zonee=Label(self.green_frame1,text=self.p9,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			zonee.grid()#row=10,columnspan=2,pady=3,sticky="w")
		
		
		if self.p10<100 and self.p10>71:

			nirma=Label(self.green_frame,text=wheat_brand3[2],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			nirma.grid()#row=11,columnspan=2,pady=3,sticky="w")

			nirma=Label(self.green_frame1,text=self.p10,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			nirma.grid()#row=11,columnspan=2,pady=3,sticky="w")

		if self.p11<100 and self.p11>71:

			nirma=Label(self.green_frame,text=wheat_brand3[3],fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			nirma.grid()#row=11,columnspan=2,pady=3,sticky="w")

			nirma=Label(self.green_frame1,text=self.p11,fg="white",font=("times new rooman",15,"bold"),bg="#272822")
			nirma.grid()#row=11,columnspan=2,pady=3,sticky="w")


		
		
		

		
	def fetch(self):
		mydb=mysql.connector.connect(host="localhost",database="lakan",user="root",passwd="")
		mycurser=mydb.cursor()

		mycurser.execute("select * from storekirana2")
		rows=mycurser.fetchall()
		if len(rows)!=0:
			self.s_table.delete(*self.s_table.get_children())
			self.p=0
			for row in rows:
				self.p+=1
				self.s_table.insert('',END,values=row)
				print(self.p)
			mydb.commit()
		mydb.close()
		


root=Tk()
bacground=Window(root)	
ob=Dake(root)


root.mainloop()




