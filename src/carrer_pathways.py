import os
import json
import re
import google.generativeai as genai

api_key='AIzaSyAlIJ4_gQ2g1CxNZWkjtu8MSZiUhOi9Tj0'
genai.configure(api_key=api_key)


def carrer_pathways(courses, skills, education):
    prompt = f"""
    You are a Career Pathway Generator AI.
    Based on User's selected career, skills (may be incomplete),
    and Education (Bachelor's, Master's, PhD, Diploma),
    create a structured pathway including roadmap, course suggestions and projects.
    Do not give 404 error for course suggestions such as "No courses found".
    There should be only 3 projects (Beginner, Intermediate, Advanced).Projects must be according/relevant to the carrer.
    
    RULES:
    All recommendations (roadmap, courses, projects) MUST be directly relevant to the chosen career: "{courses}".
    Do NOT recommend programming or data science unless the career requires it.
    Include exactly 3 projects: Beginner, Intermediate, Advanced.
    Courses must be real and from well-known platforms (Coursera, Udemy, edX, Unacademy, LinkedIn Learning, etc.).

    Carrers:{courses}
    Skills:{skills}
    Education:{education}

   
    IMPORTANT:You must respond with valid JSON only.
    {{
        "Carrer":"Data Scientist",
        "Skills":["Python","Machine Learning","Statistics"],
        "roadmap":[
            "step 1: __",
            "step 2: __",
            "step 3: __"
        ],
        "Courses":[
            {{
                "Course_name":"Python for Data Science and Machine Learning Bootcamp",
                "Course_link":"https://www.udemy.com/course/python-for-data-science-and-machine-learning-bootcamp/?couponCode=MT180825C",
                "Platform":"Udemy"
            }},
            {{
                "Course_name":"IBM Data Science Professional Certificate",
                "Course_link":"https://www.coursera.org/professional-certificates/ibm-data-science",
                "Platform":"Coursera"
            }},
            {{
                "Course_name":"Complete Data Science ,Machine Learning,DL,NLP Bootcamp",
                "Course_link":"https://www.udemy.com/course/complete-machine-learning-nlp-bootcamp-mlops-deployment/?couponCode=MT180825C",
                "Platform":"Udemy"
            }}
        ],
        "Projects":[
            {{
                "level":"Beginner",
                "Project_title":"Movie Recommendation System",
                "Description":"A System that suggest movies to user based on their past ratings, preference, or similarity based on user."
            }},
            {{
                "level":"Intermediate",
                "Project_title":"Sentiment Analysis on Tweets/Reviews",
                "Description":"A project that classifies tweets or reviews as positive, negative, or neutral based on text content"
            }},
            {{
                "level":"Advanced",
                "Project_title":"Medical Image Analysis",
                "Description":"A project that uses deep learning to detect disease or abnormalities from medical images like X-rays or MRI"
            }},
            
        ],
        "Carrer":"IAS Officer(Civil Services)",
        "Skills":["Current Affairs","Public Administration"],
        "roadmap":["Step 1:__","Step 2:__","Step 3:__"],
        "Courses":[
            {{
                "Course_name":"UPSC General - Volume 1",
                "Course_link":"https://www.udemy.com/course/upsc-general-volume-1/?couponCode=25BBPMXNVD35CTRL",
                "Platform":"Udemy"
            }},
            {{
                "Course_name":"UPSC Laxmikanth Polity- Easy to understand/ Easy to remember",
                "Course_link":"https://www.udemy.com/course/upscpolity/?couponCode=25BBPMXNVD35CTRL",
                "Platform":"Udemy"
            }},
            {{
                "Course_name":"Crack UPSC CSE - GS with Unacademy",
                "Course_link":"https://unacademy.com/goal/upsc-civil-services-examination-ias-preparation/KSCGY",
                "Platform":"Unacademy"
            }}
            ],
            "Projects":[
                {{
                    "level":"Beginner",
                    "Project_title":"Daily Current Affairs Journal",
                    "Description":"Create a habit of reading two quality newspapers every day (e.g., The Hindu, Indian Express). Summarize key news in your own words in one page — write what happened, why it matters, and which syllabus topic it connects to (like Economy, Polity, Environment). At the end of the week, make a one-page “Weekly Review” of the main issues."
                }},
                {{
                    "level":"Intermediate",
                    "Project_title":"Local Governance Study",
                    "Description":"Choose one real problem in your area (e.g., waste management, water shortage, traffic). Study which government body is responsible, what schemes exist, and whether they work. Collect basic data (from talking to people or looking at official sites) and write a short 2–3-page note with your findings and suggested solutions."
                }},
                {{
                    "level":"Advanced",
                    "Project_title":"Policy Draft & Discussion",
                    "Description":"Pick a big national issue (e.g., unemployment, climate change, education quality). Research India’s and the world’s approaches. Write a one-page “policy brief” that states the problem, lists key causes, suggests 3–4 solutions, and predicts possible results. Then hold a debate or group discussion (offline or online) to defend your policy and hear counter-arguments."
                }}
            ],
            
            
            
    }}
    """
    model = genai.GenerativeModel("gemini-2.5-pro")

    response = model.generate_content(prompt)

    try:
        response_text = response.text.strip()
        json_match = re.search(r'({.*})', response_text, re.DOTALL)
        if not json_match:
            raise json.JSONDecodeError("Invalid JSON from Gemini", response_text, 0)
        cleaned_json = json_match.group(1)
        parsed = json.loads(cleaned_json)
        
       
        return parsed

    except Exception as e:
        print(f"[ERROR] career_pathway fallback triggered: {str(e)}")
        return {
            "parsing_error": True,
            "message": "Could not generate pathway",
            "raw_response": getattr(response, 'text', str(response)),
            "roadmap": [],
            "courses": [],
            "projects": []
        }

if __name__ == "__main__":
    test_pathway = carrer_pathways(
        courses="Administrative Assistant",
        skills="Python, Machine Learning, Statistics",
        education="Bachelor's"
    )
    print(json.dumps(test_pathway, indent=2))


