from ConfigClass import *

class Processes_Store(ConfigClass):

    def __init__(self):
        ConfigClass.__init__(self)
        self._uuid = uuid.uuid4()
        logging.basicConfig(level=logging.FATAL)

    def printTree(self):
        print(self.TREE)

    def getHyperGraph(self, eductMolecules: list, numberOfIterations: int):
        print("\n####################################################################")
        print("# Generating the hypergraph...")
        print("####################################################################\n")
        ######################################
        # RULES
        ######################################
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
        allyl_shift = ruleGML("allylshift.gml")
        wagner_meerwein = ruleGML("WMshift.gml")
        popFilePrefix()
        # General breadth-first derivation strategy
        strat = (addSubset(eductMolecules) >> repeat[numberOfIterations](inputRules))
        # Defining labels
        ls = LabelSettings(LabelType.Term, LabelRelation.Unification)
        # Generating the hypergraph
        hypergraph = dgRuleComp(inputGraphs, strat, ls)
        hypergraph.calc()
        return hypergraph

    def getNodeRule(self, rules):
        for rule in rules:
            mergeId = uuid.uuid4()
            ruleNode = Node("Rule", mergeId=str(mergeId), modId=rule.id, modName=str(rule.name))
        return ruleNode

    def storeGraph(self, hypergraph):
        print("\n####################################################################")
        print("# Storing the hypergraph in the Neo4J graph database...")
        print("####################################################################\n")
        g = self.getDatabaseConnection()  # opening a connection
        g.run("MATCH (n) DETACH DELETE n") # clean database
        g.run("CREATE INDEX ON :Compound(modName)")
        g.run("CREATE INDEX ON :Rule(modName)")
        for hyperedge in hypergraph.edges:  # for each hyperedge into derivation graph
            currentHyperegde = hypergraph.findEdge(hyperedge.sources, hyperedge.targets)
            rules = currentHyperegde.rules
            sources = currentHyperegde.sources
            targets = currentHyperegde.targets
            ruleNode = self.getNodeRule(rules)
            tx = g.begin()  # beginning the transaction
            tx.merge(ruleNode, "Rule", "modName")
            for source in sources: # source nodes
                if source.graph.isMolecule: 
                    sourceNode = Node("Compound",
                                    modId=str(source.id),
                                    modName=str(source.graph.name),
                                    modSmiles=str(source.graph.smiles),
                                    pubchem="",
                                    chemspider="",
                                    commonName="",
                                    molecularFormula="",
                                    molecularWeight="",
                                    monoisotopicMass="",
                                    averageMass="",
                                    nominalMass="",
                                    smiles="",
                                    imageUrl=""
                                    )
                    tx.merge(sourceNode, "Compound", "modId")
                    sourceToRule = Relationship(sourceNode, "TO", ruleNode)
                    tx.create(sourceToRule)
            for target in targets: # target nodes
                if target.graph.isMolecule: 
                    targetNode = Node("Compound",
                                    modId=str(target.id),
                                    modName=str(target.graph.name),
                                    modSmiles=str(target.graph.smiles),
                                    pubchem="",
                                    chemspider="",
                                    commonName="",
                                    molecularFormula="",
                                    molecularWeight="",
                                    monoisotopicMass="",
                                    averageMass="",
                                    nominalMass="",
                                    smiles="",
                                    imageUrl=""
                                    )
                    tx.merge(targetNode, "Compound", "modId")
                    ruleToTarget = Relationship(ruleNode, "TO", targetNode)
                    tx.create(ruleToTarget)
            tx.commit()
            sys.stdout.write('.')
        print ("\n")
        return None

    def getAllCompoundsFromDatabase(self):
        g = self.getDatabaseConnection()
        compounds = list(g.nodes.match("Compound"))
        return compounds

    def assignScenarios(self):
        print("\n####################################################################")
        print("# Assigning biological scenarios for the predicted compounds...")
        print("####################################################################\n")
        g = self.getDatabaseConnection()
        with open("scenarios.csv", "r") as file:
            scenarios = file.readlines()
        file.close()
        compounds = self.getAllCompoundsFromDatabase()
        for compound in compounds:            
            for scenario in scenarios[1:]:
                scenario = scenario.split("\t")
                scenarioId = str(scenario[0].strip("\n"))
                ncbiTaxon = str(scenario[1].strip("\n"))
                ncbiSpecies = str(scenario[2].strip("\n"))
                ncbiAccession = str(scenario[3].strip("\n"))
                pubmedAccession = str(scenario[4].strip("\n"))
                modName = str(scenario[5].strip("\n").replace(" ", ""))
                experiment = str(scenario[6].strip("\n"))
                tissue = str(scenario[7].strip("\n"))
                condition = str(scenario[8].strip("\n"))
                compoundYield = str(scenario[9].strip("\n"))
                ec = str(scenario[10].strip("\n"))
                kegg = str(scenario[11].strip("\n"))
                rhea = str(scenario[12].strip("\n"))
                iubmb = str(scenario[13].strip("\n"))
                # Is there a scenario for the current compound?            
                if str(modName) == str(compound['modName']):
                    print(compound['modName'] + " == "+ modName)
                    scenarioNode = Node("Scenario", scenarioId=scenarioId, ncbiTaxon=ncbiTaxon, 
                                            ncbiSpecies=ncbiSpecies, ncbiAccession=ncbiAccession, 
                                            pubmedAccession=pubmedAccession, modName=modName,
                                            experiment=experiment, tissue=tissue, condition=condition,  
                                            compoundYield=compoundYield, ec=ec, kegg=kegg, rhea=rhea, 
                                            iubmb=iubmb)
                    tx = g.begin()  # begin transaction
                    tx.merge(scenarioNode, "Scenario", "scenarioId")
                    compoundToScenario = Relationship(compound, "OCCURS", scenarioNode)
                    tx.create(compoundToScenario)
                    tx.commit()  # commit transaction                 
        return None

######################################
# Running SETUP
######################################
processes = Processes_Store()
processes.printTree()
eductMolecules = [fpp, H2O]
############################################################################
# hypergraph generation
############################################################################
hypergraph = processes.getHyperGraph(eductMolecules, 6)
############################################################################
# Storing the hypergraph 
# ##########################################################################
processes.storeGraph(hypergraph)
############################################################################
# Assign biological scenarios for the predicted compounds
# ##########################################################################
processes.assignScenarios()
        
