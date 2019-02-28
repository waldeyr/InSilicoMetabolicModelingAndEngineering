# Journal: Processes 

## Special Issue: In Silico Metabolic Modeling and Engineering

## Article: Exploring plant sesquiterpene diversity by generating chemical networks

In order to embrace the reproducing the experiments, this repository contains:
* a tutorial to setup a Linux evironment 
* simulation codes

## Dependencies
It only runs in Linux environments.

### Neo4J
* [Neo4J >=3.4](https://neo4j.com/download-center)

After download it, just extract the content to your favorute folder and start the database using the comand

```
#!shell
./neo4j start
```

I a few seconds an interface will be available in your browser: http://localhost:7474/browser

### Python dependencies
* [Python >= 3.5](https://www.python.org/downloads/release/python-350/)
* [Py2Neo](https://py2neo.org/v4/) : pip install py2neo


## Install MØDatschgerl v0.7.0 on Fedora 29 scientific

### Set up folders
* mkdir $HOME/sources
* mkdir $HOME/mod-v0.7.0
* sudo ln -s /usr/include/python3.7m /usr/include/python3.7

### Downloads
* cd $HOME/sources
* sudo dnf update 
* sudo dnf install git python3-devel python3-sphinx librsvg2-devel pango-devel openbabel-devel pdf2svg -y
* wget https://dl.bintray.com/boostorg/release/1.64.0/source/boost_1_64_0.tar.gz && tar -xf boost_1_64_0.tar.gz
* wget -c https://graphviz.gitlab.io/pub/graphviz/stable/SOURCES/graphviz.tar.gz -O graphviz-2.40.1.tar.gz && tar -xf graphviz-2.40.1.tar.gz
* git clone https://github.com/jakobandersen/perm_group.git
* cd $HOME/sources/perm_group & git checkout v0.2
* cd $HOME/sources
* git clone https://github.com/jakobandersen/graph_canon.git
* git clone https://github.com/jakobandersen/mod.git


### Boost 1.64.0
* cd $HOME/sources/boost_1_64_0/
* ./bootstrap.sh --prefix=$HOME/mod-v0.7.0 --with-python=/usr/bin/python3
* ./b2 -j 2
* ./b2 install

### Graphviz
* cd $HOME/sources/graphviz-2.40.1
* ./configure --prefix=$HOME/mod-v0.7.0 --with-boost=$HOME/mod-v0.7.0 --with-python=/usr/bin/python3
* make -j 2
* make install 
### Note: Running 'which dot' should NOT give the same as 'echo $HOME/mod-v0.7.0/bin/dot'

### PermGroup
* cd $HOME/sources/perm_group
* ./bootstrap.sh
* ./configure --prefix=$HOME/mod-v0.7.0 --with-boost=$HOME/mod-v0.7.0
* make -j 2
* make install

### GraphCanon
* cd $HOME/sources/graph_canon
* ./bootstrap.sh
* ./configure --prefix=$HOME/mod-v0.7.0 --with-boost=$HOME/mod-v0.7.0
* make -j 2
* make install

### MedØlDatschgerl
* cd $HOME/sources/mod
* ./bootstrap.sh
* ./configure --prefix=$HOME/mod-v0.7.0 --with-python=/usr/bin/python3 --with-boost=$HOME/mod-v0.7.0 --with-OpenBabel=/usr/include/openbabel-2.0
* make -j 2
* make install

## Getting start

### Generating a chemical network from a set of rules and storing it in the Neo4J
* $PATH_TO_MØD/mod -f Molecules.py -f Processes_Store.py

You can change the network removing or adding rules to the my_sumulation_file.py in the proper lines:
```
#!python
pushFilePrefix("../rules/")
opp_loss_for_fpp = ruleGML('opp_loss_for_fpp.gml')
opp_loss_for_npp_c1 = ruleGML('opp_loss_for_npp_c1.gml')
opp_loss_for_npp_c3 = ruleGML('opp_loss_for_npp_c3.gml')
opp_gain_by_farnesyl_cation = ruleGML('opp_gain_by_farnesyl_cation.gml')
fpp_1_10_cyc = ruleGML("fpp-1-10Cyc.gml")
fpp_1_11_cyc = ruleGML("fpp-1-11Cyc.gml")
ring_closure_c2_c10 = ruleGML("2-10Cyc.gml")
h_shift_c1_c2 = ruleGML("1-2Hshift.gml")
h_shift_c1_c3 = ruleGML("1-3Hshift.gml")
h_loss = ruleGML("h_loss.gml")
h2o_gain = ruleGML("h2o_gain.gml")
popFilePrefix()
```

You can change the initial set of molecules in the line:
```
#!python
eductMolecules = [fpp, npp, H2O]
```

You can change the number of iterations in the line:
```
#!python
dg = hypergraph.getHyperGraph(eductMolecules, 5)
```


