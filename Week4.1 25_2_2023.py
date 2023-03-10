# -*- coding: utf-8 -*-
"""Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

fool= ctrl.Antecedent(np.arange(0,11,1),'fool')
service= ctrl.Antecedent(np.arange(0,11,1),'service')
tip= ctrl.Consequent(np.arange(10,31,1),'tip')

fool['poor']=fuzz.trimf(fool.universe,[0,0,5])
fool['average']=fuzz.trimf(fool.universe,[0,5,10])
fool['good']=fuzz.trimf(fool.universe,[5,10,10])

service['poor']=fuzz.trimf(service.universe,[0,0,5])
service['average']=fuzz.trimf(service.universe,[0,5,10])
service['good']=fuzz.trimf(service.universe,[5,10,10])

tip['less']=fuzz.trimf(tip.universe,[0,10,17.5])
tip['nomal']=fuzz.trimf(tip.universe,[15,20,25])
tip['much']=fuzz.trimf(tip.universe,[22.5,30,30])

rule1= ctrl.Rule(fool['poor']&service['poor'],tip['less'])
rule2= ctrl.Rule(fool['poor']&service['average'],tip['less'])
rule3= ctrl.Rule(fool['poor']&service['good'],tip['nomal'])
rule4= ctrl.Rule(fool['average']&service['poor'],tip['less'])
rule5= ctrl.Rule(fool['average']&service['average'],tip['less'])
rule6= ctrl.Rule(fool['average']&service['good'],tip['nomal'])
rule7= ctrl.Rule(fool['good']&service['poor'],tip['nomal'])
rule8= ctrl.Rule(fool['good']&service['average'],tip['nomal'])
rule9= ctrl.Rule(fool['good']&service['good'],tip['much'])

tipping_ctrl= ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9])
tipping= ctrl.ControlSystemSimulation(tipping_ctrl)

tipping.input['fool']=7
tipping.input['service']=3
tipping.compute()
print(tipping.output['tip'])
tip.view(sim=tipping)

