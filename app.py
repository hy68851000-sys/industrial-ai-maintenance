import streamlit as st
from zhipuai import ZhipuAI

client = ZhipuAI(api_key="a340d621d3514dfb91bb9917428806ee.Zp1oJ2QDsjhEoDWo")

st.title("🏭 工厂设备故障诊断系统")
st.write("输入设备参数，AI给出故障诊断报告")

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
    with st.spinner("AI分析中..."):
        prompt = f"""
        你是工厂设备故障诊断专家，分析以下参数：
        - 空气温度：{air_temp}K（正常：295-305K）
        - 加工温度：{process_temp}K（正常：305-315K）
        - 转速：{rpm}RPM（正常：1300-1600RPM）
        - 扭矩：{torque}Nm（正常：20-60Nm）
        - 刀具磨损：{tool_wear}min（超200需更换）
        请给出：1.风险等级 2.异常分析 3.建议措施
        """
        response = client.chat.completions.create(
            model="glm-4-flash",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content

    if "高" in result:
        st.error(result)
    elif "中" in result:
        st.warning(result)
    else:
        st.success(result)