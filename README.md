# Disease Encyclopedia 

This project entails a searchable web encyclopedia for chronic and infectious diseases. Browse conditions, search by name, and view detailed information including symptoms, treatments, and prevalence data. Each disease page also links to avideo  resource for further learning.

The app has three core pages: 
1. a home page featuring highlighted diseases
2. a search results page
3. a detailed view page for each condition

All search logic runs server-side in Python, and the home page items are rendered dynamically through JavaScript rather than hardcoded in HTML.

## features
- Search diseases by name from the navbar on any page (search is case-insensitive and matches any part of the title)
- Returns a "No results found" message for unmatched queries
- Ignores whitespace-only searches
- Click any result or featured item to view the full disease profile
- Each disease page displays description, symptoms, treatments, prevalence, year identified, and a video link
- Clicking the site title from any page returns you to the home page

## diseases covered
- Type 2 Diabetes
- Hypertension
- Asthma
- Coronary Artery Disease
- Breast Cancer
- Alzheimer's Disease
- Influenza
- COVID-19
- Rheumatoid Arthritis
- Chronic Kidney Disease

## project structure: 
```
disease-encyclopedia/
    server.py           # Flask routes, search logic, and all disease data
    templates/
        home.html       # Landing page with 3 featured diseases
        search.html     # Search results page
        view.html       # Full disease detail page
        layout.html     # Shared navbar and base template
    static/
        style.css       # Styling
        script.js       # Dynamic home page rendering
```

## how to run: 
1. Install Flask:
`pip install flask` 
2. Start the server:
`python3 server.py` 
3. Open your browser and go to http://localhost:5000

## tools used: 
- Backend: Python, Flask
- Frontend: HTML, CSS, JavaScript, Bootstrap 5
- Templating: Jinja2

Notes
Disease data is stored directly in server.py as a list of dictionaries. Each entry includes a title, description, year identified, global prevalence, symptoms list, treatments list, and a YouTube video link. Adding a new disease is as simple as appending a new dictionary to the list.
