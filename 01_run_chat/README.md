# LangChain 大模型调用示例

本目录包含使用 LangChain 调用自定义大模型 API 的示例代码。

## 文件说明

- `langchain_demo.py` - 完整的 LangChain 示例，包含多种使用场景
- `simple_test.py` - 简单的连接测试脚本
- `README.md` - 本说明文件

## API 配置

当前配置的 API 参数：
- **API_KEY**: `eazytec_ec93ce714794e79d_5bd31c12884a8d1549a1740782419d02`
- **BASE_URL**: `https://maas.eazytec-cloud.com/v1`
- **MODEL**: `maas/qwen3-235b-a22b`

## 运行示例

### 1. 快速测试连接

```bash
uv run python simple_test.py
```

这个脚本会快速测试 API 连接是否正常。

### 2. 完整示例演示

```bash
uv run python langchain_demo.py
```

这个脚本包含三个示例：
- 简单对话
- 带系统提示的对话
- 多轮对话

## 依赖要求

确保已安装以下依赖：

```bash
uv add langchain-openai
```

## 示例功能

### 简单对话
直接向模型发送问题并获取回答。

### 系统提示
使用系统提示来设定模型的角色和行为。

### 多轮对话
维护对话历史，实现上下文相关的多轮交互。

## 注意事项

1. 请确保 API_KEY 有效且有足够的配额
2. 网络连接正常，能够访问指定的 BASE_URL
3. 模型名称 MODEL 正确无误

## 错误排查

如果遇到连接问题，请检查：
- API_KEY 是否正确
- BASE_URL 是否可访问
- 模型名称是否存在
- 网络连接是否正常