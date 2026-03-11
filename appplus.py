import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from zhipuai import ZhipuAI

client = ZhipuAI(api_key="你的API_KEYa340d621d3514dfb91bb9917428806ee.Zp1oJ2QDsjhEoDWo")

# 训练模型（只在第一次运行时训练）
@st.cache_resource
def load_model():
    df = pd.read_csv('ai4i2020.csv')
    features = ['Air temperature [K]', 'Process temperature [K]',
                'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']
    X = df[features]
    y = df['Machine failure']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

model = load_model()

# 页面标题
st.title("🏭 工厂设备故障诊断系统")
st.write("输入设备参数，获取AI故障预测与诊断报告")

# 输入区域
col1, col2 = st.columns(2)
with col1:
    air_temp = st.slider("空气温度 (K)", 290, 320, 300)
    process_temp = st.slider("加工温度 (K)", 300, 330, 310)
    rpm = st.slider("转速 (RPM)", 1000, 3000, 1500)
with col2:
    torque = st.slider("扭矩 (Nm)", 10, 80, 40)
    tool_wear = st.slider("刀具磨损 (min)", 0, 300, 50)

# 诊断按钮
if st.button("🔍 开始诊断"):
    
    # 机器学习预测
    input_data = pd.DataFrame([[air_temp, process_temp, rpm, torque, tool_wear]],
                columns=['Air temperature [K]', 'Process temperature [K]',
                         'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]'])
    prob = model.predict_proba(input_data)[0][1]
    prediction = model.predict(input_data)[0]
    
    # 显示预测概率
    st.subheader("📊 机器学习预测结果")
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("故障概率", f"{prob*100:.1f}%")
    with col_b:
        if prediction == 1:
            st.error("⚠️ 预测：可能故障")
        else:
            st.success("✅ 预测：运行正常")
    
    st.progress(float(prob))
    
    # AI诊断
    st.subheader("🤖 AI诊断报告")
    with st.spinner("AI分析中..."):
        prompt = f"""
        你是工厂设备故障诊断专家。机器学习模型预测该设备故障概率为{prob*100:.1f}%。
        设备参数：
        - 空气温度：{air_temp}K（正常：295-305K）
        - 加工温度：{process_temp}K（正常：305-315K）
        - 转速：{rpm}RPM（正常：1300-1600RPM）
        - 扭矩：{torque}Nm（正常：20-60Nm）
        - 刀具磨损：{tool_wear}min（超200需更换）
        请给出：1.风险等级 2.异常参数分析 3.建议措施
        """
        response = client.chat.completions.create(
            model="glm-4-flash",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content

    if prob > 0.5:
        st.error(result)
    elif prob > 0.2:
        st.warning(result)
    else:
        st.success(result)