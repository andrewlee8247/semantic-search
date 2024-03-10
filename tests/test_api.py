def test_health_check(test_app):
    response = test_app.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_semantic_search(test_app):
    query = "How does FastAPI handle requests?"
    response = test_app.get("/api/semantic_search", params={"query": query})
    assert response.status_code == 200
    assert "answer" in response.json()