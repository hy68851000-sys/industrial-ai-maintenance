## 🌐 在线体验
👉 [点击这里直接体验](https://industrial-ai-maintenance-6f3gmop2bmuvjpicdeyq44.streamlit.app/)


# industrial-ai-maintenance
工厂设备预测性维护系统 - 机器学习+LLM诊断
# 工厂设备预测性维护系统

基于机器学习 + 大语言模型的工业设备故障预测与诊断系统

## 项目简介
使用AI4I 2020真实工厂数据集，构建了一个端到端的设备维护AI系统：
- 通过机器学习预测设备是否会发生故障
- 通过LLM将预测结果转化为自然语言诊断报告
- 通过RAG技术让AI基于设备手册回答维护问题

## 技术栈
- Python / Pandas / Numpy
- Scikit-learn（随机森林）
- ZhipuAI GLM-4（大语言模型）
- RAG（检索增强生成）

## 数据集
AI4I 2020 Predictive Maintenance Dataset
- 10000条设备运行记录
- 故障率3.39%，包含5种故障类型

## 主要结论
- 扭矩是故障最强预测信号（特征重要性32%）
- 刀具磨损超过200min后故障率显著上升
- 低转速+高扭矩是高危工况组合
- 模型准确率98%，故障召回率59%

## 项目结构
- `notebook.ipynb` - 完整代码
- `README.md` - 项目说明

## 作者
工业工程专业在读 | 工业AI方向
