def test_health_check(test_app):
    response = test_app.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_semantic_search(test_app):
    # Send a request to the route with a sample query
    query = "How does FastAPI handle requests?"
    response = test_app.get("/semantic_search", params={"query": query})

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response body contains the expected fields
    assert "answer" in response.json()