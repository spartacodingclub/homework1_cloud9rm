from flask import Flask,render_template,jsonify,request

app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

@app.route('/')
def home():
    return render_template('main.html')

## API 역할을 하는 부분
@app.route('/orderlist', methods=['POST'])
def write_orderlist():
    # 1. 클라이언트가 준 title, author, review 가져오기.
    name_receive=request.form['name_give']
    quantity_receive=request.form['quantity_give']
    address_receive=request.form['address_give']
    pnum_receive=request.form['pnum_give']

    orderinfo={
        'name' : name_receive,
        'quantity' : quantity_receive,
        'address':address_receive,
        'pnum' : pnum_receive
    }

    # 2. DB에 정보 삽입하기
    db.orderinfo.insert_one(orderinfo)

    # 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'msg': '주문이 성공적으로 등록되었습니다.'})


@app.route('/orderlist', methods=['GET'])
def read_orderlist():
		# 1. DB에서 리뷰 정보 모두 가져오기
    orderinfo = list(db.orderinfo.find({},{'_id':0}))
		# 2. 성공 여부 & 리뷰 목록 반환하기
    return jsonify({'result': 'success', 'orderinfo': orderinfo})



if __name__ == '__main__':
    app.run('127.0.0.1', port=5001, debug=True)