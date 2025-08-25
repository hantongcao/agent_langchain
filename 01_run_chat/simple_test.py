#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的 LangChain 测试脚本
用于快速测试 API 连接
"""

from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# API 配置
API_KEY = "eazytec_ec93ce714794e79d_5bd31c12884a8d1549a1740782419d02"
BASE_URL = "https://maas.eazytec-cloud.com/v1"
MODEL = "maas/qwen3"

def test_connection():
    """
    测试 API 连接
    """
    print("正在测试 API 连接...")
    
    try:
        # 创建聊天模型
        chat = ChatOpenAI(
            model=MODEL,
            openai_api_key=API_KEY,
            openai_api_base=BASE_URL,
            temperature=0.7
        )
        
        # 发送测试消息
        message = HumanMessage(content="你好，你是谁？")
        response = chat([message])
        
        print("✅ API 连接成功！")
        print(f"问题: 你好，你是谁？")
        print(f"回答: {response.content}")
        
    except Exception as e:
        print(f"❌ API 连接失败: {e}")
        print("请检查 API_KEY、BASE_URL 和 MODEL 配置是否正确")

if __name__ == "__main__":
    test_connection()