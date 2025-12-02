# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa

import os
import pandas as pd

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

def generate_csv(ruta, target):
    texts = []
    for file_name in os.listdir(ruta):
            file_path = os.path.join(ruta, file_name)
            
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                texts.append(content)
            
    df = pd.DataFrame([[text, target] for text in texts], columns=["phrase", "target"])
    return df


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/u
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```

    """

    
    targets = ["negative", "neutral", "positive"]
    csvs_train = []

 
    for target in targets:
        csvs_train.append(generate_csv("./files/input/train/"+target, target))

    train_csv = pd.concat(csvs_train, ignore_index=True)

    csvs_test = []
    for target in targets:
        csvs_test.append(generate_csv("./files/input/test/"+target, target))

    test_csv = pd.concat(csvs_test, ignore_index=True)

    save_rute = "./files/output"
    filename_train = "train_dataset.csv"
    filename_test = "test_dataset.csv"

    os.makedirs(save_rute, exist_ok=True)

    train_csv.to_csv(os.path.join(save_rute, filename_train), index=False, encoding="utf-8")
    test_csv.to_csv(os.path.join(save_rute, filename_test), index=False, encoding="utf-8")

    print(f"Archivos guardados en: {save_rute}")

   
         


pregunta_01()