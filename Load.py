#施加梁单元荷载
#** {base url} + db/BMLD**​
#**Active Methods**
#|**Get, Post, Put, Delete**|

{
    "BMLD": {
        "ITEMS": {
            "__DESC__": "Beam Load Items",
            "__TYPE__": [
                {
                    "ID": {
                        "__DESC__": "ID",
                        "__TYPE__": "Integer"
                    },
                    "LCNAME": {
                        "__DESC__": "Load Case Name",
                        "__TYPE__": "String"
                    },
                    "GROUP_NAME": {
                        "__DESC__": "Group Name",
                        "__TYPE__": "String"
                    },
                    "CMD": {
                        "__DESC__": "Element Type",
                        "__TYPE__": "String"
                    },
                    "TYPE": {
                        "__DESC__": "LoadTYPE",
                        "__TYPE__": "String"
                    },
                    "DIRECTION": {
                        "__DESC__": "Load Direction",
                        "__TYPE__": "String"
                    },
                    "VX": {
                        "__DESC__": "Vector X",
                        "__TYPE__": "Real"
                    },
                    "VY": {
                        "__DESC__": "Vector Y",
                        "__TYPE__": "Real"
                    },
                    "VZ": {
                        "__DESC__": "Vector Z",
                        "__TYPE__": "Real"
                    },
                    "USE_PROJECTION": {
                        "__DESC__": "Use Projection",
                        "__TYPE__": "Bool"
                    },
                    "USE_ECCEN": {
                        "__DESC__": "Is Eccentricity",
                        "__TYPE__": "Bool"
                    },
                    "ECCEN_TYPE": {
                        "__DESC__": "Eccentricity Type",
                        "__TYPE__": "Integer"
                    },
                    "ECCEN_DIR": {
                        "__DESC__": "Eccentricity Direction",
                        "__TYPE__": "String"
                    },
                    "I_END": {
                        "__DESC__": "Distance I",
                        "__TYPE__": "Real"
                    },
                    "J_END": {
                        "__DESC__": "Distance J",
                        "__TYPE__": "Real"
                    },
                    "USE_J_END": {
                        "__DESC__": "Use Distance J",
                        "__TYPE__": "Bool"
                    },
                    "D": {
                        "__DESC__": "Distance Ratio",
                        "__TYPE__": [
                            "Real",
                            4
                        ]
                    },
                    "P": {
                        "__DESC__": "Force Type",
                        "__TYPE__": [
                            "Real",
                            4
                        ]
                    },
                    "USE_ADDITIONAL": {
                        "__DESC__": "Use Additional",
                        "__TYPE__": "Bool"
                    },
                    "ADDITIONAL_I_END": {
                        "__DESC__": "Additional Distance I",
                        "__TYPE__": "Real"
                    },
                    "ADDITIONAL_J_END": {
                        "__DESC__": "Additional Distance J",
                        "__TYPE__": "Real"
                    },
                    "USE_ADDITIONAL_J_END": {
                        "__DESC__": "Use Additional Distance J",
                        "__TYPE__": "Bool"
                    }
                }
            ]
        }
    }
}
#EXample Uniform
{
    "BMLD": {
        "1": {
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "DL",
                    "GROUP_NAME": "GN1",
                    "CMD": "BEAM",
                    "TYPE": "UNILOAD",
                    "DIRECTION": "GZ",
                    "USE_PROJECTION": false,
                    "USE_ECCEN": false,
                    "D": [
                        0,
                        1,
                        0,
                        0
                    ],
                    "P": [
                        -20,
                        -20,
                        0,
                        0
                    ],
                    "USE_ADDITIONAL": false,
                    "ADDITIONAL_I_END": 0,
                    "ADDITIONAL_J_END": 0,
                    "USE_ADDITIONAL_J_END": false
                }
            ]
        }
    }
}
