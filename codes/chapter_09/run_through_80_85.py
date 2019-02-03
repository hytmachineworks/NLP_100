# coding = utf-8
"""
create on : 2018/12/15
project name : NLP_100
file name : run_through_80_85

easy to try problem no.80 to 85
"""
import datetime
from problem_no_80 import problem_no_80
from problem_no_81 import problem_no_81
from problem_no_82 import problem_no_82
from problem_no_83 import problem_no_83
from problem_no_84 import problem_no_84
from problem_no_85 import problem_no_85


if __name__ == "__main__":
    start = datetime.datetime.now()

    print("problem no 80 ----------------------")
    print(problem_no_80())
    print("problem no 81 ----------------------")
    print(problem_no_81())
    print("problem no 82 ----------------------")
    print(problem_no_82())
    print("problem no 83 ----------------------")
    print(problem_no_83())
    print("problem no 84 ----------------------")
    print(problem_no_84())
    print("problem no 85 ----------------------")
    print(problem_no_85())

    end = datetime.datetime.now()
    elapse = end - start

    print("\nrun through problem no.80 to 85 finished !!!!!!\n")
    print("problem no.80 to 85 start at datetime :", start)
    print("problem no.80 to 85 end at datetime :", end)
    print("problem no.80 to 85 elapsed time", elapse)
