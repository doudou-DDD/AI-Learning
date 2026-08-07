score=float(input('What is your score? '))
if 90<=score<=100:
    print('You are excellent!')      
elif 60<=score<90:
    print('You are pass!')
elif 0<=score<60:
    print('You need to improve!')   
else:
    print('Invalid score!')