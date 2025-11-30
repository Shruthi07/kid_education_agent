# kid_education_agent
A friendly AI agent that provides fun answers and quiz to kids on specific subjects.

### Problem Statement / Overview
Kids in elementary are inclined to learn new content, but might be overwhelmed with big terms and jargons. This AI Agent assistant helps to provide fun and interactive content followed by quiz on specific topics like science, finance and geography. It helps curious kids to type in their queries to get curated story type responses for easy understanding. Quiz helps them to check and gain more knowledge on same content.

### Why agents? 
When kids have queries, they might not be able to reach their teachers/parents. And searching through books may be time consuming. With Agent, kids can type in the terms that they want to learn and get concise, easy to understand story based examples in few minutes. They also can try out quizzes that are asked after to test their knowledge.

### What you created and Demo -

It creates an interactive learning platform for kids. The content below describes main agent, its sub agent and tools used under each, the technology and platforms used.

The main root agent for **kid_education_agent** provides multi sub agent support to support kids in their interactive learning process. It has modular approach, such that many additional topics can be added along the learning process flow.

****science_agent -**** 
It answers queries related to science in kid friendly manner. Also, it has specific tool defined as below. Based on the output from tools, it creates a fun and creative response for kids. It also poses a quiz session after it, to be answered with 3 retries. If correct, it cheers up and if not encourages in comforting tone to find right one. 

*****get_element_info_by_name(element_name)*****
This tool is specific to describe chemical elements present in periodic table. It uses external public library to get element details. When kid asks any element, it provides basic details like its name, number, symbol and mass. 

****finance_agent -****
It uses **LLM Agent** to provide creative content related to finance terms. It also has few Safety configuration settings to prevent harmful contents.

****geography_agent -****
It generates engaging content related to geography concepts. We have used library to get country related details in tool as below. Once it has details, it generates content and similar to science agent creates a trivia quiz about that country.

**get_country_details(country_name)**
This tool is used to get basic country details like name, capital, language spoken, currency used and timezone. When a kid is curious know about a country and its culture, the sub agent with help of this tool provides both specific queries (capital) or creative content explaining the country specialities.

<img width="524" height="366" alt="image" src="https://github.com/user-attachments/assets/2fcc0394-7485-4628-ba9b-0bfd2566fffd" />


### If I had more time, this is what I'd do

It can be improved to have small images generated along with content, for kids to have visual learning. Many additional topics as tools and subjects as sub agents can be added.

