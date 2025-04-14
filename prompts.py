def get_intro_prompt():
    return (
        "Hi there! 👋 I’m the Hiring Assistant for TalentScout. "
        "I'll guide you through a short screening process to collect your info and test your skills. Let's get started! "
        "Please enter your full name."
    )

def get_tech_questions_prompt(tech_stack):
    return f"""
You are an expert technical interviewer. Generate 3 to 5 interview questions for a candidate skilled in the following tech stack: {tech_stack}.
Include a mix of conceptual and practical questions to assess real-world proficiency.
"""
