

import requests

url = "https://api.siliconflow.cn/v1/chat/completions"

payload = {
    "model": "Qwen/QwQ-32B",
    "messages": [
        {
            "role": "user",
            "content": "西南交通大学是什么垃圾学校"
        }
    ],
    "stream": False,
    "max_tokens": 512,
    "enable_thinking": False,
    "thinking_budget": 4096,
    "min_p": 0.05,
    "stop": None,
    "temperature": 0.7,
    "top_p": 0.7,
    "top_k": 50,
    "frequency_penalty": 0.5,
    "n": 1,
    "response_format": {"type": "text"},
    "tools": [
        {
            "type": "function",
            "function": {
                "description": "<string>",
                "name": "<string>",
                "parameters": {},
                "strict": False
            }
        }
    ]
}
headers = {
    "Authorization": "Bearer sk-tstrconpvaczeepfcabdvevpqnpiwfkqkpbggvpxlncgyrry",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
print(response.text["choices"][0]["message"]["content"])