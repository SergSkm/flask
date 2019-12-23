# views.py

from flask import render_template, make_response, jsonify, request
from json2html import *
from random import random

from app import app

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")



# {
#     "language" : "Python",
#     "framework" : "Flask",
#     "website" : "Scotch",
#     "version_info" : {
#         "python" : 3.4,
#         "flask" : 0.12
#     },
#     "examples" : ["query", "form", "json"],
#     "boolean_test" : true
# }





@app.route('/get-tweet-sentiment', methods=['POST']) #GET requests will be blocked
def get_tweet_sentiment():
    req_data = request.get_json(force=True)

    try:
        # report_date = req_data['report_date'],
        # tweet_id = req_data['tweet_id'],
        text = req_data['text'],
        # language = req_data['language'],
        # user_location = req_data['user_location'],
        # nb_likes = req_data['nb_likes'],
        # nb_retweets = req_data['nb_retweets'],
        # isSensitive = req_data['isSensitive'],
        # isRetweet = req_data['isRetweet'],
        # isRetweeted = req_data['isRetweeted'],
        # user_id = req_data['language'],
        # user_description = req_data['user_description'],
        # keyword = req_data['keyword']
    except:
        print("JSON fields are wrong")

    json_out = {"sentiment": random()*2-1}
    return(str(json_out))




####__________________Testing__________________
stock = {
    "fruit": {
        "apple": 30,
        "banana": 45,
        "cherry": 1000
    }
}

@app.route("/stock")
def get_stock():

    res = make_response(jsonify(stock), 200)

    return res


# Sample Jaba JSON
# tweet = {
#     "tweet": {
#         "bank_name": "Sberbank",
#         "text": "Here should be tweet text. Here should be tweet text. Here should be tweet text. Here should be tweet text.",
#         "tweet_id": 123412341351235,
#         "favourite_count":12,
#         "retweets":2
#     }
# }
# URL received:"http://127.0.0.1:5000/get_tweet_sentiment?bank_name=Python?bank_name=Python?bank_name=Python?bank_name=Python?bank_name=Python"
# request.args.get('language')
#
# @app.route("/get_tweet_sentiment/<collection>", methods=["POST"])
# def create_collection(collection):
#
#     """ Creates a new collection if it doesn't exist """
#
#     req = request.get_json()
#
#     if collection in stock:
#         res = make_response(jsonify({"error": "Collection already exists"}), 400)
#         return res
#
#     stock.update({collection: req})
#
#     res = make_response(jsonify({"message": "Collection created"}), 201)
#     return res





# {
#     "language" : "Python",
#     "framework" : "Flask",
#     "website" : "Scotch",
#     "version_info" : {
#         "python" : 3.4,
#         "flask" : 0.12
#     },
#     "examples" : ["query", "form", "json"],
#     "boolean_test" : true
# }

@app.route('/json-example', methods=['POST']) #GET requests will be blocked
def json_example():
    req_data = request.get_json(force=True)

    language = req_data['language']
    framework = req_data['framework']
    python_version = req_data['version_info']['python'] #two keys are needed because of the nested object
    example = req_data['examples'][0] #an index is needed because of the array
    boolean_test = req_data['boolean_test']

    # return 1234
    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)







@app.route('/twitter_keyword_search')
def twitter_kwd_srch():
    df = {
      "data": [
        {
          "id": "1",
          "name": "John Q Public",
          "position": "System Architect",
          "salary": "$320,800",
          "start_date": "2011/04/25",
          "office": "Edinburgh",
          "extn": "5421"
        },
        {
          "id": "2",
          "name": "Larry Bird",
          "position": "Accountant",
          "salary": "$170,750",
          "start_date": "2011/07/25",
          "office": "Tokyo",
          "extn": "8422"
        }
        ]
    }
    # html_data = json2html.convert(json=input)
    # return render_template_string(json2html.convert(json=df))
    # return render_template(json2html.convert(json=df))

    return render_template("test.html")


    return render_template("twitter_keyword_search.html")





@app.route('/GetData2')
def GetData2():
    input = {
            "sample": [{
                    "a":1, "b":2, "c":3
            }, {
                    "a":5, "b":6, "c":7
            }]
    }
    return json2html.convert(json = input)

# @app.route("/GetData")
# def GetData():
#     df = {
#       "data": [
#         {
#           "id": "1",
#           "name": "John Q Public",
#           "position": "System Architect",
#           "salary": "$320,800",
#           "start_date": "2011/04/25",
#           "office": "Edinburgh",
#           "extn": "5421"
#         },
#         {
#           "id": "2",
#           "name": "Larry Bird",
#           "position": "Accountant",
#           "salary": "$170,750",
#           "start_date": "2011/07/25",
#           "office": "Tokyo",
#           "extn": "8422"
#         }]
#     }
#     columnNames = df.data.values
#     return render_template('record.html', records=temp, colnames=columnNames)



# @app.route('/twitter_keyword_search2')
# def twitter_kwd_srch():
#       data = {
#         "data": [
#           {
#             "id": "1",
#             "name": "John Q Public",
#             "position": "System Architect",
#             "salary": "$320,800",
#             "start_date": "2011/04/25",
#             "office": "Edinburgh",
#             "extn": "5421"
#           },
#           {
#             "id": "2",
#             "name": "Larry Bird",
#             "position": "Accountant",
#             "salary": "$170,750",
#             "start_date": "2011/07/25",
#             "office": "Tokyo",
#             "extn": "8422"
#           }]
#       }
#     return render_template_string(
#         '''
#             <table>
#                     <tr>
#                         <td> Name </td>
#                         <td> Status </td>
#                     </tr>
#
#
#             {% for name, status in data.data.items() %}
#
#                     <tr>
#                         <td>{{ name }}</td>
#                         <td>{{ status }}</td>
#                     </tr>
#
#             {% endfor %}
#
#
#             </table>
#         ''', labels=data)









@app.route('/tweeter_ToJava')
def stuff():
  # Assume data comes from somewhere else
  data = {
    "data": [
      {
        "id": "1",
        "name": "John Q Public",
        "position": "System Architect",
        "salary": "$320,800",
        "start_date": "2011/04/25",
        "office": "Edinburgh",
        "extn": "5421"
      },
      {
        "id": "2",
        "name": "Larry Bird",
        "position": "Accountant",
        "salary": "$170,750",
        "start_date": "2011/07/25",
        "office": "Tokyo",
        "extn": "8422"
      }]
  }
  return jsonify(data)


# # A welcome message to test our server
# @app.route('/')
# def index():
#     return "<h1>Welcome to our server !!</h1>"



@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })
