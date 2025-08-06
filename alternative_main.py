#!/usr/bin/env python
"""
Versión temporal del main que funciona sin chromadb
"""
import sys
import warnings
from datetime import datetime
from pprint import pprint

import pandas as pd
import nbformat
from nbformat.v4 import new_notebook, new_code_cell

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Mock de la clase ContentMarketingProjectManager
class MockContentMarketingProjectManager:
    def crew(self):
        return MockCrew()

class MockCrew:
    def kickoff(self, inputs):
        # Simular el resultado de CrewAI
        mock_result = MockResult()
        return mock_result
    
    def calculate_usage_metrics(self):
        pass
    
    @property
    def usage_metrics(self):
        return None

class MockResult:
    @property
    def pydantic(self):
        return MockPydantic()

class MockPydantic:
    def dict(self):
        return {
            "tasks": [
                {
                    "id": "TASK-001",
                    "title": "Develop Blog Series Strategy",
                    "description": "Create a comprehensive strategy for a 5-part blog series addressing key pain points for B2B SaaS decision-makers",
                    "priority": "High",
                    "estimated_hours": 16,
                    "deliverables": ["Content strategy document", "Blog outline templates", "SEO keyword research"],
                    "dependencies": []
                },
                {
                    "id": "TASK-002", 
                    "title": "Create Lead Magnet Content",
                    "description": "Design and write an eBook and checklist to support gated campaigns",
                    "priority": "High",
                    "estimated_hours": 20,
                    "deliverables": ["eBook PDF", "Downloadable checklist", "Landing page copy"],
                    "dependencies": ["TASK-001"]
                },
                {
                    "id": "TASK-003",
                    "title": "Email Nurture Sequence",
                    "description": "Write a 4-part email sequence tied to blog and lead magnet topics",
                    "priority": "Medium",
                    "estimated_hours": 12,
                    "deliverables": ["4 email templates", "Subject line variations", "CTA copy"],
                    "dependencies": ["TASK-001", "TASK-002"]
                },
                {
                    "id": "TASK-004",
                    "title": "Social Media Assets",
                    "description": "Design promotional assets for LinkedIn, Twitter, and Instagram",
                    "priority": "Medium",
                    "estimated_hours": 18,
                    "deliverables": ["15 LinkedIn posts", "10 Twitter graphics", "8 Instagram stories"],
                    "dependencies": ["TASK-001"]
                },
                {
                    "id": "TASK-005",
                    "title": "Explainer Video Production",
                    "description": "Produce a 2-minute explainer video for new feature set",
                    "priority": "High",
                    "estimated_hours": 25,
                    "deliverables": ["Video script", "Storyboard", "Final video file"],
                    "dependencies": []
                },
                {
                    "id": "TASK-006",
                    "title": "Webinar Coordination",
                    "description": "Schedule and coordinate live webinar with guest speakers",
                    "priority": "Medium",
                    "estimated_hours": 15,
                    "deliverables": ["Webinar agenda", "Speaker coordination", "Registration page"],
                    "dependencies": ["TASK-001"]
                }
            ],
            "assignments": [
                {
                    "team_member": "Sarah Lee (Content Strategist)",
                    "assigned_tasks": ["TASK-001", "TASK-002"],
                    "total_hours": 36,
                    "role": "Lead Strategist"
                },
                {
                    "team_member": "Mark Johnson (SEO Writer)",
                    "assigned_tasks": ["TASK-001", "TASK-003"],
                    "total_hours": 28,
                    "role": "Content Writer"
                },
                {
                    "team_member": "Priya Desai (Graphic Designer)",
                    "assigned_tasks": ["TASK-004"],
                    "total_hours": 18,
                    "role": "Visual Designer"
                },
                {
                    "team_member": "Carlos Rivera (Email Marketing Specialist)",
                    "assigned_tasks": ["TASK-003"],
                    "total_hours": 12,
                    "role": "Email Marketing"
                },
                {
                    "team_member": "Emma Chen (Social Media Manager)",
                    "assigned_tasks": ["TASK-004"],
                    "total_hours": 18,
                    "role": "Social Media"
                },
                {
                    "team_member": "Liam Brown (Video Producer)",
                    "assigned_tasks": ["TASK-005"],
                    "total_hours": 25,
                    "role": "Video Production"
                }
            ],
            "milestones": [
                {
                    "milestone": "Content Strategy Complete",
                    "date": "Week 2",
                    "description": "Blog strategy and lead magnet strategy finalized",
                    "deliverables": ["TASK-001", "TASK-002"]
                },
                {
                    "milestone": "Content Creation Phase 1",
                    "date": "Week 4", 
                    "description": "Email sequence and social assets completed",
                    "deliverables": ["TASK-003", "TASK-004"]
                },
                {
                    "milestone": "Video and Webinar Ready",
                    "date": "Week 6",
                    "description": "Video production and webinar setup complete",
                    "deliverables": ["TASK-005", "TASK-006"]
                }
            ],
            "content_calendar": """
📅 CONTENT CALENDAR SUMMARY - Q1 2025

WEEK 1-2: STRATEGY & PLANNING
- Blog series strategy development (Sarah, Mark)
- Lead magnet content outline (Sarah)
- SEO keyword research (Mark)

WEEK 3-4: CONTENT CREATION PHASE 1  
- Email nurture sequence writing (Carlos, Mark)
- Social media asset design (Priya, Emma)
- Blog post drafts (Mark)

WEEK 5-6: MULTIMEDIA & EVENTS
- Explainer video production (Liam)
- Webinar setup and speaker coordination (Sarah)
- Lead magnet finalization (Sarah)

ONGOING ACTIVITIES:
- Weekly social media posts (Emma)
- Blog SEO optimization (Mark)
- Email campaign monitoring (Carlos)
- Brand guideline compliance (All team members)

QUARTERLY THEME: "Scaling with Smart Systems"
All content aligned with Q1 messaging strategy focused on helping B2B SaaS companies optimize their operations and scale efficiently.
            """
        }

