import tkinter as tk
from tkinter import messagebox
import Assistant_Logic as al
import Prediction_Logic as pl


class MedicalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Medical Assistant (No-PyAudio)")
        self.root.geometry("450x550")

        tk.Label(root, text="Medical Assistant", font=("Arial", 18, "bold")).pack(pady=10)

        self.input_box = tk.Entry(root, font=("Arial", 14), width=30)
        self.input_box.pack(pady=10)

        self.btn_voice = tk.Button(root, text="🎤 Speak (5 sec)", command=self.voice_input, bg="#3498db", fg="white")
        self.btn_voice.pack(pady=5)

        self.btn_predict = tk.Button(root, text="Predict", command=self.text_predict, bg="#2ecc71", fg="white")
        self.btn_predict.pack(pady=5)

        self.result_text = tk.Label(root, text="", font=("Arial", 11), justify="left")
        self.result_text.pack(pady=20)

    def voice_input(self):
        text = al.get_voice()
        if text:
            self.input_box.delete(0, tk.END)
            self.input_box.insert(0, text)
            self.text_predict()
        else:
            messagebox.showinfo("Info", "Could not capture voice. Try typing.")

    def text_predict(self):
        val = self.input_box.get()
        if not val: return

        disease, conf = pl.predict_disease([val])
        info = al.get_disease_info(disease)

        self.result_text.config(text=f"Disease: {disease} ({conf:.1f}%)\n\n"
                                     f"Precaution: {info['precaution']}\n"
                                     f"Specialist: {info['specialist']}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MedicalApp(root)
    root.mainloop()