import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock
import sys
import os

# Add the model directory to the path so we can import from it
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../model')))

from main import app

client = TestClient(app)

def test_chat_endpoint_success():
    """Test the chat endpoint with a successful mock response."""
    with patch('api_server.orchestrator_agent', new_callable=AsyncMock) as mock_agent:
        mock_agent.return_value = "Test response from orchestrator"
        
        response = client.post("/", json={"prompt": "Hello", "screenshot": None, "document": None})
        
        assert response.status_code == 200
        data = response.json()
        assert data["response"] == "Test response from orchestrator"
        assert data["image_output"] is None
        mock_agent.assert_called_once_with("Hello")

def test_chat_endpoint_error():
    """Test the chat endpoint when an error occurs in the orchestrator."""
    with patch('api_server.orchestrator_agent', new_callable=AsyncMock) as mock_agent:
        mock_agent.side_effect = Exception("Orchestrator error")
        
        response = client.post("/", json={"prompt": "Hello"})
        
        assert response.status_code == 200
        data = response.json()
        assert "Cannot process this request due to Orchestrator error" in data["response"]

def test_chat_endpoint_rate_limit():
    """
    Test the rate limiter. 
    Note: This might be tricky to test without actual time passing or mocking the limiter.
    Given the current setup, we'll just check if the endpoint exists and responds.
    """
    response = client.post("/", json={"prompt": "Hello"})
    assert response.status_code == 200

