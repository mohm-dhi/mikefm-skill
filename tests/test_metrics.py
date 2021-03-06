import pytest
import numpy as np

from mikefm_skill.metrics import bias, mean_absolute_error, nash_sutcliffe_efficiency, root_mean_squared_error, corr_coef, scatter_index, r2


def test_nse_optimal():

    np.random.seed(42)
    obs = np.random.uniform(size=100)

    assert nash_sutcliffe_efficiency(obs, obs) == 1.0

def test_nse_suboptimal():

    obs = np.array([1.0,0.5,0])
    mod = np.array([1.0,0.0,0.5])

    assert nash_sutcliffe_efficiency(obs, mod) == 0.0

def test_bias():
    obs = np.arange(100)
    mod = obs + 1.0

    assert bias(obs, mod) == 1.0

def test_rmse():
    obs = np.arange(100)
    mod = obs + 1.0

    rmse = root_mean_squared_error(obs,mod)

    assert rmse == 1.0

def test_mae():
    obs = np.arange(100)
    mod = obs + 1.0

    mae = mean_absolute_error(obs,mod)

    assert mae == 1.0

def test_corr_coef():

    obs = np.arange(100)
    mod = obs + 1.0

    r = corr_coef(obs,mod)

    assert -1.0 <= r <= 1.0

def test_scatter_index():

    obs = np.arange(100)
    mod = obs + 1.0

    si = scatter_index(obs,mod)

    assert si >= 0.0

def test_r2():

    obs = np.arange(100)
    mod = obs + 1.0

    res = r2(obs,mod)
    assert np.isscalar(res)
    assert 0.0 <= res <= 1.0