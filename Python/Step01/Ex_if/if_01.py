#===========if 사용문===================

# pocket = ['paper','cellphone','money']
# if 'money' in pocket:
#     print("택시를 타고 가라")
# else:
#     print("걸어 가라")
#     

#==========if를 사용하지 않는 PASS =====

# pocket=['paper', 'money', 'cellphone']
# if 'money' in pocket:
#     pass
# else:
#     print("카드를 꺼내라")

#========== 여러 조건의 경우 ===========
# pocket=['paper', 'cellphone']
# card=0
# if 'money' in pocket:
#     print("택시를 타고 가라")
# else:
#     if card:
#         print("택시를 타고 가라")
#     else:
#         print("걸어 가라")

#========== elif 사용 ==================
# pocket = ['paper', 'cellphone']
# card=1
# if 'money' in pocket:
#     print("택시를 타고 가라")
# elif card:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")

# =========If문 한 줄로 작성하기==========
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")



        
        
    
    