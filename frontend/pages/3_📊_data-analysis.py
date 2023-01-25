import json
from datetime import datetime
from urllib.parse import urljoin

import requests
import streamlit as st
from config.setting import API_ROOT_PREFIX

# ページ設定
page_title = "データ分析関係"
page_icon = "📊"
endpoint_prefix = "dataanalysis"
st.set_page_config(page_title=page_title, page_icon=page_icon)


st.write(f"# {page_title}{page_icon}")


with st.container():
    # リクエスト先
    endpoint_url = urljoin(API_ROOT_PREFIX, f"{endpoint_prefix}/generate-table")

    # リクエスト用パラメータ
    param_name = "column_name"
    param_type = "column_type"
    param_min = "min_val"
    param_max = "max_val"
    types = ["int", "float"]

    # セッションに情報リストを持たせる
    if "columns" not in st.session_state:
        st.session_state.columns = []

    st.write("## テーブルデータ生成🧑‍🍳")

    # 入力フォーマット
    record_cnt = st.number_input("〇生成するレコード数を入力してください", min_value=5, max_value=10000, step=1)

    st.write("〇追加する項目情報")
    col1, col2, col3, col4 = st.columns(4)

    add_column = {}
    with col1:
        # 項目名
        add_column[param_name] = st.text_input("項目名", f"項目{len(st.session_state.columns)}")
    with col2:
        # 型
        add_column[param_type] = st.selectbox("int or float", types, index=0)
    with col3:
        # 最小値
        add_column[param_min] = st.number_input("最小値", value=0.0)
    with col4:
        # 最大値
        add_column[param_max] = st.number_input("最大値", value=100.0)

    col1, col2 = st.columns((1, 4))
    with col1:
        if st.button("項目追加"):
            st.session_state.columns.append(add_column)
    with col2:
        if st.session_state.columns:
            if st.button("項目削除"):
                del st.session_state.columns[-1]

    # ファイルを生成する
    col1, col2 = st.columns((1, 4))
    with col1:
        submitted = st.button("生成する")
        if submitted:
            with st.spinner("Wait for it..."):
                response = requests.post(
                    endpoint_url, data=json.dumps({"columns": st.session_state.columns, "record_cnt": record_cnt})
                )
                if response.status_code == 200:
                    with col2:
                        st.download_button(
                            "csvダウンロード",
                            response.content,
                            file_name=f"{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.csv",
                        )
                else:
                    with col2:
                        st.error("データ生成に失敗しました")

    st.write("〇作成する項目")
    st.table(st.session_state.columns)
