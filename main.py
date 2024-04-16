import csv
import time
import tkinter as tk
from tkinter import END, RIGHT, Button, Frame, PhotoImage, Scrollbar, StringVar, Text, messagebox
from tkinter import scrolledtext
from tkinter.filedialog import askopenfilename

# from Tkinter import *
import os
import phonenumbers
from phonenumbers import carrier, timezone, geocoder
from phonenumbers.phonenumberutil import number_type
import requests
import random
import codecs
import argparse
import random
import json
from csv import writer

import random

is_otp_send = False
line_at_which_error_occured = 0

def validation():
    # print(is_otp_send)
    # is_otp_send = ""
    # is_otp_send = False
    global is_otp_send  
    # if is_otp_send == True:
        
    #     is_otp_send = False
    #     print(is_otp_send)   
    number =entry1.get()
    print(is_otp_send)
    
    msg = ''

    if len(number) == 0:
        msg = 'Number can\'t be empty'
    else:
        try:
            if any(ch.isalpha() for ch in number):
                msg = 'Number can\'t have characters'
                entry1.config(state="disabled")
            elif len(number) < 10:
                msg = 'Number is too short.'
                entry2.config(state="disabled")
                
            elif len(number) > 13:
                msg = 'number is too long.'
                entry2.config(state="disabled")
            elif(is_otp_send ==  False):
                is_otp_send = True
                print(is_otp_send)
                msg =" otp send on your mobile number"
                # entry1.config(state="disabled")
                entry2.config(state= "normal")
                button1.config(text="SUBMIT")
                # 
                #  here i will add code to send otp 
                
                def getNumber(x):
                    
                    if x[0] == "0":
                        return x[1:].replace(" ", "")
                    else:
                        return x.replace(" ", "")
        
                def truecallerpy_get_random_phone():
                    
                    data = [
                        {
                            "manufacturer": "Xiaomi",
                            "model": "M2010J19SG"
                        },
                        {
                            "manufacturer": "Xiaomi",
                            "model": "POCO F1"
                        },
                        {
                            "manufacturer": "Xiaomi",
                            "model": "Redmi 9A"
                        },
                        {
                            "manufacturer": "Xiaomi",
                            "model": "Xiaomi Mi 4"
                        },
                        {
                            "manufacturer": "Xiaomi",
                            "model": "Redmi Note 10 pro"
                        },
                        {
                            "manufacturer": "Xiaomi",
                            "model": "Redmi Note 10"
                        },
                        {
                            "manufacturer": "Xiaomi",
                            "model": "Xiaomi Redmi 1S"
                        },
                        {
                            "manufacturer": "Xiaomi",
                            "model": "Xiaomi Mi 10T"
                        },
                        {
                            "manufacturer": "Xiaomi",
                            "model": "Xiaomi Redmi 6 Pro"
                        },
                        {
                            "manufacturer": "Xiaomi",
                            "model": "Xiaomi Redmi Y3"
                        },
                        {
                            "manufacturer": "Xiaomi",
                            "model": "Xiaomi Redmi 9 Prime"
                        },
                        {
                            "manufacturer": "Xiaomi",
                            "model": "Redmi Note 7"
                        },
                        {
                            "manufacturer": "Vivo",
                            "model": "Vivo Y33s"
                        },
                        {
                            "manufacturer": "Vivo",
                            "model": "Vivo V21 5G"
                        },
                        {
                            "manufacturer": "Vivo",
                            "model": "Vivo Y20T"
                        },
                        {
                            "manufacturer": "Vivo",
                            "model": "Vivo Y73 2021"
                        },
                        {
                            "manufacturer": "Vivo",
                            "model": "Vivo X60"
                        },
                        {
                            "manufacturer": "Vivo",
                            "model": "Vivo X70 Pro 5G"
                        },
                        {
                            "manufacturer": "Vivo",
                            "model": "Vivo U3x"
                        },
                        {
                            "manufacturer": "Vivo",
                            "model": "Vivo V20 Pro"
                        },
                        {
                            "manufacturer": "Vivo",
                            "model": "Vivo Y21 2021"
                        },
                        {
                            "manufacturer": "Vivo",
                            "model": "Vivo Y53s"
                        },
                        {
                            "manufacturer": "Vivo",
                            "model": "Vivo S12 Pro"
                        },
                        {
                            "manufacturer": "Vivo",
                            "model": "Vivo V21e 5G"
                        },
                        {
                            "manufacturer": "OnePlus",
                            "model": "OnePlus Nord CE 5G"
                        },
                        {
                            "manufacturer": "OnePlus",
                            "model": "OnePlus 9 Pro"
                        },
                        {
                            "manufacturer": "OnePlus",
                            "model": "OnePlus 8T"
                        },
                        {
                            "manufacturer": "OnePlus",
                            "model": "OnePlus 9"
                        },
                        {
                            "manufacturer": "OnePlus",
                            "model": "OnePlus 7T"
                        },
                        {
                            "manufacturer": "OnePlus",
                            "model": "OnePlus 6T"
                        },
                        {
                            "manufacturer": "OnePlus",
                            "model": "OnePlus Nord 2"
                        },
                        {
                            "manufacturer": "OnePlus",
                            "model": "OnePlus 7 Pro"
                        },
                        {
                            "manufacturer": "OnePlus",
                            "model": "OnePlus Nord"
                        },
                        {
                            "manufacturer": "Realme",
                            "model": "RMX2185"
                        },
                        {
                            "manufacturer": "Realme",
                            "model": "Realme GT Neo2 5G"
                        },
                        {
                            "manufacturer": "Realme",
                            "model": "Realme 8 5G"
                        },
                        {
                            "manufacturer": "Realme",
                            "model": "Realme C11 2021"
                        },
                        {
                            "manufacturer": "Realme",
                            "model": "Realme GT"
                        },
                        {
                            "manufacturer": "Realme",
                            "model": "Realme Narzo 30"
                        },
                        {
                            "manufacturer": "Realme",
                            "model": "Realme Q3i 5G"
                        },
                        {
                            "manufacturer": "Realme",
                            "model": "Realme 8s 5G"
                        },
                        {
                            "manufacturer": "Realme",
                            "model": "Realme 8i"
                        },
                        {
                            "manufacturer": "Realme",
                            "model": "Realme Narzo 50A"
                        },
                        {
                            "manufacturer": "Realme",
                            "model": "Realme C21Y"
                        },
                        {
                            "manufacturer": "Oppo",
                            "model": "OPPO A55"
                        },
                        {
                            "manufacturer": "Oppo",
                            "model": "OPPO A74 5G"
                        },
                        {
                            "manufacturer": "Oppo",
                            "model": "OPPO A53"
                        },
                        {
                            "manufacturer": "Oppo",
                            "model": "OPPO A31"
                        },
                        {
                            "manufacturer": "Oppo",
                            "model": "OPPO A12"
                        },
                        {
                            "manufacturer": "Oppo",
                            "model": "OPPO Reno6 Pro"
                        },
                        {
                            "manufacturer": "Oppo",
                            "model": "OPPO Reno6"
                        },
                        {
                            "manufacturer": "Oppo",
                            "model": "OPPO F19 Pro"
                        },
                        {
                            "manufacturer": "Oppo",
                            "model": "OPPO F19s"
                        },
                        {
                            "manufacturer": "Oppo",
                            "model": "Oppo F19 Pro+"
                        },
                        {
                            "manufacturer": "Oppo",
                            "model": "Oppo A33"
                        },
                        {
                            "manufacturer": "Oppo",
                            "model": "Oppo Reno 3 Pro"
                        },
                        {
                            "manufacturer": "Oppo",
                            "model": "Oppo Reno 4 Pro"
                        },
                        {
                            "manufacturer": "Oppo",
                            "model": "Oppo Find X2"
                        },
                        {
                            "manufacturer": "Oppo",
                            "model": "OPPO F15"
                        },
                        {
                            "manufacturer": "Oppo",
                            "model": "OPPO Reno 2F"
                        },
                        {
                            "manufacturer": "Oppo",
                            "model": "OPPO K3"
                        },
                        {
                            "manufacturer": "Oppo",
                            "model": "OPPO A9"
                        },
                        {
                            "manufacturer": "Oppo",
                            "model": "OPPO A1k"
                        },
                        {
                            "manufacturer": "Oppo",
                            "model": "OPPO A5s"
                        },
                        {
                            "manufacturer": "Samsung",
                            "model": "Samsung Galaxy M31s"
                        },
                        {
                            "manufacturer": "Samsung",
                            "model": "Samsung Galaxy M32"
                        },
                        {
                            "manufacturer": "Samsung",
                            "model": "Samsung Galaxy F62"
                        },
                        {
                            "manufacturer": "Samsung",
                            "model": "Samsung Galaxy M52 5G"
                        },
                        {
                            "manufacturer": "Samsung",
                            "model": "Samsung Galaxy M12"
                        },
                        {
                            "manufacturer": "Samsung",
                            "model": "Samsung Galaxy M51"
                        },
                        {
                            "manufacturer": "Samsung",
                            "model": "Samsung Galaxy F12"
                        },
                        {
                            "manufacturer": "Samsung",
                            "model": "Samsung Galaxy F22"
                        },
                        {
                            "manufacturer": "Samsung",
                            "model": "Samsung Galaxy A52"
                        },
                        {
                            "manufacturer": "Samsung",
                            "model": "Samsung Galaxy S20 FE 5G"
                        },
                        {
                            "manufacturer": "Samsung",
                            "model": "Samsung Galaxy M52"
                        },
                        {
                            "manufacturer": "Samsung",
                            "model": "Samsung Galaxy M62"
                        },
                        {
                            "manufacturer": "Samsung",
                            "model": "Samsung Galaxy S21 Ultra"
                        },
                        {
                            "manufacturer": "Samsung",
                            "model": "Samsung Galaxy A52s 5G"
                        },
                        {
                            "manufacturer": "Samsung",
                            "model": "Samsung Galaxy S21"
                        },
                        {
                            "manufacturer": "Samsung",
                            "model": "Samsung Galaxy M21 2021"
                        },
                        {
                            "manufacturer": "Samsung",
                            "model": "Samsung Galaxy F42"
                        },
                        {
                            "manufacturer": "Samsung",
                            "model": "Samsung Galaxy A12"
                        },
                        {
                            "manufacturer": "Samsung",
                            "model": "Samsung Galaxy F41"
                        },
                        {
                            "manufacturer": "Samsung",
                            "model": "Samsung Galaxy M01 Core"
                        }
                    ]

                    return data[random.randint(0, len(data) - 1)]
                xx = truecallerpy_get_random_phone()
                print(xx)
                global request_data
                global phoneNumber
                global phoneNumberNational
                
                if "HOME" in os.environ:
                    config_dir = os.environ['HOME'] + "/.config"
                else:
                    # changed here from .\ to /
                    config_dir = os.environ['HOMEPATH'] + "/.config"
                directory = "truecallerpy"
                file = "authkey.json"
                dir_path = os.path.join(config_dir, directory)
                path = os.path.join(config_dir, directory, file)
                r_path = os.path.join(config_dir, directory, "request.json")
                try:
                    os.makedirs(dir_path, exist_ok=True)
                except OSError as error:
                    
                    # raise SystemExit(error):
                    msg = error
                number = entry1.get()

                if number[0] != "+":
                    

                    msg = '\x1b[31mEnter valid phone number in International Format\x1b[0m'
                phoneNumber = phonenumbers.parse(number, None)
                # check if a number is valid
                if phonenumbers.is_valid_number(phoneNumber) == False:
                        
                            
                    msg = '\x1b[31mEnter valid phone number in International Format\x1b[0m'
                phoneNumberNational = phonenumbers.format_number(
                        phoneNumber, phonenumbers.PhoneNumberFormat.NATIONAL)
                phoneSpecs = truecallerpy_get_random_phone() 
                data = {
                        "countryCode": phonenumbers.region_code_for_number(phoneNumber),
                        "dialingCode": phonenumbers.country_code_for_region(phonenumbers.region_code_for_number(phoneNumber)),
                        "installationDetails": {
                            "app": {
                                "buildVersion": 5,
                                "majorVersion": 11,
                                "minorVersion": 7,
                                "store": "GOOGLE_PLAY"
                            },
                            "device": {
                                "deviceId": ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrst') for i in range(16)),
                                "language": "en",
                                "manufacturer": "{}".format(phoneSpecs["manufacturer"]),
                                "model": "{}".format(phoneSpecs["model"]),
                                "osName": "Android",
                                "osVersion": "10",
                                "mobileServices": ["GMS"]
                            },
                            "language": "en"
                        },
                        "phoneNumber": getNumber(phoneNumberNational),
                        "region": "region-2",
                        "sequenceNo": 2
                    }
                headers = {
                        'content-type': 'application/json; charset=UTF-8',
                        'accept-encoding': 'gzip',
                        'user-agent': 'Truecaller/11.75.5 (Android;10)',
                        'clientsecret': 'lvc22mp3l1sfv6ujg83rd17btt'
                    }
               
                if os.path.exists(r_path):
                    
                        with open(r_path) as f:
                            req_file = json.load(f)
                        if req_file['status'] == False:
                            try:
                                
                                msg = "\x1b[31mSomthing when wrong\x1b[0m"
                                os.remove(r_path)
                            except IOError:

                                msg = "Unable to delete file\n Delete '{}' this file and try again".format(r_path)
                        else:
                            if '+{}'.format(req_file['parsedPhoneNumber']) == getNumber(number):
                                msg = (" line 491 Previous request was found for this mobile number.\n")
                                
                                
 
                                answer = messagebox.askyesno("Do you want to enter previous OTP (y/n): ")
                                if answer ==True:
                                    x = "y"
                                else:
                                    x = "n"
                                x_status = True
                                while x_status:
                                    if x == "y" or x == "yes":
                                        x_status = False
                                        request_data = req_file
                                    elif x == "n" or x == "no":
                                        x_status = False
                                        try:
                                            os.remove(r_path)
                                        except IOError:
                                            msg = "Unable to delete file\n Delete '{}' this file and try again"
 
                                        try:
                                            postRequest = requests.post('https://account-asia-south1.truecaller.com/v2/sendOnboardingOtp', headers=headers, json=data)
                                        except requests.exceptions.RequestException as e:
                                            msg = "line 551"
                                        requestFile = open(r_path, "w")
                                        json.dump(postRequest.json(),
                                                requestFile, indent=3)
                                        requestFile.close()
                                        request_data = postRequest.json()
                                        if request_data['status'] == 1 or request_data['status'] == 9 or request_data['message'] == "Sent":
                                           
                                            msg = "Otp sent successfully"
                                                
                                    else:

                                        answer = messagebox.askyesno("Do you want to enter previous OTP (y/n): ")
    #Create a Label
                                        if answer ==True:
                                            x = "y"
                                        else:
                                            x = "n"
                            else:
                                try:
                                    postRequest = requests.post(
                                        'https://account-asia-south1.truecaller.com/v2/sendOnboardingOtp', headers=headers, json=data)
                                except requests.exceptions.RequestException as e:
                                    
                                    msg = "line 577"
                                    # raise SystemExit(e)
                                requestFile = open(r_path, "w")
                                json.dump(postRequest.json(), requestFile, indent=3)
                                requestFile.close()
                                request_data = postRequest.json()
                                if request_data['status'] == 1 or request_data['status'] == 9 or request_data['message'] == "Sent":
                                    msg = "Otp sent successfully"
                        

                                    
                else:
                        try:
                            postRequest = requests.post(
                                'https://account-asia-south1.truecaller.com/v2/sendOnboardingOtp', headers=headers, json=data)
                        except requests.exceptions.RequestException as e:
                            
                            msg = "line594"
                        requestFile = open(r_path, "w")
                        json.dump(postRequest.json(), requestFile, indent=3)
                        requestFile.close()
                        request_data = postRequest.json()
                        if request_data['status'] == 1 or request_data['status'] == 9 or request_data['message'] == "Sent":
                            msg = "Otp sent successfully"

                            
               
            elif(len(entry2.get()) != 0):
                
                def getNumber(x):
                    
                    if x[0] == "0":
                        return x[1:].replace(" ", "")
                    else:
                        return x.replace(" ", "")
                if "HOME" in os.environ:
                    config_dir = os.environ['HOME'] + "/.config"
                else:
                    config_dir = os.environ['HOMEPATH'] + "\.config"
                # print(config_dir)
                directory = "truecallerpy"
                file = "authkey.json"
                dir_path = os.path.join(config_dir, directory)
                path = os.path.join(config_dir, directory, file)
                r_path = os.path.join(config_dir, directory, "request.json")
                headers = {
                    'content-type': 'application/json; charset=UTF-8',
                    'accept-encoding': 'gzip',
                    'user-agent': 'Truecaller/11.75.5 (Android;10)',
                    'clientsecret': 'lvc22mp3l1sfv6ujg83rd17btt'
                }
                if request_data['status'] == 1 or request_data['status'] == 9 or request_data['message'] == "Sent":
                    otp = entry2.get()
                    postData = {
                        "countryCode": phonenumbers.region_code_for_number(phoneNumber),
                        "dialingCode": phonenumbers.country_code_for_region(phonenumbers.region_code_for_number(phoneNumber)),
                        "phoneNumber": getNumber(phoneNumberNational),
                        "requestId": request_data['requestId'],
                        "token": otp
                    }
                    otpPostRequest = requests.post(
                        'https://account-asia-south1.truecaller.com/v1/verifyOnboardingOtp', headers=headers, json=postData)
                
                    otp_req_data = otpPostRequest.json()
                    
                    if otp_req_data['status'] == 2 and otp_req_data['suspended'] == False:

                        msg = '\x1b[33mYour installationId\x1b[0m : \x1b[32m {}\x1b[0m'.format(
                            otp_req_data['installationId'])
                        is_otp_send = False
                        authKeyFile = open(path, "w")
                        json.dump(otp_req_data, authKeyFile, indent=3)
                        authKeyFile.close()

                        msg = "Logged in successfully."
                        button1.config(text="get otp")

                        try:
                            os.remove(r_path)
                        except IOError:
                            msg =  "Unable to delete file\n Delete '{}' this file and try again. \nDon't worry about this error your login was successfull".format(r_path)
                    elif otp_req_data['status'] == 11 or otp_req_data['message'] == "Invalid credentials":
                        msg = "Invalid OTP"
                        button1.config(text="get otp")

                    else:
                        msg = otp_req_data['message']
                        # is_otp_send = False
                elif (request_data['status'] == 6 or request_data['status'] == 5):
   
                    msg = '\x1b[31mYou have exceeded the limit of verification attempts.\nPlease try again after some time.\x1b[0m'
                    try:
                        os.remove(r_path)
                    except IOError:
                        msg = "Unable to delete file\n Delete '{}' this file and try again".format(r_path)

                else:
                    msg = '\x1b[31m {} \x1b[0m'.format(request_data['message'])


            else:
            
                msg ="NO OTP WAS ENTERED"
                

        except Exception as ep:
            messagebox.showerror('error', ep)
        
    messagebox.showinfo('message', msg)
    
    
