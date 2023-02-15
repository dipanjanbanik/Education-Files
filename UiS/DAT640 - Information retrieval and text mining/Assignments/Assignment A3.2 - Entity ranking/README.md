## Scenario

In this project, we use retrieval models for entities. 

## Task

You will implement document-at-a-time scoring strategy documents in the collection with respect to an input query. In this task, you will score documents using **SDM** for single field scoring and **FSDM** for multi-field document scoring.

In the public tests, we make use of a "dummy" (toy-sized) collection to test your function. Try to pass it all.

## Files



## Scoring

Complete each function and method according to instructions. There is a test for each scoring method. Make sure that your code passes all the tests.

## Submission deadline

The submission deadline is **26/10 16:00**. Your submission is the last uploaded file at that time. Complete the functions which have **# TODO**

## Specific steps

## Environment

We recommend using download elasticsearch version 7.17.6 ([Download](https://www.elastic.co/downloads/past-releases/elasticsearch-7-17-6)).

Your environment is expected to be an Anaconda base environment of Python 3.7+, with the following additional libraries installed:
  * elasticsearch version 7.17.6
  
**DO NOT** install additional libraries. You are only allowed to import standard Python libraries from the base Python 3.7 distribution ([link](https://docs.python.org/3.7/py-modindex.html)).

## Sequential Dependence Model (SDM)

The SDM ranking function is given by a weighted combination of three feature functions
 
 $$score(e, q) =\lambda_T \sum^n_{i=1} f_T(q_i, e) + \lambda_O \sum^{n−1}_{i=1}f_O(q_i, q_{i+1}, e) + \lambda_U \sum^{n−1}_{i=1}f_U(q_i, q_{i+1}, e)$$
 
 * The query is represented as a sequence of terms $q=\langle q_1, \dots , q_n \rangle$
 * Feature weights are subject to the constraint $\lambda_T + \lambda_O + \lambda_U= 1$

Feature functions are based on language modeling estimates using Dirichlet prior smoothing.


### Unigram matches

Unigram matches are based on smoothed entity language models
 
  $$f_T(q_i, e) = log(P(t| \theta_{e}) = log(\frac{c_{q_i, e}+\mu P(q_i|\varepsilon)}{l_e+\mu})$$

 * $c(q_i,e)$ is the raw term frequency in the description of an entity $e$
 * $l_e$ is the length of the entity’s description (number of terms)
 * $\varepsilon$ is the entity catalog (set of all entities)
 * $\mu$ is the smoothing parameter
 * The background language model is a maximum likelihood estimate:

### Ordered bigram matches

$$f_O(q_i, q_{i+1}, e) =log(\frac{c_o(q_i, q_{i+1}, e) + \mu P_o(q_i, q_{i+1}|\varepsilon)}{l_e+\mu})$$

 * $c_o(q_i, q_{i+1}, e)$ denotes the number of times the terms $q_i$, $q_{i+1}$ occur in this exact order in the description of $e$
 * The background language model is a maximum likelihood estimate:
 
 $$P_o(q_i, q_{i+1}|\varepsilon) =\frac{\sum_{e \in \varepsilon}c_o(q_i, q_{i+1}, e)}{\sum_{e\in\varepsilon}l_e}$$

 ### Unordered bigram matches

$$f_U(q_i, q_{i+1}, e) =log(\frac{c_\omega(q_i, q_{i+1}, e) + \mu P_\omega(q_i, q_{i+1}|\varepsilon)}{l_e+\mu})$$

 * $c_\omega(q_i, q_{i+1}, e)$ counts the co-occurrence of terms $q_i$ and $q_{i+1}$ in e, within an unordered window of $\omega$ term positions
 * The background language model is a maximum likelihood estimate:
 
 $$P_\omega(q_i, q_{i+1}|\varepsilon) =\frac{\sum_{e \in \varepsilon}c_\omega(q_i, q_{i+1}, e)}{\sum_{e\in\varepsilon}l_e}$$

**NB!** For the collection language models, ordered and unordered bigrams should be computed for all documents. In practice, this is very expensive, so we only calculate bigram matches contributions for the documents retrieved with the baseline retrieval. We assume that all other documents have no bigram matches.

## Fielded Sequential Dependence Model (FSDM)

Unigram matches are MLM-estimated probabilities:

$$f_T(q_i, e) =log \sum_{f F} \omega^T_f P(t| \theta_{f_e})$$

 * $\omega^T_f$ are the field mapping weights (for each field)

Ordered bigram matches:

$$f_O(q_i, q_{i+1}, e) = log \sum_{f\in F}\omega^O_f\frac{c_o(q_i, q_{i+1}, f_e) + \mu_f P_o(q_i, q_{i+1}|f_{\varepsilon})}{l_{f_e} + \mu_f}$$

Unordered bigram matches:

$$f_U(q_i, q_{i+1}, e) =log \sum_{f \in F}\omega^U_f \frac{c^{\omega}_u(q_i, q_{i+1}, f_e) + \mu_f P^{\omega}_u(q_i, q_{i+1}|f_{\varepsilon})}{l_{f_e}+\mu_f}$$

 * $\omega^O_f$ and $\omega^U_f$ are the field mapping weights (for each field)
