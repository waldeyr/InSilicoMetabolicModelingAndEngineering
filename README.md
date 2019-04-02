# Journal: Processes 

## Special Issue: In Silico Metabolic Modeling and Engineering

## Article: Exploring plant sesquiterpene diversity by generating chemical networks


## Install Environment on Linux

[Install Environment on Linux](https://github.com/waldeyr/InSilicoMetabolicModelingAndEngineering/wiki/Install-Environment-on-Linux)


## Install Environment with Docker

[Install Environment with Docker](https://github.com/waldeyr/InSilicoMetabolicModelingAndEngineering/wiki/Install-Environment-with-Docker)

## Getting Started

After install the environment, test it with: `$HOME/mod-v0.7.0/bin/mod`

### How to run the simulations?

Clone this repository:
`git clone https://github.com/waldeyr/InSilicoMetabolicModelingAndEngineering.git`

Running the simulation 01

`cd InSilicoMetabolicModelingAndEngineering/simulation_01`

`./runSimulation01`

Running the simulation 02

`cd InSilicoMetabolicModelingAndEngineering/simulation_02`

`./runSimulation02`

Running the simulation 03

`cd InSilicoMetabolicModelingAndEngineering/simulation_03`

`./runSimulation03`

### How to run the simulations on Docker environment?

`cd InSilicoMetabolicModelingAndEngineering/simulation_store`

Check if the database is running:

`./neo4jStatus`

If not, start it:

`./neo4jStart`

Enter on the simulation folder

`./runSimulationStoringWithNeo4J`

![Screenshot of simulation and results storing](https://github.com/waldeyr/InSilicoMetabolicModelingAndEngineering/blob/master/screenshots/Screenshot_Processes_Store.png)


You can change the resulting network removing or adding [rules](https://github.com/waldeyr/InSilicoMetabolicModelingAndEngineering/tree/master/rules) to the simulation from the [Processes_Store.py](https://github.com/waldeyr/InSilicoMetabolicModelingAndEngineering/blob/master/simulation_store/Processes_Store.py) in the proper lines:

```
#!python
pushFilePrefix("../rules/")
opp_loss_for_fpp = ruleGML('opp_loss_for_fpp.gml')
fpp_1_10_cyc = ruleGML("fpp-1-10Cyc.gml")
fpp_1_11_cyc = ruleGML("fpp-1-11Cyc.gml")
ring_closure_c2_c10 = ruleGML("2-10Cyc.gml")
h_shift_c1_c2 = ruleGML("1-2Hshift.gml")
h_shift_c1_c3 = ruleGML("1-3Hshift.gml")
h_loss = ruleGML("h_loss.gml")
h2o_gain = ruleGML("h2o_gain.gml")
wagner_meerwein = ruleGML("WMshift.gml")
allyl_shift = ruleGML("allylshift.gml")
popFilePrefix()
```

You can change the initial set of molecules in the line:
```
#!python
eductMolecules = [fpp, H2O]
```

You can change the number of iterations in the line:
```
#!python
dg = hypergraph.getHyperGraph(eductMolecules, 4)
```

