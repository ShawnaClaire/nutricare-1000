import streamlit as st


st.set_page_config(page_title="Chatbot Assistant", page_icon=":material/smart_toy:", layout="wide")
st.title("NutriCare 1000 Chatbot Assistant")

with st.chat_message(name="assistant"):
    st.write("Halo, Ibu [Nama]! Anda berada di HPK ke-60 atau usia kehamilan ibu sudah memasuki 2 bulan dan trimester pertama. Hari ini tanggal 2 November 2024")

with st.chat_message(name="assistant"):
    st.write("Di HPK ini normal jika ibu mengalami beberapa gejala berikut: ")
    st.write("(1) Mual dan Muntah: Sering disebut sebagai morning sickness, yang umum terjadi pada trimester pertama. Mual bisa berlangsung sepanjang hari dan biasanya akan berkurang setelah trimester pertama. ")
    st.write("(2) Kelelahan dan Mudah Lelah: Tubuh bekerja keras untuk membangun plasenta, jadi rasa lelah adalah hal yang wajar.")
    st.write("(3) Perubahan Nafsu Makan dan Keinginan Makan Tertentu: Keinginan untuk makanan tertentu atau bahkan penolakan terhadap beberapa jenis makanan biasa terjadi.")

with st.chat_message(name="assistant"):
    st.write("Yuk, status kenaikan berat badan kehamilan Ibu!")
    st.write("Berapa berat badan ibu (kg) hari ini?")

with st.chat_message(name="user"):
    st.write("57 kg")

with st.chat_message(name="assistant"):
    st.write("Status kenaikan berat badan Ibu normal :) Ini menjadi tanda awal bahwa gizi ibu dan bayi sudah tercukupi, good job ibu :)")
    st.write("Status ini berdasarkan informasi berat badan dan tinggi badan Ibu sebelum hamil. Dengan berat badan (54 kg), tinggi badan (158 cm), maka sebelum hamil Ibu memiliki BMI 21,6. BMI ini masuk kedalam kategori normal. Dengan BMI Ibu yang masuk kategori normal, berdasarkan WHO, rata-rata kenaikan berat badan yang normal saat hamil ialah sebesar 0,42 kg/minggu atau (0,35-0,5 kg/minggu).") 
    st.write("Saat ini Anda mengalami kenaikan sebesar 3 kg dengan rata-rata kenaikan berat badan ibu tiap minggu sebesar 0,38 kg dan ini normal, good job ibu!")

with st.chat_message(name="assistant"):
    st.write("Sekarang, yuk, kita cek gizi makanan ibu!")
    st.write("Hari ini ibu makan apa?")
    
with st.chat_message(name="user"):
    st.write("Hari ini aku makan nasi, sayur bayam, dan telur goreng.")

with st.chat_message(name="assistant"):
    st.write("Berdasarkan makanan ibu hari ini, asupan gizi yang ibu dapatkan meliputi:")
    st.write("(1) Karbohidrat dari nasi sebagai sumber energi utama.")
    st.write("(2) Protein dari telur, yang baik untuk pertumbuhan jaringan dan otot ibu dan janin.")
    st.write("(3) Vitamin dan Mineral:Asam folat dan zat besi dari bayam, penting untuk mencegah anemia dan mendukung pertumbuhan janin. Vitamin A dan C dari bayam yang baik untuk kesehatan kulit, kekebalan tubuh, dan jaringan ibu.")
    st.write("(4) Lemak sehat dari telur, yang membantu penyerapan vitamin dan menjaga energi.")

with st.chat_message(name="assistant"):
    st.write("Makanan hari ini sudah cukup seimbang, tetapi ibu bisa mempertimbangkan untuk menambah variasi agar kebutuhan nutrisi lebih lengkap, seperti:")
    st.write("- Buah-buahan untuk menambah vitamin C, serat, dan antioksidan (misalnya, jeruk atau apel).")
    st.write("- Susu atau produk olahan susu (jika ibu tidak alergi) untuk tambahan kalsium dan vitamin D, yang baik untuk perkembangan tulang janin.")


# === ECHO CHATBOT === 
# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # React to user input
# if prompt := st.chat_input("Masukan pertanyaan Anda"):
#     # Display user message in chat message container
#     with st.chat_message("user"):
#         st.markdown(prompt)
#     # Add user message to chat history
#     st.session_state.messages.append({"role":"user", "content":prompt})

#     response = f"Echo: {prompt}"
#     # Display assistant response in chat message container
#     with st.chat_message("assistant"):
#         st.markdown(response)
#     # Add assistant response to chat history
#     st.session_state.messages.append({"role":"assistant", "content":response})
