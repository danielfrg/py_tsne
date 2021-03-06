def test_seed():
    import numpy as np
    from sklearn.datasets import load_iris

    from tsne import bh_sne

    iris = load_iris()

    X = iris.data
    # y = iris.target

    t1 = bh_sne(X, random_state=np.random.RandomState(0), copy_data=True)
    t2 = bh_sne(X, random_state=np.random.RandomState(0), copy_data=True)

    assert t1.shape[0] == 150
    assert t1.shape[1] == 2
    assert np.all(t1 == t2)
