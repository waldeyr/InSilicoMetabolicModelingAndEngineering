######################################
#  PIVOT MOLECULES
######################################
fpp = graphDFS("CC(=CCCC(=CCCC(=CCO[P](=O)(O)O[P](=O)(O)O)C)C)C", "FPP")
npp = graphDFS("CC(C)=CCCC(C)=CCCC(C)(OP(O)(OP(O)(O)=O)=O)C=C", "NPP")
opp = graphDFS("OP(O)(OP(O)([O-])=O)=O", "OPP-")
cationC1 = smiles("CC(C)=CCCC(C)=CCCC(C)=C[CH2+]", "FPP cation (C1)")
cationC3 = smiles("C[C+](CCC=C(C)CCC=C(C)C)C=C", "FPP/NPP C3+")
H = graphDFS("[H+]", "H+")
H2O = smiles("[OH2]", "H2O")
######################################
# CATIONS
######################################
# farnesyl cation
farnesylC1 = smiles("C[C]([CH][CH2+])CCC=C(C)CCC=C(C)C", "farnesyl C1+")
farnesylC2 = smiles("C[C+][C](C)CCC=C(C)CCC=C(C)C", "farnesyl C2+")
farnesylC3 = smiles("[CH2][CH][C+](C)CCC=C(C)CCC=C(C)C", "farnesyl C3+")
# 1-11 group
humulylC10 = smiles("CC1CC[CH+]C(C)(C)CC=C(C)CCC=1", "humulyl C10+")
# 1-10 group
germacrenylC11 = smiles("C[C+](C)C1CCC(C)=CCCC(C)=CC1", "germacrenyl C11+")
germacrenylC1 = smiles("C[C](C)C1CCC(C)=CCCC(C)=C[CH2+]1", "germacrenyl C1+")
germacrenylAC7 = smiles("C[C+]1[CH]CCC(C)=CCC(CC1)C(C)=C", "germacrene A C7+")
germacrenylBC7 = smiles("C[C+]1[CH]CCC(C)=CCC(CC1)=C(C)C", "germacrene B C7+")
germacrenylCC7 = smiles("C[C](C)C1CC[C+](C)[CH]CCC(C)=C[CH2]=1", "germacrene C C7+")
germacrenylDC7 = smiles("C[C](C)C1CC[C+](C)[CH]CCC(C=[CH2]1)=C", "germacrene D C7+")
# 1-6 group
bisabolylC1a = smiles("C[C](CCC=C(C)C)C1CCC(C)=C[CH2+]1", "bisabolyl C1+")
bisabolylC1b = smiles("CC(CCC=C(C)C)C1CCC(C)=C[CH+]1", "bisabolyl C1+")
bisabolylC2a = smiles("CC(CCC=C(C)C)C1C[CH+]C(C)=CC1", "bisabolyl C2+")
bisabolylC2b = smiles("CC(CCC=C(C)C)C1CCC(C)=[C+]C1", "bisabolyl C2+")
bisabolylC3 = smiles("C[C](CCC=C(C)C)C1CC[C+](C)=CC1", "bisabolyl C3+")
bisabolylC6 = smiles("CC(CCC=C(C)C)[C+]1CCC(C)=CC1", "bisabolyl C6+")
bisabolylC7 = smiles("C[C+](CCC=C(C)C)C1CCC(C)=CC1", "bisabolyl C7+")
bisabolylC8 = smiles("CC([CH+]CC=C(C)C)C1CCC(C)=CC1", "bisabolyl C8+")
bisabolylC5a = smiles("C[C](CCC=C(C)C)C1CC=C(C)C[CH2+]1", "bisabolyl C5+")
bisabolylC5b = smiles("CC(CCC=C(C)C)C1CC=C(C)C[CH+]1", "bisabolyl C5+")
bisabolylC9a = smiles("C[C](C[CH2+]C=C(C)C)C1CCC(C)=CC1", "bisabolyl C9+")
bisabolylC9b = smiles("CC(C[CH+]C=C(C)C)C1CCC(C)=CC1", "bisabolyl C9+")
bisabolylC10 = smiles("CC(CC[C+]=C(C)C)C1CCC(C)=CC1", "bisabolyl C10+")
bisabolylC14 = smiles("CC(C)=CCCC([CH2+])C1CCC(C)=CC1", "bisabolyl C14+")
# important intermediates
bergamotenylC3 = smiles("C[C+]1CCC2CC1C2(C)CCC=C(C)C", "bergamotenyl C3+")
farnesylC2a = smiles("CC(CCC=C(C)CCC=C(C)C)[C+]=C", "farnesyl C2+a")
farnesylC2b = smiles("C[C+]=C(C)CCC=C(C)CCC=C(C)C", "farnesyl C2+b")
farnesylC4 = smiles("CC([CH+]CC=C(C)CCC=C(C)C)C=C", "farnesyl C4+")
farnesylC5a = smiles("C[C](C[CH2+]C=C(C)CCC=C(C)C)C=C", "farnesyl C5+a")
farnesylC5b = smiles("CC(C[CH+]C=C(C)CCC=C(C)C)C=C", "farnesyl C5+b")
farnesylC6 = smiles("CC(CC[C+]=C(C)CCC=C(C)C)C=C", "farnesyl C6+")
farnesylC15 = smiles("CC(C)=CCCC(C)=CCCC([CH2+])C=C", "farnesyl C15+")
cadinan_7_yl_C7 = smiles("C[C](C)C1CC[C+](C)C2CCC(C)=C[CH2]12", "cadinan-7-yl C7+")
cadinan_3_yl_C3 = smiles("C[C](C)C1CC[C](C)C2CCC(C)=C[CH2+]12", "cadinan-3-yl C3+")
copaenylC3 = smiles("C[C](C)C1CCC2(C)C3CC[C+](C)C2[CH2]13", "copaenyl C3+")
#bergamotenylC3 = smiles("C[C+]1CCC2CC1C2(C)CCC=C(C)C", "bergamotenyl C3+")
selenylC3a = smiles("C[C+]1CC[CH]C2(C)CCC(CC12)C(C)=C", "selenyl C3+a")
selenylC3b = smiles("C[C+]1CC[CH]C2(C)CCC(CC12)=C(C)C", "selenyl C3+b")
selenylC3c = smiles("C[C](C)C1CCC2(C)[CH]CC[C+](C)C2[CH2]=1", "selenyl C3+c")
selenylC3d = smiles("C[C](C)C1CCC2(C)[CH]CCC(C2[CH2+]1)=C", "selenyl C3+d")
elemennyl = smiles("CC(C1CCC2(C)[CH](C1)=C(C)C[CH2+]C=2)=C", "elemenyl C+")
elemenylC11 = smiles("C[C+](C)C1CCC(C)(C=C)C(C1)C(C)=C", "elemenyl C11+")

