import pandas as pd

data = pd.read_json("plik.json")
data = pd.json_normalize(data["quiz"])

score = 0
quest = 0

for index, row in data.iterrows():
    
    question = row["question"]
    index += 1

    print(f"Q {index}: {question} \n \n")
    ans = input("Podaj odpowiedz >> ")
    
    if( ans.upper() == row["correct_answer"]):
        print("dobra odpowiedz\n")
        score += 1
        print(f"Obecny wynik to {score}\n")
    else:
        print("błędna odpowiedz\n")

    quest = index


print(f"Końcowy wynik to {score}/{quest}")


    
    


