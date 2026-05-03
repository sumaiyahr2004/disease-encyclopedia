from flask import Flask, render_template, request
app = Flask(__name__)

# Created by: Sumaiyah Rahman

items = [
    {
        "id": 1,
        "title": "Type 2 Diabetes",
        "media_link": "https://youtu.be/JAjZv41iUJU?si=HtIMjKpTg8-Ysa-H",
        "description": """Type 2 diabetes is a chronic metabolic condition 
that affects how the body processes blood sugar. It occurs when the body 
becomes resistant to insulin or does not produce enough insulin. The 
condition is strongly associated with lifestyle factors such as diet and 
physical activity. If untreated, it can lead to complications including 
heart disease, kidney failure, and nerve damage.""",
        "year_identified": 1936,
        "prevalence_millions": 422,
        "symptoms": ["Increased thirst", "Frequent urination", "Fatigue", 
"Blurred vision"],
        "treatments": ["Lifestyle changes", "Metformin", "Insulin therapy"]
    },
    {
        "id": 2,
        "title": "Hypertension",
        "media_link": "https://youtu.be/Qm5kB5X70oA?si=y3CK4LKeGBG2LCeG",
        "description":"""Hypertension, also known as high blood pressure, 
is a common cardiovascular disorder. It occurs when the force of blood 
against artery walls remains consistently elevated. Over time, 
uncontrolled hypertension damages blood vessels and vital organs. It 
significantly increases the risk of stroke, heart attack, and kidney 
disease.""",
        "year_identified": 1896,
        "prevalence_millions": 1280,
        "symptoms": ["Headaches", "Shortness of breath", "Dizziness"],
        "treatments": ["ACE inhibitors", "Beta blockers", "Reduced sodium diet"]
    },
    {
        "id": 3,
        "title": "Asthma",
        "media_link": "https://youtu.be/PzfLDi-sL3w?si=gwfcw-hG9k5oPd3w",
        "description": """Asthma is a chronic respiratory condition 
characterized by airway inflammation. It leads to episodes of wheezing, 
coughing, and shortness of breath. Triggers may include allergens, 
exercise, and respiratory infections. Proper treatment allows most 
individuals to manage symptoms effectively.""",
        "year_identified": 400,
        "prevalence_millions": 262,
        "symptoms": ["Wheezing", "Chest tightness", "Coughing"],
        "treatments": ["Inhaled corticosteroids", "Bronchodilators"]
    },
    {
        "id": 4,
        "title": "Coronary Artery Disease",
        "media_link": "https://youtu.be/EATkbpqlxvc?si=qBKTap-J_wTOt-cy",
        "description": """Coronary artery disease occurs when the coronary 
arteries become narrowed or blocked. This reduces blood flow to the heart 
muscle. It is often caused by plaque buildup over many years. The 
condition can lead to chest pain and heart attacks.""",
        "year_identified": 1772,
        "prevalence_millions": 244,
        "symptoms": ["Chest pain", "Shortness of breath", "Fatigue"],
        "treatments": ["Statins", "Lifestyle changes", "Bypass surgery"]
    },
    {
        "id": 5,
        "title": "Breast Cancer",
        "media_link": "https://youtu.be/EATkbpqlxvc?si=qBKTap-J_wTOt-cy",
        "description": """Breast cancer is a disease in which malignant 
cells form in breast tissue. It is one of the most common cancers 
worldwide. Early detection through screening significantly improves 
survival rates. Treatment options vary depending on stage and tumor 
characteristics.""",
        "year_identified": 1894,
        "prevalence_millions": 2.3,
        "symptoms": ["Breast lump", "Skin changes", "Nipple discharge"],
        "treatments": ["Surgery", "Chemotherapy", "Radiation therapy"]
    },
    {
        "id": 6,
        "title": "Alzheimer's Disease",
        "media_link": "https://youtu.be/wfLP8fFrOp0?si=M6Ct-y0p0b37AMW7",
        "description": """Alzheimer's disease is a progressive 
neurological 
disorder that affects memory and cognition. It is the most common cause of 
dementia in older adults. The disease gradually impairs daily functioning. 
There is currently no cure, but treatments may slow progression.""",
        "year_identified": 1906,
        "prevalence_millions": 55,
        "symptoms": ["Memory loss", "Confusion", "Difficulty speaking"],
        "treatments": ["Cholinesterase inhibitors", "Supportive care"]
    },
    {
        "id": 7,
        "title": "Influenza",
        "media_link": "https://youtu.be/N88Dzu5k8Pc?si=68QbFvol0GMuhzdf",
        "description": """Influenza is a contagious viral infection that 
affects the respiratory system. It spreads easily through droplets from 
coughing or sneezing. Symptoms typically appear suddenly and may be 
severe. Annual vaccination is the best prevention strategy.""",
        "year_identified": 1933,
        "prevalence_millions": 1000,
        "symptoms": ["Fever", "Body aches", "Cough"],
        "treatments": ["Antiviral medications", "Rest", "Fluids"]
    },
    {
        "id": 8,
        "title": "COVID-19",
        "media_link": "https://youtu.be/BtN-goy9VOY?si=7rJhm5lK6jpQYY--",
        "description": """COVID-19 is an infectious disease caused by the 
SARS-CoV-2 virus. It was first identified in 2019 and rapidly became a 
global pandemic. Symptoms range from mild respiratory illness to severe 
complications. Vaccination and public health measures have reduced severe 
outcomes.""",
        "year_identified": 2019,
        "prevalence_millions": 760,
        "symptoms": ["Fever", "Cough", "Loss of taste or smell"],
        "treatments": ["Antiviral drugs", "Oxygen therapy", "Vaccination"]
    },
    {
        "id": 9,
        "title": "Rheumatoid Arthritis",
        "media_link": "https://youtu.be/Yc-9dfem3lM?si=TLvnTBSanpQ4SVeC",
        "description": """Rheumatoid arthritis is an autoimmune disorder 
that primarily affects joints. It causes inflammation, pain, and swelling. 
Over time, joint damage may occur. Early treatment can significantly 
improve long-term outcomes.""",
        "year_identified": 1800,
        "prevalence_millions": 18,
        "symptoms": ["Joint pain", "Swelling", "Morning stiffness"],
        "treatments": ["DMARDs", "Biologic therapy", "Physical therapy"]
    },
    {
        "id": 10,
        "title": "Chronic Kidney Disease",
        "media_link": "https://youtu.be/Ywe5jjiJJJo?si=JtfJ_aY0NzXqoBON",
        "description": """Chronic kidney disease is a long-term condition 
in 
which the kidneys gradually lose function. It often develops as a 
complication of diabetes or hypertension. Early stages may have few 
symptoms. Severe cases may require dialysis or kidney transplantation.""",
        "year_identified": 1827,
        "prevalence_millions": 850,
        "symptoms": ["Fatigue", "Swelling", "Nausea"],
        "treatments": ["Blood pressure control", "Dialysis", "Kidney transplant"]
    }
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    query = request.args.get("query", "").strip()

    if query == "":
        return render_template("search.html", results=[], query=query)

    results = [
        item for item in items
        if query.lower() in item["title"].lower()
    ]

    return render_template("search.html", results=results, query=query)

@app.route("/view/<int:item_id>")
def view(item_id):
    item = next((i for i in items if i["id"] == item_id), None)
    return render_template("view.html", item=item)

if __name__ == "__main__":
    app.run(debug=True)
