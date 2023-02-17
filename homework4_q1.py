def cal(pi,p,c_list,i):
    answer=1
    for j in range(i+1):
        if c_list[j]==0:
            answer*=p
        if c_list[j]==1:
            answer*=(1-p)
    answer*=pi
    return answer


def my_Bayes_candy(pi_list, p_list, c_list):
    
    posterior_probabilities = [[0]*5 for i in range(10)] # Default initialization with 0s.
    
    for i in range(10):
        sum=0
        for k in range(5):
            sub=cal(pi_list[k],p_list[k],c_list,i)
            sum+=sub
        for j in range(5):
            answer=cal(pi_list[j],p_list[j],c_list,i)/sum
            posterior_probabilities[i][j]=answer
    
    for i in range(10):
        print(posterior_probabilities[i])
    return posterior_probabilities