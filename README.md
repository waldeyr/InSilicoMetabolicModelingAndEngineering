# Journal: Processes 

## Special Issue: In Silico Metabolic Modeling and Engineering

## Article: Exploring plant sesquiterpene diversity by generating chemical networks

In order to embrace the reproducing of the experiments, this repository contains:
* A tutorial to setup a Linux evironment 
* A tutorial to setup a Linux Docker evironment (recommended)
* Code to run the paper simulations 


## Install MØDatschgerl v0.7.0 on Fedora 26

### Dependencies

It only runs in Linux environments. 

The examples here were built for [Fedora Linux](https://getfedora.org/). We going to provide an Ubuntu tutorial as soon as possible.

#### Neo4J
* [Neo4J >=3.4](https://neo4j.com/download-center)

After download it, just extract the content to your favourite folder and start the database using the comand

`./neo4j start`

I a few seconds an interface will be available in your browser: http://localhost:7474/browser

Another way is to install Neo4J with rpm:

`cd /tmp && wget http://debian.neo4j.org/neotechnology.gpg.key && rpm --import neotechnology.gpg.key`

```
cat <<EOF>  /etc/yum.repos.d/neo4j.repo
[neo4j]
name=Neo4j Yum Repo
baseurl=http://yum.neo4j.org/stable
enabled=1
gpgcheck=1
EOF
```
`dnf install neo4j -y`

#### Python dependencies
* [Python >= 3.5](https://www.python.org/downloads/release/python-350/) - Python 3 programming language
* [Py2Neo](https://py2neo.org/v4/) - python driver and API for Neo4J:

`pip install py2neo`

`python3 -m pip install pip --upgrade`

`python3 -m pip install py2neo`

### Set up folders
`mkdir $HOME/sources`
`mkdir $HOME/mod-v0.7.0`
`sudo ln -s /usr/include/python3.7m /usr/include/python3.7`

### Downloads

`cd $HOME/sources`

`sudo dnf update`

`dnf install which nano git python3-devel python3-sphinx librsvg2-devel pango-devel openbabel-devel pdf2svg autoconf automake libtool boost-python3-devel gcc-c++ texlive-scheme-full texi2html texinfo wget -y`

`wget https://dl.bintray.com/boostorg/release/1.64.0/source/boost_1_64_0.tar.gz && tar -xf boost_1_64_0.tar.gz`

`wget -c https://graphviz.gitlab.io/pub/graphviz/stable/SOURCES/graphviz.tar.gz -O graphviz-2.40.1.tar.gz && tar -xf graphviz-2.40.1.tar.gz`

`git clone https://github.com/jakobandersen/perm_group.git`

`cd $HOME/sources/perm_group && git checkout v0.2 && cd $HOME/sources`

`git clone https://github.com/jakobandersen/graph_canon.git`

`cd $HOME/sources/graph_canon && git checkout v0.2 && cd $HOME/sources`

`git clone https://github.com/jakobandersen/mod.git`


## Boost 1.64.0
`cd $HOME/sources/boost_1_64_0/ && ./bootstrap.sh --prefix=$HOME/mod-v0.7.0 --with-python=/usr/bin/python3 && ./b2 -j 4 && ./b2 install`

## Graphviz
`cd $HOME/sources/graphviz-2.40.1 && ./configure --prefix=$HOME/mod-v0.7.0 --with-boost=$HOME/mod-v0.7.0 --with-python=/usr/bin/python3 && make -j 4 && make install`

## PermGroup
`cd $HOME/sources/perm_group && ./bootstrap.sh --prefix=$HOME/mod-v0.7.0 --with-python=/usr/bin/python3 && ./configure --prefix=$HOME/mod-v0.7.0 --with-boost=$HOME/mod-v0.7.0 && make -j 4 && make install`

## GraphCanon
`cd $HOME/sources/graph_canon && ./bootstrap.sh --prefix=$HOME/mod-v0.7.0 --with-python=/usr/bin/python3 && ./configure --with-perm_group=$HOME/mod-v0.7.0 --prefix=$HOME/mod-v0.7.0 --with-boost=$HOME/mod-v0.7.0 && make -j 4 && make install`

## MedØlDatschgerl
`cd $HOME/sources/mod && ./bootstrap.sh --prefix=$HOME/mod-v0.7.0 --with-python=/usr/bin/python3 && ./configure --prefix=$HOME/mod-v0.7.0 --with-boost=$HOME/mod-v0.7.0 --with-OpenBabel=/usr/include/openbabel-2.0 && make -j 4 && make install`


## Install MØDatschgerl v0.7.0 with DOCKER?

Have you installed docker in your computer? 

Try: https://docs.docker.com/install

Downloading the docker container with all environment

`docker pull waldeyr/fedora26_mod-v0.7.0:2path`

Running a docker with a ready environment 

`docker run -ti waldeyr/fedora26_mod-v0.7.0:mod-v0.7.0 bash`

Optionally, you can map the docker simulation folder and neo4j ports to your local computer

`docker run -p 7474:7474 -v /home/mendes/docker/shared:/home/docker/shared -ti waldeyr/fedora26_mod-v0.7.0:2path15 bash`

* Don't forget to start the database inside the docker container: `neo4j start`

Please note that:
* Neo4J browser runs in the port 7474 (default). So you can access from your browser http://localhost:7474
* The neo4j authentication was disabled in the Docker container

## Getting Started

After install the envirnment, test it with: `$HOME/mod-v0.7.0/bin/mod`

### How to run the simulations?

Running the simulation 01

`cd $HOME/InSilicoMetabolicModelingAndEngineering/simulation_01`

`$HOME/mod-v0.7.0/bin/mod -f processes_simulation_01.py`

Running the simulation 02

`cd $HOME/InSilicoMetabolicModelingAndEngineering/simulation_02`

`$HOME/mod-v0.7.0/bin/mod -f processes_simulation_02.py`

Running the simulation 03

`cd $HOME/InSilicoMetabolicModelingAndEngineering/simulation_03`

`$HOME/mod-v0.7.0/bin/mod -f processes_simulation_03.py`


### How to run and store the simulations on Neo4J?

Check if the database is running:

`neo4j status`

If not, start the database:

`neo4j start`

Enter on the simulation folder

`cd $PATH_TO/InSilicoMetabolicModelingAndEngineering/simulation_store`

`$PATH_TO/mod-v0.7.0/bin/mod -f Molecules.py -f Processes_Store.py`

![Screenshot of simulation and results storing](https://github.com/waldeyr/InSilicoMetabolicModelingAndEngineering/blob/master/screenshots/Screenshot_Processes_Store.png)


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

