#!/usr/bin/env python3

import ast
import cgi #CGIのフォーム入力を受け付けてくれるモジュール
import datetime
import json
import linecache
import cgitb
import send_mail_to as mailTo

cgitb.enable() 
form = cgi.FieldStorage() #フォーム入力(URLからの入力)が入る
name_file_json  = 'output.json'
path_file_json  = "./" + name_file_json

print("content-Type: text/html\n\n")
print('<h1>めぐすり、さした？</h1>')

today   = {'day': str(datetime.date.today())}
#print('日本語')

read_date_last = linecache.getline(name_file_json, 2) #jsonファイルの2行目を取得
change_date_last_to_dict = ast.literal_eval(read_date_last)
#print(change_date_last_to_dict['day'])

if today == change_date_last_to_dict :
    message_done = '今日は既に目薬さしたよ。まつ毛のびちゃう。日付:' + today['day'] 
    print('<p>' + message_done + '</p>')
    mailTo.send_mail_to(form['password'].value, form['toAddress'].value, message_done)
else:
    message_good = 'よく思い出しました！あっぱれ！日付:' + today['day']
    print('<p>' + message_good + '</p>')
    mailTo.send_mail_to(form['password'].value, form['toAddress'].value, message_good)

with open(name_file_json,'wb') as f:
    f.seek(0, 2)
    #if f.tell() == 0:
    f.write('[\n'.encode())
    f.write(json.dumps(today,  ensure_ascii=False).encode())
    f.write('\n]'.encode())