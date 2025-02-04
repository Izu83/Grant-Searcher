# GrantSearcher

GrantSearcher is an integrated system designed to aggregate, store, and process grant-related data, making it easily accessible for users through a simple user interface powered by a Large Language Model (LLM). This README outlines the main components and workflow of the system.

---

## System Architecture

### 1. **Data Aggregation and Storage**
This module handles the collection and preparation of data from external websites, ensuring it is stored in a structured format for further processing.

- **Website (Input Source):**  
  The system sends requests to websites containing grant-related information. This serves as the primary data source.

- **Data Scraper:**  
  A web scraping tool collects data from the websites and converts it into a usable format.  
  - **Step 1:** A request is sent to the target website.  
  - **Step 2:** The website responds with the required data.

- **Data Preparation:**  
  The collected raw data is processed, cleaned, and formatted for storage.  
  - **Step 3:** The scraped data is passed through preparation scripts to ensure consistency.

- **Storage:**  
  The processed data is stored in a database, allowing easy access for subsequent processing.  
  - **Step 4:** The prepared data is saved in structured storage.

---

### 2. **Model Training**
This module utilizes the stored data to train a Large Language Model (LLM) for answering user queries.

- **Training:**  
  - **Step 5:** The LLM is trained on the prepared data to understand grant-related topics and provide accurate, relevant answers.

---

### 3. **User Input and User Interface**
This module provides a seamless interface for users to interact with the system and receive answers to their questions.

- **User Interaction:**  
  - **Step 6:** The user submits a question via the User Interface (UI).  

- **Query Processing:**  
  - **Step 7:** The UI sends the user’s query to the trained LLM.  
  - **Step 8:** The LLM processes the query and returns an answer.

- **Response Delivery:**  
  - **Step 9:** The UI displays the answer back to the user.

---

## Workflow Summary

1. Data is scraped from websites containing grant information.  
2. The scraped data is processed and stored in a structured database.  
3. The stored data is used to train an LLM on grant-related topics.  
4. Users submit questions through the UI, which forwards the query to the LLM.  
5. The LLM provides an answer, which is then displayed to the user.

---

## Components

- **Data Scraper:** Automates the extraction of data from websites.  
- **Storage:** A database for storing processed grant information.  
- **LLM (Large Language Model):** Provides intelligent query handling and responses.  
- **UI (User Interface):** A frontend application enabling user interaction with the system.

---

## Key Features

- Automated data aggregation from multiple grant websites.  
- Robust data preparation and storage pipeline.  
- Intelligent query answering using an LLM trained on grant-related data.  
- User-friendly interface for seamless interaction.

---

## Future Enhancements

- Expand scraping capabilities to include more data sources.  
- Improve LLM accuracy with continuous retraining on updated data.  
- Add advanced filtering and recommendation features in the UI.

---

## License

This project is licensed under the MIT License.
