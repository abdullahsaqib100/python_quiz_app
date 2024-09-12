questions = ["Which city of Pakistan has largest population? " ,
             "Capital of Pakistan is? " ,
             "Which programming language is widely use in AI?" ,
             "Who is the founder of Microsoft?" ,
             "Where the headquarter of Google is situated? "]

options = {
    1: ["A. Lahore" , "B. Islamabad" , "C. Karachi" , "D. Faisalabad" ],
    2: ["A. Rawalpindi" , "B. KPK" , "C. Lahore" , "D. Islamabad"],
    3: ["A. Ruby" , "B. Python" ,"C. C++" , "D. JavaSript"],
    4: ["A. Bill Gates" , "B. Mark Zukerberg" , "C. Tim Cock" , "D. Sundar Pachai"],
    5: ["A. India" , "B. UK" , "C. Japan" , "D. USA"]
}

answers = { 
           1: "C" ,
           2: "D" ,
           3: "B" ,
           4: "A" ,
           5: "D" ,
}

score = 0

def quiz():
    global score
    print("\nWelcome to the simple Quiz Game")
    print("Answer the given quizes by selcting an option from (A , B , C , D) and view your score after answering all the questions" )

    for i in range (1, len(questions) +1):
        print("\nQuestion" , i , ":" , questions[i - 1] )

        for option in options[i]:
            print(option)

        answer = input("Choose any one option from (A, B, C, OR D): ").upper()

        if answer == answers[i]:
            print ("WOW! Correct Answer")
            score += 1

        else:
            print(f"Awww! Wrong Answer. The correct answer was {answers[i]}. ")

    if score == 5:
        print(f"Congratulations! Your final score is {score} out of {len(questions)}. You have done a greate job")
    elif 2< score <5:
        print(f" Not Bad. Your final score is {score} out of {len(questions)}. Keep trying to improve")
    elif 0 < score <=2:
        print(f"Need Much Improvements. Your final score is {score} out of {len(questions)}. ")
    else:
        print("You have Failed. Try Again")
quiz()

        





