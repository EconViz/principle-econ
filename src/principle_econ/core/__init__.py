"""Core domain and solvers for linear market analysis."""

from principle_econ.core.controls import (
    PriceControlResult,
    PriceControlScenario,
    PriceControlType,
    evaluate_price_control,
)
from principle_econ.core.elasticity import (
    arc_price_elasticity,
    classify_elasticity,
    point_price_elasticity,
)
from principle_econ.core.equilibrium import EquilibriumResult, solve_equilibrium
from principle_econ.core.line import Line
from principle_econ.core.shifts import (
    ComparativeStaticsResult,
    ShiftScenario,
    ShiftSpec,
    ShiftedMarket,
    apply_shifts,
    comparative_statics,
)

__all__ = [
    "arc_price_elasticity",
    "classify_elasticity",
    "ComparativeStaticsResult",
    "EquilibriumResult",
    "evaluate_price_control",
    "Line",
    "point_price_elasticity",
    "PriceControlResult",
    "PriceControlScenario",
    "PriceControlType",
    "ShiftScenario",
    "ShiftSpec",
    "ShiftedMarket",
    "apply_shifts",
    "comparative_statics",
    "solve_equilibrium",
]
