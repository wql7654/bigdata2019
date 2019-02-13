def tw_ti(x):
    return x*2

m_result=map(tw_ti,[1,2,3,4])
l_result=list(m_result)
result2=list(filter(tw_ti,[1,2,3,4]))

print(l_result)
print(result2)