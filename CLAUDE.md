# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

共享剪贴板 - 一个简单的局域网剪贴板共享 Web 应用，基于 Flask。

## 常用命令

```bash
# 启动应用
python run.py
# 默认监听 http://0.0.0.0:5000
```

## 架构说明

- **run.py**: Flask 后端，提供剪贴板存储和展示功能
  - `/` - 主页，展示剪贴板内容并发送新内容
  - `/text` - 历史记录页面
  - 使用内存存储剪贴板内容（非持久化）

- **templates/index.html**: 前端页面，使用原生 HTML/CSS/JS，无框架依赖

- **可选配置**: 通过环境变量 `FILESHARE_URL` 配置配套的文件共享站点链接