END to END ML model for the Regression Based IC50 Values prediction of XPO1 inhibitors using python script. 

*****

After installing the requirements in an Virtual Environment
or creating a new environment using conda by using "environment_dependencies.yml" file
just open the command prompt or Terminal in the above created virtual environment
run the command given below
### Using Decision Tree regression Algorithm based prediction
python DT_regression-XPO1.py test.smi

similarly, for any unknown molecule when just use the command by specifying the path
of "*.smi" file.

python DT_regression-XPO1.py [specify_path]*.smi


The result will be displayed in the terminal as pIC50 value and IC50 value of the Molecule.


###
While testing the script using given test.smi, it will generate below output.

###  pIC50 value for the molecule is  4.916917019483667
###  IC50 value for the molecule is  12108.294642720226 nM

###Decision Tree model has R-squared value of 0.8184270843497391 after Hyperparameter Tuning. 