# def enable_entry():
    # entry2.config(state= "normal")
    # global my_text
    # button1.config(text = "SUBMIT")


def getAuthKey():
    msg = ''

    if "HOME" in os.environ:
        config_dir = os.environ['HOME'] + "/.config"
    else:
        config_dir = os.environ['HOMEPATH'] + "\.config"

    directory = "truecallerpy"
    file = "authkey.json"
    path = os.path.join(config_dir, directory, file)

    try:
        with open(path, encoding='utf-8-sig') as authKeyFile:
            authkey = json.load(authKeyFile)
        return authkey
    except FileNotFoundError:
        msg = "error"
        # return "error"
    messagebox.showinfo('message', msg)


def truecallerpy_get_installationId():
    msg = ""
    authenticationJson = getAuthKey()
    if authenticationJson == "error":
        msg = "Please login to your account"
        # print('\x1b[33mPlease login to your account\x1b[0m')
    else:
        installationId = authenticationJson["installationId"]
        return installationId
    messagebox.showinfo('message', msg)

        # print(installationId)
def getNumber(x):
                    
    if x[0] == "0":
        return x[1:].replace(" ", "")
    else:
                        return x.replace(" ", "")


def search_phonenumber(phoneNumber, regionCode, installationId):
    phNumber = phonenumbers.parse(phoneNumber, regionCode)
    nationalPhoneNumber = phonenumbers.format_number(
        phNumber, phonenumbers.PhoneNumberFormat.NATIONAL)

    params = {
        'q': getNumber(nationalPhoneNumber),
        'countryCode': "{}".format(phonenumbers.region_code_for_number(phNumber)),
        'type': '4',
        'locAddr': '',
        'placement': 'SEARCHRESULTS,HISTORY,DETAILS',
        'encoding': 'json'
    }
    headers = {
        'content-type': 'application/json; charset=UTF-8',
        'accept-encoding': 'gzip',
        'user-agent': 'Truecaller/11.75.5 (Android;10)',
        'clientsecret': 'lvc22mp3l1sfv6ujg83rd17btt',
        'authorization': 'Bearer ' + installationId}
    try:
        req = requests.get(
            'https://search5-noneu.truecaller.com/v2/search', headers=headers, params=params)
        #print(req.status_code, req.text)
        if req.status_code == 429:
            x = {
                "errorCode": 429,
                "errorMessage": "too many requests.",
                "data": None
            }
            return x
        elif req.json().get('status'):
            x = {
                "errorCode": 401,
                "errorMessage": "Your previous login was expired.",
                "data": None
            }
            return x
        else:
            return req.json()
    except requests.exceptions.RequestException as e:
        msg = e
    messagebox.showinfo('message', msg)



