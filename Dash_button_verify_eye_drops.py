#!/usr/bin/env python3

import ast
import datetime
import json
import linecache

import send_mail_to as mailTo

name_file_json  = 'output.json'
path_file_json  = "./" + name_file_json

today   = {'day': str(datetime.date.today())}


read_date_last = linecache.getline(name_file_json, 2) #jsonファイルの2行目を取得
change_date_last_to_dict = ast.literal_eval(read_date_last)


if today == change_date_last_to_dict :
    message_done = '今日は既に目薬さしたよ。まつ毛のびちゃう。日付:' + today['day']     
    mailTo.send_mail_to('set_password_from_gmailAdress', 'set_sendTo_gmailAdress', message_done)
else:
    message_good = 'よく思い出しました！あっぱれ！日付:' + today['day']
    mailTo.send_mail_to('eyedrops365', 'kazenokojiro@gmail.com', message_good)

with open(name_file_json,'wb') as f:
    f.seek(0, 2)
    f.write('[\n'.encode())
    f.write(json.dumps(today,  ensure_ascii=False).encode())
    f.write('\n]'.encode())
