"""Public API facade."""

from principle_econ.api.facade import (
    build_dwl_report,
    build_tax_visual_guide,
    compare_tax_scenario,
    comparative_statics,
    compute_arc_elasticity,
    compute_point_elasticity,
    compute_surplus,
    evaluate_price_control,
    line_from_inverse,
    line_from_standard,
    solve_equilibrium,
    solve_tax_equilibrium,
)

__all__ = [
    "build_dwl_report",
    "build_tax_visual_guide",
    "compare_tax_scenario",
    "comparative_statics",
    "compute_arc_elasticity",
    "compute_point_elasticity",
    "compute_surplus",
    "evaluate_price_control",
    "line_from_inverse",
    "line_from_standard",
    "solve_equilibrium",
    "solve_tax_equilibrium",
]