def import_csv_data():
    global line_at_which_error_occured
    id = truecallerpy_get_installationId()
    list11 = []

    try:
         file1 = open("numbers.txt","r+") 
    except:
            msg = "pls create or number.txt file was not found"
    with open(r"numbers.txt", 'r') as fp:
            lines = len(fp.readlines())
            
    number_of_lines = lines
    print(number_of_lines)
    list11.append(file1.read())

    num =str(list11[0]).replace("\n",",").split(',')
    # data = []
    fields = ['Number', 'Name' , 'City'] 
    
        # line_at_which_error_occured= ""
    # for i in range(line_at_which_error_occured,number_of_lines) :
    #         if (num[i] == "error"):
    #             line_at_which_error_occured = i
    #             break
    #         print(num[i])
    for i in range(line_at_which_error_occured,number_of_lines) :
        
        try:
        
            main_data = search_phonenumber(num[i],"IN", id)
            
            
            if(main_data['data'] == None):
                
                line_at_which_error_occured = i
                print(line_at_which_error_occured)

                msg = main_data['errorMessage']
                messagebox.showinfo('message', msg)
                # button3.config(state="normal")
                break
            
            
         
            else:           
                # print( main_data['data'][0])
                if "phones" in main_data['data'][0]:
                    
                            
                    phones = main_data['data'][0]['phones'][0]['e164Format']
                        
                else:
                    phones = " number not found"
                if "name" in main_data['data'][0]:
                    name = main_data['data'][0]['name']
                            
                else:
                    name = "unknown name"
                if "city" in main_data['data'][0]['addresses'][0]:
                    city = main_data['data'][0]['addresses'][0]['city']
                        
                else:
                    city = "unknown city"
                data.append([phones, name , city])
                with open('result.csv', 'w', encoding="utf-8") as f:
                        write = csv.writer(f)
                        write.writerow(fields)
                        write.writerows(data)
                        
                        
        except:
                    msg = "error"
                    messagebox.showinfo('message', msg)
                    # root.quit()
                    break
    
    
    # my_Script()
    # print(line_at_which_error_occured)
    

