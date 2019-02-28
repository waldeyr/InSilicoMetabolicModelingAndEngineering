# Processes Special Issue "In Silico Metabolic Modeling and Engineering"
# Rule refrence:  (Christianson, 2017) https://doi.org/10.1021/acs.chemrev.7b00287
rule [
    ruleID "FPP 1,10 cyclization"
    left [
        node [ id 11 label "C" ]
        node [ id 12 label "OPP" ]
        edge [ source 1  target 12 label "-" ]  
        edge [ source 10 target 11 label "=" ]
    ]
    context [
        node [ id 1  label "C" ]
        node [ id 2  label "*" ]
        node [ id 3  label "*" ]
        node [ id 4  label "*" ]
        node [ id 5  label "*" ]
        node [ id 6  label "*" ]
        node [ id 7  label "*" ]
        node [ id 8  label "*" ]
        node [ id 9  label "*" ]
        node [ id 10 label "C" ]
        edge [ source 1 target 2  label "*" ]
        edge [ source 2 target 3  label "*" ]
        edge [ source 3 target 4  label "*" ]
        edge [ source 4 target 5  label "*" ]
        edge [ source 5 target 6  label "*" ]
        edge [ source 6 target 7  label "*" ]
        edge [ source 7 target 8  label "*" ]
        edge [ source 8 target 9  label "*" ]
        edge [ source 9 target 10 label "*" ]
    ]
    right [
    node [ id 11 label "C+" ]
    node [ id 12 label "OPP-" ]
    edge [ source 10 target 1  label "-" ]
    edge [ source 10 target 11 label "-" ]
    ]
]