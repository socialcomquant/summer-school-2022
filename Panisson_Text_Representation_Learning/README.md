-------------------------------------------------------------------------------------------------------------------------------
# SUMMER SCHOOL 2022:
## Text mining and Natural Language Processing for Computational Social Sciences

### SocialComQuant Project - Online Teaching Module: Text Representation Learning

### André Panisson

-------------------------------------------------------------------------------------------------------------------------------


## Setup the Environment

Open a command line, go to the directory of the project, for example:

```bash
cd /home/student/PATH-TO-PROJECT
```

Check that conda is installed and working:
```bash
conda --version
```
(this command should show the version of conda installed in your system, e.g. `conda 4.13.0`)

Create a new environment using the file `environment.yml`:
```bash
conda env create -f environment.yml
```
Activate the environment:
```bash
conda activate transformers
```
Register the new environment as a kernel for Jupyter notebook:
```bash
python -m ipykernel install --user --name=transformers
```
Finally, open this notebook on Jupyter and check if all cells run without exceptions:
[1.Environment-Setup.ipynb](1.Environment-Setup.ipynb)


### If it doesn't work...

If the setup does not work, you still should be able to open the notebook on Google Colab:

**1.Environment-Setup.ipynb**: [Colab Link](https://colab.research.google.com/github/socialcomquant/summer-school-2022/blob/master/Panisson_Text_Representation_Learning/1.Environment-Setup.ipynb)

**2.BagOfWords.ipynb**: [Colab Link](https://colab.research.google.com/github/socialcomquant/summer-school-2022/blob/master/Panisson_Text_Representation_Learning/2.BagOfWords.ipynb)

**3.Word2Vec.ipynb**: [Colab Link](https://colab.research.google.com/github/socialcomquant/summer-school-2022/blob/master/Panisson_Text_Representation_Learning/3.Word2Vec.ipynb.ipynb)

**4.1.Transformer-Train.ipynb**: [Colab Link](https://colab.research.google.com/github/socialcomquant/summer-school-2022/blob/master/Panisson_Text_Representation_Learning/4.1.Transformer-Train.ipynb)

**4.2.Transformer-Test.ipynb**: [Colab Link](https://colab.research.google.com/github/socialcomquant/summer-school-2022/blob/master/Panisson_Text_Representation_Learning/4.2.Transformer-Test.ipynb)

**5.Translate.ipynb**: [Colab Link](https://colab.research.google.com/github/socialcomquant/summer-school-2022/blob/master/Panisson_Text_Representation_Learning/5.Translate.ipynb)