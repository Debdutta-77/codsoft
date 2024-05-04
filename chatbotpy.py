def chatbot_response(user_input):
    # Convert user input to lowercase for easier comparison
    user_input = user_input.lower()

    # Define some predefined rules and responses
    if "hello" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but thank you for asking!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif user_input.isdigit():
        group_number = int(user_input)
        if 1 <= group_number <= 11:  # Assuming there are 11 groups
            return get_question_group(group_number)
        else:
            return "Invalid group number. Please enter a number between 1 and 11."
    elif ":" in user_input and user_input.split(":")[0].isdigit():
        group_number = int(user_input.split(":")[0])
        question_number = int(user_input.split(":")[1])
        if 1 <= group_number <= 11:  # Assuming there are 11 groups
            if 1 <= question_number <= 3:  # Assuming each group has 3 questions
                return get_answer(group_number, question_number)
            else:
                return "Invalid question number. Please enter a number between 1 and 3."
        else:
            return "Invalid group number. Please enter a number between 1 and 11."
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

def get_question_group(group_number):
    question_groups = {
        1: "College Programs and Majors",
        2: "Admissions and Financial Aid",
        3: "Campus Life and Facilities",
        4: "Academic Support and Opportunities",
        5: "Student Engagement and Activities",
        6: "International Programs and Diversity",
        7: "Career Services and Employment",
        8: "Miscellaneous",
        9: "Graduation and Research",
        10: "Student Services",
        11: "Academic Affairs"
    }
    questions = {
        1: [
            "1. What majors does the college offer?",
            "2. Can students double major or pursue a minor?",
            "3. Are there opportunities for undergraduate research?"
        ],
        2: [
            "1. What are the admission requirements?",
            "2. Is financial aid available?",
            "3. What scholarships are available?"
        ],
        3: [
            "1. What are the campus facilities like?",
            "2. Is there on-campus housing?",
            "3. Are there opportunities for community service?"
        ],
        4: [
            "1. What support services are available for students with disabilities?",
            "2. Does the college offer study groups or tutoring services?",
            "3. What mental health resources are available on campus?"
        ],
        5: [
            "1. What extracurricular activities are available?",
            "2. Are there opportunities for leadership development?",
            "3. What recreational facilities are available?"
        ],
        6: [
            "1. Can students study abroad?",
            "2. What is the diversity of the student body?",
            "3. Are there opportunities for international students to get involved on campus?"
        ],
        7: [
            "1. What career services are available to students?",
            "2. What is the average starting salary for graduates?",
            "3. Are there opportunities for internships?"
        ],
        8: [
            "1. What is the graduation rate?",
            "2. What is the average class size?",
            "3. What is the college's mission or values?"
        ],
        9: [
            "1. What is the graduation rate?",
            "2. Are there opportunities for undergraduate research?",
            "3. What is the average starting salary for graduates?"
        ],
        10: [
            "1. Are there opportunities for community service or volunteering?",
            "2. Is there a health center on campus?",
            "3. Are there opportunities for leadership development?"
        ],
        11: [
            "1. What is the college's accreditation status?",
            "2. What are the requirements for joining Greek life organizations?",
            "3. Is there a career center that helps students find internships?"
        ]
    }
    group_heading = question_groups.get(group_number, "Miscellaneous")
    group_questions = questions.get(group_number, [])
    response = f"{group_heading}\n\n"
    response += "\n".join(group_questions)
    response += "\n\nPlease select the question number to get more details."
    return response

