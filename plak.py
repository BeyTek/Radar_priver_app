import streamlit as st
import requests
from streamlit.components.v1 import html

radar_priver = ['ex-012-bk', 'fp-836-sb', 'dm-599-bf', 'ev-765-vw', 'ez-285-bp', 'fp-940-sb', 'fw-013-xm', 'ex-163-bl', 'fw-778-yq', 'dm-252-by', 'ex-224-bl', 'dm-202-by', 'fp-866-sb', 'fp-896-sb', 'el-032-ka', 'ez-318-bp', 'dx-307-mb', 'fp-814-sb', 'dj-364-fz', 'dp-575-rg', 'fc-397-tl', 'ez-441-ca', 'fw-988-xl', 'fp-900-sb', 'fw-018-xm', 'ez-627-bp', 'fp-811-sb', 'dp-646-rg', 'fc-288-wl', 'el-304-ka', 'fp-889-sb', 'dj-658-fz', 'fp-747-sb', 'ez-994-pt', 'fp-827-sb', 'ez-942-cj', 'dx-802-ly', 'ez-505-br', 'fc-717-tl', 'fp-907-sb', 'fp-956-sb', 'ez-701-bp', 'dm-213-by', 'dx-353-mb', 'ex-474-bp', 'dx-841-ly', 'ex-311-bl', 'dy-178-zg', 'el-429-ka', 'fw-810-yq', 'dj-631-fz', 'df-098-yh', 'ez-179-br', 'dx-753-sy', 'fp-398-sb', 'dx-775-ly', 'el-440-ka', 'fp-856-sb', 'gb-283-jw', 'fp-572-sb', 'fw-800-yq', 'gb-702-jt', 'fw-779-yq', 'fc-693-wl', 'fw-757-yq', 'ez-254-bp', 'fw-989-xl', 'ex-921-bp', 'fw-835-yq', 'fp-779-sb', 'fp-933-sb', 'fp-904-sb', 'ex-755-gf', 'df-108-nh', 'ex-202-bl', 'fc-651-tl', 'df-135-sf', 'dy-126-zg', 'ex-269-bl', 'gb-837-jv', 'fp-447-sb', 'dx-358-mb', 'ex-283-bl', 'fw-053-xm', 'gb-769-jt', 'el-006-ka', 'df-171-sf', 'dx-380-mb', 'fp-741-sb', 'fw-768-yq', 'dm-633-bf', 'fp-555-sb', 'gb-008-jx', 'dp-634-rg', 'dx-231-mb', 'fp-668-sb', 'fp-588-sb', 'fc-767-wg', 'gb-656-jt', 'fp-599-sb', 'fp-912-sb', 'ez-266-jf', 'fw-845-yq', 'fp-505-sb', 'el-450-ka', 'fc-484-tl', 'gb-253-jv', 'fc-307-tl', 'fw-888-xl', 'dj-882-fy', 'ez-739-jf', 'gb-849-jt', 'ex-489-bp', 'ex-243-bk', 'ex-181-bl', 'ex-146-bk', 'fp-347-sb', 'fp-703-sb', 'ez-491-bp', 'ez-402-ca', 'gb-338-jv', 'el-419-ka', 'ew-644-ax', 'fp-894-sb', 'dx-235-mb', 'dm-661-bf', 'gb-294-jv', 'fc-894-wg', 'fc-376-tl', 'gk-639-lj', 'ez-929-pt', 'ex-901-bp', 'fw-788-yq', 'fp-643-sb', 'ez-356-br', 'fp-729-sb', 'fw-783-yq', 'dx-244-mb', 'ex-340-bl', 'ex-151-bq', 'dx-365-mb', 'fp-482-sb', 'fp-659-sb', 'ez-838-bp', 'fp-953-sb', 'ez-739-bp', 'fw-937-xl', 'ex-066-bk', 'fw-843-yq', 'fp-689-sb', 'dp-543-rm', 'dm-211-by', 'dx-343-mb', 'dx-331-mb', 'fw-834-yq', 'fp-615-sb', 'fw-996-xl', 'ex-192-bk', 'fc-783-wf', 'dx-099-mb', 'fp-803-sb', 'fz-135-le', 'ez-468-bp', 'fw-044-xm', 'ez-548-br', 'dx-226-mb', 'fp-843-sb', 'fw-920-xl', 'fw-973-xl', 'dx-888-vl', 'ex-104-bk', 'ez-897-bp', 'ez-283-br', 'ez-806-bp', 'ez-468-ca', 'ex-019-bq', 'ex-252-bl', 'fp-944-sb', 'dp-614-rm', 'fw-946-xl', 'fp-757-sb', 'fc-473-wg', 'ez-322-br', 'ez-441-br', 'ez-043-ck', 'fw-906-xl', 'dx-318-mb', 'fp-431-sb', 'ev-372-vw', 'fw-999-xl', 'fw-031-xm', 'dx-769-sy', 'ex-324-bl', 'dj-560-fz', 'fw-848-yq', 'ex-300-bl', 'fp-463-sb', 'dj-550-fz', 'fc-256-tl', 'dj-534-fz', 'dj-641-fz', 'df-108-nh', 'df-237-nh', 'dj-616-fz', 'df-146-nh', 'df-171-sf', 'df-098-yh', 'df-213-nh', 'df-169-yh', 'dj-395-fz', 'dj-074-fz', 'dj-658-fz', 'df-168-sf', 'dj-560-fz', 'df-135-sf', 'df-159-sf', 'dj-631-fz', 'dj-882-fy', 'dj-534-fz', 'dj-364-fz', 'dj-568-fz', 'dj-550-fz', 'dm-627-bf', 'dp-559-sc', 'dp-590-sc', 'dm-168-by', 'dm-311-by', 'dp-620-sc', 'eh-501-ka', 'dp-539-sc', 'el-055-ka', 'el-979-jz', 'el-012-ka', 'eh-657-ka', 'eh-527-ka', 'el-045-ka', 'fw-867-xl', 'fw-772-yq', 'fw-049-xm', 'fw-794-yq', 'fw-039-xm', 'fw-770-yq', 'fw-781-yq', 'fw-817-yq', 'fw-793-yq', 'fw-762-yq', 'fw-830-yq', 'fw-839-yq', 'dx-154-mb', 'dx-669-vl', 'dx-159-mb', 'dx-152-mb', 'dx-223-mb', 'dx-164-mb', 'dx-786-sy', 'dx-112-mb', 'el-317-ka', 'dx-894-ly', 'dx-646-vl', 'dx-239-mb', 'el-457-ka', 'el-436-ka', 'ex-991-bp', 'ex-040-bk', 'ex-215-bk', 'ex-045-bq', 'ex-072-bq', 'ex-100-bq', 'ex-462-bp', 'ex-938-bp', 'ex-958-bp', 'ex-974-bp', 'ex-243-bl', 'ew-308-av', 'ew-320-ax', 'ga-242-gl', 'ez-390-bp', 'ez-876-bp', 'ez-352-jf', 'ez-521-bp', 'ez-006-ck', 'ez-777-bp', 'ez-587-bp', 'ez-253-br', 'ez-979-cj', 'gb-934-jt', 'gb-209-jv', 'gb-523-jw', 'fp-719-sb', 'fp-946-sb', 'fp-883-sb', 'fp-419-sb', 'fp-949-sb', 'fp-714-sb', 'fp-929-sb', 'fp-830-sb', 'fp-634-sb', 'fp-853-sb', 'fp-821-sb', 'fp-858-sb', 'fp-880-sb', 'fp-495-sb', 'fp-918-sb', 'fp-626-sb', 'fp-365-sb', 'fc-981-wg', 'fc-808-wl', 'fc-210-tl', 'fc-326-wl', 'fc-227-xc', 'ez-412-jf', 'dp-377-bn', 'eh-567-ka', 'ez-387-br', 'el-022-ka', 'fp-873-sb', 'el-992-jz', 'eh-620-ka', 'eh-638-ka', 'ex-012-bk', 'fp-836-sb', 'dm-599-bf', 'ev-765-vw', 'fp-814-sb', 'fw-013-xm', 'ex-163-bl', 'dm-252-by', 'fw-778-yq', 'ex-224-bl', 'dm-202-by', 'fp-866-sb', 'fp-896-sb', 'el-032-ka', 'ez-318-bp', 'dx-307-mb', 'dj-364-fz', 'dp-575-rg', 'fp-904-sb', 'fc-397-tl', 'ez-441-ca', 'fw-988-xl', 'fp-907-sb', 'fw-018-xm', 'ez-627-bp', 'fp-811-sb', 'el-304-ka', 'fp-889-sb', 'gb-934-jt', 'dj-658-fz', 'fp-747-sb', 'fp-419-sb', 'ez-994-pt', 'fp-827-sb', 'ez-942-cj', 'dx-802-ly', 'ez-505-br', 'fc-717-tl', 'fp-956-sb', 'ez-701-bp', 'gb-253-jv', 'ex-474-bp', 'dx-841-ly', 'ex-311-bl', 'dy-178-zg', 'el-429-ka', 'ez-254-bp', 'dj-631-fz', 'df-098-yh', 'ez-179-br', 'dx-753-sy', 'fw-800-yq', 'fp-398-sb', 'dx-775-ly', 'el-440-ka', 'fp-856-sb', 'gb-283-jw', 'fp-572-sb', 'ez-285-bp', 'gb-702-jt', 'fw-779-yq', 'fc-693-wl', 'fw-757-yq', 'fw-989-xl', 'ex-921-bp', 'fw-835-yq', 'fp-779-sb', 'fp-933-sb', 'ex-755-gf', 'df-108-nh', 'ex-202-bl', 'gb-837-jv', 'fp-555-sb', 'fc-651-tl', 'df-135-sf', 'dy-126-zg', 'ex-269-bl', 'fp-447-sb', 'ex-283-bl', 'dx-358-mb', 'fw-053-xm', 'gb-769-jt', 'el-006-ka', 'df-171-sf', 'dm-633-bf', 'fp-741-sb', 'fw-768-yq', 'gb-008-jx', 'dp-634-rg', 'dx-231-mb', 'fp-668-sb', 'fp-588-sb', 'fc-767-wg', 'gb-656-jt', 'fp-599-sb', 'fp-912-sb', 'ez-266-jf', 'fw-845-yq', 'fp-505-sb', 'el-450-ka', 'fc-484-tl', 'fc-307-tl', 'fw-888-xl', 'ez-739-jf', 'dj-882-fy', 'gb-849-jt', 'ex-489-bp', 'ex-243-bk', 'ex-146-bk', 'fp-347-sb', 'fp-703-sb', 'ez-491-bp', 'ez-402-ca', 'gb-338-jv', 'el-419-ka', 'ex-181-bl', 'ew-644-ax', 'fp-894-sb', 'dx-235-mb', 'dm-661-bf', 'fc-894-wg', 'fc-376-tl', 'fw-794-yq', 'gk-639-lj', 'ez-929-pt', 'ex-901-bp', 'fw-788-yq', 'fp-643-sb', 'el-045-ka', 'ez-356-br', 'fp-729-sb', 'fw-783-yq', 'dx-244-mb', 'ex-340-bl', 'ex-151-bq', 'dx-365-mb', 'fp-482-sb', 'fp-659-sb', 'ez-838-bp', 'gb-294-jv', 'ez-739-bp', 'fp-953-sb', 'fw-937-xl', 'ex-066-bk', 'fw-843-yq', 'fp-689-sb', 'dp-543-rm', 'dm-211-by', 'dx-343-mb', 'dx-331-mb', 'dx-099-mb', 'fw-834-yq', 'fp-615-sb', 'fw-996-xl', 'ex-192-bk', 'fc-783-wf', 'fp-803-sb', 'fw-044-xm', 'fz-135-le', 'ez-468-bp', 'ez-548-br', 'dx-226-mb', 'fp-843-sb', 'fw-920-xl', 'fw-973-xl', 'dx-888-vl', 'ex-104-bk', 'ez-897-bp', 'ez-283-br', 'ez-806-bp', 'ez-468-ca', 'fp-944-sb', 'ex-019-bq', 'ex-252-bl', 'dp-614-rm', 'fw-946-xl', 'fp-757-sb', 'dm-168-by', 'fc-473-wg', 'ez-322-br', 'ez-441-br', 'ez-043-ck', 'fw-906-xl', 'dx-318-mb', 'fp-431-sb', 'ev-372-vw', 'dx-769-sy', 'fw-999-xl', 'fw-031-xm', 'ex-324-bl', 'dj-560-fz', 'fw-848-yq', 'ex-300-bl', 'fp-463-sb', 'dj-550-fz', 'fc-256-tl', 'dj-534-fz', 'dj-641-fz', 'df-108-nh', 'df-237-nh', 'dj-616-fz', 'df-146-nh', 'df-171-sf', 'df-098-yh', 'df-213-nh', 'df-169-yh', 'dj-395-fz', 'dj-074-fz', 'dj-658-fz', 'df-168-sf', 'dj-560-fz', 'df-135-sf', 'df-159-sf', 'dj-631-fz', 'dj-882-fy', 'dj-534-fz', 'dj-364-fz', 'dj-568-fz', 'dj-550-fz', 'dm-627-bf', 'dp-559-sc', 'dp-590-sc', 'dp-646-rg', 'dm-311-by', 'dm-213-by', 'dp-620-sc', 'eh-501-ka', 'dp-539-sc', 'el-055-ka', 'el-979-jz', 'el-012-ka', 'eh-657-ka', 'eh-527-ka', 'fw-867-xl', 'fw-772-yq', 'fw-810-yq', 'fw-049-xm', 'fw-039-xm', 'fw-770-yq', 'fw-781-yq', 'fw-817-yq', 'fw-793-yq', 'fw-762-yq', 'fw-830-yq', 'fw-839-yq', 'dx-154-mb', 'dx-669-vl', 'dx-159-mb', 'dx-152-mb', 'dx-223-mb', 'dx-164-mb', 'dx-786-sy', 'dx-112-mb', 'el-317-ka', 'dx-894-ly', 'dx-646-vl', 'dx-380-mb', 'dx-239-mb', 'dx-353-mb', 'el-457-ka', 'el-436-ka', 'ex-991-bp', 'ex-040-bk', 'ex-215-bk', 'ex-045-bq', 'ex-072-bq', 'ex-100-bq', 'ex-462-bp', 'ex-938-bp', 'ex-958-bp', 'ex-974-bp', 'ex-243-bl', 'ew-308-av', 'ew-320-ax', 'ga-242-gl', 'ez-390-bp', 'ez-876-bp', 'ez-352-jf', 'ez-521-bp', 'ez-006-ck', 'ez-777-bp', 'ez-587-bp', 'ez-253-br', 'ez-979-cj', 'gb-209-jv', 'gb-523-jw', 'fp-719-sb', 'fp-946-sb', 'fp-940-sb', 'fp-883-sb', 'fp-949-sb', 'fp-714-sb', 'fp-929-sb', 'fp-830-sb', 'fp-634-sb', 'fp-853-sb', 'fp-900-sb', 'fp-821-sb', 'fp-858-sb', 'fp-880-sb', 'fp-495-sb', 'fp-918-sb', 'fp-626-sb', 'fp-365-sb', 'fc-288-wl', 'fc-981-wg', 'fc-808-wl', 'fc-210-tl', 'fc-326-wl', 'fc-227-xc', 'ez-412-jf', 'dp-377-bn', 'eh-567-ka', 'ez-387-br', 'el-022-ka', 'fp-873-sb', 'el-992-jz', 'eh-620-ka', 'eh-638-ka']



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
        if message in radar_priver:
            return f"Voiture Radar Confirmée!!!\n{car_info}"
        else:
            return f"Cette voiture ne semble pas être un radar\n{car_info}"
    if not car_info:
        return f"Désolé, nous ne parvenons pas à trouver les informations de cette plaque d'immatriculation."

def main():
    st.title("Correspondance de plaques d'immatriculation avec notre liste de radars privés")
    user_input = st.text_input("Entrez une plaque d'immatriculation :")
    button_rech = st.button("Rechercher")
    
    if button_rech:
        response = get_response(user_input.lower())
        st.write(response)
    
    if st.button("Telecharger pour android"):
        # Lien URL
        url1 = "https://urlz.fr/ndDy"
        # Ouvrir le lien dans une nouvelle fenêtre du navigateur
        st.markdown(f"[Télécharger pour Android]({url1})", unsafe_allow_html=True)
    
    if st.button("Propulsé par BeyTek"):
        # Lien URL
        url = "https://beytek.fr"
        # Ouvrir le lien dans une nouvelle fenêtre du navigateur
        st.markdown(f"[Propulsé par BeyTek]({url})", unsafe_allow_html=True)
    
    st.title(f"Nombre total de plaques dans la base de données : {len(radar_priver)}")

if __name__ == '__main__':
    main()






