def main():
    runner_up()
def runner_up() -> None:
    total_student = int(input('Total student:'))
    print('Enter score:')
    max_score = 0.0
    average = 0.0

    for i in range(total_student):
        score = int(input())
        if score > max_score:
            runner_score = max_score
            max_score = score
        elif score < max_score and score > runner_score:
            runner_score = score
        average += score
        average_score = average / total_student
    print('---')
    print('Max score is:', '%.2f' %(max_score))
    if runner_score == 0:
        print('Runner up is: None')
    else:
        print('Runner up is:', '%.2f' %(runner_score))
    
    print('Average is:', '%.2f' %(average_score))




if __name__ == '__main__':
    main()