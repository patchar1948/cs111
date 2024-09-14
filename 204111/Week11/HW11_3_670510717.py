#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW11_3
# 204111 Sec 003

def main():
    runner_up()
def runner_up() -> None:
    t_student = int(input("Total student:"))
    print("Enter score:")
    max_score = 0
    average =  0.0
    for i in range(0, t_student):
        score = int(input())

        if score > max_score:
            runner_score = max_score
            max_score = score
        elif score < max_score and score > runner_score: # เช็คที่ 2
            runner_score = score
        average += score
    average_score = average / t_student
    
    print("---")
    print("Max score is:", '%.2f' %(max_score))
    if runner_score == 0:
        print("Runner up: is None")
    else:
        print("Runner up is:", '%.2f' %(runner_score))
        
    print("Average is:", '%.2f' %(average_score))

if __name__ == "__main__":
    main()
