"""Smoke tests: run the two built-in self-checks as unittest cases.

这些不是替代 `python3 embodiment.py` / `python3 reproductive_state.py` 的完整验收；
它们只保证仓库被引入 Python 环境后，核心自检仍然可运行、可被发现。

运行（仓库根目录）：

    python3 -m unittest discover -s tests -v
"""

from __future__ import annotations

import unittest

import embodiment
import reproductive_state


class BuiltInSelfCheckSmokeTest(unittest.TestCase):
    def test_embodiment_self_check(self) -> None:
        embodiment._self_check()

    def test_reproductive_state_selftest(self) -> None:
        reproductive_state._selftest()


if __name__ == "__main__":
    unittest.main()
