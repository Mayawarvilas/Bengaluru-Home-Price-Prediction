from flask import Flask,request,jsonify
import util

app=Flask(__name__)


@app.route('/get_location_names')
def get_location_names():
    response=jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-control-allow-origin','*')
    return response

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    try:
        total_sqft=float(request.form['total_sqft'])
        location=request.form['location']
        bhk=int(request.form['bhk'])
        bath=int(request.form['bath'])

        estimated_price=util.get_estimted_price(location,total_sqft,bath,bhk)

        response=jsonify({
        'estimated_price':estimated_price
        })

        response.headers.add('Access-control-allow-origin','*')

        return response
    except Exception as e:
        return jsonify({'error':str(e)})
    except ValueError as v:
        return jsonify({'error':str(v)})
    except KeyError as k:
        return jsonify({'error':str(k)})


if __name__=='__main__':
    print("strating pyhton flask for the home price prediction")
    util.load_save_artifactes()
    app.run()