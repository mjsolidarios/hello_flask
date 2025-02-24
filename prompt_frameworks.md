## Common Prompt Engineering Frameworks

**1. RACE Framework (Role, Action, Context, Expectation):**

    Example (Patient Education):
        Role: "You are a patient education specialist."
        Action: "Explain the risks and benefits."
        Context: "of a new diabetes medication to a patient with limited medical literacy."
        Expectation: "Provide a clear and concise summary that the patient can easily understand."
    Example (Medical Research):
        Role: "You are a medical researcher."
        Action: "Summarize the findings."
        Context: "of recent clinical trials on a new cancer treatment."
        Expectation: "Provide a detailed report including key statistics and potential implications for patient care."

**2. CRISPE Framework (Clarity, Relevance, Iteration, Specificity, Parameters, Examples):**

    Example (Diagnostic Support):
        Clarity: "Analyze the following patient symptoms."
        Relevance: "Focus on potential causes of acute chest pain."
        Iteration: "Provide a preliminary diagnosis, and then refine it based on these additional test results."
        Specificity: "Include differential diagnoses and the reasoning behind each."
        Parameters: "Use the latest clinical guidelines from the American Heart Association."
        Examples: "Compare the patient's symptoms to known cases of myocardial infarction and pulmonary embolism."
    Example (Generating patient after visit summaries):
        Clarity: "Create a patient after-visit summary"
        Relevance: "For a patient that has just had a check-up for hypertension."
        Iteration: "Include the doctor's notes, and then include the patient's current medication list."
        Specificity: "Include specific instructions for medication adherence, and lifestyle changes."
        Parameters: "Use language that is appropriate for a 60-year-old patient with a 9th-grade reading level."
        Examples: "Include examples of low-sodium meals."

**3. PGTC (Persona, Goal, Task, Context):**

    Example (Clinical Decision Support):
        Persona: "You are an experienced emergency room physician."
        Goal: "To quickly assess and prioritize patients."
        Task: "Analyze the vital signs and symptoms of a patient presenting with shortness of breath."
        Context: "The patient has a history of asthma and COPD."
    Example (Healthcare Administration):
        Persona: "You are a hospital administrator."
        Goal: "To reduce patient wait times."
        Task: "Analyze patient flow data, and provide recommendations."
        Context: "The emergency department is experiencing a surge in patient volume."
