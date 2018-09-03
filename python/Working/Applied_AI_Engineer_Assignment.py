import tensorflow as tf
import numpy as np

m = 5
n = 2
p = 6

mat1 = np.random.randint(0,100,(m,n))
mat2 = np.random.randint(0,100,(n,p))

t1 = tf.convert_to_tensor(mat1,np.float32) 
t2 = tf.convert_to_tensor(mat2,np.float32) 

matrix_mul = tf.matmul(t1,t2)

mat3 = np.random.randint(0,100,(m,n))
mat4 = np.random.randint(0,100,(m,n))

t3 = tf.convert_to_tensor(mat3,tf.float64) 
t4 = tf.convert_to_tensor(mat4,tf.float64) 

t3 = tf.reshape(t3, [-1])
t4 = tf.reshape(t4,[-1])

cov_xx = 1 / (tf.shape(t3)[0] - 1) * tf.reduce_sum((t3 - tf.reduce_mean(t3))**2)
cov_yy = 1 / (tf.shape(t3)[0] - 1) * tf.reduce_sum((t4 - tf.reduce_mean(t4))**2)
cov_xy = 1 / (tf.shape(t3)[0] - 1) * tf.reduce_sum((t3 - tf.reduce_mean(t4)) * (t4 - tf.reduce_mean(t4)))

#create  tensorflow session
with tf.Session() as sess:
    print("Multiplication Matrix: \n",sess.run(matrix_mul))
    sess.run([cov_xx, cov_yy, cov_xy])
    cov = tf.constant([[cov_xx.eval(), cov_xy.eval()], [cov_xy.eval(),cov_yy.eval()]])
    print("\nCovariance Matrix: \n",cov.eval())
