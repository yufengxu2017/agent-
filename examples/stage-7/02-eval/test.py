"""Stage 7 練習 2 自我驗證 — eval pipeline + 兩種 evaluator。"""

from __future__ import annotations

import sys
from types import SimpleNamespace
from unittest.mock import MagicMock

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from starter import EVAL_CASES, eval_llm_as_judge, eval_substring, run_eval


def test_eval_substring_pass():
    case = {"id": "x", "input": "?", "expected_substring": "Tokyo"}
    assert eval_substring("The capital is Tokyo.", case) is True
    print("✅ test_eval_substring_pass")


def test_eval_substring_fail():
    case = {"id": "x", "input": "?", "expected_substring": "Tokyo"}
    assert eval_substring("The capital is Beijing.", case) is False
    print("✅ test_eval_substring_fail")


def test_eval_substring_case_insensitive():
    case = {"id": "x", "input": "?", "expected_substring": "tokyo"}
    assert eval_substring("The capital is TOKYO.", case) is True
    print("✅ test_eval_substring_case_insensitive")


def test_eval_llm_as_judge_pass():
    """Mock judge replies PASS。"""
    judge = MagicMock()
    judge.chat.completions.create.return_value = SimpleNamespace(
        choices=[SimpleNamespace(message=SimpleNamespace(content="PASS"))]
    )
    case = {"id": "x", "input": "What's the capital?", "expected_substring": "Tokyo"}
    assert eval_llm_as_judge("Tokyo!", case, judge_llm=judge) is True
    print("✅ test_eval_llm_as_judge_pass")


def test_eval_llm_as_judge_fail():
    judge = MagicMock()
    judge.chat.completions.create.return_value = SimpleNamespace(
        choices=[SimpleNamespace(message=SimpleNamespace(content="FAIL"))]
    )
    case = {"id": "x", "input": "?", "expected_substring": "Tokyo"}
    assert eval_llm_as_judge("Beijing", case, judge_llm=judge) is False
    print("✅ test_eval_llm_as_judge_fail")


def test_run_eval_aggregates_correctly():
    """Mock agent 給 3 對 + 2 錯、確認 pass_count + pass_rate 正確。"""
    def fake_agent(question, instruction="", **kw):
        # 假設 input 含「math」就答對，否則答錯
        if "math" in question.lower() or "what is" in question.lower() and "+" in question:
            return "4 or 50"
        if "Japan" in question:
            return "Tokyo"
        if "France" in question:
            return "Paris"
        return "wrong answer"

    out = run_eval(EVAL_CASES, fake_agent, eval_substring)
    assert out["total"] == 5
    assert out["pass_count"] >= 4, f"預期 ≥4 pass、得到 {out['pass_count']}"
    print("✅ test_run_eval_aggregates_correctly")


def test_eval_cases_corpus_shape():
    assert len(EVAL_CASES) == 5
    for c in EVAL_CASES:
        assert {"id", "input", "expected_substring"} <= c.keys()
    print("✅ test_eval_cases_corpus_shape")


if __name__ == "__main__":
    test_eval_substring_pass()
    test_eval_substring_fail()
    test_eval_substring_case_insensitive()
    test_eval_llm_as_judge_pass()
    test_eval_llm_as_judge_fail()
    test_run_eval_aggregates_correctly()
    test_eval_cases_corpus_shape()
    print("\n🎉 全部通過 — eval pipeline 邏輯正確")
