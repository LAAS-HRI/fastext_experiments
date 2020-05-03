# fasttext_experiments

FastText is an open source software based on subword static word embeddings for efficient text classification. It allow to compute embeddings for unknown words based on subwords and provide multilabel supervised classification. Word embeddings pretrained on Common Crawl and Wikipedia for [157 languages](https://fasttext.cc/docs/en/crawl-vectors.html) are also provided.

This repository contains an easy way of generating sentences based on templates that can be used for supervised multi-label learning with FastText.

More information in [FastText website](https://fasttext.cc/).

## Quick launch

```
git clone
./install_dependencies.sh
python generate_data.py --max_per_template 80
python train_and_evaluate.py
```

## Generate your own data

To generate your own data, you will need 2 files:

- The individuals (.csv file) that contain each class and the set of individuals that will be randomlly picked to fill the templates (see [the example](https://github.com/LAAS-HRI/fasttext_experiments/blob/master/individuals.csv)).

- The templates (.txt file) that contains the labels and sentences with specials tags `<...>` that describe which class will be filled in (see [the example](https://github.com/LAAS-HRI/fasttext_experiments/blob/master/templates.txt)).
