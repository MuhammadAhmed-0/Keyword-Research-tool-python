# Import necessary libraries
import requests
import xml.etree.ElementTree as ET
import streamlit as st

# Define Class
class QuestionsExplorer:
    def GetQuestions(self, questionType, userInput, countryCode):
        questionResults = []
        # Build Google Search Query
        searchQuery = questionType + " " + userInput + " "
        # API Call
        googleSearchUrl = "http://google.com/complete/search?output=toolbar&gl=" + \
            countryCode + "&q=" + searchQuery

        # Call The URL and Read Data
        result = requests.get(googleSearchUrl)
        tree = ET.ElementTree(ET.fromstring(result.content))
        root = tree.getroot()
        for suggestion in root.findall('CompleteSuggestion'):
            question = suggestion.find('suggestion').attrib.get('data')
            questionResults.append(question)

        return questionResults

# Define Streamlit app
def main():
    # Set page title
    st.title("Questions Explorer")

    # Get user input using text input widget
    userInput = st.text_input("Enter a Keyword:")

    # Create Object of the QuestionsExplorer Class
    qObj = QuestionsExplorer()

    # Define a button to trigger the API call
    if st.button("Search"):
        # Call The Method and pass the parameters
        questions = qObj.GetQuestions("is", userInput, "us")

        # Display the questions using a loop
        st.subheader("Search Results:")
        for result in questions:
            st.write(result)

# Run the app
if __name__ == "__main__":
    main()
