# Python Reverse API Client (Streaming Support)

This project demonstrates how to reverse-engineer and interact with an undocumented third-party chat API using Python. It showcases advanced HTTP handling, header manipulation, and processing Server-Sent Events (SSE) for real-time streaming responses.

## 🚀 Key Features

* **Reverse Engineering:** Replicates browser behavior using custom HTTP headers (`User-Agent`, `Referer`, `Origin`).
* **Stream Handling:** implementation of `iter_lines()` to process live data streams (Server-Sent Events) instead of waiting for a full response.
* **UUID Generation:** Dynamically generates unique message IDs for session management.
* **JSON Payload Construction:** Structures complex nested JSON payloads required by the endpoint.

## 🛠 Technologies Used

* Python 3.x
* `requests` library (for HTTP handling)
* `uuid` (for unique ID generation)
* `json` (for payload formatting)

## 📂 Installation & Usage

1.  Clone the repository:
    ```bash
    git clone [https://github.com/yourusername/python-reverse-api-client.git](https://github.com/yourusername/python-reverse-api-client.git)
    cd python-reverse-api-client
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Run the script:
    ```bash
    python main.py
    ```

## 📝 Code Overview

The script mimics a legitimate browser request by setting specific headers to bypass basic bot detection mechanisms. It sends a prompt to the API and listens for a chunked response, printing the output token-by-token as it arrives.

```python
# Snippet: Handling the stream
for line in response.iter_lines():
    if line:
        decoded_line = line.decode('utf-8')
        if decoded_line.startswith("data:"):
            # Process real-time data chunks
