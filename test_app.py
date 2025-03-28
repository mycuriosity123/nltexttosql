from src.app import app
import json

def test_home():
    headers = {'Content-Type': 'application/json'}
    response = app.test_client().post("/generate_query",data=json.dumps({"question":"How many runs are there?"}),headers=headers)

    assert response.status_code==200 