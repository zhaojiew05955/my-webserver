from bottle import route, run, template, static_file, view
from bottle import post, get, request, response
from bottle import error
import socket
from mylog import logger_config
logger = logger_config("infolog.txt","test-log-info")

@route('/log')
def mylog():
    logger.info("info")
    logger.error("error")
    logger.debug("debug")
    logger.warning("warning")

@route('/test/<name>')
def index(name="Stranger"):
    ip = socket.gethostbyname(socket.gethostname())
    info = dict()
    info["name"] = name
    info["serverip"] = ip
    #info["sourceip"] = request.environ.get('REMOTE_ADDR')
    info["sourceip"] = request.remote_addr
    info["header"] = dict(request.headers)
    info["cookies"] = dict(request.cookies)
    return info

@route('/json')
def testjson():
    info = dict()
    info["info"] = "user"
    all_user = [
        {'id':1, 'sex':1, 'real_name':'xiaohua'},
        {'id':2, 'sex':0, 'real_name':'xiaoming'},
        {'id':3, 'sex':0, 'real_name':'xiaohei'}
    ]
    info["users"] = all_user
    return info

@post('/sns')
def message():
    f = request.body
    while True:
        s = f.readline()    
        if s == "":
            break
        print(s.strip())
    return '<b>success</b>!'

@route('/template')
@view('hello_template')
def template():
    name="test"
    blog="xzan.ngrok.cc"
    myfriend=['sam','mary','lisi']
    myinfodir={'age':20,'weight':130}
    info={'name':name,'age':myinfodir,'weight':myinfodir,'blog':blog,'SNS':myfriend}
    return info

@route('/response')
def returnresp():
    print(response.status_code)
    print(response.status)
    print(response.body)
    response.body = "hello"
    return response

@route('/sourceip')
def show_ip():
    ip = request.environ.get('REMOTE_ADDR')
    # or ip = request.get('REMOTE_ADDR')
    # or ip = request['REMOTE_ADDR']
    return template("Your IP is: {{ip}}", ip=ip)

@route('/static/<filename>')
def server_static(filename):
    print(filename)
    return static_file(filename, root='./static')
    
@get('/')
def health():
    return 'success'

@error(404)
def error404(error):
    return 'Nothing here, sorry'

run(host='0.0.0.0', port=80)
