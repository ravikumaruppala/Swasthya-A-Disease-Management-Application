import tkinter as tk
from tkinter import messagebox, ttk

# Disease data
fever = {
    "NAME": "FEVER",
    "Symptoms": ["Cough", "Sweating", "Headache", "Chills and Shivering", "Dehydration", "General Weakness"],
    "Prevention": "Wash your hands often\nAvoid touching your nose or mouth",
    "Home remedies": "Drink plenty of fluids and take adequate rest"
}

diarrhea = {
    "NAME": "DIARRHEA",
    "Symptoms": ["Belly cramps or pain", "Nausea", "Vomiting", "Fever", "Blood in the stool", "Mucus in the stool"],
    "Prevention": "Access to safe drinking water\nUse of improved sanitation\nHand washing with soap\nRotavirus vaccination",
    "Home remedies": "Drink plenty of water, avoid fatty foods, and try probiotics"
}

lung = {
    "NAME": "LUNG CANCER",
    "Symptoms": ["Breathlessness", "Sputum Production", "Chronic Cough"],
    "Prevention": "Stop smoking\nAvoid Secondhand smoke\nTest for radon\nAvoid Asbestos",
    "Home remedies": "Quit smoking\nImprove air quality\nManage stress levels\nDevelop muscle strength"
}

# Disease mapping
diseases = [fever, diarrhea, lung]
categories = {"General": [fever], "Digestive": [diarrhea], "Respiratory": [lung]}

# ---------------- GUI ---------------- #
root = tk.Tk()
root.title("SWASTHYA - Health Diagnosis")
root.geometry("700x600")
root.configure(bg="#f0f8ff")

title = tk.Label(root, text="\u2695 SWASTHYA - Health Self Diagnosis", 
                 font=("Arial", 18, "bold"), bg="#4682b4", fg="white", pady=10)
title.pack(fill="x")

# Frame for category
frame_category = tk.LabelFrame(root, text="Select Disease Category", font=("Arial", 12, "bold"), bg="#f0f8ff", padx=10, pady=10)
frame_category.pack(fill="x", padx=20, pady=10)

# Frame for symptoms
frame_symptoms = tk.LabelFrame(root, text="Select Symptoms", font=("Arial", 12, "bold"), bg="#f0f8ff", padx=10, pady=10)
frame_symptoms.pack(fill="both", expand=True, padx=20, pady=10)

# Frame for results
frame_result = tk.LabelFrame(root, text="Diagnosis Result", font=("Arial", 12, "bold"), bg="#f0f8ff", padx=10, pady=10)
frame_result.pack(fill="both", expand=True, padx=20, pady=10)

# Category dropdown
category_var = tk.StringVar(value="General")
category_menu = ttk.Combobox(frame_category, textvariable=category_var, values=list(categories.keys()), state="readonly", font=("Arial", 11))
category_menu.pack(pady=5)

symptom_vars = []
checkboxes = []

def load_symptoms(*args):
    for cb in checkboxes:
        cb.destroy()
    symptom_vars.clear()
    checkboxes.clear()

    selected_category = category_var.get()
    selected_diseases = categories[selected_category]

    all_symptoms = set()
    for d in selected_diseases:
        all_symptoms.update(d["Symptoms"])

    for i, symptom in enumerate(sorted(all_symptoms)):
        var = tk.IntVar()
        cb = tk.Checkbutton(frame_symptoms, text=symptom, variable=var, bg="#f0f8ff", anchor="w", font=("Arial", 10))
        cb.pack(fill="x", pady=2)
        symptom_vars.append((symptom, var))
        checkboxes.append(cb)

category_menu.bind("<<ComboboxSelected>>", load_symptoms)
load_symptoms()

# Display function
def display():
    selected_symptoms = [s for s, var in symptom_vars if var.get() == 1]
    if not selected_symptoms:
        messagebox.showwarning("No Symptoms", "Please select at least one symptom.")
        return

    count2 = [0, 0, 0]
    matched_diseases = set()
    prevention = set()
    homer = set()

    for s in selected_symptoms:
        for j, d in enumerate(diseases):
            if s in d["Symptoms"]:
                matched_diseases.add(d["NAME"])
                prevention.add(d["Prevention"])
                homer.add(d["Home remedies"])
                count2[j] += 1

    for widget in frame_result.winfo_children():
        widget.destroy()

    if max(count2) == 0:
        tk.Label(frame_result, text="⚠ No disease matched with selected symptoms.", font=("Arial", 12), bg="#f0f8ff", fg="red").pack()
        return

    inde = count2.index(max(count2))
    probable = diseases[inde]

    # Show main disease
    tk.Label(frame_result, text=f"\u2705 Most Probable Disease: {probable['NAME']}", font=("Arial", 14, "bold"), fg="darkgreen", bg="#f0f8ff").pack(pady=5)

    tk.Label(frame_result, text="\u26E8 Preventions:", font=("Arial", 12, "bold"), bg="#f0f8ff").pack(anchor="w")
    tk.Label(frame_result, text=probable["Prevention"], font=("Arial", 11), bg="#f0f8ff", wraplength=600, justify="left").pack(anchor="w", padx=20)

    tk.Label(frame_result, text="\u2302 Home Remedies:", font=("Arial", 12, "bold"), bg="#f0f8ff").pack(anchor="w", pady=(10,0))
    tk.Label(frame_result, text=probable["Home remedies"], font=("Arial", 11), bg="#f0f8ff", wraplength=600, justify="left").pack(anchor="w", padx=20)

    # Other possibilities
    other = matched_diseases - {probable["NAME"]}
    if other:
        tk.Label(frame_result, text=f"\u2753 Other Possibilities: {', '.join(other)}", font=("Arial", 11, "italic"), fg="blue", bg="#f0f8ff").pack(pady=10)

# Diagnose button (replaced 🔍 with ▶ to avoid Tcl error)
diagnose_btn = tk.Button(root, text="\u25B6 Diagnose", command=display, font=("Arial", 12, "bold"), 
                         bg="#32cd32", fg="white", relief="raised", padx=15, pady=5)
diagnose_btn.pack(pady=10)

root.mainloop()
