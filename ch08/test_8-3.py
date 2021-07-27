import tensorflow as tf

tf.compat.v1.disable_eager_execution()

# tf.diag(diagonal)  返回一个给定对角值的对角tensor

# diagonal = tf.constant([1, 2, 3, 4])
# sess = tf.compat.v1.Session()
# print(sess.run(tf.compat.v1.diag(diagonal)))

# tf.diag(diagonal)  与diag作用相反

# diagonal = tf.constant([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
# sess = tf.compat.v1.Session()
# print(sess.run(tf.compat.v1.diag_part(diagonal)))
# print(sess.run(tf.compat.v1.trace(diagonal)))

# 调换tensor的维度顺序，按照列表perm的维度排列调换tensor的顺序

x = tf.constant([[1, 2, 3], [4, 5, 6]])
sess = tf.compat.v1.Session()
print(sess.run(tf.transpose(x, perm=[1, 0])))

# tf.matmul(a,b,transpose_a=False,transpose_b=False,a_is_sparse=False,b_is_sparse=False,name=None)  矩阵相乘

# tf.matrix_determinant(input,name=None)  返回矩阵的行列式

# tf.matrix_inverse(input,adjoint=None,name=None)  求方阵的逆矩阵，adjoint为True时，计算输入共轭矩阵的逆矩阵

# tf.cholesky(input,name=None)  对输入方阵cholesky分解，即把一个对称正定的矩阵表示成一个下三角矩阵L和其转置的乘机的分解A=LL^T

# tf.matrix_solve(matrix,rhs,adjoint=None,name=None)  求解  matrix为方阵，shape为[M,M],rhs的shape为[M,K],output为[M,K]

