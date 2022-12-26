# flask render_template example
 
from flask import Flask, render_template, request, redirect, url_for
import os
from os.path import join, dirname, realpath
from flask_mysqldb import MySQL,MySQLdb
 
# WSGI Application
# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
 
# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
UPLOAD_FOLDER = 'database'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'wahab'
 
mysql = MySQL(app)
 
#Creating a connection cursor



# Root URL
@app.route('/',methods=["GET", "POST"])
def index():
     if request.method == "POST":
          first_name = request.form.get("name")
          last_name = request.form.get("address")
          mobile_num = request.form.get("number")
          national_id = request.form.get("idcard")
          f = request.files['file']
          file_path = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
          f.save(file_path)
          

          cursor = mysql.connection.cursor()
          cursor.execute(''' INSERT INTO mytable VALUES(%s,%s,%s,%s,%s)''',(first_name,last_name,mobile_num,national_id,file_path))
          mysql.connection.commit()
          cursor.close()




          
     
     return render_template('index.html')




     


UPLOAD_FOLDER1 = 'input'
app.config['UPLOAD_FOLDER1'] =  UPLOAD_FOLDER1
@app.route("/upload", methods=['GET','POST'])
def uploadFiles():

      # get the uploaded file
      uploaded_file = request.files['file']
      print(uploaded_file)
      if uploaded_file.filename != '':
          import os
          file_path = os.path.join(app.config['UPLOAD_FOLDER1'], uploaded_file.filename)
          uploaded_file.save(file_path)
          import re
          file1 = open(file_path, 'r')
          text = ""
          all_speakers = []
          for each in file1.readlines():
               text = text + each
               y = re.search(r'<NA> <NA>(.*?)<NA> <NA>', each).group(1)
               all_speakers.append(y)
          unique_speakers = list(set(all_speakers))
          unique_speakers1 = len(unique_speakers)
          valu = unique_speakers1
          file1 = open(file_path, 'r')
          first_speaker = []
          from pydub import AudioSegment
          file_path1 = 'input\sound43.wav'
          sound = AudioSegment.from_file(file_path1)
          first_person = AudioSegment.empty()
          for each in file1.readlines():
               if 'SPEAKER_00' in each:
                    y = re.search(r'SPEAKER sound 1(.*?)<NA> <NA>', each).group(1)
                    y = y.split()
                    start = float(y[0]) * 1000
                    end = float(y[1]) * 1000 + start
                    separate = sound[start:end]
                    first_person += separate
                    first_person.export("input1/first_person.wav", format="wav")
          second_person = AudioSegment.empty()
          file1 = open(file_path, 'r')
          for each in file1.readlines():
               if 'SPEAKER_01' in each:
                    y = re.search(r'SPEAKER sound 1(.*?)<NA> <NA>', each).group(1)
                    y = y.split()
                    start = float(y[0]) * 1000
                    end = float(y[1]) * 1000 + start
                    separate = sound[start:end]
                    second_person += separate
                    second_person.export("input1/second_person.wav", format="wav")
          file1 = open(file_path, 'r')
          third_person = AudioSegment.empty()
          for each in file1.readlines():
               if 'SPEAKER_02' in each:
                    y = re.search(r'SPEAKER sound 1(.*?)<NA> <NA>', each).group(1)
                    y = y.split()
                    start = float(y[1]) * 1000
                    end = float(y[1]) * 1000 + start
                    separate = sound[start:end]
                    third_person += separate
                    third_person.export("input1/third_person.wav", format="wav")
          import librosa
          from dtw import dtw
          import os
          from numpy.linalg import norm
          path = 'database'
          file_path1 = 'input1'
          y = os.listdir(path)
          y5 = os.listdir(file_path1)
          pct_similirity = []
          all_database = []
          for each1 in [y[0]]:
               for each in [y5[0]]:
                    y1 = os.path.join(path,each1)
                    y11 = os.path.join(file_path1,each)
                    if os.path.isfile(y1):
                         y3,sr3 = librosa.load(y1)
                         y2, sr2 = librosa.load(y11)
                         mfcc1 = librosa.feature.mfcc(y3,sr3)   #Computing MFCC values
                         mfcc2 = librosa.feature.mfcc(y2, sr2)
                         dist = dtw(mfcc1.T, mfcc2.T)
                         y10 = 100 - dist.normalizedDistance
                         if y10 < 0:
                              y10 = 0
                         pct_similirity.append(y10)
                         name3=each1.split('.')[0]
                         all_database.append(name3)
                         print("similarity with {name} is {name1} percent."
                         .format(name=each1.split('.')[0], name1 = y10))
                         name2 = len(pct_similirity)
                         name4 = len(all_database)
                         mobile_numbers = []
                         id = []
                         all_names = []
                         cur = mysql.connection.cursor() 
                         cur.execute("SELECT * FROM `mytable` WHERE 1")
                         user = cur.fetchall()
                         for each in user:
                              mobile_numbers.append(each[2])
                              id.append(each[3])
                              all_names.append(each[0])
          
          return render_template('third.html', valu=valu,name2=name2,pct_similirity=pct_similirity,all_names=all_names,all_speakers=all_speakers,unique_speakers=unique_speakers,id=id,mobile_numbers=mobile_numbers)
          
              



                     





if (__name__ == "__main__"):
     app.run(port = 5000)