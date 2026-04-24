from __future__ import annotations

import json

from principle_econ.cli.main import main


def test_cli_equilibrium_outputs_json(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        "sys.argv",
        [
            "principle-econ",
            "equilibrium",
            "--demand-intercept",
            "10",
            "--demand-slope",
            "-1",
            "--supply-intercept",
            "2",
            "--supply-slope",
            "1",
        ],
    )
    main()
    out = capsys.readouterr().out
    payload = json.loads(out)
    assert "q_star" in payload
    assert "p_star" in payload


def test_cli_tax_outputs_json(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        "sys.argv",
        [
            "principle-econ",
            "tax",
            "--demand-intercept",
            "10",
            "--demand-slope",
            "-1",
            "--supply-intercept",
            "2",
            "--supply-slope",
            "1",
            "--tax-type",
            "per_unit",
            "--amount",
            "1",
            "--tax-on",
            "producer",
        ],
    )
    main()
    out = capsys.readouterr().out
    payload = json.loads(out)
    assert "post_tax" in payload
    assert "delta_q" in payload