def import_csv_data_RE(line_error):
    
    
    # entry2.config(state="disabled")

    # global v
    # global line_at_which_error_occured

    def my_Script_2(index1):
          
        # import sys
        
        id = truecallerpy_get_installationId()
        # print(id)
        list11 = []

        try:
         file1 = open("numbers.txt","r+") 
        except:
            msg = "pls create or number.txt file was not found"
        with open(r"numbers.txt", 'r') as fp:
            lines = len(fp.readlines())
            
        number_of_lines = lines
        print(number_of_lines)
        list11.append(file1.read())
        

        num =str(list11[0]).replace("\n",",").split(',')
        # data = []
        print(num)
        # print(num.index(index1)+1)
        fields = ['Number', 'Name' , 'City'] 
        # line_at_which_error_occured= ""
        for i in range(index1, number_of_lines): 
            
            
            # print(num[i])
            # main_data = search_phonenumber(num[i],"IN", id)
            # print(main_data)
            try:
                
                print(i)

                
                main_data = search_phonenumber(num[i],"IN", id)
                # print(main_data)
                if(main_data['data'] == None):
                    line_at_which_error_occured = i
                    msg = main_data['errorMessage']
                    # root.destroy()
                    messagebox.showinfo('message', msg)
                    # root.destroy()
                    button3.config(state="normal")
                    print("")
                    print(line_at_which_error_occured)
                    # button1.config(state=)
                    # print(line_at_which_error_occured)
                    break
                    
                    # sys.exit("")   
                else:
                    
                    
                    # print( main_data['data'][0])
                    if "phones" in main_data['data'][0]:
                        
                        phones = main_data['data'][0]['phones'][0]['e164Format']
                        # print(phones)
                    else:
                        phones = " number not found"
                    if "name" in main_data['data'][0]:
                        name = main_data['data'][0]['name']
                        # print(name)
                    else:
                        name = "unknown name"
                    if "city" in main_data['data'][0]['addresses'][0]:
                        city = main_data['data'][0]['addresses'][0]['city']
                        # print(city)
                    else:
                        city = "unknown city"
                    data.append([phones, name , city])
                # with open('result.csv', 'a', newline="",encoding="utf-8") as f:
                #     write = csv.writer(f)
                    
                        
                #     write.writerow(fields)
                #     write.writerows(data)
                # print(data)

             
                    
            except:
                
                # print("dlkwandlkwandlaw")
                
                # time.sleep(30)
                   

                msg = "error"
                messagebox.showinfo('message', msg)
                root.quit()
                break
        with open('result.csv', 'a', newline="",encoding="utf-8") as f:
                    write = csv.writer(f)
                    
                        
                    write.writerow(fields)
                    write.writerows(data)
        print(data)
        # with open('result.csv', 'a', newline="",encoding="utf-8") as f:
                
                
        #         writer_object = writer(f)
    
        #                 # Pass the list as an argument into
        #                 # the writerow()
        #         writer_object.writerow(data)
                    
        #                 # Close the file object
        #         f.close()
    my_Script_2(line_error)


