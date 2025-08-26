import json
from jinja2 import Environment, FileSystemLoader
import os

# Load profile data from JSON
with open("profile.json", "r", encoding="utf-8") as f:
    profile_data = json.load(f)

# Transform profile_data to match template structure
cv = {
    "title": profile_data.get("title"),
    "name": profile_data.get("name"),
    "mobile": profile_data.get("mobile"),
    "email": profile_data.get("email"),
    "web": profile_data.get("web"),
    "city": profile_data.get("city"),
    "country": profile_data.get("country"),
    "linkedin": profile_data.get("linkedin"),
    "self_intro": "\n".join(profile_data.get("profile", [])),
    "summary": "\n".join(profile_data.get("profile", [])),
    "certificates": [
        {"start_date": cert["date"], "name": cert["name"]} for cert in profile_data.get("certificates", [])
    ],
    "educations": [
        {
            "duration": profile_data["education"]["period"],
            "degree_and_major": profile_data["education"]["degree"],
            "school": profile_data["education"]["institution"],
            "location": profile_data["education"]["location"]
        }
    ],
    "languages": profile_data.get("languages", []),
    "experiences": [
        {
            "company": job["company"],
            "title": job["title"],
            "description": "\n".join(job.get("responsibilities", []))
        } for job in profile_data.get("employment_history", [])
    ],
    "skills": [
        {"name": skill, "level": "Expert"} for skill in profile_data.get("skills", {}).get("expert", [])
    ] + [
        {"name": skill, "level": "Experienced"} for skill in profile_data.get("skills", {}).get("experienced", [])
    ],
    "hobbies": ", ".join(profile_data.get("hobbies", []))
}

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("responsive1.html")

# Render the template
rendered_html = template.render(cv=cv)

# Save the output
with open("output_cv_updated.html", "w", encoding="utf-8") as f:
    f.write(rendered_html)

print("Updated CV rendered and saved to output_cv_updated.html")
