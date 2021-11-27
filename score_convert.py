# get a number and if that number is over 90, print A, if it is over 80, print B, if it is over 70, print C, if it is over 60, print D, if it is less than 60, print F


def score_convert(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

scores = []
for i in range(3):
    scores.append(int(input("Enter a score: ")))
sum = 0
for score in scores:
    print(score_convert(score))
    sum += score

print("The average score is: ", sum / len(scores))