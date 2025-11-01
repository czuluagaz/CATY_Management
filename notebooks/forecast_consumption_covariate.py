# Forecast consumption of utilities for a household using weather as a covariate
# Forecast consumption of utilities using building characteristics as a covariate
# Forecast consumption of utilities using weather and building characteristics as covariates
# Forecast consumption of utilities using weather and building characteristics as covariates and interactions
# Use Mlflow to log the results of the models
# Use the best model to forecast the consumption of utilities for a household
# date: 2024-09-25
# author: Camilo Zuluaga

import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt
