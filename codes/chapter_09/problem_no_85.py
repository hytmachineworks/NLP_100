# coding = utf-8
"""
create on : 2018/12/07
project name : NLP_100
file name : problem_no_85 

"""
import datetime

from scipy.sparse import load_npz
from scipy.sparse.linalg import svds
import numpy as np
from numpy import savez


def problem_no_85():
    """ word vector x reduce to 300 dimensions

    :return: message
    """

    start = datetime.datetime.now()
    print("start datetime :", start)

    x_vector = load_npz("./x_vector.npz")
    x = x_vector.tocsr()
    print("read x vector finish")

    u, s, vt = svds(x, k=300, return_singular_vectors="vh")
    savez("./x_vector_vt.npz", vt)

    del u, s

    print("calculate svd finish")

    v = np.transpose(vt)
    x_svd = x @ v

    savez("./x_vector_svd.npz", x_svd)

    print("calculate reduce dimension finish")

    end = datetime.datetime.now()
    print("end datetime :", end)

    elapse = end - start
    print("elapsed time", elapse)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_85())
