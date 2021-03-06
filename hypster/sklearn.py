# AUTOGENERATED! DO NOT EDIT! File to edit: 05_sklearn.ipynb (unless otherwise specified).

__all__ = ['SEED', 'path', 'df', 'df', 'cat_names', 'cont_names', 'dep_var', 'run_learner', 'study']

# Cell
from .oo_hp import *
from .hypster_prepare import *

import fastai2
from fastai2.tabular.all import *
from fastai2.metrics import *

from sklearn.model_selection import train_test_split

from copy import deepcopy

import optuna

# Cell
SEED = 42

# Cell
path = untar_data(URLs.ADULT_SAMPLE)
path.ls()

# Cell
df = pd.read_csv(path/'adult.csv')
df.head()

# Cell
df = df.sample(frac=0.1)

# Cell
cat_names = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race']
cont_names = ['age', 'fnlwgt', 'education-num']
dep_var = "salary"

# Cell
train_df, test_df, y_train, y_test = train_test_split(df, y, test_size=0.6,
                                                     random_state=SEED,
                                                     stratify=y)

# Cell
import datetime
def run_learner(fit_method, get_metric, n_trials=5): #learner
    class Objective():
        def __init__(self, fit_method, get_metric): #learner
            #self.learner   = learner
            self.fit_method = fit_method
            self.get_metric = get_metric

        def __call__(self, trial):
            #learner = self.learner.sample(trial)
            self.fit_method.sample(trial)
            res = self.get_metric.sample(trial)
            #print(self.fit_method.base_call)
            #print(self.get_metric.base_call.base_call)
            print(res)
            return res

    objective = Objective(fit_method, get_metric) #learner
    optuna.logging.set_verbosity(0)
    pruner = optuna.pruners.NopPruner()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    study = optuna.create_study(direction="maximize", study_name = now, pruner=pruner)
    study.optimize(objective, n_trials=n_trials, n_jobs=1, timeout=600)
    return study

# Cell
study = run_learner(#learner    = learner,
                    fit_method = pipe.fit(train_df, y_train),
                    get_metric = pipe.score(test_df, y_test),
                    n_trials   = 3
                   )

# Cell
print("Number of finished trials: {}".format(len(study.trials)))

# Cell
study.trials_dataframe()