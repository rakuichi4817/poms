from urllib.parse import urljoin

import requests
import streamlit as st

from config.setting import API_ROOT_PREFIX

# ページ設定
page_title = "APIリクエストサンプル"
page_icon = "🔰"
endpoint_prefix = "sample"
st.set_page_config(page_title=page_title, page_icon=page_icon)


st.write(f"# {page_title}{page_icon}")


with st.form("get_sample_form"):
    # リクエスト先
    endpoint_url = urljoin(API_ROOT_PREFIX, f"{endpoint_prefix}/plus")
    # 表示と入力
    st.write("## 足し算（a + b）")
    st.write("Getリクエスト（クエリ付き）")
    a = st.number_input("a を入れてください")
    b = st.number_input("b を入れてください")

    # 計算リクエスト
    submitted = st.form_submit_button("計算する")
    if submitted:
        response = requests.get(endpoint_url, params={"a": a, "b": b})
        if response.status_code == 200:
            result = response.json()["result"]
            st.success(f"**{result}**")
        else:
            st.error(f"{response.status_code}エラーが発生しました。詳細は以下を参照ください")
            st.json(response.json())
