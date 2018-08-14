import tensorflow as tf
x = tf.add(2,3)
with tf.Session() as sess:
    writer = tf.train.SummaryWriter(sess.graph)
    print(sess.run(x))
writer.close()
