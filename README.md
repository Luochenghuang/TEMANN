
                ___           ___           ___           ___           ___           ___     
               /\  \         /\  \         /\__\         /\  \         /\__\         /\__\    
               \:\  \       /::\  \       /::|  |       /::\  \       /::|  |       /::|  |   
                \:\  \     /:/\:\  \     /:|:|  |      /:/\:\  \     /:|:|  |      /:|:|  |   
                /::\  \   /::\~\:\  \   /:/|:|__|__   /::\~\:\  \   /:/|:|  |__   /:/|:|  |__ 
               /:/\:\__\ /:/\:\ \:\__\ /:/ |::::\__\ /:/\:\ \:\__\ /:/ |:| /\__\ /:/ |:| /\__\
              /:/  \/__/ \:\~\:\ \/__/ \/__/~~/:/  / \/__\:\/:/  / \/__|:|/:/  / \/__|:|/:/  /
             /:/  /       \:\ \:\__\         /:/  /       \::/  /      |:/:/  /      |:/:/  / 
             \/__/         \:\ \/__/        /:/  /        /:/  /       |::/  /       |::/  /  
                            \:\__\         /:/  /        /:/  /        /:/  /        /:/  /   
                             \/__/         \/__/         \/__/         \/__/         \/__/    
                   
# TEMANN
* ThermoElectric Materials Artifical Neural Network (TEMANN) is a python package that can be used to predict **Seebeck coefficients** for novel materials in units of **uV/K**. All that is required for prediction is the material's chemical formula, the space group of the material, and the temperature (K) of interest.

# Use Cases

1. Input novel materials to generate predicted Seebeck coefficent.
2. Input three elements and generate a ternary heatmap of the Seebeck coefficients.

# Example
```
>>> import temann
>>> temann.predict_seebeck('CaMnO3', 62, 400)
-435.9079284667969
>>> temann.plot_ternary('CaMnO')
```
![](https://raw.githubusercontent.com/Luochenghuang/TEMANN/examples/ternary_example.png)

# Installation
```
git clone https://github.com/Luochenghuang/TEMANN.git
cd TEMANN
python setup.py install
```

# Workflow
![alt text](https://raw.githubusercontent.com/Luochenghuang/TEMANN/master/doc/TEMANN.jpg "This is our flowchart")



