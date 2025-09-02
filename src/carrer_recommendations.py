import os
import json
import re
import base64
import google.generativeai as genai

api_key = "AIzaSyAlIJ4_gQ2g1CxNZWkjtu8MSZiUhOi9Tj0"
genai.configure(api_key=api_key)



def carrer_recommendation(user_profile):
    prompt=f"""
    You are a Carrer recommendation system.
    You are given a user profile and your job is to tell the 3 best carrer options for the user.
    
    User Profile:
    Name: {user_profile.get("name")}
    Skills: {user_profile.get("skills")}
    Education: {user_profile.get("education")}
   

IMPORTANT:You must respond with valid JSON only.
    {{
        "user_name": "{user_profile.get("name")}",
        "Recommendations":[
        {{  "Carrer":"Data Scientist",
            "match_percent":85,
            "Description":"You are a good knowlege of machine learning and data analysis"
            
        }},
        {{  "Carrer":"Digital Marketing"
            "match_percent":78,
            "Description":"You have good knowlege of SEO,SEM and content marketing"
            
        }},
        
        {{  "Carrer":"Web Developer"
            "match_percent":72,
            "Description":"You have good knowlege of HTML,CSS,JavaScript and web development frameworks"
             
            
        }},
        {{
            "Carrer":"IAS Officer(Civil Services)",
            "match_percent":80,
            "Description":"You have good knowlege of current affairs and public administration"
            
            
        }}
        ]
    }}
    """
        
    model=genai.GenerativeModel("gemini-2.5-pro")
    
    response=model.generate_content(prompt)
    
    try:
        response_text = response.text.strip()
        json_match = re.search(r'({.*})', response_text, re.DOTALL)
        if not json_match:
            raise json.JSONDecodeError("Invalid JSON from Gemini", response_text, 0)
        cleaned_json = json_match.group(1)
        parsed = json.loads(cleaned_json)
        return parsed
            
    except Exception as e:
        print(f"[ERROR] career_recommendations fallback triggered: {str(e)}")
        return json.dumps({
            "parsing_error": True,
            "message": "Could not generate career recommendations",
            "raw_response": getattr(response, 'text', str(response)),
            "Recommendations": []
        })
        
if __name__ == "__main__":
    test_profile = {
        "name": "Harsh Gangawane",
        "Skills":"Python,Machine Learning,Statistics",
        "education": "Bachelor's"
    }
    recs = carrer_recommendation(test_profile)
    print(json.dumps(recs, indent=2))