betaCaryophyllene = smiles("CC1CCC2[C](CC2(C)C)C(CCC=1)=[CH3]", "beta-caryophyllene")
alphaHumulene = smiles("CC1=CCC(C=CCC(=CCC1)C)(C)C", "alpha-humulene")
betaBisabolene = smiles("CC1=CCC(CC1)C(=C)CCC=C(C)C", "beta-bisabolene")
betaSesquiphellandrene = smiles("C[C](CCC=C(C)C)C1CCC(C=[CH2]1)=C", "beta-sesquiphellandrene")
alphaZingiberene = smiles("C[C](CCC=C(C)C)C1CC=C(C)C=[CH2]1", "alpha-zingiberene")
alphaMuurolene = smiles("C[C](C)C1CC=C(C)C2CCC(C)=C[CH2]12", "alpha-muurolene or alpha-cadinene")
gammaMuurolene = smiles("C[C](C)C1CCC(C2CCC(C)=C[CH2]12)=C",
						"gamma-muurolene or gamma-cadinene or gamma-amorphene")
alphaCopaene = smiles("C[C](C)C1CCC2(C)C3CC=C(C)C2[CH2]13", "alpha-copaene")
alphaSelinene = smiles("CC(C1CCC2(C)[CH]CC=C(C)C2C1)=C", "alpha-selinene")
betaSelinene = smiles("CC(C1CCC2(C)[CH]CCC(C2C1)=C)=C", "beta-selinene")
germacreneB = smiles("CC(C)=C1CCC(C)=CCCC(C)=CC1", "germacrene B")
germacreneD = smiles("C[C](C)C1CCC(C)=CCCC(C=[CH2]1)=C", "germacrene D")
betaBergamotene = smiles("CC(C)=CCCC1(C)C2CCC(C1C2)=C", "beta-bergamotene")
alphaBergamotene = smiles("CC(C)=CCCC1(C)C2CCC(C)=C1C2", "alpha-bergamotene or trans-alpha-bergamotene")
alphaElemene = smiles("[CH2][C](C)[CH]1C(C)(CCC([CH2]=1)=C(C)C)C=C", "alpha-elemene")
betaElemene = smiles("CC(C1CCC(C)(C=C)C(C1)C(C)=C)=C", "beta-elemene")
betaBisabolol = smiles("C[C](CCC=C(C)C)C1CC=C(C)C[CH2]1O", "beta-bisabolol")
alphaBisabolol = smiles("CC(C)=CCCC(C)(O)C1CCC(C)=CC1", "alpha-bisabolol")
alphaCadinol = smiles("C[C](C)C1CCC(C)(O)C2CCC(C)=C[CH2]12", "alpha-cadinol or tau-muurolol or tau-cadinol")
bicyclogermacrene = smiles("CC1CCC2[CH2](C=C(C)CCC=1)C2(C)C", "bicyclogermacrene")
cadalene = smiles("C[C](C)[CH]1[CH2]=[CH2]C(C)=C2[CH2]=[CH2]C(C)=C[CH2]2=1", "cadalene")
alphaFarnesene = smiles("CC(C)=CCCC(C)=CCC=C(C)C=C", "alpha-farnesene")
betaFarnesene = smiles("CC(C)=CCCC(C)=CCCC(C=C)=C", "beta-farnesene")
farnesol = smiles("CC(C)=CCCC(C)=CCCC(C)=CCO", "farnesol")
alphaBisabolene = smiles("CC(C)=CCC=C(C)C1CCC(C)=CC1", "alpha-bisabolene")
deltaCadinene = smiles("C[C](C)C1CCC(C)=C2CCC(C)=C[CH2]12", "delta-cadinene")
gammaSelinene = smiles("CC(C1CCC2(C)[CH]CCC(C)=C2C1)=C", "selina-4,11-diene")
alphaCurcumene = smiles("CC1=CC=C(C=C1)C(C)CCC=C(C)C", "alpha-curcumene")
deltaElemene = smiles("CC(C)C1=CC(C(CC1)(C)C=C)C(=C)C", "delta-elemene")
germacreneA = smiles("CC1=CCCC(=CCC(CC1)C(=C)C)C", "germacrene A")
germacreneC = smiles("C[C](C)C1CCC(C)=CCCC(C)=C[CH2]=1", "germacrene C")
cyclohexene = smiles("CC(C)=CCCC(C)=C1CCC(C)=CC1", "cyclohexene")
#betaCurcumene = smiles("C[C](CCC=C(C)C)C1CC=C(C)C[CH2]=1", "beta-curcumene")
gammaCurcumene = smiles("C[C](CCC=C(C)C)C1CCC(C)=C[CH2]=1", "gamma-curcumene")
deltaBisabolene = smiles("CC(CCC=C(C)C)C1CCC(C)=CC=1", "delta-bisabolene")
gammaBisabolene = smiles("C[C](CCC=C(C)C)C1CC=C(C)C[CH2]=1", "gamma-bisabolene")
gammaElemeneA = smiles("[CH2][CH]C1(C)CCC(CC1C(C)=C)=C(C)C", "gamma-elemene")
gammaElemeneB = smiles("C[C](C)C1CCC(C)(C=C)C([CH2]=1)C(C)=C", "gamma-elemene")
gammaElemeneC = smiles("CC(C)=C1CCC(C)(C=C)C(C1)C(C)=C", "gamma-elemene")
transBetaCaryophyllene = smiles("CC1CCC2[C](CC2(C)C)C(C)=[CH2]CC=1", "trans-Caryophyllene")
guaiene = smiles("C[C]1CC[CH]2[C](C)CCC(CC1=2)C(C)=C", "guaiene")
