# **Marketing Tool** 📢

## **Overview**
The **Marketing Tool** is a Streamlit-based web application that generates age-specific marketing content using OpenAI's GPT-4 model. Users can select an **age group** and a **task type** (e.g., writing a sales copy, creating a tweet, or writing a product description), enter a query, and receive AI-generated responses tailored to their needs.

## **Features**
✅ **Dynamic Prompting** – Uses LangChain's `FewShotPromptTemplate` to generate responses based on predefined examples for different age groups.  
✅ **Multiple Age Groups** – Generates content in the voice of a **Kid, Adult, or Senior Citizen**.  
✅ **Marketing Use Cases** – Supports content generation for:
   - Writing a **sales copy**
   - Creating a **tweet**
   - Writing a **product description**  
✅ **User-Friendly Interface** – Built with **Streamlit** for easy input selection and response generation.  

---

## **Tech Stack**
- **Python 3.11**  
- **Streamlit** – For UI development  
- **LangChain** – For prompt engineering  
- **OpenAI GPT-4** – For AI-generated text responses  
- **Dotenv** – For managing API keys securely  

---

## **Installation & Setup**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-github-username/Marketing-Tool.git
cd Marketing-Tool
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up API Keys**
- Create a `.env` file in the project directory.
- Add your OpenAI API Key:
  ```sh
  OPENAI_API_KEY="your-api-key-here"
  ```

### **5️⃣ Run the Application**
```sh
streamlit run app.py
```

---

## **Usage**
1. **Enter text** in the input box.
2. **Select the task type** (Sales Copy, Tweet, or Product Description).
3. **Choose an age group** (Kid, Adult, or Senior Citizen).
4. **Set a word limit** using the slider.
5. **Click "Generate"** to receive AI-generated content.

---

## **Example Output**
### **Input**
- **Task:** Write a sales copy  
- **Age Group:** Senior Citizen  
- **User Query:** "Why should you buy our new ergonomic chair?"

### **Generated Response**
> "As we age, comfort and support become more important than ever. Our new ergonomic chair is designed with **lumbar support, memory foam cushioning, and an adjustable recline** to give you the best seating experience. Invest in your comfort today!"

---

## **Contributing**
🚀 **Contributions are welcome!** If you find a bug or want to add features:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Commit changes: `git commit -m "Added new feature"`
4. Push to your branch: `git push origin feature-branch`
5. Open a **Pull Request**.

---

## **License**
📜 This project is licensed under the **MIT License**.

---

## **Contact**
👤 **Created by**: Trevor Alpert  
📧 **Email**: trevoralpert1@gmail.com  
🔗 **GitHub**: [your-github-profile](https://github.com/your-github-username)  

---

### ✅ **Next Steps**
- If you have any additional features you’d like to document, let me know! 🚀  
- Feel free to replace **your-github-username** with your actual GitHub profile.  

Would you like me to format this file for you in Markdown and push it to your repo? 😊
