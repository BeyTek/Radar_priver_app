import streamlit as st
import requests
from streamlit.components.v1 import html
import json
st.set_page_config(
    page_title="Radar privé",
    page_icon="📷",
)
def load_plates_from_json(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        return data

radar_priver = load_plates_from_json("plaque.json")


def get_car_info(plate):
    try:
        response = requests.get(f'https://www.yakarouler.com/car_search/immat?immat={plate}&name=undefined&redirect=true')
        data = response.text
        finder_start = data.find('<h2 class="title-car">')
        car = data[finder_start+22:data.find('</h2>')]
        model = car[:car.find('(')]
        tab = car.split()
        for spec in tab:
            if '(' in spec and 'kw' not in spec:
                gen = spec
            elif '.' in spec:
                size = spec
            elif 'cv' in spec or 'CV' in spec:
                hp = spec
        return f"C'est un(e) {model} de {hp}"
    except:
        return ''

def get_response(message):
    car_info = get_car_info(message)
    if car_info:
        if message.lower() in radar_priver:
            return f"Voiture Radar Confirmée!!!\n{car_info}"
        else:
            return f"Cette voiture ne semble pas être un radar\n{car_info}"
    if not car_info:
        return f"Désolé, nous ne parvenons pas à trouver les informations de cette plaque d'immatriculation."

def main():
    st.title("Correspondance de plaques d'immatriculation avec notre liste de radars privés")
    user_input = st.text_input("Entrez une plaque d'immatriculation :")
    user_input = user_input.replace("-", "").lower()  # Suppression des tirets et conversion en minuscules
    button_rech = st.button("Rechercher")
    st.text("Format✅: az-123-jl ")
    st.text("Format🚫: AZ-123-JL & az123jl")
    if button_rech:
        response = get_response(user_input.lower())
        st.write(response)
    

    

    
    st.title(f"Nombre total de plaques dans la base de données : {len(radar_priver)}")

    st.markdown("---")
    st.title("Credits")
    st.write("Made by [BeyTek](https://www.beytek.fr)")
    st.write("[CBD&+](https://purplebey.fr/boutique)")
    st.write("[Verison Android](https://urlz.fr/ndDy)")
if __name__ == '__main__':
    main()






