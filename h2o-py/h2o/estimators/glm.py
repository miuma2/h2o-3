#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from __future__ import absolute_import, division, print_function, unicode_literals

from h2o.estimators.estimator_base import H2OEstimator
from h2o.exceptions import H2OValueError
from h2o.frame import H2OFrame
from h2o.utils.typechecks import assert_is_type, Enum, numeric
import h2o


class H2OGeneralizedLinearEstimator(H2OEstimator):
    """
    Generalized Linear Modeling

    Fits a generalized linear model, specified by a response variable, a set of predictors, and a
    description of the error distribution.

    Returns
    -------
    A subclass of ModelBase is returned. The specific subclass depends on the machine learning task at hand
    (if it's binomial classification, then an H2OBinomialModel is returned, if it's regression then a
    H2ORegressionModel is returned). The default print-out of the models is shown, but further GLM-specific
    information can be queried out of the object. Upon completion of the GLM, the resulting object has
    coefficients, normalized coefficients, residual/null deviance, aic, and a host of model metrics including
    MSE, AUC (for logistic regression), degrees of freedom, and confusion matrices.
    """

    algo = "glm"

    def __init__(self, **kwargs):
        super(H2OGeneralizedLinearEstimator, self).__init__()
        self._parms = {}
        names_list = {"model_id", "training_frame", "validation_frame", "nfolds", "seed",
                      "keep_cross_validation_predictions", "keep_cross_validation_fold_assignment", "fold_assignment",
                      "fold_column", "response_column", "ignored_columns", "ignore_const_cols", "score_each_iteration",
                      "offset_column", "weights_column", "family", "tweedie_variance_power", "tweedie_link_power",
                      "solver", "alpha", "lambda_", "lambda_search", "early_stopping", "nlambdas", "standardize",
                      "missing_values_handling", "compute_p_values", "remove_collinear_columns", "intercept",
                      "non_negative", "max_iterations", "objective_epsilon", "beta_epsilon", "gradient_epsilon", "link",
                      "prior", "lambda_min_ratio", "beta_constraints", "max_active_predictors", "interactions",
                      "balance_classes", "class_sampling_factors", "max_after_balance_size",
                      "max_confusion_matrix_size", "max_hit_ratio_k", "max_runtime_secs"}
        if "Lambda" in kwargs: kwargs["lambda_"] = kwargs.pop("Lambda")
        for pname, pvalue in kwargs.items():
            if pname == 'model_id':
                self._id = pvalue
                self._parms["model_id"] = pvalue
            elif pname in names_list:
                # Using setattr(...) will invoke type-checking of the arguments
                setattr(self, pname, pvalue)
            else:
                raise H2OValueError("Unknown parameter %s = %r" % (pname, pvalue))

    @property
    def training_frame(self):
        """str: Id of the training data frame (Not required, to allow initial validation of model parameters)."""
        return self._parms.get("training_frame")

    @training_frame.setter
    def training_frame(self, training_frame):
        assert_is_type(training_frame, None, H2OFrame)
        self._parms["training_frame"] = training_frame


    @property
    def validation_frame(self):
        """str: Id of the validation data frame."""
        return self._parms.get("validation_frame")

    @validation_frame.setter
    def validation_frame(self, validation_frame):
        assert_is_type(validation_frame, None, H2OFrame)
        self._parms["validation_frame"] = validation_frame


    @property
    def nfolds(self):
        """int: Number of folds for N-fold cross-validation (0 to disable or >= 2). (Default: 0)"""
        return self._parms.get("nfolds")

    @nfolds.setter
    def nfolds(self, nfolds):
        assert_is_type(nfolds, None, int)
        self._parms["nfolds"] = nfolds


    @property
    def seed(self):
        """int: Seed for pseudo random number generator (if applicable) (Default: -1)"""
        return self._parms.get("seed")

    @seed.setter
    def seed(self, seed):
        assert_is_type(seed, None, int)
        self._parms["seed"] = seed


    @property
    def keep_cross_validation_predictions(self):
        """bool: Whether to keep the predictions of the cross-validation models. (Default: False)"""
        return self._parms.get("keep_cross_validation_predictions")

    @keep_cross_validation_predictions.setter
    def keep_cross_validation_predictions(self, keep_cross_validation_predictions):
        assert_is_type(keep_cross_validation_predictions, None, bool)
        self._parms["keep_cross_validation_predictions"] = keep_cross_validation_predictions


    @property
    def keep_cross_validation_fold_assignment(self):
        """bool: Whether to keep the cross-validation fold assignment. (Default: False)"""
        return self._parms.get("keep_cross_validation_fold_assignment")

    @keep_cross_validation_fold_assignment.setter
    def keep_cross_validation_fold_assignment(self, keep_cross_validation_fold_assignment):
        assert_is_type(keep_cross_validation_fold_assignment, None, bool)
        self._parms["keep_cross_validation_fold_assignment"] = keep_cross_validation_fold_assignment


    @property
    def fold_assignment(self):
        """
        Enum["auto", "random", "modulo", "stratified"]: Cross-validation fold assignment scheme, if fold_column is not
        specified. The 'Stratified' option will stratify the folds based on the response variable, for classification
        problems. (Default: "auto")
        """
        return self._parms.get("fold_assignment")

    @fold_assignment.setter
    def fold_assignment(self, fold_assignment):
        assert_is_type(fold_assignment, None, Enum("auto", "random", "modulo", "stratified"))
        self._parms["fold_assignment"] = fold_assignment


    @property
    def fold_column(self):
        """str: Column with cross-validation fold index assignment per observation."""
        return self._parms.get("fold_column")

    @fold_column.setter
    def fold_column(self, fold_column):
        assert_is_type(fold_column, None, str)
        self._parms["fold_column"] = fold_column


    @property
    def response_column(self):
        """str: Response variable column."""
        return self._parms.get("response_column")

    @response_column.setter
    def response_column(self, response_column):
        assert_is_type(response_column, None, str)
        self._parms["response_column"] = response_column


    @property
    def ignored_columns(self):
        """List[str]: Names of columns to ignore for training."""
        return self._parms.get("ignored_columns")

    @ignored_columns.setter
    def ignored_columns(self, ignored_columns):
        assert_is_type(ignored_columns, None, [str])
        self._parms["ignored_columns"] = ignored_columns


    @property
    def ignore_const_cols(self):
        """bool: Ignore constant columns. (Default: True)"""
        return self._parms.get("ignore_const_cols")

    @ignore_const_cols.setter
    def ignore_const_cols(self, ignore_const_cols):
        assert_is_type(ignore_const_cols, None, bool)
        self._parms["ignore_const_cols"] = ignore_const_cols


    @property
    def score_each_iteration(self):
        """bool: Whether to score during each iteration of model training. (Default: False)"""
        return self._parms.get("score_each_iteration")

    @score_each_iteration.setter
    def score_each_iteration(self, score_each_iteration):
        assert_is_type(score_each_iteration, None, bool)
        self._parms["score_each_iteration"] = score_each_iteration


    @property
    def offset_column(self):
        """
        str: Offset column. This will be added to the combination of columns before applying the link function.
        """
        return self._parms.get("offset_column")

    @offset_column.setter
    def offset_column(self, offset_column):
        assert_is_type(offset_column, None, str)
        self._parms["offset_column"] = offset_column


    @property
    def weights_column(self):
        """
        str: Column with observation weights. Giving some observation a weight of zero is equivalent to excluding it
        from the dataset; giving an observation a relative weight of 2 is equivalent to repeating that row twice.
        Negative weights are not allowed.
        """
        return self._parms.get("weights_column")

    @weights_column.setter
    def weights_column(self, weights_column):
        assert_is_type(weights_column, None, str)
        self._parms["weights_column"] = weights_column


    @property
    def family(self):
        """
        Enum["gaussian", "binomial", "quasi_binomial", "multinomial", "poisson", "gamma", "tweedie"]: Family. Use
        binomial for classification with logistic regression, others are for regression problems. (Default: "gaussian")
        """
        return self._parms.get("family")

    @family.setter
    def family(self, family):
        assert_is_type(family, None, Enum("gaussian", "binomial", "quasi_binomial", "multinomial", "poisson", "gamma", "tweedie"))
        self._parms["family"] = family


    @property
    def tweedie_variance_power(self):
        """float: Tweedie variance power (Default: 0)"""
        return self._parms.get("tweedie_variance_power")

    @tweedie_variance_power.setter
    def tweedie_variance_power(self, tweedie_variance_power):
        assert_is_type(tweedie_variance_power, None, numeric)
        self._parms["tweedie_variance_power"] = tweedie_variance_power


    @property
    def tweedie_link_power(self):
        """float: Tweedie link power (Default: 1)"""
        return self._parms.get("tweedie_link_power")

    @tweedie_link_power.setter
    def tweedie_link_power(self, tweedie_link_power):
        assert_is_type(tweedie_link_power, None, numeric)
        self._parms["tweedie_link_power"] = tweedie_link_power


    @property
    def solver(self):
        """
        Enum["auto", "irlsm", "l_bfgs", "coordinate_descent_naive", "coordinate_descent"]: AUTO will set the solver
        based on given data and the other parameters. IRLSM is fast on on problems with small number of predictors and
        for lambda-search with L1 penalty, L_BFGS scales better for datasets with many columns. Coordinate descent is
        experimental (beta). (Default: "auto")
        """
        return self._parms.get("solver")

    @solver.setter
    def solver(self, solver):
        assert_is_type(solver, None, Enum("auto", "irlsm", "l_bfgs", "coordinate_descent_naive", "coordinate_descent"))
        self._parms["solver"] = solver


    @property
    def alpha(self):
        """
        List[float]: distribution of regularization between L1 and L2. Default value of alpha is 0 when SOLVER =
        'L-BFGS', 0.5 otherwise
        """
        return self._parms.get("alpha")

    @alpha.setter
    def alpha(self, alpha):
        assert_is_type(alpha, None, numeric, [numeric])
        self._parms["alpha"] = alpha


    @property
    def lambda_(self):
        """List[float]: regularization strength"""
        return self._parms.get("lambda")

    @lambda_.setter
    def lambda_(self, lambda_):
        assert_is_type(lambda_, None, numeric, [numeric])
        self._parms["lambda"] = lambda_


    @property
    def lambda_search(self):
        """
        bool: use lambda search starting at lambda max, given lambda is then interpreted as lambda min (Default: False)
        """
        return self._parms.get("lambda_search")

    @lambda_search.setter
    def lambda_search(self, lambda_search):
        assert_is_type(lambda_search, None, bool)
        self._parms["lambda_search"] = lambda_search


    @property
    def early_stopping(self):
        """
        bool: stop early when there is no more relative improvement on train or validation (if provided) (Default: True)
        """
        return self._parms.get("early_stopping")

    @early_stopping.setter
    def early_stopping(self, early_stopping):
        assert_is_type(early_stopping, None, bool)
        self._parms["early_stopping"] = early_stopping


    @property
    def nlambdas(self):
        """
        int: Number of lambdas to be used in a search. Default indicates: If alpha is zero, with lambda search set to
        True, the value of nlamdas is set to 30 (fewer lambdas are needed for ridge regression) otherwise it is set to
        100. (Default: -1)
        """
        return self._parms.get("nlambdas")

    @nlambdas.setter
    def nlambdas(self, nlambdas):
        assert_is_type(nlambdas, None, int)
        self._parms["nlambdas"] = nlambdas


    @property
    def standardize(self):
        """bool: Standardize numeric columns to have zero mean and unit variance (Default: True)"""
        return self._parms.get("standardize")

    @standardize.setter
    def standardize(self, standardize):
        assert_is_type(standardize, None, bool)
        self._parms["standardize"] = standardize


    @property
    def missing_values_handling(self):
        """
        Enum["mean_imputation", "skip"]: Handling of missing values. Either MeanImputation or Skip. (Default:
        "mean_imputation")
        """
        return self._parms.get("missing_values_handling")

    @missing_values_handling.setter
    def missing_values_handling(self, missing_values_handling):
        assert_is_type(missing_values_handling, None, Enum("mean_imputation", "skip"))
        self._parms["missing_values_handling"] = missing_values_handling


    @property
    def compute_p_values(self):
        """
        bool: request p-values computation, p-values work only with IRLSM solver and no regularization (Default: False)
        """
        return self._parms.get("compute_p_values")

    @compute_p_values.setter
    def compute_p_values(self, compute_p_values):
        assert_is_type(compute_p_values, None, bool)
        self._parms["compute_p_values"] = compute_p_values


    @property
    def remove_collinear_columns(self):
        """bool: in case of linearly dependent columns remove some of the dependent columns (Default: False)"""
        return self._parms.get("remove_collinear_columns")

    @remove_collinear_columns.setter
    def remove_collinear_columns(self, remove_collinear_columns):
        assert_is_type(remove_collinear_columns, None, bool)
        self._parms["remove_collinear_columns"] = remove_collinear_columns


    @property
    def intercept(self):
        """bool: include constant term in the model (Default: True)"""
        return self._parms.get("intercept")

    @intercept.setter
    def intercept(self, intercept):
        assert_is_type(intercept, None, bool)
        self._parms["intercept"] = intercept


    @property
    def non_negative(self):
        """bool: Restrict coefficients (not intercept) to be non-negative (Default: False)"""
        return self._parms.get("non_negative")

    @non_negative.setter
    def non_negative(self, non_negative):
        assert_is_type(non_negative, None, bool)
        self._parms["non_negative"] = non_negative


    @property
    def max_iterations(self):
        """int: Maximum number of iterations (Default: -1)"""
        return self._parms.get("max_iterations")

    @max_iterations.setter
    def max_iterations(self, max_iterations):
        assert_is_type(max_iterations, None, int)
        self._parms["max_iterations"] = max_iterations


    @property
    def objective_epsilon(self):
        """
        float: Converge if  objective value changes less than this. Default indicates: If lambda_search is set to True
        the value of objective_epsilon is set to .0001. If the lambda_search is set to False and lambda is equal to
        zero, the value of objective_epsilon is set to .000001, for any other value of lambda the default value of
        objective_epsilon is set to .0001. (Default: -1)
        """
        return self._parms.get("objective_epsilon")

    @objective_epsilon.setter
    def objective_epsilon(self, objective_epsilon):
        assert_is_type(objective_epsilon, None, numeric)
        self._parms["objective_epsilon"] = objective_epsilon


    @property
    def beta_epsilon(self):
        """
        float: converge if  beta changes less (using L-infinity norm) than beta esilon, ONLY applies to IRLSM solver
        (Default: 0.0001)
        """
        return self._parms.get("beta_epsilon")

    @beta_epsilon.setter
    def beta_epsilon(self, beta_epsilon):
        assert_is_type(beta_epsilon, None, numeric)
        self._parms["beta_epsilon"] = beta_epsilon


    @property
    def gradient_epsilon(self):
        """
        float: Converge if  objective changes less (using L-infinity norm) than this, ONLY applies to L-BFGS solver.
        Default indicates: If lambda_search is set to False and lambda is equal to zero, the default value of
        gradient_epsilon is equal to .000001, otherwise the default value is .0001. If lambda_search is set to True, the
        conditional values above are 1E-8 and 1E-6 respectively. (Default: -1)
        """
        return self._parms.get("gradient_epsilon")

    @gradient_epsilon.setter
    def gradient_epsilon(self, gradient_epsilon):
        assert_is_type(gradient_epsilon, None, numeric)
        self._parms["gradient_epsilon"] = gradient_epsilon


    @property
    def link(self):
        """
        Enum["family_default", "identity", "logit", "log", "inverse", "tweedie"]:  (Default: "family_default")
        """
        return self._parms.get("link")

    @link.setter
    def link(self, link):
        assert_is_type(link, None, Enum("family_default", "identity", "logit", "log", "inverse", "tweedie"))
        self._parms["link"] = link


    @property
    def prior(self):
        """
        float: prior probability for y==1. To be used only for logistic regression iff the data has been sampled and the
        mean of response does not reflect reality. (Default: -1)
        """
        return self._parms.get("prior")

    @prior.setter
    def prior(self, prior):
        assert_is_type(prior, None, numeric)
        self._parms["prior"] = prior


    @property
    def lambda_min_ratio(self):
        """
        float: Min lambda used in lambda search, specified as a ratio of lambda_max. Default indicates: if the number of
        observations is greater than the number of variables then lambda_min_ratio is set to 0.0001; if the number of
        observations is less than the number of variables then lambda_min_ratio is set to 0.01. (Default: -1)
        """
        return self._parms.get("lambda_min_ratio")

    @lambda_min_ratio.setter
    def lambda_min_ratio(self, lambda_min_ratio):
        assert_is_type(lambda_min_ratio, None, numeric)
        self._parms["lambda_min_ratio"] = lambda_min_ratio


    @property
    def beta_constraints(self):
        """str: beta constraints"""
        return self._parms.get("beta_constraints")

    @beta_constraints.setter
    def beta_constraints(self, beta_constraints):
        assert_is_type(beta_constraints, None, H2OFrame)
        self._parms["beta_constraints"] = beta_constraints


    @property
    def max_active_predictors(self):
        """
        int: Maximum number of active predictors during computation. Use as a stopping criterion to prevent expensive
        model building with many predictors. Default indicates: If the IRLSM solver is used, the value of
        max_active_predictors is set to 7000 otherwise it is set to 100000000. (Default: -1)
        """
        return self._parms.get("max_active_predictors")

    @max_active_predictors.setter
    def max_active_predictors(self, max_active_predictors):
        assert_is_type(max_active_predictors, None, int)
        self._parms["max_active_predictors"] = max_active_predictors


    @property
    def interactions(self):
        """
        List[str]: A list of predictor column indices to interact. All pairwise combinations will be computed for the
        list.
        """
        return self._parms.get("interactions")

    @interactions.setter
    def interactions(self, interactions):
        assert_is_type(interactions, None, [str])
        self._parms["interactions"] = interactions


    @property
    def balance_classes(self):
        """
        bool: Balance training data class counts via over/under-sampling (for imbalanced data). (Default: False)
        """
        return self._parms.get("balance_classes")

    @balance_classes.setter
    def balance_classes(self, balance_classes):
        assert_is_type(balance_classes, None, bool)
        self._parms["balance_classes"] = balance_classes


    @property
    def class_sampling_factors(self):
        """
        List[float]: Desired over/under-sampling ratios per class (in lexicographic order). If not specified, sampling
        factors will be automatically computed to obtain class balance during training. Requires balance_classes.
        """
        return self._parms.get("class_sampling_factors")

    @class_sampling_factors.setter
    def class_sampling_factors(self, class_sampling_factors):
        assert_is_type(class_sampling_factors, None, [float])
        self._parms["class_sampling_factors"] = class_sampling_factors


    @property
    def max_after_balance_size(self):
        """
        float: Maximum relative size of the training data after balancing class counts (can be less than 1.0). Requires
        balance_classes. (Default: 5)
        """
        return self._parms.get("max_after_balance_size")

    @max_after_balance_size.setter
    def max_after_balance_size(self, max_after_balance_size):
        assert_is_type(max_after_balance_size, None, float)
        self._parms["max_after_balance_size"] = max_after_balance_size


    @property
    def max_confusion_matrix_size(self):
        """
        int: [Deprecated] Maximum size (# classes) for confusion matrices to be printed in the Logs (Default: 20)
        """
        return self._parms.get("max_confusion_matrix_size")

    @max_confusion_matrix_size.setter
    def max_confusion_matrix_size(self, max_confusion_matrix_size):
        assert_is_type(max_confusion_matrix_size, None, int)
        self._parms["max_confusion_matrix_size"] = max_confusion_matrix_size


    @property
    def max_hit_ratio_k(self):
        """
        int: Max. number (top K) of predictions to use for hit ratio computation (for multi-class only, 0 to disable)
        (Default: 0)
        """
        return self._parms.get("max_hit_ratio_k")

    @max_hit_ratio_k.setter
    def max_hit_ratio_k(self, max_hit_ratio_k):
        assert_is_type(max_hit_ratio_k, None, int)
        self._parms["max_hit_ratio_k"] = max_hit_ratio_k


    @property
    def max_runtime_secs(self):
        """float: Maximum allowed runtime in seconds for model training. Use 0 to disable. (Default: 0)"""
        return self._parms.get("max_runtime_secs")

    @max_runtime_secs.setter
    def max_runtime_secs(self, max_runtime_secs):
        assert_is_type(max_runtime_secs, None, numeric)
        self._parms["max_runtime_secs"] = max_runtime_secs



    @property
    def Lambda(self):
        """[DEPRECATED] Use self.lambda_ instead"""
        return self._parms["lambda"] if "lambda" in self._parms else None

    @Lambda.setter
    def lambda_(self, value):
        """[DEPRECATED] Use self.lambda_ instead"""
        self._parms["lambda"] = value

    @staticmethod
    def getGLMRegularizationPath(model):
        """
        Extract full regularization path explored during lambda search from glm model.
        @param model - source lambda search model
        """
        x = h2o.api("GET /3/GetGLMRegPath", data={"model": model._model_json["model_id"]["name"]})
        ns = x.pop("coefficient_names")
        res = {
            "lambdas": x["lambdas"],
            "explained_deviance_train": x["explained_deviance_train"],
            "explained_deviance_valid": x["explained_deviance_valid"],
            "coefficients": [dict(zip(ns, y)) for y in x["coefficients"]],
        }
        if "coefficients_std" in x:
            res["coefficients_std"] = [dict(zip(ns, y)) for y in x["coefficients_std"]]
        return res

    @staticmethod
    def makeGLMModel(model, coefs, threshold=.5):
        """
        Create a custom GLM model using the given coefficients.
        Needs to be passed source model trained on the dataset to extract the dataset information from.
          @param model - source model, used for extracting dataset information
          @param coefs - dictionary containing model coefficients
          @param threshold - (optional, only for binomial) decision threshold used for classification
        """
        model_json = h2o.api(
            "POST /3/MakeGLMModel",
            data={"model": model._model_json["model_id"]["name"],
                  "names": list(coefs.keys()),
                  "beta": list(coefs.values()),
                  "threshold": threshold}
        )
        m = H2OGeneralizedLinearEstimator()
        m._resolve_model(model_json["model_id"]["name"], model_json)
        return m
