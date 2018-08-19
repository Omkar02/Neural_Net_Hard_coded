import matplotlib.pyplot as plt

w11 = 0.05
w12 = 0.1
w21 = 0.2
w22 = 0.2
print('Epoch:' ,0)
bias_1 = 0.3
bias_2 = 0.15
alpha = 0.05
x1 = [1,1,-1,-1]
x2 = [1,-1,1,-1]
y = [1,-1,1,-1]
cnt = 0
ep = 0
(x_plt, y_plt) = [] , []
sum_of_error = 0
per_error = 1
perror = 0
while True:
    w11_new = w11
    w12_new = w12
    w21_new = w21
    w22_new = w22
    bias_new_1 = bias_1
    bias_new_2 = bias_2
    z1 = bias_new_1 + (x1[cnt]*w11_new)+(x2[cnt]*w21_new)
    z2 = bias_new_2 + (x1[cnt]*w12_new)+(x2[cnt]*w22_new)
    y_in = 0.5+(z1*0.5)+(z2*0.5)
    if y_in>0:
        y_in=1
    elif y_in<0:
        y_in =-1
    elif y_in ==0:
        y_in =0
    error = (y[cnt]-y_in)**2
    e = y[cnt] - y_in
    w11 = w11_new + (alpha * (y[cnt]-z1) * x1[cnt])
    w12 = w12_new + (alpha * (y[cnt]-z2) * x1[cnt])
    w21 = w21_new + (alpha * (y[cnt]-z1) * x2[cnt])
    w22 = w22_new + (alpha * (y[cnt]-z2) * x2[cnt])
    bias_1 = bias_new_1 +(alpha*(y[cnt]-z1))
    bias_2 = bias_new_2 + (alpha * (y[cnt]-z2))
    sum_of_error = sum_of_error + error

    print(cnt, ':', 'W11: ',format(w11,'.2f'), 'W12: ', format(w12, '.2f'), 'W21: ',format(w21,'.2f'), 'W22: ', format(w22, '.2f')
          , 'Bias_1:', format(bias_1, '.2f'), 'Bias_2:', format(bias_2, '.2f'), "Output:",format(y_in, '.2f'), 'Target:', y[cnt],'z1:',format(z1, '.2f')
          ,'z2:',format(z2, '.2f'),'Error:', e)
    cnt+=1
    if cnt == 4 :
        x_plt.append(ep)
        y_plt.append(sum_of_error)
        print('RMS = ', sum_of_error)
        print('Epoch:',ep+1)
        # plt.plot(x_plt, y_plt)
        # plt.xlabel('Epoch')
        # plt.ylabel('RMS_value')
        # plt.title('ARDALINE')
        # plt.grid(True)
        # plt.show(block=False)
        # time.sleep(0.1)
        # plt.close()

        if sum_of_error <= per_error and cnt == 4:
            print("*******************The network is trained************************************************")
            print('W11: ', w11, '|', 'W12: ', w12, '|', 'Bias1: ', bias_1, 'W21: ', w21, '|', 'W22: ', w22, '|','Bias2: ',bias_2, 'Rms_Error:', sum_of_error)
            print('******************************************************************************************')
            break
        sum_of_error = 0
        ep+=1
        cnt = 0









plt.plot(x_plt, y_plt)
plt.xlabel('Epoch')
plt.ylabel('RMS_value')
plt.title('MARDALINE')
plt.grid(True)
plt.show()
