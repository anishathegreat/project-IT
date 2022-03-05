print("              Hiii There!!!")
print("      Welcome to our Online Quiz Portal!!\n")
print("                                             ")

print("""            The quiz contains 6 questions and there is no time limit.
            You’ll get 1 point for each correct answer.
            At the end of the quiz, you’ll receive a total score. 
            The maximum score is 100%. Good luck!
            """)



def python_prog():
    score = 0
    score = int(score)

    print("what is apple??")
    a=print("(a)fruit")
    b=print("(b)veg")
    c=print("(c)song")
    d=print("(d)nothing")
    opt=input("Choose your option from (a)(b)(c)(d):")
    ans= "a"
    if opt==ans:
        print("Correct Answer")
        score=score+1
    else:
        print("Wrong Answer")
    print("Correct one is","a")

    print("\nwhat is blue??")
    p = print("(a)fruit")
    q = print("(b)colour")
    r = print("(c)song")
    s = print("(d)nothing")
    opt = input("Choose your option from (a)(b)(c)(d):")
    an = "b"
    if opt == an:
        print("Correct Answer")
        score=score+1
    else:
        print("Wrong Answer")

    print("Correct one is","b")
    print("Your score is :",score)
    return




def java_prog_easy():
    score = 0
    score = int(score)

    print("what is ball??")
    a=print("(a)tree")
    b=print("(b)veg")
    c=print("(c)toy")
    d=print("(d)nothing")
    opt=input("Choose your option from (a)(b)(c)(d):")
    ans="c"
    if opt==ans:
        print("Correct Answer")
        score = score + 1
    else:
        print("Wrong Answer")

    print("Correct one is","c")

    print("\nwhat is blue??")
    q = print("(a)fruit")
    q = print("(b)colour")
    r = print("(c)song")
    s = print("(d)nothing")
    opt = input("Choose your option from (a)(b)(c)(d):")
    an = "b"
    if opt == an:
        print("Correct Answer")
        score = score + 1
    else:
        print("Wrong Answer")

    print("Correct one is", "b")
    print("Your score is :", score)
    return



def java_prog_hard():
    score = 0
    score = int(score)

    print("what is ball??")
    a=print("(a)tree")
    b=print("(b)veg")
    c=print("(c)toy")
    d=print("(d)nothing")
    opt=input("Choose your option from (a)(b)(c)(d):")
    ans="c"
    if opt==ans:
        print("Correct Answer")
        score = score + 1
    else:
        print("Wrong Answer")

    print("Correct one is","c")
    print("Your score is :", score)


def cc_prog():
    score = 0
    score = int(score)


    print("what is ball??")
    a=print("(a)tree")
    b=print("(b)veg")
    c=print("(c)toy")
    d=print("(d)nothing")
    opt=input("Choose your option from (a)(b)(c)(d):")
    ans="c"
    if opt==ans:
        print("Correct Answer")
        score = score + 1
    else:
        print("Wrong Answer")

    print("Correct one is","c")

    print("\nwhat is blue??")
    q = print("(a)fruit")
    q = print("(b)colour")
    r = print("(c)song")
    s = print("(d)nothing")
    opt = input("Choose your option from (a)(b)(c)(d):")
    an = "b"
    if opt == an:
        print("Correct Answer")
        score = score + 1

    else:
        print("Wrong Answer")

    print("Correct one is", "b")
    print("Your score is :", score)
    return




def c_prog():
    score = 0
    score = int(score)

    print("what is ball??")
    a=print("(a)tree")
    b=print("(b)veg")
    c=print("(c)toy")
    d=print("(d)nothing")
    opt=input("Choose your option from (a)(b)(c)(d):")
    ans="c"
    if opt==ans:
        print("Correct Answer")
        score = score + 1
    else:
        print("Wrong Answer")

    print("Correct one is","c")

    print("\nwhat is blue??")
    q = print("(a)fruit")
    q = print("(b)colour")
    r = print("(c)song")
    s = print("(d)nothing")
    opt = input("Choose your option from (a)(b)(c)(d):")
    an = "b"
    if opt == an:
        print("Correct Answer")
        score = score + 1
    else:
        print("Wrong Answer")

    print("Correct one is", "b")
    print("Your score is :", score)
    return




for i in range(1):
       sele = input('''\nChoose Subject for Quiz
           PYTHON
           JAVA 
           C++
           C:\n''')
       l1=["python","java","c++","c"]

       level=input("Choose level of Difficulty: easy or hard:\n")
       l2=["easy","hard"]

       if (sele == l1[0]):
           python_prog()


       elif (sele == l1[1]):
           if (level==l2[0]):
            java_prog_easy()
           else:
               java_prog_hard()

       elif (sele == l1[2]):
           cc_prog()

       elif (sele == l1[3]):
           c_prog()
       else:
          print("Choose correctly")
