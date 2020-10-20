from imageai.Prediction.Custom import CustomImagePrediction
import tkinter as tk
import webbrowser
from tkinter import filedialog

def analisisFunction(file_path):
    n = 0
    prediction = CustomImagePrediction()
    prediction.setModelTypeAsResNet()
    prediction.setModelPath("assets/models/model_061-0.7933.h5")
    prediction.setJsonPath("assets/json/model_class.json")
    prediction.loadModel(num_objects=10)

    predictions, probabilities = prediction.predictImage(file_path, result_count=3)
    encabezado = "RESULTADOS:", file_path
    Lb1.insert(n, encabezado)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        n += 1
        pro = round(float(eachProbability),2)
        line = eachPrediction, pro , " %"
        print(line)
        Lb1.insert(n, line)

    Lb1.insert(n+1, " ")

def mainFunction():
    root = tk.Tk()
    root.withdraw()

    try:
        file_path = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = [("Supported Files", "*.jpg *.jpeg *.png")])
        if file_path:
            analisisFunction(file_path)
    except:
        Lb1.insert(0, "Archivo no válido")

def openLink():
    webbrowser.open('https://github.com/DianelRavilla/6TO-SIS-EMI-IA-GRUPO1-PROYECTO', new=2)

top = tk.Tk()
top.geometry('500x600+0+0')
top.title("RI - TERMINAL")
Lb1 = tk.Listbox(top,height=22, width=50, font=("Consolas",13))
tk.Button(top, text="OPEN IMAGE", command=mainFunction).pack()
label1 = tk.Label(top,text="RECONOCIMIENTO DE IMÁGENES EDICIÓN : PROFESIONES", fg="gray", font=("Arial Narrow",13))
label1.place(x=20,y=500)
label2 = tk.Label(top,text="Encuentra el código en:", fg="gray", font=("Arial Narrow",13))
label2.place(x=20,y=520)
label3 = tk.Button(top,text="GITHUB", fg="gray", font=("Arial",15), command=openLink)
label3.place(x=20,y=540)

Lb1.pack()
top.mainloop()

