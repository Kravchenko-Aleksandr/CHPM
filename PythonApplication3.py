import numpy as np
a=np.matrix('2 3 1; -1 1 0; 1 2 -1')
b=np.matrix('1 2 1; 0 1 2; 3 1 1')
print('A-B ',a-b)


a1=np.matrix('-1 0 2; 0 1 0; 1 2 -1')
print('A^2 ', a1*2)

a2=np.matrix('5 8 -4; 6 9 -5; 4 7 -3')
b2=np.matrix('3 2 5; 4 -1 3; 9 6 5')
print('A*B ', a2*b2)

a3=np.matrix('2 4 5; 1 1 2; 2 4 3')
det_a3=np.linalg.det(a3)
print ('det_a3 ', det_a3)

a4=np.matrix('2 3 4 1; 1 2 3 4; 3 4 1 2; 4 1 2 3')
det_a4=np.linalg.det(a4)
print('det_a4 ', det_a4)

a5=np.matrix('2 5 7; 6 3 4; 5 -2 -3')
a5=np.linalg.inv(a5)
print('a5',a5)

a6=np.matrix('-2 3 1 -1; 3 2 1 4; 1 2 3 4; 0 2 3 3')
rank=np.linalg.matrix_rank(a6)
print(a6,'\n' 'rank ', rank)

an1=np.array([[7, 3, 6],[7, 9, 9],[2, 4, 9]])
det_an1=np.linalg.det(an1)
an2=np.array([[-1, 3, 6],[5, 9, 9],[28, 4, 9]])
det_an2=np.linalg.det(an2)
an3=np.array([[7, -1, 6],[7, 5, 9],[2, 28, 9]])
det_an3=np.linalg.det(an3)
an4=np.array([[7, 3, -1],[7, 9, 5], [2, 4, 28]])
det_an4=np.linalg.det(an4)
print('an1= ', det_an1, 'an2= ', det_an2, 'an3=', det_an3, 'an4=', det_an4)
x=det_an2/det_an1
y=det_an3/det_an1
z=det_an4/det_an1
print('x= ', x, '\n' 'y= ', y,'\n' 'z= ', z, '\n')


a8=np.matrix([[2, -1, 1],[3, 4, -2],[1, -3, 1]])
a18=np.matrix([[5],[-3],[4]])
a28=np.linalg.inv(a8)
res=a28*a18
print(res,'\n',np.linalg.solve(a8,a18))
