def test_index(client):
    res = client.get('/')
    assert res.status_code == 200
    
def test_courses(client):
    res = client.get('/courses')
    assert res.status_code == 200
    assert b"<h1>Courses</h1>" in res.data
    assert b"<li>Course 1</li>" in res.data
    assert b"<li>Course 2</li>" in res.data
    assert b"<li>Course 3</li>" in res.data
    assert b"<li>Course 4</li>" in res.data
 