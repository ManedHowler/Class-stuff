
# Input the student's test score and class rank
testScoreString = input("Enter the student's test score: ")
classRankString = input("Enter the student's class rank: ")

# Convert scores into integers
testScore = int(testScoreString)
classRank = int(classRankString)

if testScore >= 90:
  if classRank >= 25:
    print("Accept")
  else:
    print("Reject")
else:
  if testScore >= 80:
    if classRank >= 50:
      print("Accept")
    else:
      print("Reject")
  else:
    if testScore >= 70:
      if classRank >= 75:
        print("Accept")
      else:
        print("Reject")
    else:
      print("Reject")
