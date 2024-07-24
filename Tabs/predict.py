import streamlit as st

from web_function import predict

def app(df, x, y):
    st.title("Halaman Prediksi Penyakit")

    col1, col2, col3 = st.columns(3)

    with col1:
        bp = st.text_input ('Input Nilai Tekanan Darah')
    with col1:
        sg = st.text_input ('Input Nilai Berat Jenis Urine')
    with col1:
        al = st.text_input ('Input Nilai Kadar Albumin dalam Urine')
    with col1:
        su	= st.text_input ('Input Nilai Kadar Gula dalam Urine')
    with col1:
        rbc	= st.text_input ('Input Nilai Sel Darah Merah dalam Urine')
    with col1: 
        pc = st.text_input ('Input Nilai Sel Nanah dalam Urine')
    with col1:
        pcc = st.text_input ('Input Nilai Kumpulan Sel Nanah dalam Urine')
    with col1:
        ba = st.text_input ('Input Nilai Bakteri dalam Urine')
    with col2:
        bgr = st.text_input ('Input Nilai Kadar Gula Darah Acak')
    with col2:
        bu = st.text_input ('Input Nilai Kadar Urea dalam Darah')
    with col2:
        sc = st.text_input ('Input Nilai Kreatinin Serum')
    with col2:
        sod	= st.text_input ('Input Nilai Kadar Natrium dalam Darah')
    with col2:
        pot	= st.text_input ('Input Nilai (Kadar Kalium dalam Darah')
    with col2:
        hemo = st.text_input ('Input Nilai Kadar Hemoglobin dalam Darah')
    with col2:
        pcv = st.text_input ('Input Nilai Volume Sel Darah Merah')
    with col2:
        wc = st.text_input ('Input Nilai Jumlah Sel Darah Putih')
    with col3:
        rc = st.text_input ('Input Nilai Jumlah Sel Darah Merah')
    with col3:
        htn	= st.text_input ('Input Nilai Hipertensi')
    with col3:
        dm = st.text_input ('Input Nilai Diabetes Melitus')
    with col3:
        cad	= st.text_input ('Input Nilai Penyakit Arteri Koroner')
    with col3:
        appet = st.text_input ('Input Nilai Nafsu Makan')
    with col3:
        pe = st.text_input ('Input Nilai Edema Pedal')
    with col3:
        ane = st.text_input ('Input Nilai Anemia')

    features = [bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc,htn,dm,cad,appet,pe,ane]

    #button prediksi
    if st.button("Prediksi"):
        prediction, score = predict(x,y,features)
        score=score
        st.info("Prediksi Sukses")

        if (prediction == 1):
            st.warning("Pasien tersebut rentan terkena penyakit batu ginjal")
        else:
            st.success("Pasien tersbut relatif aman dari penyakit batu ginjal")

        st.write("Model yang digunakan memiliki tingkat akurasi ", (score*100),"%")