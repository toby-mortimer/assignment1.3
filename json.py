import requests

json = """{
    "title": "Further Maths",
    "type": "A Level",
    "teacher_info": "Phil Greenwood - Teacher of Maths and Further Maths",
    "requirements": "Minimum 5 GCSE's at Grade 4 or above. Including at least grade 7 in Maths. Can only be studied alongside A Level Maths",
    "ucas_points": "Up to 56 UCAS Points",
    "topics": "Complex numbers, advanced calculus, use of power series, statistical techniques, advanced mechanics, algorithm Matrices",
    "description": "Further Maths builds on skills in A Level Maths, expanding into more complex general methods known as pure maths as well as applying them to statistics, mathematical physics and methods used in computing and project management. Students who have studied Further Maths have found that it gives a great start on university courses such as physics, engineering, astronomy, computing and, of course, maths. The course introduces the study of complex numbers which are numbers that don't exist in the real world, however, as an abstract concept they are invaluable in many aspects of physics, especially quantum mechanics, being used, for example, to model wind flow as used in the testing of aircraft design. A large section of the syllabus looks at advanced use of calculus which is the most used tool on university courses with a mathematical base.",
    "testimonials": "'Further Maths is a great challenge and makes you feel like a proper mathematician! I love the range of topics and the cool stuff you discover— like imaginary numbers.' \\n Naomi, previously St Edmund' s Girls' School ",
    "exam_details": "100% exams"
},,{
    "title": "Geography",
    "type": "A Level",
    "teacher_info": "Susan Murphy - Teacher of Geography",
    "requirements": "Minimum 5 GCSE's at Grade 4 or above. Including at least grade 4 in Maths",
    "ucas_points": "Up to 56 UCAS Points",
    "topics": "Hazards, water and carbon cycles, coastal systems and landscapes, global governance, changing places, population and the environment",
    "description": "Geography helps you to make sense of the world around you. It's hands on, it's relevant, and it's fun. Our physical and human geography topics cover a wide range of exciting and dynamic global issues including hazards, water and carbon cycles, coastal systems and landscapes, population and the environment, global governance and changing places. You will have the opportunity to do your own fieldwork investigation on any geographical topic which interests you, researching independently and building on your skills to produce a report which is worth 20% of your final grade. To help you with this we will do plenty of fieldwork including a two day residential at Leeson House in Dorset (coastal and urban regeneration) and local fieldwork around the Salisbury area.",
    "testimonials": "'Geography is an interesting and exciting subject to study. The freedom of the coursework topic gives a feeling of independence. The fieldwork varies your studying and is a lot of fun!' \\n Skye, previously Gillingham School",
    "exam_details": "80% exams \\n 20% coursework"
},,{
    "title": "History",
    "type": "A Level",
    "teacher_info": "Sally Tye - Faculty Lead (Humanities), Teacher of History and RS",
    "requirements": "Minimum 5 GCSE's at Grade 4 or above. Including at least grade 5 in English",
    "ucas_points": "Up to 56 UCAS Points",
    "topics": "British History, 1930-1997, Tudor Rebellions, The Crusades and the Crusader States",
    "description": "History at S6C covers nearly 1000 years of history from the Crusades to 20th Century British Politics. You will learn about Richard the Lionheart, one of the most famous medieval kings, and his 3rd Crusade to Jerusalem; Churchill, from his 'wilderness years' to his heroic leadership during World War Two; the many rebellions faced by Tudor Monarchs; and Thatcher's reign of glory (or terror, depending on your perspective). This course will not only introduce you to an impressive range of histories covering medieval, early modern and modern periods but also social, political and religious issues giving you the best possible preparation for further study in any humanities area. You will be taught how to form detailed and evidence-based arguments on a range of topics whilst developing your skills of independent analysis.",
    "testimonials": "'There is never a dull moment in class. I have never worked so hard but I love it!' \\n Gabriel, previously Avon Valley College",
    "exam_details": "80% exams \\n 20% coursework"
},,{
    "title": "HSC (Extended Certificate)",
    "type": "CTEC",
    "teacher_info": "Jo Mason - Teacher Health & Social Care Luke Muchmore - Teacher of Sport and Health & Social Care",
    "requirements": "Minimum 5 GCSE's at Grade 4 or above.",
    "ucas_points": "Up to 56 UCAS Points",
    "topics": "Building positive relationships, equality, diversity and rights, health, safety and security, anatomy and physiology, infection control, person-centred approach to care, safeguarding, supporting people with learning disabilities, mental health conditions and dementia, promoting positive behaviour",
    "description": "The health and social care industry is one of the fastest growing in the UK – people are living longer and there is an increasing need for care and support as well as working with children in early years. By studying Health and Social Care you will learn how to help others improve their physical health and impact the wellbeing of people in your community as well as developing skills in working with young children. If you want to help make a positive difference to people's lives then Health and Social Care is the course for you. The Extended Certificate is equivalent to 1 A Level and awards UCAS points towards university applications. You will develop professional and personal skills to allow you to offer specific, person-centred care and support and build positive relationships with the people you are working with, so that their needs and requirements are met while they maintain control of their own care and support. There is no requirement for work experience however we strongly recommend any work experience or part time work is related in some way to the sector.",
    "testimonials": "'I am really enjoying Health & Social Care because I can see issues that people face in a different light and interpret how our world has changed as well as giving me the qualifications I need to succeed.' \\n Sophie, previously Burgate School",
    "exam_details": "50% exams \\n 50% coursework"
},,{
    "title": "HSC (Extended Diploma)",
    "type": "CTEC",
    "teacher_info": "Jo Mason - Teacher Health & Social Care Luke Muchmore - Teacher of Sport and Health & Social Care",
    "requirements": "Minimum 5 GCSE's at Grade 4 or above.",
    "ucas_points": "Up to 168 UCAS Points",
    "topics": "Building positive relationships, equality, diversity and rights, health, safety and security, anatomy and physiology, public health, sexual health, reproduction and early years development",
    "description": "The health and social care industry is one of the fastest growing in the UK – people are living longer and there is an increasing need for care and support as well as working with children in early years. By studying Health and Social Care you will learn how to help others improve their physical health and impact the wellbeing of people in your community as well as developing skills in working with young children. If you want to help make a positive difference to people's lives then Health and Social Care is the course for you. In the first year you will study the Certificate and on successful completion you will continue onto the second year to complete the Extended Certificate or the Extended Diploma. You will develop professional and personal skills to allow you to offer specific, person-centred care and support and build positive relationships with the people you are working with, so that their needs and requirements are met while they maintain control of their own care and support.",
    "testimonials": "'It is an interesting and enjoyable course that covers a wide range of topics' \\n Morgan, previously The Trafalgar School at Downton",
    "exam_details": "30% exams \\n 70% coursework"
},,{
    "title": "HSC Accelerated Pathway",
    "type": "CTEC",
    "teacher_info": "Jo Mason - Teacher Health & Social Care Luke Muchmore - Teacher of Sport and Health & Social Care",
    "requirements": "Minimum 5 GCSE's at Grade 3 or above.",
    "ucas_points": "Up to 48 UCAS Points",
    "topics": "Building positive relationships, equality, diversity and rights, health, safety and security, anatomy and physiology, public health, sexual health, reproduction and early years development, the impact of long term physiological conditions, supporting people with dementia, supporting people with mental health conditions",
    "description": "This exciting Accelerated Pathway in Health & Social Care offers you the opportunity to develop the knowledge and practical skills needed for future work in the healthcare and education industries over two years. It will help you to develop essential skills for the world of Health and Social Care such as Safeguarding, Anatomy & Physiology, Infection Control, Equality & Diversity as well as numeracy, communication, teamwork and other transferable skills. In Year 1 you will begin on a CTEC Certificate in Health and Social Care, which is made up of various core, mandatory and optional units offered within the context of the unique S6C Study Programme which also includes GCSE Maths and English retake if necessary, work experience, enrichment and career education – all supported by a strong tutorial programme. After successful completion of the introductory units you can either proceed to a Diploma in Health and Social Care or apply for an apprenticeship. This pathway enhances the skills and knowledge established in the introductory units and prepares you for Higher Education, a Higher Level Apprenticeship or the workplace.",
    "testimonials": "'I am really enjoying Health & Social Care because it gives me an insight on what people have to go through on a daily basis which makes me want to become a health professional even more.' \\n Lilly, previously Penair School",
    "exam_details": "35% exams \\n 65% coursework"
},,{
    "title": "Maths",
    "type": "A Level",
    "teacher_info": "Phil Greenwood - Teacher of Maths and Further Maths",
    "requirements": "Minimum 5 GCSE's at Grade 4 or above. Including at least grade 7 in Maths",
    "ucas_points": "Up to 56 UCAS Points",
    "topics": "Calculus, coordinate geometry, sequences and series, trigonometry, exponential growth and decay, statistical distributions, probability theory, kinetics, motion of projectiles, forces of Newton's Laws of Motion",
    "description": "If Maths gives you a buzz at GCSE and you enjoy solving problems then taking it further could be for you. Maths is a subject that brings many others together and is a tool used in a wide range of areas. Maths supports work undertaken in sciences, as well as subjects such as Psychology, Business and Geography. It is a subject held in high regard by higher education institutions and employers. You will learn how to analyse a situation, select the methods required and confidently apply them successfully to solve the problem and be able to explain how you have done it. These methods will include some you have done already but at a greater level and many new ones such as calculus and probability methods. With these you will be able to see how strategies to cure diseases are created while looking at methods that are used in quantum mechanics to create algorithms used by satellites, GPS and population behaviour investigations.",
    "testimonials": "'I knew that Maths would be beneficial to me for studying Chemistry and Biology. The teaching is really fantastic and it makes Maths really fun to learn, even when it's difficult!' \\n Corrina, previously The Stonehenge School",
    "exam_details": "100% exams"
},,{
    "title": "Physics",
    "type": "A Level",
    "teacher_info": "Chris Papp - Teacher of Physics and Chemistry",
    "requirements": "Minimum 5 GCSE's at Grade 4 or above. Including at least grade 6 in Maths and Physics (or Combined Science 6 6)",
    "ucas_points": "UP to 56 UCAS points",
    "topics": "Mechanics, materials, D.C circuits, waves and optics, radiation and particle physics, fields, thermal physics, capacitors, radioactivity and nuclear physics",
    "description": "Physics encompasses the study of the Universe from the largest galaxies to the smallest subatomic particles. It is crucial to understanding the world around us, the world inside us, and the world beyond us. It is the most basic and fundamental Science. Physics challenges our imaginations and leads to great discoveries, like computers and lasers, which lead to technologies which change our lives – from healing joints, to curing cancer, to developing sustainable energy solutions. It is only in Physics that you will find yourself thinking about everything from how the Universe started to how a bridge stays up. You will study topics including mechanics, materials, D.C. Circuits, waves and optics, radiation and particle physics, fields, radioactivity and nuclear physics, thermal physics and capacitors. Our STEM club complements the Science courses by allowing you to develop your own practical project and maybe even gain a Crest Award.",
    "testimonials": "'You get to understand, not just know; you learn the reasons behind a lot of content you were just told at school.' \\n Sam, previously St Joseph's Catholic School",
    "exam_details": "100% exams 40% calculations"
},,{
    "title": "Psychology",
    "type": "A Level",
    "teacher_info": "Kirsty White - Faculty Lead (STEM), Teacher of Psychology and Polly Cordell",
    "requirements": "Minimum 5 GCSE's at Grade 4 or above. Including at least grade 5 in English, Maths and a Science",
    "ucas_points": "UP to 56 UCAS Points",
    "topics": "Social influence, memory, attachment, psychopathology, approaches, biopsychology, research methods, issues and debates, gender, schizophrenia, addiction",
    "description": "Psychology is the scientific study of the human mind and behaviour: how we think, feel, act and interact both individually and in groups. In A Level Psychology we learn about each of the approaches to explaining the way your thoughts and feelings act and interact – what makes you, 'you'. A Level Psychology is designed to give you an introduction to a broad range of topics in the field, and provides the basis for a number of engaging debates on what is at the heart of human nature. Students studying Psychology at A Level have gone on to study the subject at degree level and see the subject as an ideal stepping stone to this additional study. It also complements other subjects incredibly well; if you're looking at completing a mostly scientific programme, it acts as an excellent addition but equally complements humanities and arts subjects. ",
    "testimonials": "'I have found Psychology to be a unique and stimulating subject to study. I have also developed beneficial skills such as essay writing and statistical analysis.' \\n Gemma, previously St Edmund's Girls' School",
    "exam_details": "100% exams \\n 10% calculations"
},,{
    "title": "Religious Studies",
    "type": "A Level",
    "teacher_info": "Sally Tye - Faculty Lead (Humanities), Teacher of History and RS",
    "requirements": "Minimum 5 GCSE's at Grade 4 or above. Including at least grade 5 in English",
    "ucas_points": "UP to 56 UCAS Points",
    "topics": "Philosophy of religion, religion and ethics, developments in Christian thought",
    "description": "RS (Philosophy and Ethics) will take you from Dante's Inferno to spinning Sufi Muslims. Religion has been a fundamental part of human development and, in the 21st century, religion still addresses the same eternal questions about life and death, values and relationships, right and wrong. You will consider a range of fundamental questions about the human condition: Why is there evil? Can you prove the existence of God? Why be moral? This offers a broad and thought provoking approach to the study of religion and is accessible to students of any religious persuasion or none. It requires you to be organised, enthusiastic and prepared to tackle challenging ideas. It will develop the skills needed to examine ethical, philosophical and religious issues in a critical and analytical way. ",
    "testimonials": "'Studying RS (Philosophy & Ethics) has really required me to think. It has opened my mind and changed my perception of day to day life' \\n Eli, previously The Stonehenge School",
    "exam_details": "100% exams"
},,{
    "title": "Sociology",
    "type": "A Level",
    "teacher_info": "Andrew Lomas - Teacher of Sociology",
    "requirements": "Minimum 5 GCSE's at Grade 4 or above.",
    "ucas_points": "UP to 56 UCAS Points",
    "topics": "Sociology of family, sociology of education, sociology of beliefs, sociology of crime and deviance, theory and methods",
    "description": "Sociology is the study of society – it enables students to understand, question and interpret today's society. You will examine the problems facing society and the way sociologists go about studying society and social conditions. You will develop essay writing skills focusing on a range of subjects from the family, politics, history, education, religion to examining theories of, and solutions to, crime. You will also learn how society has changed over time, and which factors influence the growth and development of society. Furthermore, you will examine your own place in society and how factors may influence you throughout your lifetime. Around half of Sociology students at S6C opt to study the subject at university, and usually find work in teaching, law, the NHS, social work and the Civil Service.",
    "testimonials": "'I am really enjoying Sociology A level. Everything we have been taught is so interesting and is taught in an effective way.'\\n Ava, previously St Edmund's Girls' School",
    "exam_details": "100% exams"
},,{
    "title": "Software Design & Development",
    "type": "BTEC",
    "teacher_info": "Craig Chambers - Assistant Head of College",
    "requirements": "Minimum 5 GCSE's at Grade 4 or above.",
    "ucas_points": "Up to 84 UCAS Points",
    "topics": "A1 Skills development, A2 Creative project",
    "description": "The computer science industry is immense and provides a huge opportunity for employment across many areas. While studying this course, you will gain current skills and techniques across various disciplines relevant to industry today. The computer science industry changes at an extremely rapid pace. By studying this course you will learn to adapt and mirror the skill sets required. This course provides a foundation to all aspects of software design and programming, with a strong bias to practical study that reflects how industry works. You will examine a range of current topics to establish your skill set and make you more attractive to industry and university. You will be introduced to HTML, CSS and Javascript, along with languages such as Python, Swift and C#, with a focus on business applications and the opportunity to learn PWA cross platform application development. ",
    "testimonials": "'The course has a hands-on approach which gives you a realistic idea of programming as a career.' \\n Mike, previously Wyvern College",
    "exam_details": "100% coursework"
},,{
    "title": "Sport (Extended Certificate)",
    "type": "CTEC",
    "teacher_info": "Emma Thompson - Teacher of Sport",
    "requirements": "Minimum 5 GCSE's at Grade 4 or above.",
    "ucas_points": "UP to 56 UCAS Points",
    "topics": "Body systems & effects of physical activity, sports coaching, sports organisation and development, sociology of sports and exercise, practical skills in sport",
    "description": "The Sport course at S6C has been designed to broaden your knowledge in a wide range of areas within sport and exercise while developing your personal and employability skills. Units have been carefully selected to cover a range of different sectors to give you a taste of what different job roles entail allowing you to make an informed decision about your options after college. The course will help to support you whether directly into employment, apprenticeships or Higher Education with innovative and challenging lessons to equip you with the knowledge and personal skills essential to the sport and exercise industry. We will use local facilities such as a sport science laboratory, guest speakers and trips to universities and outdoor adventure activities. There will be coaching opportunities at the local primary schools to help you apply the knowledge you have gained in the classroom and develop your leadership skills.",
    "testimonials": "'As part of the course, I organised my own work experience at Salisbury Football Club which gave me the confidence to pursue this as a career' \\n Adam, previously Test Valley School",
    "exam_details": "100% coursework"
},,{
    "title": "Sport (Extended Diploma)",
    "type": "CTEC",
    "teacher_info": "Emma Thompson - Teacher of Sport",
    "requirements": "Minimum 5 GCSE's at Grade 4 or above.",
    "ucas_points": "Up to 168 UCAS points",
    "topics": "Sports science, sports development and, coaching, health and fitness, business of sport, sport sociology",
    "description": "Studying an Extended Diploma in Sport and Physical Activity Development at S6C will broaden your knowledge and understanding of the ever growing industry of sport and exercise. On this course you will have the opportunity to study a range of topics, this will allow you to gain an idea of which sector interests you most and which area you may like to pursue a career. For example, Anatomy and Physiology may pique your interests, or you may find a passion for coaching or fitness! While studying Sport at S6C you may also have the opportunity to gain additional qualifications such as first aid certificates and coaching badges. These opportunities are only a small part of the growth and development that you will have while studying this course. Previous trips and experiences on this course  have included Go Ape and Bath University. Students will have to purchase an S6C sports top to wear on work experience and in practical lessons",
    "testimonials": "'As part of the course, I organised my own work experience at Salisbury Football Club which gave me the confidence to pursue this as a career'\\n Adam, previously Test Valley School",
    "exam_details": "100% coursework"
}"""
myList = json.split(",,")

for course in myList:
    url = 'http://127.0.0.1:/course'
    r = requests.post(url, course)
    print(f"Status Code: {r.status_code}, Response: {r.json()}")

# print(myList[0])

# print(myList)

# for course in myList:
#     print(course)


# r = requests.post('http://127.0.0.1:/course', myList)
# print(f"Status Code: {r.status_code}, Response: {r.json()}")
