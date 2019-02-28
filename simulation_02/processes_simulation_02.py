######################################
#  PROCESSES SIMULATION 02
#  BETA-CARYOPHYLLENE AND SIDE PRODUCTS
######################################

# GRAMMAR
ls = LabelSettings(LabelType.Term, LabelRelation.Unification)
######################################
#  PIVOT MOLECULES
######################################
fpp = graphDFS("CC(=CCCC(=CCCC(=CCO[P](=O)(O)O[P](=O)(O)O)C)C)C", "FPP")
npp = graphDFS("CC(C)=CCCC(C)=CCCC(C)(OP(O)(OP(O)(O)=O)=O)C=C", "NPP")
cationC1 = smiles("CC(C)=CCCC(C)=CCCC(C)=C[CH2+]", "FPP cation C1+")
cationC3 = smiles("C[C+](CCC=C(C)CCC=C(C)C)C=C", "FPP/NPP C3+")
H = graphDFS("[H+]", "H+")
H2O = smiles("[OH2]", "H2O")
######################################
# ANIONS
######################################
opp = graphDFS("OP(O)(OP(O)([O-])=O)=O", "OPP-")
######################################
# CATIONS
######################################
farnesylC1 = smiles("C[C]([CH][CH2+])CCC=C(C)CCC=C(C)C", "farnesyl C1+")
farnesylC2 = smiles("C[C+][C](C)CCC=C(C)CCC=C(C)C", "farnesyl C2+")
farnesylC3 = smiles("[CH2][CH][C+](C)CCC=C(C)CCC=C(C)C", "farnesyl C3+")
# 1-11 group
e_e_humulyl_cation = smiles("CC1(C)[CH+]CCC(C)=CCCC(C)=CC1", "E,E Humulyl cation C11+");
e_z_humulyl_cation = graphDFS("CC1(C)[C+]CCC(C)=CCCC(C)=CC1", "E,Z Humulyl cation C11+");
# 1-10 group
germacrenylC11 = smiles("C[C+](C)C1CCC(C)=CCCC(C)=CC1", "germacrenyl C11+")
germacrenylC1 = smiles("C[C](C)C1CCC(C)=CCCC(C)=C[CH2+]1", "germacrenyl C1+")
germacrenylAC7 = smiles("C[C+]1[CH]CCC(C)=CCC(CC1)C(C)=C", "germacrene A C7+")
germacrenylBC7 = smiles("C[C+]1[CH]CCC(C)=CCC(CC1)=C(C)C", "germacrene B C7+")
germacrenylCC7 = smiles("C[C](C)C1CC[C+](C)[CH]CCC(C)=C[CH2]=1", "germacrene C C7+")
germacrenylDC7 = smiles("C[C](C)C1CC[C+](C)[CH]CCC(C=[CH2]1)=C", "germacrene D C7+")

######################################
# TARGET MOLECULES
######################################
beta_caryophyllene = smiles("CC1CCC2C(CC2(C)C)C(CCC=1)=C", "beta-caryophyllene")
alpha_humulene = smiles("CC1CCC=C(C)CC=CC(C)(C)CC=1", "alpha-humulene")
beta_farenesene = smiles("C[C](CCC=C(C)CCC=C(C)C)[C]=C", "beta-farnesene")

######################################
# RULES
######################################
pushFilePrefix("../rules/")
opp_loss_for_fpp = ruleGML('opp_loss_for_fpp.gml')
#opp_loss_for_npp_c1 = ruleGML('opp_loss_for_npp_c1.gml')
#opp_loss_for_npp_c3 = ruleGML('opp_loss_for_npp_c3.gml')
#opp_gain_by_farnesyl_cation = ruleGML('opp_gain_by_farnesyl_cation.gml')
#fpp_1_10_cyc = ruleGML("fpp-1-10Cyc.gml")
fpp_1_11_cyc = ruleGML("fpp-1-11Cyc.gml")
ring_closure_c2_c10 = ruleGML("2-10Cyc.gml")
#h_shift_c1_c2 = ruleGML("1-2Hshift.gml")
#h_shift_c1_c3 = ruleGML("1-3Hshift.gml")
h_loss = ruleGML("h_loss.gml")
#h2o_gain = ruleGML("h2o_gain.gml")
popFilePrefix()

######################################
# DEFINE LIST OF INITIAL INPUTS
######################################
eductMols = [fpp]

######################################
# HYPERGRAPH GENERATION
######################################

# comput overall charge of molecule
def overallCharge(a):
    return sum(int(v.charge) for v in a.vertices)

# calculate the cyclomatic number
def countCycs(a):
        return a.numEdges - a.numVertices + 1

# a general breadth-first expansion strategy
strat = (addSubset(eductMols) >> repeat[7](inputRules))

# calculate derivation graph (hypergraph)
dg = dgRuleComp(inputGraphs, strat, ls)
dg.calc()

######################################
# PDF PRINTER
######################################
p = DGPrinter()
# print molecule with all the hydrogenes attached
p.graphPrinter.collapseHydrogens = True
# color molecules with rings red, charged molecules blue
p.pushVertexColour(lambda g, dg: "red" if overallCharge(g) != 0 else "black" if countCycs(g) > 0 else "black")

postSection("Generated Hypergraph")
dg.print(p)

postSection("Rules")
for r in inputRules:
	r.print()

# Print product SMILES to stdout
for v in dg.vertices:
    m = v.graph
    if m.isMolecule:
        print(m.name, m.smiles)
    else:
        print(m.name, m.graphDFS)    