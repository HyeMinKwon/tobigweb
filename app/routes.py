from flask import Flask, render_template
#application instance를 생성, 객체의 이름은 app
#__name은 모듈 이름
app = Flask(__name__)

#생성한 객체의 route설정. URL설정
@app.route('/')

#함수 생성
def home():
    return render_template('home.html')


@app.route('/about')
def about():
  return render_template('about.html')

#run함수를 이용하여 로컬서버에 어플리케이션을 실행
if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host = '0.0.0.0')

#실행은 cmd창에서 이 파일 실행