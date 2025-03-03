from flask import Flask , request , jsonify
from src.run_local import write_query , execute_query
app = Flask(__name__) 

# routing the decorator function hello_name 
@app.route('/generate_query',methods=['POST']) 
def generate_query():
    data=request.get_json()
    user_ques = data["question"]
    # write_query({"question": "How many Employees are there?"})
    sql_query = write_query(ques_dict={"question": user_ques})
    return jsonify(sql_query)

@app.route('/execute_sql_query',methods=['POST'])
def execute_sql_query():
    data=request.get_json()
    sql_execute = data["query"]
    # execute_query({"query": "SELECT COUNT(*) FROM Employee;"})
    query_output = execute_query(query_dic={"query": f"{sql_execute}"})
    return jsonify(query_output)





if __name__ == '__main__': 
    app.run(debug = True,host="0.0.0.0",port=5001) 
