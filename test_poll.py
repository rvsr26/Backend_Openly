from polls import PollCreate

data = {
    "question": "test",
    "type": "multiple",
    "options": [{"text": "yes"}, {"text": "no"}],
    "allow_anonymous": True
}

try:
    poll = PollCreate(**data)
    print("Success:", poll)
except Exception as e:
    print("Error:", e)
