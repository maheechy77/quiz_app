import requests

params ={
    "amount":10,
    "type":"boolean"
}

response = requests.get("https://opentdb.com/api.php",params=params)
question_data=[]
for result in response.json()["results"]:
   question_data.append({
       "category": result["category"],
       "type": result["type"],
       "difficulty": result["difficulty"],
       "question": result["question"],
       "correct_answer": result["correct_answer"],
       "incorrect_answers": result["incorrect_answers"]
   })

