import os
import sys
import pytest
import calculation

directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.join(directory, "..", "submission.py")))

import submission

variable_strings = [
    "Temperature (C)",
    "Cloud Density",
    "Photosynthesis",
    "Plants Density",
    "Oxygen",
    "Carbon Dioxide",
    "ASI",
    "Rainfall Intensity",
    "Radius of wet ground",
    "Rainfall Area",
    "Power",
    "UV index",
    "Pollution",
    "Health Risk",
    "Crop Yield",
    "Hunger",
    "Water Resources",
    "Thirst",
    "Albedo",
]


def test_team_name():
    teams = [
        "Coding Rizzlers",
        "Prime time",
        "AI GIRLS",
        "Radiance",
        "Gameover",
        "SIA",
        "Karachi kings",
        "team xlr",
        "Ben Dover",
        "SES",
        "The mathletes",
        "ligma Theorem", 
        "Syntax squad",
        "They who must be named",
        "The Pi-rates",
        "Doubleaa", 
        "Mathemagicians",
        "Code Crusaders", 
        "TeaMDEX",
        "AMK",
        "calculators",
        "Desires",
        "Alto Coders",
        "auto-checkmate",
        "JMT",
        "bazooka",
        "Infinity squad", 
        "Champions", 
        "fermatslasttheorem",
        "Mathstronauts",
        "Mad math",
        "Thebugers",
        "Mak",
        "stellars",
        "Nueral Obsidians",
        "WM team"
    ]

    assert hasattr(submission, "TEAM_NAME"), "TEAM_NAME not found in submission.py"
    assert submission.TEAM_NAME in teams, "TEAM_NAME is not valid"


def test_computation():
    """
    Tests the computation of variables using the engine built from the evaluation order
    defined in the submission module.
    The test performs the following checks:
    1. Ensures that the 'evaluation_order' attribute exists in the submission module.
    2. Initializes a dictionary of independent variables.
    3. Builds the computation engine using the evaluation order.
    4. Computes the variables using the engine and the independent variables.
    5. Asserts that the computation does not raise any exceptions.
    6. Asserts that the computed variables are not None.
    7. Asserts that the independent variables are not modified.
    8. Checks that all expected variable strings are present in the computed variables.
    9. Asserts that the number of computed variables is correct (18 plus the number of independent variables).
    Raises:
        AssertionError: If any of the assertions fail.
    """

    assert hasattr(
        submission, "evaluation_order"
    ), "evaluation_order not found in submission.py"

    indep_vars = {"Solar Intensity": 0, "Humidity": 0, "Wind Speed": 0, "Population": 0}

    engine = calculation.build_engine(submission.evaluation_order)
    vars = None
    try:
        vars = engine.compute(indep_vars)
    except Exception as e:
        assert False, f"Error in compute method: {e}"

    assert vars is not None, "No variables computed"
    assert vars is not indep_vars, "indep_vars should not be modified"

    for variable in variable_strings:
        assert variable in vars, f"{variable} not found in computed variables"

    assert len(vars) == 19 + len(indep_vars), "Incorrect number of variables computed"

calculation