import streamlit as st

def main():
    st.title("Sustaining Customer Loyalty: E-commerce Churn Prediction Models")

    # Menampilkan informasi tentang proyek
    st.header("About Project")
    st.write("Menjaga Pelanggan Setia: Model Peramalan Churn E-commerce")

    # Menampilkan informasi anggota tim
    st.header("Team Members")
    st.write("1. Joshua Namora Sende Hasibuan")
    st.write("2. Fadli Alamsyah")
    st.write("3. Zirly Khodijah Jamil")
    st.write("Mohammad Adam Fahri")

    # Menampilkan tombol untuk menjalankan Streamlit app
    st.header("Run Streamlit App")
    st.write("Klik tombol di bawah untuk menjalankan Streamlit app.")
    
    # Menjalankan Streamlit app ketika tombol ditekan
    if st.button("Run Streamlit App"):
        st.success("Streamlit App is running!")
        run_streamlit_app()

def run_streamlit_app():
    # Menjalankan streamlit app dengan perintah terminal
    import subprocess
    subprocess.run(["streamlit", "run", "dash.py"])

if __name__ == "__main__":
    main()
