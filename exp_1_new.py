import random
random.seed(500)
w1 = random.randrange(0, 2)
w2 = random.randrange(0, 2)
#X = [[-1,-1],[-1,1],[1,-1],[1,1]]
x1 = [-1,-1,1,1]
x2 = [-1,1,-1,1]
y = [-1,-1,-1,1]  #and gate
# print(w1,w2)
epoch = int(input("Enter no. of irrition :"))
learning_rate = 0.5
cnt = 0
cn = 0
op = 0
while True:
    w1_new = w1
    w2_new = w2
    net_input = (w1_new*x1[cnt]+x2[cnt]*w2_new)
    print(cnt, ':', 'W1: ', w1, 'W2: ', w2, "Output:", net_input, 'Target:', y[cnt])
    cnt += 1
   # print('why =',cnt ,net_input ,y[3] )
    if cnt ==4 and net_input==2 and y[3]==1:
        print("The network is trained:",'W1_trained: ',w1,'W2_trained: ',w2)
        break
    if cn == 4*epoch:
        break
    if cnt ==4:
        print('Epoch =',op)
        w1_ne = 1 * x1[cn] * net_input
        w2_ne = 1 * x2[cn] * net_input
        w1 = w1_ne
        w2 = w2_ne
        op+=1
        cnt =0
    cn += 1