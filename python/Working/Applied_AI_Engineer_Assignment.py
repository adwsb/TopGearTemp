import tensorflow as tf 

c = tf.constant([[1,2,3], [4,5,6]])
d = tf.constant([[7,8], [9,10], [11,12]])
e = tf.matmul(c,d)

# sess = tf.Session()
# result = sess.run(e)

tf.Print(e,e)