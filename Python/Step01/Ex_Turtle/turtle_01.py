#============ 기본적인 방향 ===========================
# import turtle as t
# t.shape('turtle')
# t.forward(100)
# # t.fd(100)
# t.right(100)
# # t.rt(100)
# t.left(10)
# # lt(100)
# t.backward(100)
# # t.back(100)
#=============== for 문을 이용한 그리기 ===============
# for i in range(5):
#     t.fd(150)
#     t.right(360)
#================== 육각형 그리기 =====================
# import turtle as t
# t.shape('turtle')
# t.fd(100)
# t.lt(60)
# t.fd(100)
# t.lt(60)
# t.fd(100)
# t.lt(60)
# t.fd(100)
# t.lt(60)
# t.fd(100)
# t.lt(60)
# t.fd(100)
#==================다각형 그리기 =======================
# t.rt(30)
# t.fd(100)
# t.rt(30)
# t.fd(100)
# t.rt(30)
# t.fd(100)
# t.rt(30)
# t.fd(100)
# t.rt(30)
# t.fd(100)
# t.rt(30)
# t.fd(100)
# t.rt(30)
# t.fd(100)
# t.rt(30)
# t.fd(100)
# t.rt(30)
# t.fd(100)
# t.rt(30)
# t.fd(100)
# t.rt(30)
# t.fd(100)
# t.rt(30)
# t.fd(100)
#================= n 각형 그리기(미완) ===========================
# import turtle as t
# t.shape('arrows')
# 
# for i in range(n):
#     p.forward(50)
#     p.right(360 / n)
#     
# p.color('red')

#================= 도형 색 채우기 ==========================
import turtle as t
t.shape('turtle')
t.color('blue')
t.begin_fill()
for i in range(6):
    t.fd(50)
    t.rt(360 / 6)
t.end_fill()



    