def reset():
    # is_otp_send = False
    validation()
    # import_csv_data()



if __name__== "__main__":    
    root= tk.Tk()
    root.title('Keyss')

    canvas1 = tk.Canvas(root, width=400, height=400, relief='raised')
    canvas1.pack()



    label1 = tk.Label(root, text='CHECK NUMBERS')
    label1.config(font=('helvetica', 14))
    canvas1.create_window(200, 25, window=label1)
    label2 = tk.Label(root, text='Mobile Number:')
    label2.config(font=('helvetica', 10))
    canvas1.create_window(70, 140, window=label2)

    entry1 = tk.Entry(root) 
    canvas1.create_window(200, 140, window=entry1)

    label3 = tk.Label(root,text="OTP:")
    label3.config(font=('helvetica', 10))
    canvas1.create_window(70,180,window=label3)

    entry2 = tk.Entry(root,state='normal') 
    canvas1.create_window(200, 180, window=entry2)
    
    button1 = tk.Button(text='Get OTP',command=lambda:[validation()],bg='green',fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 220, window=button1)
    # line_at_which_error_occured = ""
    data = []
    button2 = tk.Button(root, text='Procced',command=import_csv_data,state="normal")
    canvas1.create_window(200, 260, window=button2)  
    button3 = tk.Button(root, text='Re_Authenticate',command=reset,state="normal")

    canvas1.create_window(200, 300, window=button3)
    root.mainloop()


        