def get_answer(group_number, question_number):
    answers = {
        (1, 1): "The college offers majors in various fields such as Engineering, Business, Psychology, etc.",
        (1, 2): "Yes, students can double major or pursue a minor. They should consult with their academic advisor for more information.",
        (1, 3): "Yes, there are opportunities for undergraduate research through faculty-led projects and independent studies.",
        (2, 1): "Admission requirements typically include high school transcripts, standardized test scores (SAT/ACT), letters of recommendation, and a personal statement.",
        (2, 2): "Yes, financial aid is available in the form of scholarships, grants, loans, and work-study programs. Students should apply through the FAFSA.",
        (2, 3): "Various scholarships are available for both incoming and current students. These scholarships may be based on academic merit, financial need, or other criteria.",
        (3, 1): "Campus facilities include libraries, labs, sports facilities, dining halls, dormitories, and student centers.",
        (3, 2): "Yes, the college offers on-campus housing options for students. They can apply for housing through the housing office.",
        (3, 3): "Yes, students have opportunities for community service through volunteer programs, service-learning courses, and campus organizations dedicated to community engagement.",
        (4, 1): "Support services for students with disabilities include accommodations such as extended test time, note-taking assistance, and accessible campus facilities.",
        (4, 2): "Yes, the college offers study groups, tutoring services, and academic support centers to assist students with their coursework.",
        (4, 3): "Mental health resources include counseling services, support groups, workshops, and referrals to off-campus professionals if needed.",
        (5, 1): "Extracurricular activities include clubs, sports teams, student government, performing arts groups, and cultural organizations.",
        (5, 2): "Yes, there are opportunities for leadership development through leadership programs, workshops, and involvement in student organizations.",
        (5, 3): "Recreational facilities include fitness centers, sports fields, outdoor trails, and intramural sports leagues.",
        (6, 1): "Yes, students can study abroad through various programs offered by the college. They can spend a semester or a year studying in another country.",
        (6, 2): "The college prides itself on its diverse student body, which includes students from different cultural, ethnic, and socioeconomic backgrounds.",
        (6, 3): "International students can get involved on campus through cultural clubs, international student organizations, and events celebrating diversity.",
        (7, 1): "Career services provide assistance with resume writing, interview preparation, job search strategies, networking, and career counseling.",
        (7, 2): "The average starting salary for graduates depends on factors such as their major, industry, location, and level of experience. It typically ranges from $X to $Y per year.",
        (7, 3): "Yes, students can find internship opportunities through the college's career center, job fairs, employer partnerships, and alumni networks.",
        (8, 1): "The graduation rate is X%, indicating the percentage of students who complete their degree within a specified time frame.",
        (8, 2): "The average class size varies depending on the course and the level of study. It typically ranges from X to Y students per class.",
        (8, 3): "The college's mission is to [mission statement], emphasizing academic excellence, diversity, community engagement, and lifelong learning.",
        (9, 1): "The graduation rate is X%, indicating the percentage of students who complete their degree within a specified time frame.",
        (9, 2): "Yes, there are opportunities for undergraduate research through faculty-led projects, research assistantships, and summer research programs.",
        (9, 3): "The average starting salary for graduates varies depending on factors such as their major, industry, and level of experience. It typically ranges from $X to $Y per year.",
        (10, 1): "Yes, students have opportunities for community service and volunteering through campus organizations, service-learning courses, and local outreach programs.",
        (10, 2): "Yes, the college has a health center on campus that provides medical services, counseling, wellness programs, and referrals to specialists if needed.",
        (10, 3): "Yes, there are opportunities for leadership development through leadership programs, workshops, and involvement in student government and clubs.",
        (11, 1): "The college is accredited by NBA, ensuring academic quality and meeting standards set by accrediting organizations.",
        (11, 2): "Requirements for joining Greek life organizations vary but may include academic standing, participation in recruitment events, and payment of dues.",
        (11, 3): "Yes, the college's career center offers services to help students find internships, job opportunities, and career resources.",
    }
    return answers.get((group_number, question_number), "No answer found.")

# Main function to run the chatbot
def main():
    print("\nWELCOME to the simple rule-based CHATBOT!! \n\nI will help you to know more about our college.\nTYPE back to return to the groups section.")
    while True:
        print("\nEnter the group number to see related questions:\n")
        print("1. College Programs and Majors")
        print("2. Admissions and Financial Aid")
        print("3. Campus Life and Facilities")
        print("4. Academic Support and Opportunities")
        print("5. Student Engagement and Activities")
        print("6. International Programs and Diversity")
        print("7. Career Services and Employment")
        print("8. Miscellaneous")
        print("9. Graduation and Research")
        print("10. Student Services")
        print("11. Academic Affairs")
        user_input_group = input("You: ")
        if user_input_group.lower() == 'bye':
            print(chatbot_response(user_input_group))
            break
        else:
            group_number = int(user_input_group)
            if 1 <= group_number <= 11:
                print(get_question_group(group_number))
                while True:
                    user_input_question = input("You: ")
                    if user_input_question.lower() == 'back':
                        break
                    elif user_input_question.isdigit():
                        question_number = int(user_input_question)
                        if 1 <= question_number <= 3:
                            print(get_answer(group_number, question_number))
                            print("\nEnter back to return to the group menu:")
                        else:
                            print("Invalid question number. Please enter a number between 1 and 3.")
                    else:
                        print("Invalid input. Please enter a number or 'back'.")

            else:
                print("Invalid group number. Please enter a number between 1 and 11.")

if __name__ == "__main__":
    main()
