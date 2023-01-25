from urllib.parse import urljoin

import requests
import streamlit as st

from config.setting import API_ROOT_PREFIX

# ページ設定
page_title = "画像関連処理"
page_icon = "📷"
endpoint_prefix = "images"
st.set_page_config(page_title=page_title, page_icon=page_icon)


st.write(f"# {page_title}{page_icon}")


with st.container():
    # リクエスト先
    endpoint_url = urljoin(API_ROOT_PREFIX, f"{endpoint_prefix}/mosaic")

    # 表示と入力
    st.write("## 顔モザイク処理👻")
    st.write("Postリクエスト（画像ファイルの扱い）")

    uploaded_file = st.file_uploader("モザイクを入れる画像を選択")
    col1, col2 = st.columns(2)
    with col1:
        if uploaded_file:
            bytes_data = uploaded_file.getvalue()
            st.image(bytes_data)
            submitted = st.button("モザイク処理")
            with col2:
                if submitted:
                    with st.spinner("Wait for it..."):
                        response = requests.post(endpoint_url, files={"file": bytes_data})
                        if response.status_code == 200:
                            st.image(response.content)
                        else:
                            st.error("モザイク処理に失敗しました")
    if uploaded_file is None:
        st.info("画像を選択してください")
