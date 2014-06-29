from flask import render_template, Flask, jsonify, request
from app import app
import sys
sys.path.append("/Users/SeoHyeonDeok/studying/github/LikelionKhu_using_git/Likelion_Khu/SeoLikelion/pusher")
import pusher




@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html')

@app.route('/_add_numbers')
def add_numbers():

    a = request.args.get('a')


    p = pusher.Pusher(
        app_id='79161',
        key='00c655f076d9940088e8',
        secret='c4e74cc8e2a00cd553fb'
    )
    p['seokhulikelion'].trigger('my_event', {'message': a})

    return jsonify(result=a)
