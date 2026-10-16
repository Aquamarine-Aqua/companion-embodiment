# Testing

这份仓库的测试分两层：**作者内置自检**和**冒烟测试入口**。它们能保证状态机/管道在示例用例下 behaved as expected，但不等于生产可用验收。

## 快速运行

仓库根目录执行：

```bash
python3 embodiment.py
python3 reproductive_state.py
python3 minimal_gateway.py
python3 -m unittest discover -s tests -v
```

- `embodiment.py`：直接运行会执行 `_self_check()`，覆盖内分泌惯性、失聪耳朵优先、器官被戳中的即时皮质醇 bump、敏感度上下限等。
- `reproductive_state.py`：直接运行会执行 `_selftest()`，覆盖 ready 回差、显式事件驱动、进入/锁结门槛、恢复期持久化、标记变体与擦除、身体不适分层词表等。
- `minimal_gateway.py`：是**叙事演示脚本**，会打印注入、模型输出、擦标记后的正文和动作痕迹；它不是断言式测试套件，主要用于人工检查管道形状。
- `python3 -m unittest discover -s tests -v`：把前两个内置自检包成 `unittest` 用例，方便 CI 或本地统一发现。

## 冒烟测试覆盖范围

`tests/test_smoke.py` 只验证：

1. `embodiment._self_check()` 可导入并运行通过；
2. `reproductive_state._selftest()` 可导入并运行通过。

它**不**验证你的接入系统真的安全、合规或符合同意边界；那些必须在服务端集成测试里做。

## 接入前人工检查清单

在把这套状态机接进真实对话循环前，至少确认：

- 所有生成通道都走同一份 `strip_markers()` / `finish_turn()` 收尾逻辑；新增 endpoint、定时推送、工具调用输出都不能绕过。
- 用于校验 `start_penetration()` / `start_tie()` 的 arousal 读数在服务端现算，不接受客户端自报。
- 持久化保存 `ReproductiveState.saved` 整个 dict，尤其包含 `refractory_until`；重启后恢复期不能被清空。
- 标记解析只认约定括号变体，且会把标记周围的空壳一起收走；拒绝结果必须对使用者可见。
- `consent_active` 只能由人显式开启，不随旧会话恢复；`tie_veto` 的拒绝信息必须明确“不要补写”。
- 身体不适判定统一走 `is_physical_discomfort()`，不要按调用方各自补丁词表。
- 长期记忆开启前，先实现清除、导出、禁用和审计机制。

## 许可提醒

源码许可证以根目录 `LICENSE` / `LICENSING.md` 为准；文档与 README 以 `LICENSE-CONTENT` 为准。提交代码时不要沿用旧文件头里的许可证字样。
