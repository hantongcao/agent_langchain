#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LangChain 调用大模型 Demo
使用 LangChain 与自定义 API 端点进行交互
"""

import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# API 配置参数
API_KEY = "eazytec_ec93ce714794e79d_5bd31c12884a8d1549a1740782419d02"
BASE_URL = "https://maas.eazytec-cloud.com/v1"
MODEL = "maas/qwen3"

def create_chat_model():
    """
    创建 ChatOpenAI 实例
    """
    return ChatOpenAI(
        model=MODEL,
        openai_api_key=API_KEY,
        openai_api_base=BASE_URL,
        temperature=0.7,
        max_tokens=1000
    )

def simple_chat_demo():
    """
    简单对话示例
    """
    print("=== 简单对话示例 ===")
    
    # 创建聊天模型
    chat = create_chat_model()
    
    # 发送消息
    messages = [
        HumanMessage(content="你好，你是谁？")
    ]
    
    try:
        response = chat(messages)
        print(f"用户: 你好，你是谁？")
        print(f"AI: {response.content}")
    except Exception as e:
        print(f"错误: {e}")

def system_prompt_demo():
    """
    带系统提示的对话示例
    """
    print("\n=== 带系统提示的对话示例 ===")
    
    # 创建聊天模型
    chat = create_chat_model()
    
    # 带系统提示的消息
    messages = [
        SystemMessage(content="你是一个专业的 Python 编程助手，请用简洁明了的方式回答问题。"),
        HumanMessage(content="请解释什么是 LangChain？")
    ]
    
    try:
        response = chat(messages)
        print(f"用户: 请解释什么是 LangChain？")
        print(f"AI: {response.content}")
    except Exception as e:
        print(f"错误: {e}")

def multi_turn_conversation():
    """
    多轮对话示例
    """
    print("\n=== 多轮对话示例 ===")
    
    # 创建聊天模型
    chat = create_chat_model()
    
    # 对话历史
    conversation_history = [
        SystemMessage(content="你是一个友好的助手。")
    ]
    
    # 模拟多轮对话
    user_inputs = [
        "我想学习 Python 编程",
        "从哪里开始比较好？",
        "推荐一些学习资源"
    ]
    
    for user_input in user_inputs:
        # 添加用户消息
        conversation_history.append(HumanMessage(content=user_input))
        
        try:
            # 获取 AI 回复
            response = chat(conversation_history)
            
            print(f"用户: {user_input}")
            print(f"AI: {response.content}")
            print("-" * 50)
            
            # 将 AI 回复添加到对话历史
            conversation_history.append(response)
            
        except Exception as e:
            print(f"错误: {e}")
            break

def main():
    """
    主函数
    """
    print("LangChain 大模型调用 Demo")
    print(f"模型: {MODEL}")
    print(f"API 端点: {BASE_URL}")
    print("=" * 60)
    
    # 运行各种示例
    simple_chat_demo()
    system_prompt_demo()
    multi_turn_conversation()
    
    print("\n=== Demo 结束 ===")

if __name__ == "__main__":
    main()