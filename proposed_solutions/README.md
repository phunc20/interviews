## Analysis of Some Common ML Algorithms
01. Decision Trees
  - The way I formulate the question makes it neither classification problem, nor regression problem. It is similar to classification but not exactly. So using decision trees would make little sense to me, unless we make a new tree for each input array, and ask the leaf nodes to each contain `1` number. But this is not machine learning, and its complexity would be way to large compared to the well-known sorting algorithms.
02. SVM and others
  - Actually, due to the same reason above, all the other algorithms like logistic regression, linear regression, SVM, etc., even clustering algorithms will be of no use to us. This unless we manage to find a way to reformulate the question to make it a classification/regression/clustering problem.
03. CNN
  - No pictures here.
04. Vanilla NN
  - Possible
05. Sequential Models: RNN, LSTM, GRU, etc.
  - Possible
06. GAN, Autoencoders
  - Less likely to be useful here. For example, GAN, if we try to have train generator and discriminator, then at the end of the day, the best we can do when we have an arbitrary input array, say `[0, 7, 9, 3]`, the best we can do is to go through every permutation of the array and have the trained discriminator judges for us which is likely to be the sorted array. This can be envisioned as trainable, but it is not valuable becuase it takes too long (high complexity)
  - we can judge whether or not an array is sorted by simply iterating through the array.
07. Reinforcement Learning
  - Possible


## Corrections
I have made some wrong judgement in the course, which I shall correct here.

01. Make at least test set and training set.
  - I said there was no need for test set and validation set, but at 2nd thought we might create such a bulky Neural Network model that it simply memorizes everything, which is undesirable. So, it is still better to measure overfit/underfit.
02. There are ways to make a vanilla NN capable of tackling this question. For example, by always padding the arrays to length equal to `10` (as explain in `01-vanilla_NN/01_vanilla_NN.ipynb`)
03. Instead of naively using cross-entropy loss, we should probably define our own loss function
  - We can keep the cross-entropy loss part, but we must add some other kinds of loss part
  - Probability makes our predictions victim of making repeated judgement, but the requirement is a sorted array of distinct integers (from `0` to `9`). For an input like `[0, 9, 7, 5]`, we must punish predictions like `[0, 9, 7, 7]`.
  - Another punishment scenario: An input like `[0, 9, 7, 5]` with a prediction `[0, 9, 1, 2]`. Clearly, `1` and `2` are not in the set of `{0, 9, 7, 5}`.


## Directory and Files
- Notebooks named `XY-.ipynb`, where `XY` represents two digits, e.g. `03-.ipynb`, are notebooks where I modified and ran previous code. They worth not be read unless otherwise specified.
- Notebooks with numbers and names are in contrast records of my work.


## Conclusion and Regrets
I don't get to train a lot of models, the only weight included in the repo is `01-vanilla_NN/vanilla_NN_model.h5`. This is also the first successfully trained weight of mine. I might not even find time to evaluate it.

The problem and regret of mine is that
- I spent too much time trying to make my first model and first dataset work, while that dataset would need time to better prepared.
- That being said, the dataset can be trained on LSTM but I haven't yet found out why the training process got stuck and died often. I think the problem is at the dataset; maybe it took too much RAM.

I spent quite some time analysing and taking notes down how and what we could do in the markdown files as well as in
the notebooks. If in case the one who judges this work does not have enough time, let me list the most important files
according to their importance and chronological order:

- `02-sequential_models/01-analysis.ipynb`
- `01-vanilla_NN/01-vanilla_NN.ipynb`
- `README.md`
- `01-vanilla_NN/03-evaluation.ipynb`
- `02-sequential_models/06-dataset_fixed_length.ipynb`



