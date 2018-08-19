import random
random.seed(500)
w1 = random.randrange(-2, 2)
w2 = random.randrange(-2, 2)
bias = random.randrange(-2, 2)
x1 = [-1,-1,1,1]
x2 = [-1,1,-1,1]
y = [-1,-1,-1,1]  #and gate
threshold  = 2
epoch = int(input("The No. of irratrition :"))
print('Epoch =',0)
learning_rate = 1
cnt = 0
cn = 0
op = 0
check = 0
cnt_new = 0
while True:
    w1_new = w1
    w2_new = w2
    bias_new = bias
    net_input = bias_new+(w1_new*x1[cnt]+x2[cnt]*w2_new)
    if net_input>=threshold:
        y_new = 1
    elif net_input == threshold:
        y_new = 0
    else:
        y_new = -1
    print(cnt, ':', 'W1: ', w1, 'W2: ', w2,'Bias:',bias_new ,"Output:", y_new, 'Target:', y[cnt])
    cnt += 1
    # print('why =',cnt ,net_input ,y[3] )
    #if cnt ==4 and y_new==1 and y[3]==1 and cn==4*epoch-1:
        #break

    if check == 4*epoch-1:
        print("*******************The network is trained*******************")
        print('W1_trained: ', w1, '|', 'W2_trained: ', w2, '|', 'Bias: ', bias_new)
        print('************************************************************')
        break
    if cnt == 4:
        print('Epoch =',op+1)
        w1_ne = w1_new+learning_rate*y[cnt_new]*x1[cnt_new]
        w2_ne = w2_new+learning_rate*y[cnt_new]*x2[cnt_new]
        bias_ne = bias_new+learning_rate*y[cnt_new]
        bias = bias_ne
        w1 = w1_ne
        w2 = w2_ne
        op+=1
        cnt =0
        cn = 0
        cnt_new+=1
    cnt_new =0
    check+=1
    cn += 1