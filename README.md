# Projektin Nimi

## Asennusohjeet

1. **Luo virtuaaliympäristö** (valinnainen mutta suositeltava):

    ```sh
    python -m venv myenv
    ```

2. **Aktivoi virtuaaliympäristö**:

    Windows:
    ```sh
    myenv\Scripts\activate
    ```

    macOS/Linux:
    ```sh
    source myenv/bin/activate
    ```

3. **Asenna tarvittavat paketit**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Asenna `google-generativeai`-kirjasto** (jos ei ole jo [requirements.txt](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5Cdev-tests%5C%5Cgemini%5C%5Crequirements.txt%22%2C%22_sep%22%3A1%2C%22path%22%3A%22%2FC%3A%2Fdev-tests%2Fgemini%2Frequirements.txt%22%2C%22scheme%22%3A%22file%22%7D%7D)-tiedostossa):

    ```sh
    pip install google-generativeai
    ```

5. **Asenna `Pillow`-kirjasto** (jos ei ole jo [requirements.txt](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5Cdev-tests%5C%5Cgemini%5C%5Crequirements.txt%22%2C%22_sep%22%3A1%2C%22path%22%3A%22%2FC%3A%2Fdev-tests%2Fgemini%2Frequirements.txt%22%2C%22scheme%22%3A%22file%22%7D%7D)-tiedostossa):

    ```sh
    pip install pillow
    ```

Nyt ympäristösi on valmis käytettäväksi!