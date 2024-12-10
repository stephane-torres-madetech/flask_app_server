import json


def test_index(client):
    res = client.get('/')
    assert res.status_code == 200
    
def test_courses(client):
    res = client.get('/courses')
    assert res.status_code == 200
    result = json.loads(res.data) 
    assert result["course1"]["name"] == "Women in Tech"
    assert result["course1"]["location"] == "Manchester"
    assert result["course2"]["name"] == "Cyber Security Track Day"
    assert result["course2"]["location"] == "Manchester"

   
 
 
   