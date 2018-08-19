import matplotlib.pyplot as plt
#adaline
w1 = 0.1
w2 = 0.1
bias = 0.1
alpha = 0.01
x1 = [-1,-1,1,1]
x2 = [-1,1,-1,1]
y = [1,1,1,-1]  #and gate
threshold  = 2
cnt = 0
ep = 0
(x_plt, y_plt) = [] , []
sum_of_error = 0
per_error = 1.05
perror = 0
while True:
    w1_new = w1
    w2_new = w2
    bias_new = bias
    y_in = bias_new+(x1[cnt]*w1_new)+(x2[cnt]*w2_new)
    error = (y[cnt]-y_in)**2
    e = y[cnt] - y_in
    w1 = w1_new + (alpha * e * x1[cnt])
    w2 = w2_new + (alpha * e * x2[cnt])
    bias = bias +(alpha* e)
    sum_of_error = sum_of_error + error
    print(cnt, ':', 'W1: ', float(w1), 'W2: ', w2, 'Bias:', bias_new, "Output:", y_in, 'Target:', y[cnt],'Error:', e)
    cnt+=1


    if sum_of_error <= per_error and cnt==4:
        print("*******************The network is trained************************************************")
        print('W1_trained: ', w1, '|', 'W2_trained: ', w2, '|', 'Bias: ', bias_new, 'Error:', sum_of_error)
        print('******************************************************************************************')
        break

    elif cnt == 4 :
        x_plt.append(ep)
        y_plt.append(sum_of_error)
        # plt.plot(x_plt, y_plt)
        # plt.xlabel('Epoch')
        # plt.ylabel('RMS_value')
        # plt.title('ARDALINE')
        # plt.grid(True)
        # plt.show(block=False)
        # time.sleep(0.1)
        # plt.close()
        print('RMS = ',sum_of_error)
        print('Epoch:',ep)
        sum_of_error = 0
        ep+=1
        cnt = 0


plt.plot(x_plt, y_plt)
plt.xlabel('Epoch')
plt.ylabel('RMS_value')
plt.title('ARDALINE')
plt.grid(True)
plt.show()