# Content Marketing Project Inputs (mismos que en el original)
project_type = "Multi-Channel Content Marketing Campaign"
industry = "B2B SaaS"
project_objectives = "Drive brand awareness and lead generation through strategic content across blog, email, social media, and webinars."

team_members = """
- Sarah Lee (Content Strategist)
- Mark Johnson (SEO Writer)
- Priya Desai (Graphic Designer)
- Carlos Rivera (Email Marketing Specialist)
- Emma Chen (Social Media Manager)
- Liam Brown (Video Producer)
"""

project_requirements = """
- Create a blog series focused on solving key pain points for B2B SaaS decision-makers
- Develop lead magnet content (eBook and checklist) to support gated campaigns
- Write a 4-part email nurture sequence tied to the blog and lead magnet topics
- Design promotional assets for social media (LinkedIn, Twitter, Instagram)
- Produce a 2-minute explainer video introducing our new feature set
- Schedule and coordinate a live webinar with two guest speakers
- Ensure all content follows our brand guidelines and tone of voice
- Optimize blog posts and landing pages for SEO performance
- Align all content with the quarterly theme: "Scaling with Smart Systems"
- Track deadlines across all channels using a shared editorial calendar
"""

# Input dictionary for the crew
inputs = {
    'project_type': project_type,
    'industry': industry,
    'project_objectives': project_objectives,
    'project_requirements': project_requirements,
    'team_members': team_members
}

def run():
    """
    Run the content planning crew, display results, and export a notebook.
    """
    try:
        crew_instance = MockContentMarketingProjectManager().crew()
        result = crew_instance.kickoff(inputs=inputs)

        # Mock token usage reporting
        crew_instance.calculate_usage_metrics()
        usage = crew_instance.usage_metrics

        print("\n--- 📊 Usage Summary (Mock Data) ---")
        print("Prompt tokens: 1250")
        print("Completion tokens: 890")
        print("Total tokens: 2140")
        print("Estimated total cost: $0.0032")

        # Extract structured output
        project_plan = result.pydantic.dict()
        tasks = project_plan.get("tasks", [])
        assignments = project_plan.get("assignments", [])
        milestones = project_plan.get("milestones", [])
        calendar = project_plan.get("content_calendar", "N/A")

        # Terminal display
        print("\n--- 📝 Content Tasks ---")
        pprint(tasks)

        print("\n--- 👥 Assignments ---")
        pprint(assignments)

        print("\n--- 🎯 Milestones ---")
        pprint(milestones)

        print("\n--- 📅 Content Calendar ---")
        print(calendar if calendar else "No calendar summary provided.")

        # Create Jupyter Notebook
        nb = new_notebook()
        nb.cells.append(new_code_cell("import pandas as pd"))

        nb.cells.append(new_code_cell(
            f"tasks = {tasks}\n"
            "df_tasks = pd.DataFrame(tasks)\n"
            "df_tasks.style.set_table_attributes('border=\"1\"').set_caption(\"Task Details\").set_table_styles(\n"
            "    [{'selector': 'th, td', 'props': [('font-size', '120%')]}]\n"
            ")"
        ))

        nb.cells.append(new_code_cell(
            f"assignments = {assignments}\n"
            "df_assignments = pd.DataFrame(assignments)\n"
            "df_assignments.style.set_table_attributes('border=\"1\"').set_caption(\"Resource Assignments\").set_table_styles(\n"
            "    [{'selector': 'th, td', 'props': [('font-size', '120%')]}]\n"
            ")"
        ))

        nb.cells.append(new_code_cell(
            f"milestones = {milestones}\n"
            "df_milestones = pd.DataFrame(milestones)\n"
            "df_milestones.style.set_table_attributes('border=\"1\"').set_caption(\"Milestones\").set_table_styles(\n"
            "    [{'selector': 'th, td', 'props': [('font-size', '120%')]}]\n"
            ")"
        ))

        nb.cells.append(new_code_cell(
            f'print("📅 Content Calendar Summary:")\nprint("""{calendar}""")'
        ))

        with open("crew_output.ipynb", "w", encoding='utf-8') as f:
            nbformat.write(nb, f)

        print("\n✅ Jupyter Notebook 'crew_output.ipynb' created successfully.")
        print("\n🔧 NOTE: This is a mock version running without CrewAI due to compilation issues.")
        print("The real CrewAI version will be available once Visual C++ Build Tools are properly configured.")

    except Exception as e:
        raise Exception(f"An error occurred while running the mock crew: {e}")

if __name__ == "__main__":
    run()
