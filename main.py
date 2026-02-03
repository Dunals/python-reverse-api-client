import requests
import json
import uuid

# Define the URL
url = "https://claude.talkai.info/chat/send/"

# 1. Headers are important to look like a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://claude.talkai.info/",
    "Origin": "https://claude.talkai.info",
    "Content-Type": "application/json"
}

def chat_with_talkai(prompt):
    # 2. Construct the payload
    # We generate a random UUID for the message ID
    message_id = str(uuid.uuid4())
    
    payload = {
        "type": "chat",
        "messagesHistory": [
            {
                "id": message_id,
                "from": "you",
                "content": prompt
            }
        ],
        "settings": {
            "model": "claude-3-haiku-20240307", # You can try changing this if they support others
            "temperature": 0.7
        }
    }

    print(f"[*] Sending message: '{prompt}'")

    try:
        # 3. Send the request with stream=True
        response = requests.post(url, json=payload, headers=headers, stream=True)
        
        if response.status_code == 200:
            print("[*] Receiving response:")
            
            # 4. Process the stream
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    
                    # The lines look like: "data: Hello"
                    if decoded_line.startswith("data:"):
                        content = decoded_line[5:].strip() # Remove "data:" and whitespace
                        
                        # Stop if we hit the limit or empty end markers
                        if content == "-1" or not content:
                            continue
                            
                        # Print the chunk
                        print(content, end=" ", flush=True)
                        
            print("\n[+] Done.")
        else:
            print(f"[-] Failed with status code: {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"[-] Error: {e}")

# Run the test
if __name__ == "__main__":
    chat_with_talkai("What is the exact date today? If you don't know, give me the last news event you remember.")
